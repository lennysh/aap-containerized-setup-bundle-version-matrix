#!/usr/bin/env python3
"""Inventory every container image inside an AAP containerized setup bundle.

Usage: inspect_bundle.py <bundle.tar.gz>

The bundle is streamed (bundle tar.gz -> bundle/images/*.tar.gz docker-archives ->
layer tars); nothing is extracted to disk and nothing from the images is executed.
Layers are replayed in memory with OCI whiteout semantics, keeping only the files
needed for the inventory (rpmdb, os-release, Python package metadata, Ansible
collection manifests). The host ``rpm`` binary then queries a temporary copy of the
image rpmdb.

Prints a single JSON document on stdout.
"""
import email.parser
import json
import os
import posixpath
import re
import subprocess
import sys
import tarfile
import tempfile

BUNDLE_RE = re.compile(
    r"^ansible-automation-platform-containerized-setup-bundle-"
    r"(?P<version>(?P<aap>\d+\.\d+)-.+?)-(?P<arch>x86_64|aarch64|ppc64le|s390x)\.tar\.gz$"
)
IMAGE_MEMBER_RE = re.compile(r"(^|/)bundle/images/(?P<file>[^/]+\.tar(\.gz)?)$")
BUNDLED_COLLECTION_RE = re.compile(
    r"(^|/)bundle/collections/(?P<kind>[^/]+)/(?P<ns>[a-z0-9_]+)-(?P<name>[a-z0-9_]+)-(?P<ver>[^/]+?)\.tar\.gz$"
)
INSTALLER_COLLECTION_RE = re.compile(
    r"^[^/]+/collections/ansible_collections/(?P<ns>[a-z0-9_]+)\.(?P<name>[a-z0-9_]+)-(?P<ver>[^/]+)\.info/?$"
)
HEX_JSON_RE = re.compile(r"^[0-9a-f]{64}\.json$")
RPMDB_DIRS = ("var/lib/rpm", "usr/lib/sysimage/rpm")
OS_RELEASE = ("etc/os-release", "usr/lib/os-release")
PY_META_RE = re.compile(
    r"^(?P<site>.*/(?:site|dist)-packages)/[^/]+\.(?:dist-info/METADATA|egg-info/PKG-INFO|egg-info)$"
)
SITE_RE = re.compile(r"^(?P<prefix>.*?)/lib(?:64)?/(?P<py>python[0-9.]+)/(?:site|dist)-packages$")
COLLECTION_RE = re.compile(
    r"^(?P<root>.*/)?ansible_collections/(?P<ns>[a-z0-9_]+)/(?P<name>[a-z0-9_]+)/"
    r"(?P<file>MANIFEST\.json|galaxy\.yml|meta/runtime\.yml)$"
)
# ansible-core ships internal pseudo-collections; they are not user-facing content.
COLLECTION_EXCLUDE_RE = re.compile(r"(^|/)(ansible/_internal|ansible_test)/")
PYTHON_BIN_RE = re.compile(r"^(?:usr/)?(?:local/)?bin/python(?P<ver>3\.[0-9]+)$")


def norm(name):
    """Normalise a tar member name to a relative POSIX path; None if unsafe."""
    path = posixpath.normpath(name.lstrip("/"))
    if path in ("", ".") or path.startswith("../") or path == "..":
        return None
    return path.removeprefix("./")


def interesting(path):
    return (
        path in OS_RELEASE
        or any(path.startswith(d + "/") for d in RPMDB_DIRS)
        or PY_META_RE.match(path) is not None
        or COLLECTION_RE.match(path) is not None
    )


class Entry:
    __slots__ = ("kind", "data", "target")

    def __init__(self, kind, data=None, target=None):
        self.kind = kind      # "file", "dir", "symlink", "hardlink", "other"
        self.data = data      # bytes for interesting regular files
        self.target = target  # symlink/hardlink target


