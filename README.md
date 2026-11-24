# Red Hat Ansible Automation Platform Containerized Setup Bundle Version Matrix

[![GitHub last commit](https://img.shields.io/github/last-commit/lennysh/aap-containerized-setup-bundle-version-matrix.svg)](https://github.com/lennysh/aap-containerized-setup-bundle-version-matrix/commits/main) [![GitHub license](https://img.shields.io/github/license/lennysh/aap-containerized-setup-bundle-version-matrix.svg)](https://github.com/lennysh/aap-containerized-setup-bundle-version-matrix/blob/main/LICENSE)

A community-maintained version matrix for Red Hat Ansible Automation Platform (AAP) **containerized setup bundles** (`ansible-automation-platform-containerized-setup-bundle-*.tar.gz`, AAP 2.5+). Each bundle gets one page listing every container image it ships, with every RPM package, Python package (per environment) and Ansible collection at its exact version.

The main use is **CVE triage for a specific install**: open the page for the bundle you installed, search the consolidated RPM or Python package table for the affected package, and see which containers ship which version.

> [!IMPORTANT]
> This is a community resource. It is not official Red Hat data and is not supported by Red Hat. Package versions are read directly from the bundle contents, but whether a CVE affects your installation, or is fixed in it, is decided by [Red Hat Security Advisories and errata](https://access.redhat.com/security/security-updates/). Always confirm there.

This repo is driven by installer downloads, not a registry, so it is updated manually. For the registry-based EE/DE matrix, see [aap-container-images-version-matrix](https://github.com/lennysh/aap-container-images-version-matrix).

[comment]: <> (BEGIN Ansible Managed)
## 📦 Inspected Bundles

Each bundle page lists every container image in the bundle, with consolidated RPM and Python
package tables for CVE triage.

| Bundle (Click for details) | AAP | Architecture | Images |
| :------------------------- | :-- | :----------- | -----: |
| [2.7-12.4](./bundles/2.7-12.4-x86_64/README.md) | 2.7 | x86_64 | 21 |
| [2.7-12.2](./bundles/2.7-12.2-x86_64/README.md) | 2.7 | x86_64 | 21 |
| [2.7-4](./bundles/2.7-4-x86_64/README.md) | 2.7 | x86_64 | 19 |
| [2.6-14.4](./bundles/2.6-14.4-x86_64/README.md) | 2.6 | x86_64 | 19 |
| [2.6-12](./bundles/2.6-12-x86_64/README.md) | 2.6 | x86_64 | 19 |
| [2.6-11.1](./bundles/2.6-11.1-x86_64/README.md) | 2.6 | x86_64 | 19 |
| [2.6-5](./bundles/2.6-5-x86_64/README.md) | 2.6 | x86_64 | 18 |
| [2.6-3](./bundles/2.6-3-x86_64/README.md) | 2.6 | x86_64 | 17 |
| [2.5-25.8](./bundles/2.5-25.8-x86_64/README.md) | 2.5 | x86_64 | 14 |
[comment]: <> (END Ansible Managed)

## 🛠 Updating the version matrix

Do **not** edit `bundles/**/README.md` or the tables above by hand. They are generated.

### Prerequisites

- Ansible 2.15+ (only `ansible.builtin` is used)
- `python3` 3.9+ and `rpm` on your PATH (RHEL 9 images use the sqlite rpmdb; Fedora/RHEL 9+ hosts read it fine)
- No `podman`, registry login, or root access is needed

### Workflow

1. Download one or more containerized setup bundles from the [Red Hat Customer Portal](https://access.redhat.com/downloads/content/480) into a folder.
2. Run from the repository root:

   ```bash
   ansible-playbook bundle_inspector.yml -e bundle_dir=~/Downloads
   ```

3. Review and commit the changes under `bundles/` and `README.md`.

### How it works

`roles/bundle_inspector/files/inspect_bundle.py` **streams** each bundle. It reads the outer tarball, then each `bundle/images/*.tar.gz` docker-archive, then every layer. Layers are replayed in memory with overlay whiteout semantics, and only the files needed for the inventory are kept:

- the rpmdb (`/var/lib/rpm`), queried by the host `rpm` from a temporary copy
- `*.dist-info/METADATA` and `*.egg-info`, which cover every Python environment (system Python, `/usr/local`, venvs such as `/var/lib/awx/venv/awx`)
- `ansible_collections/*/*/MANIFEST.json` (ansible-core's internal pseudo-collections are ignored)
- `/etc/os-release`

Nothing is extracted to disk, nothing from the images is executed, and your podman storage is untouched. A typical bundle takes about a minute.

Image tags inside bundles are mostly `latest`, and the docker-archive format does not keep registry manifest digests. So images are keyed by **image ID** (config digest) and show their `version`/`release` labels and the tag used in the bundle.

Python environments are reported per prefix and interpreter (for example `/usr (python3.9)`, `/usr (python3.12)`, `/var/lib/awx/venv/awx (python3.12)`), because many images ship more than one.

### Output

| Path | Contents |
| :--- | :------- |
| `bundles/<version>-<arch>/bundle.yml` | Full inventory for the bundle: every image's metadata, RPMs, Python environments and collections, plus installer and bundled collections |
| `bundles/<version>-<arch>/README.md` | Generated bundle page: image summary, consolidated RPM and Python package tables, per-image details |

### Common options

```bash
# Re-inspect bundles that already have data
ansible-playbook bundle_inspector.yml -e bundle_dir=~/Downloads -e bundle_inspector_force=true

# Regenerate markdown only
ansible-playbook md_generator.yml

# Inspect a single bundle by hand (JSON on stdout)
python3 -I roles/bundle_inspector/files/inspect_bundle.py /path/to/bundle.tar.gz
```

## ✍️ Authors

* [LennySh](https://github.com/lennysh)

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