def read_layer(fileobj):
    """Return (whiteouts, opaque_dirs, adds) for one layer tar."""
    whiteouts, opaques, adds = [], [], []
    with tarfile.open(fileobj=fileobj, mode="r|*") as layer:
        for m in layer:
            path = norm(m.name)
            if path is None:
                continue
            base = posixpath.basename(path)
            parent = posixpath.dirname(path)
            if base == ".wh..wh..opq":
                opaques.append(parent)
                continue
            if base.startswith(".wh."):
                whiteouts.append(posixpath.join(parent, base[4:]))
                continue
            if m.isdir():
                adds.append((path, Entry("dir")))
            elif m.issym():
                adds.append((path, Entry("symlink", target=m.linkname)))
            elif m.islnk():
                adds.append((path, Entry("hardlink", target=norm(m.linkname))))
            elif m.isfile():
                data = layer.extractfile(m).read() if interesting(path) else None
                adds.append((path, Entry("file", data=data)))
            else:
                adds.append((path, Entry("other")))
    return whiteouts, opaques, adds


def remove_tree(state, path, keep_self=False):
    prefix = path + "/"
    for key in [k for k in state if k.startswith(prefix)]:
        del state[key]
    if not keep_self:
        state.pop(path, None)


def apply_layer(state, layer):
    whiteouts, opaques, adds = layer
    for d in opaques:
        remove_tree(state, d, keep_self=True)
    for p in whiteouts:
        remove_tree(state, p)
    for path, entry in adds:
        if entry.kind == "hardlink":
            src = state.get(entry.target)
            entry = Entry("file", data=src.data if src is not None else None)
        state[path] = entry


def resolve(state, path, hops=10):
    """Follow final-component symlinks inside the virtual filesystem."""
    while hops > 0:
        entry = state.get(path)
        if entry is None or entry.kind != "symlink":
            return path, entry
        target = entry.target
        if target.startswith("/"):
            path = norm(target)
        else:
            path = norm(posixpath.join(posixpath.dirname(path), target))
        if path is None:
            return None, None
        hops -= 1
    return None, None


def parse_os_release(state):
    for rel in OS_RELEASE:
        _, entry = resolve(state, rel)
        if entry is not None and entry.data:
            data = {}
            for line in entry.data.decode("utf-8", "replace").splitlines():
                key, sep, val = line.strip().partition("=")
                if sep:
                    data[key] = val.strip().strip('"')
            return data
    return {}


def rpm_packages(state):
    for dbdir in RPMDB_DIRS:
        files = {
            k: v for k, v in state.items()
            if k.startswith(dbdir + "/") and v.kind == "file" and v.data is not None
        }
        names = {posixpath.basename(k) for k in files}
        if "rpmdb.sqlite" in names:
            backend = "sqlite"
        elif "Packages" in names:
            backend = "bdb_ro"
        else:
            continue
        with tempfile.TemporaryDirectory(prefix="aap-bundle-rpmdb-") as root:
            for path, entry in files.items():
                dest = os.path.join(root, path)
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                with open(dest, "wb") as fh:
                    fh.write(entry.data)
            result = subprocess.run(
                ["rpm", "-qa", "--root", root, "--dbpath", "/" + dbdir,
                 "--define", f"_db_backend {backend}",
                 "--queryformat", "%{NAME} %{VERSION}-%{RELEASE}\\n"],
                capture_output=True, text=True, check=False,
            )
        if result.returncode != 0:
            raise RuntimeError(f"rpm query failed ({dbdir}): {result.stderr.strip()}")
        return sorted({line for line in result.stdout.splitlines() if line.strip()})
    return []


def pip_environments(state):
    parser = email.parser.HeaderParser()
    envs = {}
    for path, entry in state.items():
        match = PY_META_RE.match(path)
        if not match or entry.kind != "file" or not entry.data:
            continue
        meta = parser.parsestr(entry.data.decode("utf-8", "replace"))
        name = meta.get("Name")
        if not name:
            continue
        site = match.group("site")
        site_match = SITE_RE.match(site)
        prefix, python = ("/" + site_match.group("prefix"), site_match.group("py")) if site_match else ("/" + site, None)
        env = envs.setdefault((prefix, python or ""), {"path": prefix, "python": python, "packages": set()})
        env["packages"].add(f"{name} {meta.get('Version', '')}".strip())
    return [
        {**env, "packages": sorted(env["packages"], key=str.lower)}
        for _, env in sorted(envs.items())
    ]


def ansible_collections(state):
    found = {}
    for path, entry in state.items():
        match = COLLECTION_RE.match(path)
        if not match or COLLECTION_EXCLUDE_RE.search(path):
            continue
        key = (match.group("root") or "", match.group("ns"), match.group("name"))
        version = found.get(key, "*")
        if entry.data and match.group("file") == "MANIFEST.json":
            try:
                version = json.loads(entry.data)["collection_info"]["version"]
            except (ValueError, KeyError, TypeError):
                pass
        elif entry.data and match.group("file") == "galaxy.yml" and version == "*":
            ver = re.search(rb"^version:\s*['\"]?([^'\"\s]+)", entry.data, re.M)
            if ver:
                version = ver.group(1).decode()
        found[key] = version
    return sorted({f"{ns}.{name} {ver}" for (_, ns, name), ver in found.items()})


def python_versions(state):
    vers = {m.group("ver") for p in state if (m := PYTHON_BIN_RE.match(p))}
    return sorted(vers, key=lambda v: [int(x) for x in v.split(".")])


def inspect_image(fileobj, file_name):
    layers, small = {}, {}
    with tarfile.open(fileobj=fileobj, mode="r|*") as img:
        for m in img:
            name = norm(m.name)
            if name is None or not m.isfile():
                continue
            if name == "manifest.json" or HEX_JSON_RE.match(name):
                small[name] = img.extractfile(m).read()
            elif name.endswith(".tar"):
                layers[name] = read_layer(img.extractfile(m))
    if "manifest.json" not in small:
        raise RuntimeError(f"{file_name}: no manifest.json (not a docker-archive)")
    manifest = json.loads(small["manifest.json"])[0]
    config_name = norm(manifest["Config"])
    config = json.loads(small[config_name])
    labels = (config.get("config") or {}).get("Labels") or {}

    state = {}
    for layer_name in manifest["Layers"]:
        apply_layer(state, layers.pop(norm(layer_name)))

    repo_tags = manifest.get("RepoTags") or []
    repo_tag = repo_tags[0] if repo_tags else ""
    repo, _, tag = repo_tag.rpartition(":") if ":" in repo_tag.rsplit("/", 1)[-1] else (repo_tag, "", "")
    osr = parse_os_release(state)
    pip_envs = pip_environments(state)
    core = sorted({
        pkg.split(" ", 1)[1] for env in pip_envs for pkg in env["packages"]
        if pkg.lower().startswith("ansible-core ")
    })
    return {
        "file": file_name,
        "repo": repo,
        "bundle_tag": tag,
        "image_id": "sha256:" + config_name.removesuffix(".json"),
        "version": labels.get("version"),
        "release": labels.get("release"),
        "label_name": labels.get("name"),
        "created": config.get("created"),
        "build_date": labels.get("build-date"),
        "architecture": config.get("architecture"),
        "rhel_version": osr.get("PRETTY_NAME") or osr.get("NAME"),
        "python_versions": python_versions(state),
        "ansible_core_version": ", ".join(core) or None,
        "ansible_collections": ansible_collections(state),
        "system_packages": rpm_packages(state),
        "pip_environments": pip_envs,
    }


def inspect_bundle(path):
    base = os.path.basename(path)
    match = BUNDLE_RE.match(base)
    if not match:
        raise SystemExit(f"{base}: not an AAP containerized setup bundle file name")
    images, bundled, installer = [], set(), set()
    with tarfile.open(path, mode="r|gz") as bundle:
        for m in bundle:
            name = m.name
            inst = INSTALLER_COLLECTION_RE.match(name)
            if inst and m.isdir():
                installer.add(f"{inst['ns']}.{inst['name']} {inst['ver']}")
                continue
            if not m.isfile():
                continue
            if coll := BUNDLED_COLLECTION_RE.search(name):
                bundled.add(f"{coll['ns']}.{coll['name']} {coll['ver']} ({coll['kind']})")
            elif img := IMAGE_MEMBER_RE.search(name):
                print(f"inspecting {img['file']}", file=sys.stderr, flush=True)
                images.append(inspect_image(bundle.extractfile(m), img["file"]))
    return {
        "bundle_file": base,
        "bundle_id": f"{match['version']}-{match['arch']}",
        # Natural sort key so 2.7-12.4 sorts after 2.7-4 in generated tables.
        "sort_key": re.sub(r"\d+", lambda d: d.group(0).zfill(10), match["version"]),
        "bundle_version": match["version"],
        "aap_version": match["aap"],
        "architecture": match["arch"],
        "installer_collections": sorted(installer),
        "bundled_collections": sorted(bundled),
        "images": sorted(images, key=lambda i: i["repo"]),
    }


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    json.dump(inspect_bundle(sys.argv[1]), sys.stdout, indent=2)
    sys.stdout.write("\n")
