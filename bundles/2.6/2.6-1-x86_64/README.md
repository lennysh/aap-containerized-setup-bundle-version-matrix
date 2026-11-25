[All AAP versions](../../../README.md) / [AAP 2.6](../README.md) / 2.6-1

# AAP Containerized Setup Bundle 2.6-1 (x86_64)

- **Bundle file:** `ansible-automation-platform-containerized-setup-bundle-2.6-1-x86_64.tar.gz`
- **AAP version:** 2.6
- **Bundle created:** 2025-10-01 21:50:41 UTC
- **Container images:** 14
- **Distinct RPM package versions:** 727
- **Distinct Python package versions:** 556

> [!IMPORTANT]
> Community resource, not official Red Hat data. Confirm CVE impact and fixes with
> [Red Hat Security Advisories and errata](https://access.redhat.com/security/security-updates/).

Generated from the bundle contents; do not edit by hand. Image IDs are config digests
(what `podman images --no-trunc` shows after `podman load`), not registry manifest digests.

## Contents

- [Container Images](#container-images)
- [RPM Packages (all images)](#rpm-packages-all-images)
- [Python Packages (all images)](#python-packages-all-images)
- [Image Details](#image-details)
  - [controller-rhel9](#controller-rhel9)
  - [de-supported-rhel9](#de-supported-rhel9)
  - [eda-controller-rhel9](#eda-controller-rhel9)
  - [eda-controller-ui-rhel9](#eda-controller-ui-rhel9)
  - [ee-minimal-rhel9](#ee-minimal-rhel9)
  - [ee-supported-rhel9](#ee-supported-rhel9)
  - [gateway-proxy-rhel9](#gateway-proxy-rhel9)
  - [gateway-rhel9](#gateway-rhel9)
  - [hub-rhel9](#hub-rhel9)
  - [hub-web-rhel9](#hub-web-rhel9)
  - [receptor-rhel9](#receptor-rhel9)
  - [pcp](#pcp)
  - [postgresql-15](#postgresql-15)
  - [redis-6](#redis-6)
- [Installer Collections](#installer-collections)
- [Bundled Collections](#bundled-collections)

## Container Images

| Image | Tag in Bundle | Version | Release | Image ID | RHEL Version | Python | Ansible Core | RPMs | Python Pkgs | Collections |
|---|---|---|---|---|---|---|---|--:|--:|--:|
| [registry.redhat.io/ansible-automation-platform-26/controller-rhel9](#controller-rhel9) | `latest` | 4.7.1 | 4 | `982e48d852cb` | Red Hat Enterprise Linux 9.6 (Plow) | 3.9, 3.11 | N/A | 266 | 222 | 0 |
| [registry.redhat.io/ansible-automation-platform-26/de-supported-rhel9](#de-supported-rhel9) | `latest` | 1.2.0 | 74 | `e09120edc2cb` | Red Hat Enterprise Linux 9.6 (Plow) | 3.9, 3.11 | 2.16.14 | 228 | 64 | 1 |
| [registry.redhat.io/ansible-automation-platform-26/eda-controller-rhel9](#eda-controller-rhel9) | `latest` | 1.2.0 | 147 | `3b8d9b8a8c82` | Red Hat Enterprise Linux 9.6 (Plow) | 3.9, 3.11 | 2.16.14 | 299 | 114 | 0 |
| [registry.redhat.io/ansible-automation-platform-26/eda-controller-ui-rhel9](#eda-controller-ui-rhel9) | `latest` | 1.2.0 | 141 | `5e8655027857` | Red Hat Enterprise Linux 9.6 (Plow) | 3.9 | N/A | 301 | 18 | 0 |
| [registry.redhat.io/ansible-automation-platform-26/ee-minimal-rhel9](#ee-minimal-rhel9) | `latest` | 1.0.0 | 973 | `e96a4d533cef` | Red Hat Enterprise Linux 9.6 (Plow) | 3.11 | 2.16.14 | 199 | 63 | 0 |
| [registry.redhat.io/ansible-automation-platform-26/ee-supported-rhel9](#ee-supported-rhel9) | `latest` | 1.0.0 | 1096 | `d590c7adac8e` | Red Hat Enterprise Linux 9.6 (Plow) | 3.9, 3.11 | 2.16.14 | 311 | 267 | 54 |
| [registry.redhat.io/ansible-automation-platform-26/gateway-proxy-rhel9](#gateway-proxy-rhel9) | `latest` | 2.6.6 | 5 | `0a4ef1771371` | Red Hat Enterprise Linux 9.6 (Plow) | N/A | N/A | 113 | 0 | 0 |
| [registry.redhat.io/ansible-automation-platform-26/gateway-rhel9](#gateway-rhel9) | `latest` | 2.6.20251001 | 1 | `effabbb5cae9` | Red Hat Enterprise Linux 9.6 (Plow) | 3.9, 3.11 | N/A | 243 | 72 | 0 |
| [registry.redhat.io/ansible-automation-platform-26/hub-rhel9](#hub-rhel9) | `latest` | 4.11.0 | 159 | `ffbb3283c188` | Red Hat Enterprise Linux 9.6 (Plow) | 3.9, 3.11 | 2.16.14 | 362 | 174 | 0 |
| [registry.redhat.io/ansible-automation-platform-26/hub-web-rhel9](#hub-web-rhel9) | `latest` | 4.11.0 | 150 | `8852c4dcca6f` | Red Hat Enterprise Linux 9.6 (Plow) | 3.9 | N/A | 301 | 18 | 0 |
| [registry.redhat.io/ansible-automation-platform-26/receptor-rhel9](#receptor-rhel9) | `latest` | 1.5.7 | 11 | `920342a88459` | Red Hat Enterprise Linux 9.6 (Plow) | 3.9, 3.11 | N/A | 174 | 24 | 0 |
| [registry.redhat.io/rhel9/pcp](#pcp) | `latest` | 6 | 1758530508 | `8322c3ef2c6f` | Red Hat Enterprise Linux 9.6 (Plow) | 3.9 | N/A | 212 | 19 | 0 |
| [registry.redhat.io/rhel9/postgresql-15](#postgresql-15) | `latest` | 1 | 1758514462 | `473f17c83f4b` | Red Hat Enterprise Linux 9.6 (Plow) | 3.9 | N/A | 280 | 18 | 0 |
| [registry.redhat.io/rhel9/redis-6](#redis-6) | `latest` | 1 | 1758530358 | `66c15d0ce52b` | Red Hat Enterprise Linux 9.6 (Plow) | 3.9 | N/A | 210 | 18 | 0 |

## RPM Packages (all images)

Every RPM installed in any image of this bundle (`name version-release`). Search this table for a
package named in a CVE to see which containers ship which version.

| Package | Version-Release | Images |
|---|---|---|
| `aap-metrics-utility` | `0.6.0-3.el9ap` | controller-rhel9 |
| `acl` | `2.3.1-4.el9` | controller-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `alsa-lib` | `1.2.13-2.el9` | de-supported-rhel9 |
| `alternatives` | `1.24-2.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `ansible-automation-platform-common` | `2.6-1.el9ap` | controller-rhel9, eda-controller-rhel9, gateway-rhel9, hub-rhel9 |
| `ansible-automation-platform-selinux` | `0.2-3.el9ap` | controller-rhel9, eda-controller-rhel9, gateway-rhel9, hub-rhel9 |
| `ansible-builder` | `3.1.0-1.el9ap` | hub-rhel9 |
| `ansible-core` | `2.16.14-2.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `ansible-lint` | `25.8.2-1.el9ap` | ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `ansible-rulebook` | `1.2.0-1.el9ap` | de-supported-rhel9 |
| `ansible-runner` | `2.4.1-1.el9ap` | de-supported-rhel9, ee-minimal-rhel9, ee-supported-rhel9, receptor-rhel9 |
| `ansible-sign` | `0.1.2-1.el9ap` | ee-supported-rhel9 |
| `ansible-test` | `2.16.14-2.el9ap` | ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `apr` | `1.7.0-12.el9_3` | controller-rhel9, ee-supported-rhel9 |
| `apr-util` | `1.6.1-23.el9` | controller-rhel9, ee-supported-rhel9 |
| `apr-util-bdb` | `1.6.1-23.el9` | controller-rhel9, ee-supported-rhel9 |
| `attr` | `2.5.1-3.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `audit-libs` | `3.1.5-4.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `automation-controller` | `4.7.1-1.el9ap` | controller-rhel9 |
| `automation-controller-cli` | `4.7.1-1.el9ap` | ee-supported-rhel9 |
| `automation-controller-server` | `4.7.1-1.el9ap` | controller-rhel9 |
| `automation-controller-ui` | `4.7.1-1.el9ap` | controller-rhel9 |
| `automation-controller-venv-tower` | `4.7.1-1.el9ap` | controller-rhel9 |
| `automation-eda-controller` | `1.2.0-1.el9ap` | eda-controller-rhel9 |
| `automation-gateway-config` | `2.6.20251001-1.el9ap` | gateway-proxy-rhel9 |
| `automation-gateway-proxy-server` | `2.6.6-3.el9ap` | gateway-proxy-rhel9 |
| `automation-gateway-server` | `2.6.20251001-1.el9ap` | gateway-rhel9 |
| `automation-hub` | `4.11.0-1.el9ap` | hub-rhel9 |
| `automation-platform-ui` | `2.6.1-1.el9ap` | gateway-rhel9 |
| `avahi-libs` | `0.8-22.el9_6.1` | de-supported-rhel9, pcp |
| `basesystem` | `11-13.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `bash` | `5.1.8-9.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `bash-completion` | `2.11-5.el9` | ee-supported-rhel9 |
| `bind9.18-libs` | `9.18.29-4.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `bind9.18-utils` | `9.18.29-4.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `bindep` | `2.11.0-2.el9ap` | hub-rhel9 |
| `bsdtar` | `3.5.3-6.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15, redis-6 |
| `bzip2` | `1.0.8-10.el9_5` | ee-minimal-rhel9, ee-supported-rhel9 |
| `bzip2-libs` | `1.0.8-10.el9_5` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `ca-certificates` | `2024.2.69_v8.0.303-91.4.el9_4` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `container-selinux` | `2.237.0-2.el9_6` | hub-rhel9 |
| `containers-common` | `1-117.el9_6` | hub-rhel9 |
| `copy-jdk-configs` | `4.0-3.el9` | de-supported-rhel9 |
| `coreutils-single` | `8.32-39.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `cracklib` | `2.9.6-27.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `cracklib-dicts` | `2.9.6-27.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `crontabs` | `1.11-27.20190603git.el9_0` | controller-rhel9 |
| `crun` | `1.23.1-2.el9_6` | controller-rhel9, hub-rhel9 |
| `crypto-policies` | `20250128-1.git5269e22.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `crypto-policies-scripts` | `20250128-1.git5269e22.el9` | de-supported-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `cups-libs` | `2.3.3op2-33.el9_6.1` | de-supported-rhel9 |
| `curl-minimal` | `7.76.1-31.el9_6.1` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `cyrus-sasl-lib` | `2.1.27-21.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `dbus` | `1.12.20-8.el9` | controller-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `dbus-broker` | `28-7.el9` | controller-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `dbus-common` | `1.12.20-8.el9` | controller-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `dbus-libs` | `1.12.20-8.el9` | controller-rhel9, de-supported-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `dejavu-sans-fonts` | `2.37-18.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `device-mapper` | `1.02.202-6.el9` | pcp |
| `device-mapper-libs` | `1.02.202-6.el9` | pcp |
| `diffutils` | `3.7-12.el9` | controller-rhel9, eda-controller-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, receptor-rhel9, pcp, redis-6 |
| `dmidecode` | `3.6-1.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `dnf` | `4.14.0-25.el9` | eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `dnf-data` | `4.14.0-25.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `dumb-init` | `1.2.5-3.el9ap` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, receptor-rhel9 |
| `elfutils-default-yama-scope` | `0.192-6.el9_6` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `elfutils-libelf` | `0.192-6.el9_6` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `elfutils-libs` | `0.192-6.el9_6` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `environment-modules` | `5.3.0-1.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15, redis-6 |
| `expat` | `2.5.0-5.el9_6` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `file` | `5.39-16.el9` | ee-minimal-rhel9, ee-supported-rhel9 |
| `file-libs` | `5.39-16.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `filesystem` | `3.16-5.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `findutils` | `4.8.0-7.el9` | controller-rhel9, de-supported-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `flexiblas` | `3.0.4-8.el9` | controller-rhel9, ee-supported-rhel9 |
| `flexiblas-netlib` | `3.0.4-8.el9` | controller-rhel9, ee-supported-rhel9 |
| `flexiblas-openblas-openmp` | `3.0.4-8.el9` | controller-rhel9, ee-supported-rhel9 |
| `fontconfig` | `2.14.0-2.el9_1` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `fonts-filesystem` | `2.0.5-7.el9.1` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `freetype` | `2.10.4-10.el9_5` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `fstrm` | `0.6.1-3.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `gawk` | `5.1.0-6.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `gd` | `2.3.2-3.el9` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `gdb-gdbserver` | `14.2-4.1.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `gdbm-libs` | `1.23-1.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `gettext` | `0.21-8.el9` | eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `gettext-libs` | `0.21-8.el9` | eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `git-core` | `2.47.3-1.el9_6` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `git-lfs` | `3.6.1-2.el9_6` | controller-rhel9, ee-supported-rhel9 |
| `glib2` | `2.68.4-16.el9_6.2` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `glibc` | `2.34-168.el9_6.23` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `glibc-common` | `2.34-168.el9_6.23` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `glibc-langpack-en` | `2.34-168.el9_6.23` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-web-rhel9, postgresql-15, redis-6 |
| `glibc-locale-source` | `2.34-168.el9_6.23` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15, redis-6 |
| `glibc-minimal-langpack` | `2.34-168.el9_6.23` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `gmp` | `6.2.0-13.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `gnupg2` | `2.3.3-4.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `gnutls` | `3.8.3-6.el9_6.2` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `gobject-introspection` | `1.68.0-11.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `gpg-pubkey` | `5a6340b3-6229229e` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `gpg-pubkey` | `fd431d51-4ae0493b` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `gpgme` | `1.15.1-6.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `graphite2` | `1.3.14-9.el9` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `grep` | `3.6-5.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `groff-base` | `1.22.4-10.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15, redis-6 |
| `gzip` | `1.12-1.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `harfbuzz` | `2.7.4-10.el9` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `hostname` | `3.23-6.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp |
| `ima-evm-utils` | `1.5-3.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `iproute` | `6.11.0-1.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `java-17-openjdk-headless` | `17.0.16.0.8-2.el9` | de-supported-rhel9 |
| `javapackages-filesystem` | `6.4.0-1.el9` | de-supported-rhel9 |
| `jbigkit-libs` | `2.1-23.el9` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `jq` | `1.6-17.el9_6.2` | hub-rhel9 |
| `json-c` | `0.14-11.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `json-glib` | `1.6.6-1.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `keyutils` | `1.6.3-1.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `keyutils-libs` | `1.6.3-1.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `kmod-libs` | `28-10.el9` | controller-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `krb5-libs` | `1.21.1-8.el9_6` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `krb5-pkinit` | `1.21.1-8.el9_6` | controller-rhel9, de-supported-rhel9, ee-minimal-rhel9, ee-supported-rhel9 |
| `krb5-workstation` | `1.21.1-8.el9_6` | controller-rhel9, de-supported-rhel9, ee-minimal-rhel9, ee-supported-rhel9 |
| `langpacks-core-en` | `3.0-16.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `langpacks-core-font-en` | `3.0-16.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `langpacks-en` | `3.0-16.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `less` | `590-5.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9, hub-web-rhel9, postgresql-15, redis-6 |
| `libacl` | `2.3.1-4.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libaio` | `0.3.111-13.el9` | ee-supported-rhel9 |
| `libarchive` | `3.5.3-6.el9_6` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libassuan` | `2.5.5-3.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libattr` | `2.5.1-3.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libblkid` | `2.37.4-21.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libbpf` | `1.5.0-1.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `libbrotli` | `1.0.9-7.el9_5` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `libcap` | `2.48-9.el9_2` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libcap-ng` | `0.8.2-7.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libcbor` | `0.7.0-5.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `libcom_err` | `1.46.5-7.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libcomps` | `0.1.18-1.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `libcurl-minimal` | `7.76.1-31.el9_6.1` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libdb` | `5.3.28-57.el9_6` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libdnf` | `0.69.0-13.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libdnf-plugin-subscription-manager` | `1.29.45.1-1.el9_6` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `libeconf` | `0.4.1-4.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libedit` | `3.1-38.20210216cvs.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `libestr` | `0.1.11-4.el9` | controller-rhel9, hub-rhel9 |
| `libevent` | `2.1.12-8.el9_4` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libfastjson` | `0.99.9-5.el9` | controller-rhel9, hub-rhel9 |
| `libfdisk` | `2.37.4-21.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libffi` | `3.4.2-8.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libfido2` | `1.13.0-2.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `libgcc` | `11.5.0-5.el9_5` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libgcrypt` | `1.10.0-11.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libgfortran` | `11.5.0-5.el9_5` | controller-rhel9, ee-supported-rhel9 |
| `libgomp` | `11.5.0-5.el9_5` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `libgpg-error` | `1.42-5.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libicu` | `67.1-10.el9_6` | postgresql-15 |
| `libidn2` | `2.3.0-7.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libjpeg-turbo` | `2.0.90-7.el9` | eda-controller-ui-rhel9, hub-rhel9, hub-web-rhel9 |
| `libkadm5` | `1.21.1-8.el9_6` | controller-rhel9, de-supported-rhel9, ee-minimal-rhel9, ee-supported-rhel9 |
| `libksba` | `1.5.1-7.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libmaxminddb` | `1.5.2-4.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `libmnl` | `1.0.4-16.el9_4` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `libmodulemd` | `2.13.0-2.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libmount` | `2.37.4-21.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libnghttp2` | `1.43.0-6.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libnsl2` | `2.0.0-1.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, receptor-rhel9 |
| `libpeas` | `1.30.0-4.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, receptor-rhel9 |
| `libpipeline` | `1.5.3-4.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15, redis-6 |
| `libpkgconf` | `1.7.3-10.el9` | ee-supported-rhel9, pcp |
| `libpng` | `1.6.37-12.el9` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `libpq` | `13.20-1.el9_5` | de-supported-rhel9, eda-controller-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `libpwquality` | `1.4.4-8.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libquadmath` | `11.5.0-5.el9_5` | controller-rhel9, ee-supported-rhel9 |
| `librepo` | `1.14.5-2.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libreport-filesystem` | `2.15.2-6.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `librhsm` | `0.0.3-9.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libseccomp` | `2.5.2-2.el9` | controller-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libsecret` | `0.20.4-4.el9` | hub-rhel9 |
| `libselinux` | `3.6-3.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libselinux-utils` | `3.6-3.el9` | controller-rhel9, eda-controller-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, receptor-rhel9, redis-6 |
| `libsemanage` | `3.6-5.el9_6` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libsepol` | `3.6-2.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libserf` | `1.3.9-27.el9` | controller-rhel9, ee-supported-rhel9 |
| `libsigsegv` | `2.13-4.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libsmartcols` | `2.37.4-21.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libsolv` | `0.7.24-3.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libss` | `1.46.5-7.el9` | controller-rhel9, de-supported-rhel9, ee-minimal-rhel9, ee-supported-rhel9 |
| `libssh` | `0.10.4-13.el9` | ee-supported-rhel9 |
| `libssh-config` | `0.10.4-13.el9` | ee-supported-rhel9 |
| `libstdc++` | `11.5.0-5.el9_5` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libtasn1` | `4.16.0-9.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libtiff` | `4.4.0-13.el9` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `libtirpc` | `1.3.3-9.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, receptor-rhel9 |
| `libtool-ltdl` | `2.4.6-46.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libunistring` | `0.9.10-15.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `liburing` | `2.5-1.el9` | ee-supported-rhel9 |
| `libusbx` | `1.0.26-1.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, receptor-rhel9 |
| `libuser` | `0.63-16.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `libutempter` | `1.2.1-6.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libuuid` | `2.37.4-21.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libuv` | `1.42.0-2.el9_4` | eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15 |
| `libverto` | `0.3.2-3.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libwebp` | `1.2.0-8.el9_3` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `libX11` | `1.7.0-11.el9` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `libX11-common` | `1.7.0-11.el9` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `libXau` | `1.0.9-8.el9` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `libxcb` | `1.13.1-9.el9` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `libxcrypt` | `4.4.18-3.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libxml2` | `2.9.13-12.el9_6` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libXpm` | `3.5.13-10.el9` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `libxslt` | `1.1.34-13.el9_6` | controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-web-rhel9, postgresql-15 |
| `libyaml` | `0.2.5-7.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `libzstd` | `1.5.5-1.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `lksctp-tools` | `1.0.19-3.el9_4` | de-supported-rhel9 |
| `lmdb-libs` | `0.9.29-3.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `logrotate` | `3.18.0-9.el9` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, redis-6 |
| `lua` | `5.4.4-4.el9` | de-supported-rhel9 |
| `lua-libs` | `5.4.4-4.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `lua-posix` | `35.0-8.el9` | de-supported-rhel9 |
| `lz4-libs` | `1.9.3-5.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `mailcap` | `2.1.49-5.el9` | de-supported-rhel9, ee-supported-rhel9, hub-rhel9 |
| `man-db` | `2.9.3-7.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15, redis-6 |
| `microdnf` | `3.9.1-3.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, receptor-rhel9 |
| `mpdecimal` | `2.5.1-3.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, receptor-rhel9 |
| `mpfr` | `4.1.0-7.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `ncurses` | `6.2-10.20210508.el9_6.2` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `ncurses-base` | `6.2-10.20210508.el9_6.2` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `ncurses-libs` | `6.2-10.20210508.el9_6.2` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `nettle` | `3.10.1-1.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `nginx` | `1.24.0-4.module+el9.5.0+22954+e2d70a1c.1` | controller-rhel9, eda-controller-ui-rhel9, gateway-rhel9, hub-web-rhel9 |
| `nginx-all-modules` | `1.24.0-4.module+el9.5.0+22954+e2d70a1c.1` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `nginx-core` | `1.24.0-4.module+el9.5.0+22954+e2d70a1c.1` | controller-rhel9, eda-controller-ui-rhel9, gateway-rhel9, hub-web-rhel9 |
| `nginx-filesystem` | `1.24.0-4.module+el9.5.0+22954+e2d70a1c.1` | controller-rhel9, eda-controller-ui-rhel9, gateway-rhel9, hub-web-rhel9 |
| `nginx-mod-http-image-filter` | `1.24.0-4.module+el9.5.0+22954+e2d70a1c.1` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `nginx-mod-http-perl` | `1.24.0-4.module+el9.5.0+22954+e2d70a1c.1` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `nginx-mod-http-xslt-filter` | `1.24.0-4.module+el9.5.0+22954+e2d70a1c.1` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `nginx-mod-mail` | `1.24.0-4.module+el9.5.0+22954+e2d70a1c.1` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `nginx-mod-stream` | `1.24.0-4.module+el9.5.0+22954+e2d70a1c.1` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `npth` | `1.6-8.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `nspr` | `4.36.0-4.el9_4` | de-supported-rhel9 |
| `nss` | `3.112.0-4.el9_4` | de-supported-rhel9 |
| `nss-softokn` | `3.112.0-4.el9_4` | de-supported-rhel9 |
| `nss-softokn-freebl` | `3.112.0-4.el9_4` | de-supported-rhel9 |
| `nss-sysinit` | `3.112.0-4.el9_4` | de-supported-rhel9 |
| `nss-util` | `3.112.0-4.el9_4` | de-supported-rhel9 |
| `nss_wrapper-libs` | `1.1.13-1.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `numactl-libs` | `2.0.19-1.el9` | ee-supported-rhel9 |
| `oniguruma` | `6.9.6-1.el9.6` | hub-rhel9 |
| `openblas` | `0.3.26-2.el9` | controller-rhel9, ee-supported-rhel9 |
| `openblas-openmp` | `0.3.26-2.el9` | controller-rhel9, ee-supported-rhel9 |
| `openldap` | `2.6.8-4.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `openshift-clients` | `4.14.0-202507050036.p0.g44b3ac2.assembly.stream.el9` | ee-supported-rhel9 |
| `openssh` | `8.7p1-45.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `openssh-clients` | `8.7p1-45.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `openssl` | `3.2.2-6.el9_5.1` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `openssl-fips-provider` | `3.0.7-6.el9_5` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `openssl-fips-provider-so` | `3.0.7-6.el9_5` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `openssl-libs` | `3.2.2-6.el9_5.1` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `p11-kit` | `0.25.3-3.el9_5` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `p11-kit-trust` | `0.25.3-3.el9_5` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `pam` | `1.5.1-26.el9_6` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `passwd` | `0.80-12.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `pcp` | `6.3.7-1.el9_6` | pcp |
| `pcp-conf` | `6.3.7-1.el9_6` | pcp |
| `pcp-doc` | `6.3.7-1.el9_6` | pcp |
| `pcp-libs` | `6.3.7-1.el9_6` | pcp |
| `pcp-pmda-dm` | `6.3.7-1.el9_6` | pcp |
| `pcp-pmda-nfsclient` | `6.3.7-1.el9_6` | pcp |
| `pcp-pmda-openmetrics` | `6.3.7-1.el9_6` | pcp |
| `pcp-system-tools` | `6.3.7-1.el9_6` | pcp |
| `pcp-zeroconf` | `6.3.7-1.el9_6` | pcp |
| `pcre` | `8.44-4.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `pcre2` | `10.40-6.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `pcre2-syntax` | `10.40-6.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `perl-AutoLoader` | `5.74-481.1.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-B` | `1.80-481.1.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-base` | `2.27-481.1.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Carp` | `1.50-460.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Class-Struct` | `0.66-481.1.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-constant` | `1.33-461.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Data-Dumper` | `2.174-462.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Digest` | `1.19-4.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Digest-MD5` | `2.58-4.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Encode` | `3.08-462.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Errno` | `1.30-481.1.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Exporter` | `5.74-461.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Fcntl` | `1.13-481.1.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-File-Basename` | `2.85-481.1.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-File-Path` | `2.18-4.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-File-stat` | `1.09-481.1.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-File-Temp` | `0.231.100-4.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-FileHandle` | `2.03-481.1.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Getopt-Long` | `2.52-4.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Getopt-Std` | `1.12-481.1.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-HTTP-Tiny` | `0.076-462.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-if` | `0.60.800-481.1.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-interpreter` | `5.32.1-481.1.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-IO` | `1.43-481.1.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-IO-Socket-IP` | `0.41-5.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-IO-Socket-SSL` | `2.073-2.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-IPC-Open3` | `1.21-481.1.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-libnet` | `3.13-4.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-libs` | `5.32.1-481.1.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-MIME-Base64` | `3.16-4.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Mozilla-CA` | `20200520-6.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-mro` | `1.23-481.1.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-NDBM_File` | `1.15-481.1.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Net-SSLeay` | `1.94-1.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-overload` | `1.31-481.1.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-overloading` | `0.02-481.1.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-parent` | `0.238-460.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-PathTools` | `3.78-461.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Pod-Escapes` | `1.07-460.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Pod-Perldoc` | `3.28.01-461.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Pod-Simple` | `3.42-4.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Pod-Usage` | `2.01-4.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-podlators` | `4.14-460.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-POSIX` | `1.94-481.1.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Scalar-List-Utils` | `1.56-462.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-SelectSaver` | `1.02-481.1.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Socket` | `2.031-4.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Storable` | `3.21-460.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-subs` | `1.03-481.1.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Symbol` | `1.08-481.1.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Term-ANSIColor` | `5.01-461.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Term-Cap` | `1.17-460.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Text-ParseWords` | `3.30-460.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Text-Tabs+Wrap` | `2013.0523-460.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-Time-Local` | `1.300-7.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-URI` | `5.09-3.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `perl-vars` | `1.05-481.1.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `pgaudit` | `1.7.0-1.module+el9.2.0+17405+aeb9ec60` | postgresql-15 |
| `pinentry` | `1.1.1-8.el9` | hub-rhel9 |
| `pkgconf` | `1.7.3-10.el9` | ee-supported-rhel9, pcp |
| `pkgconf-m4` | `1.7.3-10.el9` | ee-supported-rhel9, pcp |
| `pkgconf-pkg-config` | `1.7.3-10.el9` | ee-supported-rhel9, pcp |
| `podman-remote` | `5.4.0-13.el9_6` | controller-rhel9, eda-controller-rhel9, ee-supported-rhel9, receptor-rhel9 |
| `policycoreutils` | `3.6-2.1.el9` | controller-rhel9, eda-controller-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, receptor-rhel9, redis-6 |
| `popt` | `1.18-8.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `postgresql` | `15.14-1.module+el9.6.0+23419+7863ab62` | controller-rhel9, eda-controller-rhel9, gateway-rhel9, postgresql-15 |
| `postgresql-contrib` | `15.14-1.module+el9.6.0+23419+7863ab62` | postgresql-15 |
| `postgresql-private-libs` | `15.14-1.module+el9.6.0+23419+7863ab62` | controller-rhel9, eda-controller-rhel9, gateway-rhel9, postgresql-15 |
| `postgresql-server` | `15.14-1.module+el9.6.0+23419+7863ab62` | postgresql-15 |
| `postgresql-upgrade` | `15.14-1.module+el9.6.0+23419+7863ab62` | postgresql-15 |
| `procps-ng` | `3.3.17-14.el9` | eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `protobuf-c` | `1.3.3-13.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `psmisc` | `23.4-3.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `pulpcore-selinux` | `2.0.1-1.el9ap` | hub-rhel9 |
| `python3` | `3.9.21-2.el9_6.2` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `python3-cffi` | `1.15.0-3.el9ap` | controller-rhel9, eda-controller-rhel9, gateway-rhel9, hub-rhel9 |
| `python3-chardet` | `4.0.0-5.el9` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `python3-cloud-what` | `1.29.45.1-1.el9_6` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-cryptography` | `42.0.5-1.el9ap` | controller-rhel9, eda-controller-rhel9, gateway-rhel9, hub-rhel9 |
| `python3-dateutil` | `2.8.1-7.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-dbus` | `1.2.18-2.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-decorator` | `4.4.2-6.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-dnf` | `4.14.0-25.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-dnf-plugins-core` | `4.3.0-20.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-gobject-base` | `3.40.1-6.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-gobject-base-noarch` | `3.40.1-6.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-gpg` | `1.15.1-6.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-hawkey` | `0.69.0-13.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-idna` | `2.10-7.el9_4.1` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `python3-iniparse` | `0.4-45.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-inotify` | `0.9.6-25.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-libcomps` | `0.1.18-1.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-libdnf` | `0.69.0-13.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-librepo` | `1.14.5-2.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-libs` | `3.9.21-2.el9_6.2` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `python3-libselinux` | `3.6-3.el9` | controller-rhel9 |
| `python3-libsemanage` | `3.6-5.el9_6` | controller-rhel9 |
| `python3-pcp` | `6.3.7-1.el9_6` | pcp |
| `python3-pexpect` | `4.8.0-7.el9` | controller-rhel9, ee-supported-rhel9, hub-rhel9, receptor-rhel9 |
| `python3-pip-wheel` | `21.3.1-1.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `python3-ptyprocess` | `0.6.0-12.el9` | controller-rhel9, ee-supported-rhel9, hub-rhel9, receptor-rhel9 |
| `python3-pycparser` | `2.21-2.el9pc` | controller-rhel9, eda-controller-rhel9, gateway-rhel9, hub-rhel9 |
| `python3-pysocks` | `1.7.1-12.el9` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `python3-pyyaml` | `5.4.1-6.el9` | controller-rhel9, ee-supported-rhel9, hub-rhel9, receptor-rhel9 |
| `python3-requests` | `2.25.1-10.el9_6` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `python3-rpm` | `4.16.1.3-37.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-setuptools` | `53.0.0-13.el9_6.1` | controller-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `python3-setuptools-wheel` | `53.0.0-13.el9_6.1` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `python3-six` | `1.15.0-9.el9` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `python3-subscription-manager-rhsm` | `1.29.45.1-1.el9_6` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-systemd` | `234-19.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-urllib3` | `1.26.5-6.el9` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `python3.11` | `3.11.11-2.el9_6.2` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, receptor-rhel9 |
| `python3.11-adal` | `1.2.7-1.el9ap` | eda-controller-rhel9 |
| `python3.11-aiodns` | `3.2.0-1.el9ap` | de-supported-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-aiofiles` | `23.2.1-1.el9ap` | hub-rhel9 |
| `python3.11-aiohappyeyeballs` | `2.4.4-1.el9ap` | de-supported-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-aiohttp` | `3.10.11-1.el9ap` | de-supported-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-aiosignal` | `1.3.1-1.el9ap` | de-supported-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-ansible-compat` | `25.8.1-1.el9ap` | ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-ansible-pylibssh` | `1.2.2-1.el9ap` | ee-supported-rhel9 |
| `python3.11-ansible-runner` | `2.4.1-1.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, receptor-rhel9 |
| `python3.11-argon2-cffi` | `23.1.0-1.el9ap` | gateway-rhel9 |
| `python3.11-argon2-cffi-bindings` | `21.2.0-1.el9ap` | gateway-rhel9 |
| `python3.11-asgiref` | `3.7.2-1.el9ap` | eda-controller-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-async-lru` | `2.0.4-1.el9ap` | hub-rhel9 |
| `python3.11-async-timeout` | `4.0.3-2.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-asyncio-throttle` | `1.0.2-4.el9ap` | hub-rhel9 |
| `python3.11-attrs` | `22.2.0-1.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-autobahn` | `24.4.2-1.el9ap` | eda-controller-rhel9 |
| `python3.11-Automat` | `22.10.0-3.el9ap` | eda-controller-rhel9 |
| `python3.11-awx-plugins-core` | `0.0.1~a10-1.el9ap` | eda-controller-rhel9 |
| `python3.11-awx-plugins-core+credentials-aim` | `0.0.1~a10-1.el9ap` | eda-controller-rhel9 |
| `python3.11-awx-plugins-core+credentials-aws-secretsmanager-credential` | `0.0.1~a10-1.el9ap` | eda-controller-rhel9 |
| `python3.11-awx-plugins-core+credentials-azure-kv` | `0.0.1~a10-1.el9ap` | eda-controller-rhel9 |
| `python3.11-awx-plugins-core+credentials-centrify-vault-kv` | `0.0.1~a10-1.el9ap` | eda-controller-rhel9 |
| `python3.11-awx-plugins-core+credentials-conjur` | `0.0.1~a10-1.el9ap` | eda-controller-rhel9 |
| `python3.11-awx-plugins-core+credentials-github-app` | `0.0.1~a10-1.el9ap` | eda-controller-rhel9 |
| `python3.11-awx-plugins-core+credentials-hashivault-kv` | `0.0.1~a10-1.el9ap` | eda-controller-rhel9 |
| `python3.11-awx-plugins-core+credentials-hashivault-ssh` | `0.0.1~a10-1.el9ap` | eda-controller-rhel9 |
| `python3.11-awx-plugins-core+credentials-thycotic-dsv` | `0.0.1~a10-1.el9ap` | eda-controller-rhel9 |
| `python3.11-awx-plugins-core+credentials-thycotic-tss` | `0.0.1~a10-1.el9ap` | eda-controller-rhel9 |
| `python3.11-awx-plugins-interfaces` | `0.0.1~a5-1.el9ap` | eda-controller-rhel9 |
| `python3.11-azure-core` | `1.34.0-1.el9ap` | de-supported-rhel9, eda-controller-rhel9, hub-rhel9 |
| `python3.11-azure-identity` | `1.23.0-1.el9ap` | eda-controller-rhel9 |
| `python3.11-azure-keyvault` | `4.2.0-1.el9ap` | eda-controller-rhel9 |
| `python3.11-azure-keyvault-certificates` | `4.10.0-1.el9ap` | eda-controller-rhel9 |
| `python3.11-azure-keyvault-keys` | `4.11.0-1.el9ap` | eda-controller-rhel9 |
| `python3.11-azure-keyvault-secrets` | `4.10.0-1.el9ap` | eda-controller-rhel9 |
| `python3.11-azure-storage-blob` | `12.19.0-1.el9ap` | hub-rhel9 |
| `python3.11-backoff` | `2.2.1-1.el9ap` | hub-rhel9 |
| `python3.11-black` | `24.4.2-2.el9ap` | ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-boto3` | `1.34.30-1.el9ap` | eda-controller-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-botocore` | `1.34.30-1.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-bracex` | `2.4-1.el9ap` | ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-brotli` | `1.1.0-1.el9ap` | de-supported-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-cachetools` | `5.3.2-1.el9ap` | eda-controller-rhel9, ee-supported-rhel9 |
| `python3.11-certifi` | `2023.5.7-1.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-cffi` | `1.15.1-1.el9` | de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-channels` | `4.0.0-3.el9ap` | eda-controller-rhel9 |
| `python3.11-channels+daphne` | `4.0.0-3.el9ap` | eda-controller-rhel9 |
| `python3.11-chardet` | `5.2.0-2.el9ap` | ee-supported-rhel9 |
| `python3.11-charset-normalizer` | `2.1.0-1.el9` | de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-click` | `8.1.7-1.el9ap` | eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9, receptor-rhel9 |
| `python3.11-constantly` | `15.1.0-2.el9ap` | eda-controller-rhel9 |
| `python3.11-croniter` | `2.0.1-1.el9ap` | eda-controller-rhel9 |
| `python3.11-cryptography` | `42.0.5-1.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-daemon` | `2.3.2-1.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, receptor-rhel9 |
| `python3.11-daphne` | `4.0.0-3.el9ap` | eda-controller-rhel9 |
| `python3.11-dateutil` | `2.8.2-2.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-supported-rhel9, hub-rhel9, receptor-rhel9 |
| `python3.11-defusedxml` | `0.7.1-4.el9ap` | gateway-rhel9, hub-rhel9 |
| `python3.11-deprecated` | `1.2.14-1.el9ap` | eda-controller-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-diff-match-patch` | `20230430-1.el9ap` | hub-rhel9 |
| `python3.11-dispatcherd` | `2025.5.19-2.el9ap` | eda-controller-rhel9 |
| `python3.11-dispatcherd+pg_notify` | `2025.5.19-2.el9ap` | eda-controller-rhel9 |
| `python3.11-distlib` | `0.3.8-1.el9ap` | ee-supported-rhel9 |
| `python3.11-distro` | `1.9.0-1.el9ap` | eda-controller-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-django` | `4.2.24-1.el9ap` | eda-controller-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-django-ansible-base` | `2.6.20251001-1.el9ap` | eda-controller-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-django-ansible-base+activitystream` | `2.6.20251001-1.el9ap` | gateway-rhel9 |
| `python3.11-django-ansible-base+api_documentation` | `2.6.20251001-1.el9ap` | gateway-rhel9 |
| `python3.11-django-ansible-base+authentication` | `2.6.20251001-1.el9ap` | gateway-rhel9 |
| `python3.11-django-ansible-base+channel_auth` | `2.6.20251001-1.el9ap` | eda-controller-rhel9 |
| `python3.11-django-ansible-base+feature_flags` | `2.6.20251001-1.el9ap` | eda-controller-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-django-ansible-base+jwt_consumer` | `2.6.20251001-1.el9ap` | eda-controller-rhel9, hub-rhel9 |
| `python3.11-django-ansible-base+oauth2_provider` | `2.6.20251001-1.el9ap` | gateway-rhel9 |
| `python3.11-django-ansible-base+rbac` | `2.6.20251001-1.el9ap` | eda-controller-rhel9, gateway-rhel9 |
| `python3.11-django-ansible-base+redis_client` | `2.6.20251001-1.el9ap` | eda-controller-rhel9, gateway-rhel9 |
| `python3.11-django-ansible-base+resource_registry` | `2.6.20251001-1.el9ap` | eda-controller-rhel9 |
| `python3.11-django-ansible-base+rest_filters` | `2.6.20251001-1.el9ap` | eda-controller-rhel9, gateway-rhel9 |
| `python3.11-django-auth-ldap` | `4.0.0-2.el9ap` | gateway-rhel9, hub-rhel9 |
| `python3.11-django-automated-logging` | `6.2.2-1.el9ap` | hub-rhel9 |
| `python3.11-django-crum` | `0.7.9-2.el9ap` | eda-controller-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-django-dynamic-preferences` | `1.16.0-1.el9ap` | gateway-rhel9 |
| `python3.11-django-extensions` | `3.2.3-2.el9ap` | gateway-rhel9 |
| `python3.11-django-filter` | `23.5-1.el9ap` | eda-controller-rhel9, hub-rhel9 |
| `python3.11-django-flags` | `5.0.13-1.el9ap` | eda-controller-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-django-guid` | `3.4.0-1.el9ap` | hub-rhel9 |
| `python3.11-django-import-export` | `3.3.6-2.el9ap` | hub-rhel9 |
| `python3.11-django-ipware` | `6.0.5-1.el9ap` | hub-rhel9 |
| `python3.11-django-lifecycle` | `1.1.2-1.el9ap` | hub-rhel9 |
| `python3.11-django-oauth-toolkit` | `2.3.0-1.el9ap` | gateway-rhel9 |
| `python3.11-django-picklefield` | `3.1-1.el9ap` | hub-rhel9 |
| `python3.11-django-prometheus` | `2.3.1-2.el9ap` | hub-rhel9 |
| `python3.11-django-redis` | `5.4.0-1.el9ap` | eda-controller-rhel9, gateway-rhel9 |
| `python3.11-django-rq` | `2.8.0-1.el9ap` | eda-controller-rhel9 |
| `python3.11-django-split-settings` | `1.2.0-2.el9ap` | eda-controller-rhel9 |
| `python3.11-django-storages` | `1.14.2-2.el9ap` | hub-rhel9 |
| `python3.11-django-storages+azure` | `1.14.2-2.el9ap` | hub-rhel9 |
| `python3.11-django-storages+s3` | `1.14.2-2.el9ap` | hub-rhel9 |
| `python3.11-djangorestframework` | `3.15.1-1.el9ap` | eda-controller-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-djangorestframework-queryfields` | `1.1.0-1.el9ap` | hub-rhel9 |
| `python3.11-docutils` | `0.20.1-2.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, receptor-rhel9 |
| `python3.11-dpath` | `2.1.6-1.el9ap` | de-supported-rhel9, ee-supported-rhel9 |
| `python3.11-drf-access-policy` | `1.5.0-1.el9ap` | hub-rhel9 |
| `python3.11-drf-nested-routers` | `0.93.5-1.el9ap` | hub-rhel9 |
| `python3.11-drf-spectacular` | `0.26.5-2.el9ap` | eda-controller-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-drools-jpy` | `0.3.14-1.el9ap` | de-supported-rhel9 |
| `python3.11-drools-jpy-jar` | `1.0.11-1.Final_redhat_00001.1.el9ap` | de-supported-rhel9 |
| `python3.11-dsv-sdk` | `1.0.4-1.el9ap` | eda-controller-rhel9 |
| `python3.11-dynaconf` | `3.2.11-1.el9ap` | eda-controller-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-ecdsa` | `0.18.0-1.el9ap` | eda-controller-rhel9 |
| `python3.11-et-xmlfile` | `1.1.0-3.el9ap` | hub-rhel9 |
| `python3.11-filelock` | `3.13.1-1.el9ap` | ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-flake8` | `6.1.0-2.el9ap` | hub-rhel9 |
| `python3.11-frozenlist` | `1.4.0-1.el9ap` | de-supported-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-galaxy-importer` | `0.4.33-1.el9ap` | hub-rhel9 |
| `python3.11-galaxy-ng` | `4.11.0-1.el9ap` | hub-rhel9 |
| `python3.11-gitdb` | `4.0.11-1.el9ap` | hub-rhel9 |
| `python3.11-gitpython` | `3.1.41-1.el9ap` | hub-rhel9 |
| `python3.11-gnupg` | `0.5.2-1.el9ap` | eda-controller-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-google-auth` | `2.27.0-1.el9ap` | eda-controller-rhel9, ee-supported-rhel9 |
| `python3.11-googleapis-common-protos` | `1.59.1-2.el9ap` | gateway-rhel9, hub-rhel9 |
| `python3.11-grpcio` | `1.58.3-1.el9ap` | ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-grpcio-tools` | `1.58.3-1.el9ap` | gateway-rhel9 |
| `python3.11-gunicorn` | `22.0.0-1.el9ap` | eda-controller-rhel9, hub-rhel9 |
| `python3.11-hyperlink` | `21.0.0-2.el9ap` | eda-controller-rhel9 |
| `python3.11-idna` | `3.4-1.el9` | de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-importlib-metadata` | `6.0.1-2.el9ap` | ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-incremental` | `24.7.2-1.el9ap` | eda-controller-rhel9 |
| `python3.11-inflection` | `0.5.1-4.el9ap` | eda-controller-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-insights-analytics-collector` | `0.3.2-2.el9ap` | eda-controller-rhel9, hub-rhel9 |
| `python3.11-ipware` | `3.0.0-1.el9ap` | hub-rhel9 |
| `python3.11-isodate` | `0.6.1-2.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-janus` | `1.0.0-2.el9ap` | de-supported-rhel9 |
| `python3.11-jinja2` | `3.1.6-1.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-jmespath` | `1.0.1-2.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-jpy` | `0.15.0-1.el9ap` | de-supported-rhel9 |
| `python3.11-jq` | `1.6.0-1.el9ap` | hub-rhel9 |
| `python3.11-json-stream` | `2.3.2-1.el9ap` | hub-rhel9 |
| `python3.11-json-stream-rs-tokenizer` | `0.4.26-1.el9ap` | hub-rhel9 |
| `python3.11-jsonschema` | `4.21.1-1.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-jsonschema-specifications` | `2023.12.1-1.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-jwcrypto` | `1.5.6-1.el9ap` | gateway-rhel9 |
| `python3.11-kubernetes` | `26.1.0-2.el9ap` | eda-controller-rhel9 |
| `python3.11-ldap` | `3.4.4-1.el9ap` | gateway-rhel9, hub-rhel9 |
| `python3.11-ldap-filter` | `1.0.1-1.el9ap` | gateway-rhel9 |
| `python3.11-libs` | `3.11.11-2.el9_6.2` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, receptor-rhel9 |
| `python3.11-lockfile` | `0.12.2-2.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, receptor-rhel9 |
| `python3.11-lxml` | `4.9.2-4.el9` | ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9 |
| `python3.11-markdown` | `3.5.2-1.el9ap` | hub-rhel9 |
| `python3.11-markuppy` | `1.14-4.el9ap` | hub-rhel9 |
| `python3.11-markupsafe` | `2.1.5-1.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-marshmallow` | `3.26.1-1.el9ap` | hub-rhel9 |
| `python3.11-mccabe` | `0.7.0-2.el9ap` | hub-rhel9 |
| `python3.11-msal` | `1.32.3-1.el9ap` | eda-controller-rhel9 |
| `python3.11-msal-extensions` | `1.3.1-1.el9ap` | eda-controller-rhel9 |
| `python3.11-msrest` | `0.7.1-2.el9ap` | eda-controller-rhel9 |
| `python3.11-msrestazure` | `0.6.4-1.el9ap` | eda-controller-rhel9 |
| `python3.11-multidict` | `6.0.4-1.el9ap` | de-supported-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-mypy-extensions` | `1.0.0-1.el9ap` | ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-netaddr` | `1.2.1-1.el9ap` | ee-supported-rhel9, gateway-rhel9 |
| `python3.11-nh3` | `0.2.18-1.el9ap` | hub-rhel9 |
| `python3.11-numpy` | `1.23.5-1.el9` | ee-supported-rhel9 |
| `python3.11-oauthlib` | `3.2.2-1.el9ap` | eda-controller-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-odfpy` | `1.4.1-8.el9ap` | hub-rhel9 |
| `python3.11-openpyxl` | `3.1.2-1.el9ap` | hub-rhel9 |
| `python3.11-opentelemetry-api` | `1.18.0-2.el9ap` | hub-rhel9 |
| `python3.11-opentelemetry-distro` | `0.39b0-6.el9ap` | hub-rhel9 |
| `python3.11-opentelemetry-distro+otlp` | `0.39b0-6.el9ap` | hub-rhel9 |
| `python3.11-opentelemetry-exporter-otlp` | `1.18.0-2.el9ap` | hub-rhel9 |
| `python3.11-opentelemetry-exporter-otlp-proto-common` | `1.18.0-2.el9ap` | hub-rhel9 |
| `python3.11-opentelemetry-exporter-otlp-proto-grpc` | `1.18.0-2.el9ap` | hub-rhel9 |
| `python3.11-opentelemetry-exporter-otlp-proto-http` | `1.18.0-2.el9ap` | hub-rhel9 |
| `python3.11-opentelemetry-instrumentation` | `0.39b0-6.el9ap` | hub-rhel9 |
| `python3.11-opentelemetry-instrumentation-django` | `0.39b0-6.el9ap` | hub-rhel9 |
| `python3.11-opentelemetry-instrumentation-wsgi` | `0.39b0-6.el9ap` | hub-rhel9 |
| `python3.11-opentelemetry-proto` | `1.18.0-2.el9ap` | gateway-rhel9, hub-rhel9 |
| `python3.11-opentelemetry-sdk` | `1.18.0-2.el9ap` | hub-rhel9 |
| `python3.11-opentelemetry-semantic-conventions` | `0.39b0-2.el9ap` | hub-rhel9 |
| `python3.11-opentelemetry-util-http` | `0.39b0-6.el9ap` | hub-rhel9 |
| `python3.11-packaging` | `23.2-1.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9, receptor-rhel9 |
| `python3.11-parsley` | `1.3-3.el9ap` | hub-rhel9 |
| `python3.11-pathspec` | `0.12.1-1.el9ap` | ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-pbr` | `6.0.0-2.el9ap` | ee-supported-rhel9, hub-rhel9 |
| `python3.11-persisting-theory` | `1.0-2.el9ap` | gateway-rhel9 |
| `python3.11-pexpect` | `4.9.0-1.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, receptor-rhel9 |
| `python3.11-pillow` | `10.3.0-1.el9ap` | hub-rhel9 |
| `python3.11-pip` | `22.3.1-5.el9` | de-supported-rhel9, ee-minimal-rhel9, ee-supported-rhel9 |
| `python3.11-pip-wheel` | `22.3.1-5.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, receptor-rhel9 |
| `python3.11-platformdirs` | `4.2.0-1.el9ap` | ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-ply` | `3.11-1.el9` | de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-podman` | `5.4.0.1-1.el9ap` | eda-controller-rhel9 |
| `python3.11-prometheus-client` | `0.19.0-1.el9ap` | hub-rhel9 |
| `python3.11-protobuf` | `4.21.12-2.el9ap` | ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-psycopg` | `3.2.7-1.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-psycopg+c` | `3.2.7-1.el9ap` | de-supported-rhel9 |
| `python3.11-psycopg-c` | `3.2.7-1.el9ap` | de-supported-rhel9 |
| `python3.11-ptyprocess` | `0.7.0-1.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, receptor-rhel9 |
| `python3.11-pulp-ansible` | `0.25.1-1.el9ap` | hub-rhel9 |
| `python3.11-pulp-container` | `2.19.3-1.el9ap` | hub-rhel9 |
| `python3.11-pulp-glue` | `0.23.2-1.el9ap` | hub-rhel9 |
| `python3.11-pulpcore` | `3.49.42-1.el9ap` | hub-rhel9 |
| `python3.11-pyasn1` | `0.5.1-1.el9ap` | eda-controller-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-pyasn1-modules` | `0.3.0-1.el9ap` | eda-controller-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-pycares` | `4.4.0-2.el9ap` | de-supported-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-pycodestyle` | `2.11.1-1.el9ap` | hub-rhel9 |
| `python3.11-pycparser` | `2.20-1.el9` | de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-pydantic` | `1.10.15-1.el9ap` | eda-controller-rhel9 |
| `python3.11-pyflakes` | `3.1.0-1.el9ap` | hub-rhel9 |
| `python3.11-pygithub` | `2.6.1-1.el9ap` | eda-controller-rhel9 |
| `python3.11-pygments` | `2.17.2-2.el9ap` | ee-supported-rhel9 |
| `python3.11-pygtrie` | `2.5.0-2.el9ap` | hub-rhel9 |
| `python3.11-pyjwt` | `2.7.0-2.el9ap` | eda-controller-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-pyjwt+crypto` | `2.7.0-2.el9ap` | eda-controller-rhel9 |
| `python3.11-pynacl` | `1.5.0-1.el9ap` | eda-controller-rhel9 |
| `python3.11-pyOpenSSL` | `24.1.0-1.el9ap` | eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-pyparsing` | `3.1.1-1.el9ap` | de-supported-rhel9, hub-rhel9 |
| `python3.11-pyrad` | `2.4-2.el9ap` | gateway-rhel9 |
| `python3.11-pysocks` | `1.7.1-1.el9` | ee-minimal-rhel9, ee-supported-rhel9 |
| `python3.11-python3-openid` | `3.2.0-3.el9ap` | gateway-rhel9, hub-rhel9 |
| `python3.11-python3-saml` | `1.16.0-2.el9ap` | gateway-rhel9 |
| `python3.11-pytz` | `2024.1-1.el9ap` | eda-controller-rhel9, ee-supported-rhel9 |
| `python3.11-pyyaml` | `6.0-1.el9` | de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, receptor-rhel9 |
| `python3.11-redis` | `4.6.0-2.el9ap` | eda-controller-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-referencing` | `0.36.2-1.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-requests` | `2.28.1-1.el9` | ee-minimal-rhel9 |
| `python3.11-requests` | `2.31.0-2.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-requests-oauthlib` | `1.3.1-1.el9ap` | eda-controller-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-resolvelib` | `1.0.1-1.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-rpds-py` | `0.18.1-1.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-rq` | `1.13.0-3.el9ap` | eda-controller-rhel9 |
| `python3.11-rq-scheduler` | `0.10.0-3.el9ap` | eda-controller-rhel9 |
| `python3.11-rsa` | `4.9-2.el9ap` | eda-controller-rhel9, ee-supported-rhel9 |
| `python3.11-ruamel-yaml` | `0.18.15-1.el9ap` | ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-ruamel-yaml-clib` | `0.2.8-1.el9ap` | ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-s3transfer` | `0.10.0-1.el9ap` | eda-controller-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-semantic-version` | `2.10.0-2.el9ap` | hub-rhel9 |
| `python3.11-service-identity` | `21.1.0-2.el9ap` | eda-controller-rhel9 |
| `python3.11-setuptools` | `65.5.1-4.el9_6` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, receptor-rhel9 |
| `python3.11-setuptools-wheel` | `65.5.1-4.el9_6` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, receptor-rhel9 |
| `python3.11-six` | `1.16.0-1.el9` | de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, receptor-rhel9 |
| `python3.11-smmap` | `5.0.1-1.el9ap` | hub-rhel9 |
| `python3.11-social-auth-app-django` | `5.4.1-1.el9ap` | gateway-rhel9, hub-rhel9 |
| `python3.11-social-auth-core` | `4.5.4-1.el9ap` | gateway-rhel9, hub-rhel9 |
| `python3.11-sqlparse` | `0.5.3-2.el9ap` | eda-controller-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-subprocess-tee` | `0.4.1-2.el9ap` | ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-tablib` | `3.5.0-1.el9ap` | hub-rhel9 |
| `python3.11-tablib+html` | `3.5.0-1.el9ap` | hub-rhel9 |
| `python3.11-tablib+ods` | `3.5.0-1.el9ap` | hub-rhel9 |
| `python3.11-tablib+xls` | `3.5.0-1.el9ap` | hub-rhel9 |
| `python3.11-tablib+xlsx` | `3.5.0-1.el9ap` | hub-rhel9 |
| `python3.11-tablib+yaml` | `3.5.0-1.el9ap` | hub-rhel9 |
| `python3.11-tabulate` | `0.9.0-3.el9ap` | ee-supported-rhel9, gateway-rhel9 |
| `python3.11-tacacs-plus` | `2.6-2.el9ap` | gateway-rhel9 |
| `python3.11-tss-sdk` | `1.2.3-1.el9ap` | eda-controller-rhel9 |
| `python3.11-twisted` | `24.7.0-1.el9ap` | eda-controller-rhel9 |
| `python3.11-twisted+tls` | `24.7.0-1.el9ap` | eda-controller-rhel9 |
| `python3.11-txaio` | `23.1.1-2.el9ap` | eda-controller-rhel9 |
| `python3.11-typing-extensions` | `4.9.0-1.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-uamqp` | `1.6.8-1.el9ap` | ee-supported-rhel9 |
| `python3.11-uritemplate` | `4.1.1-3.el9ap` | eda-controller-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-url-normalize` | `1.4.3-5.el9ap` | hub-rhel9 |
| `python3.11-urllib3` | `1.26.12-5.el9` | ee-minimal-rhel9 |
| `python3.11-urllib3` | `1.26.20-1.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `python3.11-uuid6` | `2024.1.12-1.el9ap` | hub-rhel9 |
| `python3.11-validators` | `0.34.0-1.el9ap` | eda-controller-rhel9 |
| `python3.11-watchdog` | `5.0.2-1.el9ap` | de-supported-rhel9, ee-supported-rhel9 |
| `python3.11-wcmatch` | `8.5-1.el9ap` | ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-websocket-client` | `1.7.0-2.el9ap` | eda-controller-rhel9, ee-supported-rhel9 |
| `python3.11-websockets` | `15.0-2.el9ap` | de-supported-rhel9 |
| `python3.11-whitenoise` | `6.6.0-1.el9ap` | hub-rhel9 |
| `python3.11-wrapt` | `1.16.0-1.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-xds-protos` | `1.58.0-2.el9ap` | gateway-rhel9 |
| `python3.11-xlrd` | `2.0.1-6.el9ap` | hub-rhel9 |
| `python3.11-xlwt` | `1.3.0-4.el9ap` | hub-rhel9 |
| `python3.11-xmlsec` | `1.3.13-2.el9ap` | gateway-rhel9 |
| `python3.11-xxhash` | `3.4.1-1.el9ap` | de-supported-rhel9, eda-controller-rhel9, ee-supported-rhel9 |
| `python3.11-yarl` | `1.13.1-1.el9ap` | de-supported-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-zipp` | `3.19.2-1.el9ap` | ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `python3.11-zope-interface` | `6.1-1.el9ap` | eda-controller-rhel9 |
| `qemu-img` | `9.1.0-15.el9_6.9` | ee-supported-rhel9 |
| `readline` | `8.1-4.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `receptor` | `1.5.7-2.el9ap` | ee-supported-rhel9, receptor-rhel9 |
| `receptorctl` | `1.5.7-2.el9ap` | ee-supported-rhel9, receptor-rhel9 |
| `redhat-logos-httpd` | `90.5-1.el9_6.1` | controller-rhel9, eda-controller-ui-rhel9, gateway-rhel9, hub-web-rhel9 |
| `redhat-release` | `9.6-0.1.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `redis` | `6.2.19-1.el9_6` | controller-rhel9, redis-6 |
| `rootfiles` | `8.1-34.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `rpm` | `4.16.1.3-37.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `rpm-build-libs` | `4.16.1.3-37.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `rpm-libs` | `4.16.1.3-37.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `rpm-plugin-selinux` | `4.16.1.3-37.el9` | controller-rhel9, eda-controller-rhel9, gateway-rhel9, hub-rhel9 |
| `rpm-sign-libs` | `4.16.1.3-37.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `rsync` | `3.2.5-3.el9` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, hub-web-rhel9, postgresql-15, redis-6 |
| `rsyslog` | `8.2412.0-1.el9` | controller-rhel9, hub-rhel9 |
| `scl-utils` | `2.0.3-4.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15, redis-6 |
| `sed` | `4.8-9.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `selinux-policy` | `38.1.53-5.el9_6` | controller-rhel9, eda-controller-rhel9, gateway-rhel9, hub-rhel9 |
| `selinux-policy-targeted` | `38.1.53-5.el9_6` | controller-rhel9, eda-controller-rhel9, gateway-rhel9, hub-rhel9 |
| `setup` | `2.13.7-10.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `shadow-utils` | `4.9-12.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `shadow-utils-subid` | `4.9-12.el9` | controller-rhel9, eda-controller-rhel9, ee-supported-rhel9, hub-rhel9, receptor-rhel9 |
| `skopeo` | `1.18.1-2.el9_6` | hub-rhel9 |
| `sos` | `4.9.2-1.el9_6` | controller-rhel9, ee-supported-rhel9, hub-rhel9, receptor-rhel9 |
| `sqlite-libs` | `3.34.1-8.el9_6` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `sshpass` | `1.09-5.el9ap` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `subscription-manager` | `1.29.45.1-1.el9_6` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `subscription-manager-rhsm-certificates` | `20220623-1.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `subversion` | `1.14.1-5.el9_0` | controller-rhel9, ee-supported-rhel9 |
| `subversion-libs` | `1.14.1-5.el9_0` | controller-rhel9, ee-supported-rhel9 |
| `supervisor` | `4.2.5-1.el9ap` | controller-rhel9, gateway-rhel9 |
| `systemd` | `252-51.el9_6.2` | controller-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `systemd-libs` | `252-51.el9_6.2` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `systemd-pam` | `252-51.el9_6.2` | controller-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `systemd-rpm-macros` | `252-51.el9_6.2` | controller-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `tar` | `1.34-7.el9` | de-supported-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `tcl` | `8.6.10-7.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15, redis-6 |
| `tpm2-tss` | `3.2.3-1.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `tzdata` | `2025b-1.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `tzdata-java` | `2025b-1.el9` | de-supported-rhel9 |
| `unzip` | `6.0-58.el9_5` | eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-web-rhel9, postgresql-15, redis-6 |
| `usermode` | `1.114-6.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `utf8proc` | `2.6.1-4.el9` | controller-rhel9, ee-supported-rhel9 |
| `util-linux` | `2.37.4-21.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `util-linux-core` | `2.37.4-21.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `uuid` | `1.6.2-55.el9` | postgresql-15 |
| `uwsgi` | `2.0.23-2.el9ap` | gateway-rhel9 |
| `vim-filesystem` | `8.2.2637-22.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15, redis-6 |
| `vim-minimal` | `8.2.2637-22.el9_6` | eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `virt-what` | `1.27-1.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `which` | `2.21-30.el9_6` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `xml-common` | `0.6.3-58.el9` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `xmlsec1` | `1.2.29-13.el9` | controller-rhel9, gateway-rhel9 |
| `xmlsec1-openssl` | `1.2.29-13.el9` | controller-rhel9, gateway-rhel9 |
| `xz` | `5.2.5-8.el9_0` | eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `xz-libs` | `5.2.5-8.el9_0` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `yajl` | `2.1.0-25.el9` | controller-rhel9, hub-rhel9 |
| `yamllint` | `1.35.1-1.el9ap` | ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9 |
| `yum` | `4.14.0-25.el9` | eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `zlib` | `1.2.11-40.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, receptor-rhel9, pcp, postgresql-15, redis-6 |
| `zstd` | `1.5.5-1.el9` | ee-minimal-rhel9, ee-supported-rhel9 |

## Python Packages (all images)

Every Python distribution found in any image (`image:environment prefix (python)`), from
`*.dist-info`/`*.egg-info` metadata. Names are normalized (PEP 503: lowercase, `-` separators). This covers system Python, `/usr/local` and application venvs.

| Package | Version | Images |
|---|---|---|
| `aap-eda` | `1.2.0` | eda-controller-rhel9:/usr (python3.11) |
| `aap-gateway` | `2.6.20251001` | gateway-rhel9:/usr (python3.11) |
| `adal` | `1.2.7` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `aiobotocore` | `2.11.2` | de-supported-rhel9:/usr/local (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `aiodns` | `3.2.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), de-supported-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `aiofiles` | `23.2.1` | hub-rhel9:/usr (python3.11) |
| `aiofiles` | `24.1.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `aiohappyeyeballs` | `2.4.3` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `aiohappyeyeballs` | `2.4.4` | de-supported-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `aiohttp` | `3.10.11` | de-supported-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `aiohttp` | `3.11.6` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `aiohttp-retry` | `2.8.3` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `aioitertools` | `0.11.0` | de-supported-rhel9:/usr/local (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `aiokafka` | `0.10.0` | de-supported-rhel9:/usr/local (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `aiosignal` | `1.3.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), de-supported-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `annotated-types` | `0.6.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `ansible-builder` | `3.1.0` | hub-rhel9:/usr (python3.11) |
| `ansible-compat` | `25.8.1` | ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `ansible-core` | `2.16.14` | de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `ansible-lint` | `25.8.2` | ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `ansible-pylibssh` | `1.2.2` | ee-supported-rhel9:/usr (python3.11) |
| `ansible-rulebook` | `1.2.0` | de-supported-rhel9:/usr (python3.11) |
| `ansible-runner` | `2.4.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), receptor-rhel9:/usr (python3.11) |
| `ansible-sign` | `0.1.2` | ee-supported-rhel9:/usr (python3.11) |
| `ansiconv` | `1.0.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `anyio` | `4.4.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `appdirs` | `1.4.4` | ee-supported-rhel9:/usr/local (python3.11) |
| `applicationinsights` | `0.11.10` | ee-supported-rhel9:/usr/local (python3.11) |
| `argcomplete` | `3.5.3` | ee-supported-rhel9:/usr/local (python3.11) |
| `argon2-cffi` | `23.1.0` | gateway-rhel9:/usr (python3.11) |
| `argon2-cffi-bindings` | `21.2.0` | gateway-rhel9:/usr (python3.11) |
| `asciichartpy` | `1.5.7` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `asgiref` | `3.7.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `asn1` | `2.7.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `async-lru` | `2.0.4` | hub-rhel9:/usr (python3.11) |
| `async-timeout` | `4.0.3` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `asyncio-throttle` | `1.0.2` | hub-rhel9:/usr (python3.11) |
| `attrs` | `22.2.0` | de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `attrs` | `23.2.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `autobahn` | `23.6.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `autobahn` | `24.4.2` | eda-controller-rhel9:/usr (python3.11) |
| `autocommand` | `2.2.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `automat` | `22.10.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11) |
| `awx` | `4.7.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `awx-plugins-core` | `0.0.1a10` | eda-controller-rhel9:/usr (python3.11) |
| `awx-plugins-interfaces` | `0.0.1a5` | eda-controller-rhel9:/usr (python3.11) |
| `awxkit` | `4.7.1` | ee-supported-rhel9:/usr (python3.11) |
| `azure-cli-core` | `2.74.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-cli-telemetry` | `1.1.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-common` | `1.1.28` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `azure-containerregistry` | `1.2.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-core` | `1.30.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `azure-core` | `1.31.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-core` | `1.34.0` | de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `azure-identity` | `1.15.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `azure-identity` | `1.19.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-identity` | `1.23.0` | eda-controller-rhel9:/usr (python3.11) |
| `azure-iot-hub` | `2.6.1` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-keyvault` | `4.2.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `azure-keyvault-certificates` | `4.10.0` | eda-controller-rhel9:/usr (python3.11) |
| `azure-keyvault-certificates` | `4.7.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `azure-keyvault-keys` | `4.11.0` | eda-controller-rhel9:/usr (python3.11) |
| `azure-keyvault-keys` | `4.8.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `azure-keyvault-secrets` | `4.10.0` | eda-controller-rhel9:/usr (python3.11) |
| `azure-keyvault-secrets` | `4.7.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `azure-keyvault-securitydomain` | `1.0.0b1` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-apimanagement` | `4.0.1` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-authorization` | `4.0.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-automation` | `1.1.0b4` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-batch` | `17.3.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-cdn` | `13.1.1` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-compute` | `33.0.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-containerinstance` | `10.1.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-containerregistry` | `10.3.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-containerservice` | `32.1.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-core` | `1.4.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-cosmosdb` | `10.0.0b3` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-datafactory` | `9.0.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-devtestlabs` | `10.0.0b2` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-dns` | `8.1.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-eventhub` | `11.1.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-hdinsight` | `9.1.0b1` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-iothub` | `3.0.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-keyvault` | `10.3.1` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-loganalytics` | `13.0.0b7` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-managedservices` | `7.0.0b2` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-managementgroups` | `1.1.0b2` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-marketplaceordering` | `1.2.0b2` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-monitor` | `6.0.2` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-mysqlflexibleservers` | `1.0.0b3` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-network` | `28.0.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-notificationhubs` | `8.1.0b1` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-nspkg` | `3.0.2` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-postgresqlflexibleservers` | `1.1.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-privatedns` | `1.2.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-rdbms` | `10.2.0b17` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-recoveryservices` | `3.0.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-recoveryservicesbackup` | `9.1.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-redis` | `14.4.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-resource` | `23.2.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-resourcegraph` | `8.0.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-resourcehealth` | `1.0.0b6` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-search` | `9.2.0b2` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-servicebus` | `8.2.1` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-sql` | `4.0.0b19` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-storage` | `21.2.1` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-trafficmanager` | `1.1.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-mgmt-web` | `7.3.1` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-nspkg` | `3.0.2` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-servicebus` | `7.12.1` | de-supported-rhel9:/usr/local (python3.11) |
| `azure-servicebus` | `7.14.2` | ee-supported-rhel9:/usr/local (python3.11) |
| `azure-storage-blob` | `12.19.0` | hub-rhel9:/usr (python3.11) |
| `azure-storage-blob` | `12.23.0b1` | ee-supported-rhel9:/usr/local (python3.11) |
| `backoff` | `2.2.1` | hub-rhel9:/usr (python3.11) |
| `bcrypt` | `3.2.0` | ee-minimal-rhel9:/usr/local (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `bindep` | `2.11.0` | hub-rhel9:/usr (python3.11) |
| `black` | `24.4.2` | ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `boto3` | `1.34.30` | eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `boto3` | `1.34.47` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `botocore` | `1.34.30` | de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `botocore` | `1.34.47` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `bracex` | `2.4` | ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `brotli` | `1.1.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), de-supported-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `cachetools` | `5.3.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11) |
| `certifi` | `2023.5.7` | de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `certifi` | `2038.12.31` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `cffi` | `1.15.0` | controller-rhel9:/usr (python3.9), eda-controller-rhel9:/usr (python3.9), gateway-rhel9:/usr (python3.9), hub-rhel9:/usr (python3.9) |
| `cffi` | `1.15.1` | de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `cffi` | `1.16.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `channels` | `3.0.5` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `channels` | `4.0.0` | eda-controller-rhel9:/usr (python3.11) |
| `channels-redis` | `4.2.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `chardet` | `4.0.0` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), ee-supported-rhel9:/usr (python3.9), hub-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), receptor-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `chardet` | `5.2.0` | ee-supported-rhel9:/usr (python3.11) |
| `charset-normalizer` | `2.1.0` | de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `charset-normalizer` | `3.3.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `click` | `8.1.7` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11), receptor-rhel9:/usr (python3.11) |
| `constantly` | `15.1.0` | eda-controller-rhel9:/usr (python3.11) |
| `constantly` | `23.10.4` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `croniter` | `2.0.1` | eda-controller-rhel9:/usr (python3.11) |
| `cryptography` | `42.0.5` | controller-rhel9:/usr (python3.9), de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.9), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.9), hub-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.9) |
| `cryptography` | `42.0.8` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `cython` | `3.1.3` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `daphne` | `3.0.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `daphne` | `4.0.0` | eda-controller-rhel9:/usr (python3.11) |
| `dbus-python` | `1.2.18` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `decorator` | `4.4.2` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `decorator` | `5.1.1` | ee-minimal-rhel9:/usr/local (python3.11) |
| `decorator` | `5.2.1` | de-supported-rhel9:/usr/local (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `defusedxml` | `0.7.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `deprecated` | `1.2.14` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `diff-match-patch` | `20230430` | hub-rhel9:/usr (python3.11) |
| `dispatcherd` | `2025.5.19` | eda-controller-rhel9:/usr (python3.11) |
| `distlib` | `0.3.8` | ee-supported-rhel9:/usr (python3.11) |
| `distro` | `1.9.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `django` | `4.2.24` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `django-ansible-base` | `2.6.20251001` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `django-auth-ldap` | `4.0.0` | gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `django-auth-ldap` | `5.1.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `django-automated-logging` | `6.2.2` | hub-rhel9:/usr (python3.11) |
| `django-cors-headers` | `4.3.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `django-crum` | `0.7.9` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `django-dynamic-preferences` | `1.16.0` | gateway-rhel9:/usr (python3.11) |
| `django-extensions` | `3.2.3` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), gateway-rhel9:/usr (python3.11) |
| `django-filter` | `23.5` | eda-controller-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `django-flags` | `5.0.13` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `django-guid` | `3.2.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `django-guid` | `3.4.0` | hub-rhel9:/usr (python3.11) |
| `django-import-export` | `3.3.6` | hub-rhel9:/usr (python3.11) |
| `django-ipware` | `6.0.5` | hub-rhel9:/usr (python3.11) |
| `django-lifecycle` | `1.1.2` | hub-rhel9:/usr (python3.11) |
| `django-oauth-toolkit` | `1.7.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `django-oauth-toolkit` | `2.3.0` | gateway-rhel9:/usr (python3.11) |
| `django-pglocks` | `1.0.4` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `django-picklefield` | `3.1` | hub-rhel9:/usr (python3.11) |
| `django-polymorphic` | `3.1.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `django-prometheus` | `2.3.1` | hub-rhel9:/usr (python3.11) |
| `django-radius` | `1.5.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `django-redis` | `5.4.0` | eda-controller-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11) |
| `django-rq` | `2.8.0` | eda-controller-rhel9:/usr (python3.11) |
| `django-solo` | `2.2.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `django-split-settings` | `1.2.0` | eda-controller-rhel9:/usr (python3.11) |
| `django-storages` | `1.14.2` | hub-rhel9:/usr (python3.11) |
| `djangorestframework` | `3.15.1` | eda-controller-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `djangorestframework` | `3.15.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `djangorestframework-queryfields` | `1.1.0` | hub-rhel9:/usr (python3.11) |
| `djangorestframework-yaml` | `2.0.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `dnspython` | `2.6.1` | ee-supported-rhel9:/usr/local (python3.11) |
| `docutils` | `0.20.1` | de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), receptor-rhel9:/usr (python3.11) |
| `dogpile-cache` | `1.1.2` | ee-supported-rhel9:/usr/local (python3.11) |
| `dpapi-ng` | `0.2.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `dpath` | `2.1.6` | de-supported-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11) |
| `drf-access-policy` | `1.5.0` | hub-rhel9:/usr (python3.11) |
| `drf-nested-routers` | `0.93.5` | hub-rhel9:/usr (python3.11) |
| `drf-spectacular` | `0.26.5` | eda-controller-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `drools-jpy` | `0.3.14` | de-supported-rhel9:/usr (python3.11) |
| `dynaconf` | `3.2.10` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `dynaconf` | `3.2.11` | eda-controller-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `ecdsa` | `0.18.0` | eda-controller-rhel9:/usr (python3.11) |
| `enum-compat` | `0.0.3` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `et-xmlfile` | `1.1.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), hub-rhel9:/usr (python3.11) |
| `filelock` | `3.13.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `flake8` | `6.1.0` | hub-rhel9:/usr (python3.11) |
| `frozenlist` | `1.4.0` | de-supported-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `frozenlist` | `1.4.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `galaxy-importer` | `0.4.33` | hub-rhel9:/usr (python3.11) |
| `galaxy-ng` | `4.11.0.dev0` | hub-rhel9:/usr (python3.11) |
| `gitdb` | `4.0.11` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), hub-rhel9:/usr (python3.11) |
| `gitpython` | `3.1.41` | hub-rhel9:/usr (python3.11) |
| `gitpython` | `3.1.42` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `google-api-core` | `2.25.1` | ee-supported-rhel9:/usr/local (python3.11) |
| `google-auth` | `2.27.0` | eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11) |
| `google-auth` | `2.28.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `google-cloud-core` | `2.4.3` | ee-supported-rhel9:/usr/local (python3.11) |
| `google-cloud-storage` | `3.3.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `google-crc32c` | `1.7.1` | ee-supported-rhel9:/usr/local (python3.11) |
| `google-resumable-media` | `2.7.2` | ee-supported-rhel9:/usr/local (python3.11) |
| `googleapis-common-protos` | `1.59.1` | gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `googleapis-common-protos` | `1.63.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `googleapis-common-protos` | `1.70.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `gpg` | `1.15.1` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `grpcio` | `1.58.3` | ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `grpcio` | `1.68.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `grpcio-tools` | `1.58.3` | gateway-rhel9:/usr (python3.11) |
| `gssapi` | `1.8.2` | ee-minimal-rhel9:/usr/local (python3.11) |
| `gssapi` | `1.9.0` | de-supported-rhel9:/usr/local (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `gunicorn` | `22.0.0` | eda-controller-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `h11` | `0.16.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `h2` | `4.1.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `hiredis` | `3.0.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `hpack` | `4.0.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `httpcore` | `1.0.9` | ee-supported-rhel9:/usr/local (python3.11) |
| `httpx` | `0.27.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `humanfriendly` | `10.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `hyperframe` | `6.0.1` | ee-supported-rhel9:/usr/local (python3.11) |
| `hyperlink` | `21.0.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11) |
| `idna` | `2.10` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), ee-supported-rhel9:/usr (python3.9), hub-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), receptor-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `idna` | `3.10` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `idna` | `3.4` | de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `importlib-metadata` | `6.0.1` | ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `importlib-metadata` | `6.2.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `incremental` | `24.7.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11) |
| `inflect` | `7.0.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `inflection` | `0.5.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `iniparse` | `0.4` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `insights-analytics-collector` | `0.3.2` | eda-controller-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `irc` | `20.3.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `iso8601` | `0.1.14` | ee-supported-rhel9:/usr/local (python3.11) |
| `isodate` | `0.6.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `janus` | `1.0.0` | de-supported-rhel9:/usr (python3.11) |
| `jaraco-collections` | `5.0.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `jaraco-context` | `4.3.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `jaraco-functools` | `4.0.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `jaraco-logging` | `3.3.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `jaraco-stream` | `3.0.3` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `jaraco-text` | `3.12.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `jinja2` | `3.1.6` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `jmespath` | `1.0.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `jpy` | `0.15.0` | de-supported-rhel9:/usr (python3.11) |
| `jq` | `1.6.0` | hub-rhel9:/usr (python3.11) |
| `jq` | `1.8.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `json-log-formatter` | `0.5.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `json-stream` | `2.3.2` | hub-rhel9:/usr (python3.11) |
| `json-stream-rs-tokenizer` | `0.4.26` | hub-rhel9:/usr (python3.11) |
| `jsonpatch` | `1.32` | ee-supported-rhel9:/usr/local (python3.11) |
| `jsonpointer` | `2.1` | ee-supported-rhel9:/usr/local (python3.11) |
| `jsonschema` | `4.21.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `jsonschema-specifications` | `2023.12.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `jwcrypto` | `1.5.4` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `jwcrypto` | `1.5.6` | gateway-rhel9:/usr (python3.11) |
| `jxmlease` | `1.0.3` | ee-supported-rhel9:/usr/local (python3.11) |
| `kafka-python` | `2.0.2` | de-supported-rhel9:/usr/local (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `keystoneauth1` | `4.3.1` | ee-supported-rhel9:/usr/local (python3.11) |
| `knack` | `0.11.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `krb5` | `0.7.1` | ee-supported-rhel9:/usr/local (python3.11) |
| `kubernetes` | `26.1.0` | eda-controller-rhel9:/usr (python3.11) |
| `kubernetes` | `29.0.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `ldap-filter` | `1.0.1` | gateway-rhel9:/usr (python3.11) |
| `libcomps` | `0.1.18` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `lockfile` | `0.12.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), receptor-rhel9:/usr (python3.11) |
| `lxml` | `4.9.2` | ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11) |
| `lxml` | `4.9.4` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `markdown` | `3.5.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), hub-rhel9:/usr (python3.11) |
| `markuppy` | `1.14` | hub-rhel9:/usr (python3.11) |
| `markupsafe` | `2.1.5` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `marshmallow` | `3.26.1` | hub-rhel9:/usr (python3.11) |
| `maturin` | `1.5.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `mccabe` | `0.7.0` | hub-rhel9:/usr (python3.11) |
| `metrics-utility` | `0.6.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `microsoft-kiota-abstractions` | `1.3.3` | ee-supported-rhel9:/usr/local (python3.11) |
| `microsoft-kiota-authentication-azure` | `1.0.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `microsoft-kiota-http` | `1.3.1` | ee-supported-rhel9:/usr/local (python3.11) |
| `microsoft-kiota-serialization-form` | `0.1.1` | ee-supported-rhel9:/usr/local (python3.11) |
| `microsoft-kiota-serialization-json` | `1.3.3` | ee-supported-rhel9:/usr/local (python3.11) |
| `microsoft-kiota-serialization-multipart` | `0.1.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `microsoft-kiota-serialization-text` | `1.0.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `microsoft-security-utilities-secret-masker` | `1.0.0b4` | ee-supported-rhel9:/usr/local (python3.11) |
| `more-itertools` | `10.2.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `msal` | `1.26.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `msal` | `1.32.3` | eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `msal-extensions` | `1.1.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `msal-extensions` | `1.2.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `msal-extensions` | `1.3.1` | eda-controller-rhel9:/usr (python3.11) |
| `msgpack` | `1.1.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `msgraph-core` | `1.1.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `msgraph-sdk` | `1.6.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `msrest` | `0.7.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `msrestazure` | `0.6.4` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `multidict` | `6.0.4` | de-supported-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `multidict` | `6.0.5` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `munch` | `2.5.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `mypy-extensions` | `1.0.0` | ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `ncclient` | `0.6.10` | ee-minimal-rhel9:/usr/local (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `netaddr` | `1.2.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11) |
| `netifaces` | `0.10.9` | ee-supported-rhel9:/usr/local (python3.11) |
| `nh3` | `0.2.18` | hub-rhel9:/usr (python3.11) |
| `nsx-policy-python-sdk` | `4.1.2.0.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `nsx-python-sdk` | `4.1.2.0.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `nsx-vmc-aws-integration-python-sdk` | `4.1.2.0.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `nsx-vmc-policy-python-sdk` | `4.1.2.0.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `ntlm-auth` | `1.5.0` | ee-minimal-rhel9:/usr/local (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `numpy` | `1.23.5` | ee-supported-rhel9:/usr (python3.11) |
| `numpy` | `1.26.4` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `oauthlib` | `3.2.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `odfpy` | `1.4.1` | hub-rhel9:/usr (python3.11) |
| `opa-python-client` | `2.0.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `openpyxl` | `3.1.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), hub-rhel9:/usr (python3.11) |
| `openshift` | `0.13.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `openstacksdk` | `0.56.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `opentelemetry-api` | `1.18.0` | hub-rhel9:/usr (python3.11) |
| `opentelemetry-api` | `1.24.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `opentelemetry-api` | `1.25.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `opentelemetry-distro` | `0.39b0` | hub-rhel9:/usr (python3.11) |
| `opentelemetry-exporter-otlp` | `1.18.0` | hub-rhel9:/usr (python3.11) |
| `opentelemetry-exporter-otlp` | `1.24.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `opentelemetry-exporter-otlp-proto-common` | `1.18.0` | hub-rhel9:/usr (python3.11) |
| `opentelemetry-exporter-otlp-proto-common` | `1.24.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `opentelemetry-exporter-otlp-proto-grpc` | `1.18.0` | hub-rhel9:/usr (python3.11) |
| `opentelemetry-exporter-otlp-proto-grpc` | `1.24.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `opentelemetry-exporter-otlp-proto-http` | `1.18.0` | hub-rhel9:/usr (python3.11) |
| `opentelemetry-exporter-otlp-proto-http` | `1.24.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `opentelemetry-instrumentation` | `0.39b0` | hub-rhel9:/usr (python3.11) |
| `opentelemetry-instrumentation` | `0.45b0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `opentelemetry-instrumentation-django` | `0.39b0` | hub-rhel9:/usr (python3.11) |
| `opentelemetry-instrumentation-logging` | `0.45b0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `opentelemetry-instrumentation-wsgi` | `0.39b0` | hub-rhel9:/usr (python3.11) |
| `opentelemetry-proto` | `1.18.0` | gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `opentelemetry-proto` | `1.24.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `opentelemetry-sdk` | `1.18.0` | hub-rhel9:/usr (python3.11) |
| `opentelemetry-sdk` | `1.24.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `opentelemetry-sdk` | `1.25.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `opentelemetry-semantic-conventions` | `0.39b0` | hub-rhel9:/usr (python3.11) |
| `opentelemetry-semantic-conventions` | `0.45b0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `opentelemetry-semantic-conventions` | `0.46b0` | ee-supported-rhel9:/usr/local (python3.11) |
| `opentelemetry-util-http` | `0.39b0` | hub-rhel9:/usr (python3.11) |
| `oras` | `0.2.37` | ee-supported-rhel9:/usr/local (python3.11) |
| `os-service-types` | `1.7.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `ovirt-engine-sdk-python` | `4.5.2` | ee-supported-rhel9:/usr/local (python3.11) |
| `ovirt-imageio` | `2.4.6` | ee-supported-rhel9:/usr/local (python3.11) |
| `packaging` | `23.2` | de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11), receptor-rhel9:/usr (python3.11) |
| `packaging` | `25.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `pandas` | `2.2.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `pandas` | `2.3.2` | ee-supported-rhel9:/usr/local (python3.11) |
| `paramiko` | `2.8.1` | ee-minimal-rhel9:/usr/local (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `parsley` | `1.3` | hub-rhel9:/usr (python3.11) |
| `pathspec` | `0.12.1` | ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `pbr` | `6.0.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `pcp` | `5.0` | pcp:/usr (python3.9) |
| `pendulum` | `3.0.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `persisting-theory` | `1.0` | gateway-rhel9:/usr (python3.11) |
| `pexpect` | `4.7.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `pexpect` | `4.8.0` | controller-rhel9:/usr (python3.9), ee-supported-rhel9:/usr (python3.9), hub-rhel9:/usr (python3.9), receptor-rhel9:/usr (python3.9) |
| `pexpect` | `4.9.0` | de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), receptor-rhel9:/usr (python3.11) |
| `pillow` | `10.3.0` | hub-rhel9:/usr (python3.11) |
| `pip` | `21.2.4` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `pip` | `22.3.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), de-supported-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11) |
| `pkgconfig` | `1.5.5` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `pkginfo` | `1.7.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `platformdirs` | `4.2.0` | ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `ply` | `3.11` | de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `podman` | `5.4.0.1` | eda-controller-rhel9:/usr (python3.11) |
| `portalocker` | `1.7.1` | ee-supported-rhel9:/usr/local (python3.11) |
| `portalocker` | `2.8.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `prometheus-client` | `0.19.0` | hub-rhel9:/usr (python3.11) |
| `prometheus-client` | `0.20.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `propcache` | `0.2.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `proto-plus` | `1.26.1` | ee-supported-rhel9:/usr/local (python3.11) |
| `protobuf` | `4.21.12` | ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `protobuf` | `4.25.8` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `psutil` | `5.9.1` | ee-supported-rhel9:/usr/local (python3.11) |
| `psutil` | `5.9.8` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `psycopg` | `3.1.18` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `psycopg` | `3.2.7` | de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `psycopg-c` | `3.2.7` | de-supported-rhel9:/usr (python3.11) |
| `ptyprocess` | `0.6.0` | controller-rhel9:/usr (python3.9), ee-supported-rhel9:/usr (python3.9), hub-rhel9:/usr (python3.9), receptor-rhel9:/usr (python3.9) |
| `ptyprocess` | `0.7.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), receptor-rhel9:/usr (python3.11) |
| `pulp-ansible` | `0.25.1` | hub-rhel9:/usr (python3.11) |
| `pulp-container` | `2.19.3` | hub-rhel9:/usr (python3.11) |
| `pulp-glue` | `0.23.2` | hub-rhel9:/usr (python3.11) |
| `pulpcore` | `3.49.42` | hub-rhel9:/usr (python3.11) |
| `py-deviceid` | `0.1.1` | ee-supported-rhel9:/usr/local (python3.11) |
| `pyang` | `2.5.3` | ee-supported-rhel9:/usr/local (python3.11) |
| `pyasn1` | `0.5.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `pyasn1-modules` | `0.3.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `pycares` | `4.4.0` | de-supported-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `pycares` | `4.5.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `pycodestyle` | `2.11.1` | hub-rhel9:/usr (python3.11) |
| `pycparser` | `2.20` | de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `pycparser` | `2.21` | controller-rhel9:/usr (python3.9), controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.9), gateway-rhel9:/usr (python3.9), hub-rhel9:/usr (python3.9) |
| `pycurl` | `7.45.3` | ee-supported-rhel9:/usr/local (python3.11) |
| `pydantic` | `1.10.15` | eda-controller-rhel9:/usr (python3.11) |
| `pydantic` | `2.5.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `pydantic-core` | `2.14.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `pyflakes` | `3.1.0` | hub-rhel9:/usr (python3.11) |
| `pygerduty` | `0.38.3` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `pygithub` | `2.6.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `pygithub` | `2.6.1` | eda-controller-rhel9:/usr (python3.11) |
| `pygments` | `2.17.2` | ee-supported-rhel9:/usr (python3.11) |
| `pygobject` | `3.40.1` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `pygtrie` | `2.5.0` | hub-rhel9:/usr (python3.11) |
| `pyinotify` | `0.9.6` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `pyjwt` | `2.7.0` | eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `pyjwt` | `2.8.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `pykerberos` | `1.2.4` | ee-minimal-rhel9:/usr/local (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `pynacl` | `1.4.0` | ee-minimal-rhel9:/usr/local (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `pynacl` | `1.5.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11) |
| `pyopenssl` | `24.0.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `pyopenssl` | `24.1.0` | eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `pyparsing` | `2.4.6` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `pyparsing` | `3.1.1` | de-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `pypsrp` | `0.5.0` | ee-minimal-rhel9:/usr/local (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `pyrad` | `2.4` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), gateway-rhel9:/usr (python3.11) |
| `pysocks` | `1.7.1` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.9), hub-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), receptor-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `pyspnego` | `0.9.0` | ee-minimal-rhel9:/usr/local (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `python-daemon` | `2.3.2` | de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), receptor-rhel9:/usr (python3.11) |
| `python-daemon` | `3.1.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `python-dateutil` | `2.8.1` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `python-dateutil` | `2.8.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11), receptor-rhel9:/usr (python3.11) |
| `python-dsv-sdk` | `1.0.4` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11) |
| `python-gnupg` | `0.5.2` | eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `python-ipware` | `3.0.0` | hub-rhel9:/usr (python3.11) |
| `python-ldap` | `3.4.4` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `python-string-utils` | `1.0.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `python-tss-sdk` | `1.2.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `python-tss-sdk` | `1.2.3` | eda-controller-rhel9:/usr (python3.11) |
| `python3-openid` | `3.2.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `python3-saml` | `1.14.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `python3-saml` | `1.16.0` | gateway-rhel9:/usr (python3.11) |
| `pytz` | `2024.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11) |
| `pyvmomi` | `8.0.3.0.1` | ee-supported-rhel9:/usr/local (python3.11) |
| `pywinrm` | `0.4.3` | ee-minimal-rhel9:/usr/local (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `pyyaml` | `5.4.1` | controller-rhel9:/usr (python3.9), ee-supported-rhel9:/usr (python3.9), hub-rhel9:/usr (python3.9), receptor-rhel9:/usr (python3.9) |
| `pyyaml` | `6.0` | de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11), receptor-rhel9:/usr (python3.11) |
| `pyyaml` | `6.0.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `pyzstd` | `0.15.10` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `receptorctl` | `1.5.7` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), ee-supported-rhel9:/usr (python3.11), receptor-rhel9:/usr (python3.11) |
| `redis` | `4.6.0` | eda-controller-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `redis` | `5.0.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `referencing` | `0.33.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `referencing` | `0.36.2` | de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `requests` | `2.25.1` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), ee-supported-rhel9:/usr (python3.9), hub-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), receptor-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `requests` | `2.28.1` | ee-minimal-rhel9:/usr (python3.11) |
| `requests` | `2.31.0` | de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `requests` | `2.32.3` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `requests-credssp` | `2.0.0` | ee-minimal-rhel9:/usr/local (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `requests-ntlm` | `1.1.0` | ee-minimal-rhel9:/usr/local (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `requests-oauthlib` | `1.3.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `requestsexceptions` | `1.4.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `resolvelib` | `1.0.1` | de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `rpds-py` | `0.18.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `rpds-py` | `0.18.1` | de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `rpm` | `4.16.1.3` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `rq` | `1.13.0` | eda-controller-rhel9:/usr (python3.11) |
| `rq-scheduler` | `0.10.0` | eda-controller-rhel9:/usr (python3.11) |
| `rsa` | `4.9` | eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11) |
| `ruamel-yaml` | `0.18.15` | ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `ruamel-yaml-clib` | `0.2.8` | ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `s3transfer` | `0.10.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `sansldap` | `0.1.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `scp` | `0.13.3` | ee-supported-rhel9:/usr/local (python3.11) |
| `selinux` | `3.6` | controller-rhel9:/usr (python3.9) |
| `semantic-version` | `2.10.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), hub-rhel9:/usr (python3.11) |
| `service-identity` | `21.1.0` | eda-controller-rhel9:/usr (python3.11) |
| `service-identity` | `24.1.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `setuptools` | `53.0.0` | controller-rhel9:/usr (python3.9), eda-controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), ee-supported-rhel9:/usr (python3.9), gateway-rhel9:/usr (python3.9), hub-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), receptor-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `setuptools` | `65.5.1` | controller-rhel9:/usr (python3.11), controller-rhel9:/var/lib/awx/venv/awx (python3.11), de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11), receptor-rhel9:/usr (python3.11) |
| `setuptools` | `80.9.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `setuptools-rust` | `1.8.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `setuptools-scm` | `8.0.4` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `six` | `1.15.0` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), ee-supported-rhel9:/usr (python3.9), hub-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), receptor-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `six` | `1.16.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11), receptor-rhel9:/usr (python3.11) |
| `slack-sdk` | `3.27.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `smmap` | `5.0.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), hub-rhel9:/usr (python3.11) |
| `sniffio` | `1.3.1` | ee-supported-rhel9:/usr/local (python3.11) |
| `social-auth-app-django` | `5.4.1` | gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `social-auth-app-django` | `5.4.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `social-auth-core` | `4.5.4` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `sos` | `4.9.2` | controller-rhel9:/usr (python3.9), ee-supported-rhel9:/usr (python3.9), hub-rhel9:/usr (python3.9), receptor-rhel9:/usr (python3.9) |
| `sqlparse` | `0.5.3` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `std-uritemplate` | `1.0.2` | ee-supported-rhel9:/usr/local (python3.11) |
| `stevedore` | `3.3.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `subprocess-tee` | `0.4.1` | ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `subscription-manager` | `1.29.45.1` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `supervisor` | `4.2.5` | controller-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11) |
| `systemd-python` | `234` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `tablib` | `3.5.0` | hub-rhel9:/usr (python3.11) |
| `tabulate` | `0.9.0` | ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11) |
| `tacacs-plus` | `1.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `tacacs-plus` | `2.6` | gateway-rhel9:/usr (python3.11) |
| `tempora` | `5.5.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `textfsm` | `0.4.1` | ee-supported-rhel9:/usr/local (python3.11) |
| `time-machine` | `2.14.2` | ee-supported-rhel9:/usr/local (python3.11) |
| `toml` | `0.10.2` | ee-minimal-rhel9:/usr/local (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `tomli` | `2.2.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `ttp` | `0.6.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `twilio` | `8.13.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `twisted` | `24.7.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11) |
| `txaio` | `23.1.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11) |
| `typing-extensions` | `4.9.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `tzdata` | `2024.1` | ee-supported-rhel9:/usr/local (python3.11) |
| `uamqp` | `1.6.8` | ee-supported-rhel9:/usr (python3.11) |
| `uritemplate` | `4.1.1` | eda-controller-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `url-normalize` | `1.4.3` | hub-rhel9:/usr (python3.11) |
| `urllib3` | `1.26.12` | ee-minimal-rhel9:/usr (python3.11) |
| `urllib3` | `1.26.20` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), gateway-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `urllib3` | `1.26.5` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), ee-supported-rhel9:/usr (python3.9), hub-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), receptor-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `uuid6` | `2024.1.12` | hub-rhel9:/usr (python3.11) |
| `uwsgi` | `2.0.28` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `uwsgitop` | `0.11` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `validators` | `0.34.0` | eda-controller-rhel9:/usr (python3.11) |
| `vapi-common-client` | `2.44.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `vapi-runtime` | `2.44.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `vcenter-bindings` | `4.2.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `vmwarecloud-aws` | `1.64.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `vmwarecloud-draas` | `1.23.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `vsphere-automation-sdk` | `1.86.0` | ee-supported-rhel9:/usr/local (python3.11) |
| `watchdog` | `5.0.2` | de-supported-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11) |
| `wcmatch` | `8.5` | ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `websocket-client` | `1.7.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11) |
| `websockets` | `15.0` | de-supported-rhel9:/usr (python3.11) |
| `wheel` | `0.42.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `whitenoise` | `6.6.0` | hub-rhel9:/usr (python3.11) |
| `wrapt` | `1.16.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `xds-protos` | `1.58.0` | gateway-rhel9:/usr (python3.11) |
| `xlrd` | `2.0.1` | hub-rhel9:/usr (python3.11) |
| `xlwt` | `1.3.0` | hub-rhel9:/usr (python3.11) |
| `xmlsec` | `1.3.13` | controller-rhel9:/var/lib/awx/venv/awx (python3.11), gateway-rhel9:/usr (python3.11) |
| `xmltodict` | `0.12.0` | ee-minimal-rhel9:/usr/local (python3.11), ee-supported-rhel9:/usr/local (python3.11) |
| `xxhash` | `3.4.1` | de-supported-rhel9:/usr (python3.11), eda-controller-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11) |
| `yamllint` | `1.35.1` | ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `yarl` | `1.13.1` | de-supported-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `yarl` | `1.17.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `zipp` | `3.17.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |
| `zipp` | `3.19.2` | ee-minimal-rhel9:/usr (python3.11), ee-supported-rhel9:/usr (python3.11), hub-rhel9:/usr (python3.11) |
| `zope-interface` | `6.1` | eda-controller-rhel9:/usr (python3.11) |
| `zope-interface` | `6.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.11) |

## Image Details

### controller-rhel9

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-26/controller-rhel9` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/controller-rhel9.tar.gz` |
| Labels `version` / `release` | `4.7.1` / `4` |
| Image ID | `sha256:982e48d852cbbdc01c961738523d276b9403321abf31435b0c35bc7a1d0ff2ff` |
| Build date | 2025-09-23T21:40:55 |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.6 (Plow) |
| Python | 3.9, 3.11 |
| Ansible Core | N/A |

<details><summary>RPM packages (266)</summary>

```text
aap-metrics-utility 0.6.0-3.el9ap
acl 2.3.1-4.el9
alternatives 1.24-2.el9
ansible-automation-platform-common 2.6-1.el9ap
ansible-automation-platform-selinux 0.2-3.el9ap
apr 1.7.0-12.el9_3
apr-util 1.6.1-23.el9
apr-util-bdb 1.6.1-23.el9
attr 2.5.1-3.el9
audit-libs 3.1.5-4.el9
automation-controller 4.7.1-1.el9ap
automation-controller-server 4.7.1-1.el9ap
automation-controller-ui 4.7.1-1.el9ap
automation-controller-venv-tower 4.7.1-1.el9ap
basesystem 11-13.el9
bash 5.1.8-9.el9
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crontabs 1.11-27.20190603git.el9_0
crun 1.23.1-2.el9_6
crypto-policies 20250128-1.git5269e22.el9
curl-minimal 7.76.1-31.el9_6.1
cyrus-sasl-lib 2.1.27-21.el9
dbus 1.12.20-8.el9
dbus-broker 28-7.el9
dbus-common 1.12.20-8.el9
dbus-libs 1.12.20-8.el9
dejavu-sans-fonts 2.37-18.el9
diffutils 3.7-12.el9
dmidecode 3.6-1.el9
dnf-data 4.14.0-25.el9
dumb-init 1.2.5-3.el9ap
elfutils-default-yama-scope 0.192-6.el9_6
elfutils-libelf 0.192-6.el9_6
elfutils-libs 0.192-6.el9_6
expat 2.5.0-5.el9_6
file-libs 5.39-16.el9
filesystem 3.16-5.el9
findutils 4.8.0-7.el9
flexiblas 3.0.4-8.el9
flexiblas-netlib 3.0.4-8.el9
flexiblas-openblas-openmp 3.0.4-8.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdbm-libs 1.23-1.el9
git-core 2.47.3-1.el9_6
git-lfs 3.6.1-2.el9_6
glib2 2.68.4-16.el9_6.2
glibc 2.34-168.el9_6.23
glibc-common 2.34-168.el9_6.23
glibc-langpack-en 2.34-168.el9_6.23
glibc-minimal-langpack 2.34-168.el9_6.23
gmp 6.2.0-13.el9
gnupg2 2.3.3-4.el9
gnutls 3.8.3-6.el9_6.2
gobject-introspection 1.68.0-11.el9
gpg-pubkey 5a6340b3-6229229e
gpg-pubkey fd431d51-4ae0493b
gpgme 1.15.1-6.el9
grep 3.6-5.el9
gzip 1.12-1.el9
hostname 3.23-6.el9
ima-evm-utils 1.5-3.el9
iproute 6.11.0-1.el9
json-c 0.14-11.el9
json-glib 1.6.6-1.el9
keyutils 1.6.3-1.el9
keyutils-libs 1.6.3-1.el9
kmod-libs 28-10.el9
krb5-libs 1.21.1-8.el9_6
krb5-pkinit 1.21.1-8.el9_6
krb5-workstation 1.21.1-8.el9_6
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
less 590-5.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-6.el9_6
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9
libbpf 1.5.0-1.el9
libcap 2.48-9.el9_2
libcap-ng 0.8.2-7.el9
libcbor 0.7.0-5.el9
libcom_err 1.46.5-7.el9
libcomps 0.1.18-1.el9
libcurl-minimal 7.76.1-31.el9_6.1
libdb 5.3.28-57.el9_6
libdnf 0.69.0-13.el9
libdnf-plugin-subscription-manager 1.29.45.1-1.el9_6
libeconf 0.4.1-4.el9
libedit 3.1-38.20210216cvs.el9
libestr 0.1.11-4.el9
libevent 2.1.12-8.el9_4
libfastjson 0.99.9-5.el9
libfdisk 2.37.4-21.el9
libffi 3.4.2-8.el9
libfido2 1.13.0-2.el9
libgcc 11.5.0-5.el9_5
libgcrypt 1.10.0-11.el9
libgfortran 11.5.0-5.el9_5
libgomp 11.5.0-5.el9_5
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libkadm5 1.21.1-8.el9_6
libksba 1.5.1-7.el9
libmnl 1.0.4-16.el9_4
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9
libnghttp2 1.43.0-6.el9
libnsl2 2.0.0-1.el9
libpeas 1.30.0-4.el9
libpwquality 1.4.4-8.el9
libquadmath 11.5.0-5.el9_5
librepo 1.14.5-2.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libseccomp 2.5.2-2.el9
libselinux 3.6-3.el9
libselinux-utils 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-2.el9
libserf 1.3.9-27.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9
libsolv 0.7.24-3.el9
libss 1.46.5-7.el9
libstdc++ 11.5.0-5.el9_5
libtasn1 4.16.0-9.el9
libtirpc 1.3.3-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libusbx 1.0.26-1.el9
libuser 0.63-16.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-12.el9_6
libxslt 1.1.34-13.el9_6
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
logrotate 3.18.0-9.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
microdnf 3.9.1-3.el9
mpdecimal 2.5.1-3.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-10.20210508.el9_6.2
ncurses-libs 6.2-10.20210508.el9_6.2
nettle 3.10.1-1.el9
nginx 1.24.0-4.module+el9.5.0+22954+e2d70a1c.1
nginx-core 1.24.0-4.module+el9.5.0+22954+e2d70a1c.1
nginx-filesystem 1.24.0-4.module+el9.5.0+22954+e2d70a1c.1
npth 1.6-8.el9
openblas 0.3.26-2.el9
openblas-openmp 0.3.26-2.el9
openldap 2.6.8-4.el9
openssh 8.7p1-45.el9
openssh-clients 8.7p1-45.el9
openssl 3.2.2-6.el9_5.1
openssl-fips-provider 3.0.7-6.el9_5
openssl-fips-provider-so 3.0.7-6.el9_5
openssl-libs 3.2.2-6.el9_5.1
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pam 1.5.1-26.el9_6
passwd 0.80-12.el9
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
podman-remote 5.4.0-13.el9_6
policycoreutils 3.6-2.1.el9
popt 1.18-8.el9
postgresql 15.14-1.module+el9.6.0+23419+7863ab62
postgresql-private-libs 15.14-1.module+el9.6.0+23419+7863ab62
psmisc 23.4-3.el9
python3 3.9.21-2.el9_6.2
python3-cffi 1.15.0-3.el9ap
python3-chardet 4.0.0-5.el9
python3-cloud-what 1.29.45.1-1.el9_6
python3-cryptography 42.0.5-1.el9ap
python3-dateutil 2.8.1-7.el9
python3-dbus 1.2.18-2.el9
python3-decorator 4.4.2-6.el9
python3-dnf 4.14.0-25.el9
python3-dnf-plugins-core 4.3.0-20.el9
python3-gobject-base 3.40.1-6.el9
python3-gobject-base-noarch 3.40.1-6.el9
python3-gpg 1.15.1-6.el9
python3-hawkey 0.69.0-13.el9
python3-idna 2.10-7.el9_4.1
python3-iniparse 0.4-45.el9
python3-inotify 0.9.6-25.el9
python3-libcomps 0.1.18-1.el9
python3-libdnf 0.69.0-13.el9
python3-librepo 1.14.5-2.el9
python3-libs 3.9.21-2.el9_6.2
python3-libselinux 3.6-3.el9
python3-libsemanage 3.6-5.el9_6
python3-pexpect 4.8.0-7.el9
python3-pip-wheel 21.3.1-1.el9
python3-ptyprocess 0.6.0-12.el9
python3-pycparser 2.21-2.el9pc
python3-pysocks 1.7.1-12.el9
python3-pyyaml 5.4.1-6.el9
python3-requests 2.25.1-10.el9_6
python3-rpm 4.16.1.3-37.el9
python3-setuptools 53.0.0-13.el9_6.1
python3-setuptools-wheel 53.0.0-13.el9_6.1
python3-six 1.15.0-9.el9
python3-subscription-manager-rhsm 1.29.45.1-1.el9_6
python3-systemd 234-19.el9
python3-urllib3 1.26.5-6.el9
python3.11 3.11.11-2.el9_6.2
python3.11-libs 3.11.11-2.el9_6.2
python3.11-pip-wheel 22.3.1-5.el9
python3.11-setuptools 65.5.1-4.el9_6
python3.11-setuptools-wheel 65.5.1-4.el9_6
readline 8.1-4.el9
redhat-logos-httpd 90.5-1.el9_6.1
redhat-release 9.6-0.1.el9
redis 6.2.19-1.el9_6
rootfiles 8.1-34.el9
rpm 4.16.1.3-37.el9
rpm-build-libs 4.16.1.3-37.el9
rpm-libs 4.16.1.3-37.el9
rpm-plugin-selinux 4.16.1.3-37.el9
rpm-sign-libs 4.16.1.3-37.el9
rsync 3.2.5-3.el9
rsyslog 8.2412.0-1.el9
sed 4.8-9.el9
selinux-policy 38.1.53-5.el9_6
selinux-policy-targeted 38.1.53-5.el9_6
setup 2.13.7-10.el9
shadow-utils 4.9-12.el9
shadow-utils-subid 4.9-12.el9
sos 4.9.2-1.el9_6
sqlite-libs 3.34.1-8.el9_6
sshpass 1.09-5.el9ap
subscription-manager 1.29.45.1-1.el9_6
subscription-manager-rhsm-certificates 20220623-1.el9
subversion 1.14.1-5.el9_0
subversion-libs 1.14.1-5.el9_0
supervisor 4.2.5-1.el9ap
systemd 252-51.el9_6.2
systemd-libs 252-51.el9_6.2
systemd-pam 252-51.el9_6.2
systemd-rpm-macros 252-51.el9_6.2
tpm2-tss 3.2.3-1.el9
tzdata 2025b-1.el9
usermode 1.114-6.el9
utf8proc 2.6.1-4.el9
util-linux 2.37.4-21.el9
util-linux-core 2.37.4-21.el9
virt-what 1.27-1.el9
which 2.21-30.el9_6
xmlsec1 1.2.29-13.el9
xmlsec1-openssl 1.2.29-13.el9
xz-libs 5.2.5-8.el9_0
yajl 2.1.0-25.el9
zlib 1.2.11-40.el9
```

</details>

<details><summary>Python packages: /usr (python3.11) (2)</summary>

```text
setuptools 65.5.1
supervisor 4.2.5
```

</details>

<details><summary>Python packages: /usr (python3.9) (26)</summary>

```text
cffi 1.15.0
chardet 4.0.0
cryptography 42.0.5
dbus-python 1.2.18
decorator 4.4.2
gpg 1.15.1
idna 2.10
iniparse 0.4
libcomps 0.1.18
pexpect 4.8.0
ptyprocess 0.6.0
pycparser 2.21
PyGObject 3.40.1
pyinotify 0.9.6
PySocks 1.7.1
python-dateutil 2.8.1
PyYAML 5.4.1
requests 2.25.1
rpm 4.16.1.3
selinux 3.6
setuptools 53.0.0
six 1.15.0
sos 4.9.2
subscription-manager 1.29.45.1
systemd-python 234
urllib3 1.26.5
```

</details>

<details><summary>Python packages: /var/lib/awx/venv/awx (python3.11) (194)</summary>

```text
adal 1.2.7
aiodns 3.2.0
aiofiles 24.1.0
aiohappyeyeballs 2.4.3
aiohttp 3.11.6
aiohttp-retry 2.8.3
aiosignal 1.3.1
annotated-types 0.6.0
ansible-runner 2.4.1
ansiconv 1.0.0
asciichartpy 1.5.7
asgiref 3.7.2
asn1 2.7.0
async-timeout 4.0.3
attrs 23.2.0
autobahn 23.6.2
autocommand 2.2.2
Automat 22.10.0
awx 4.7.1
azure-common 1.1.28
azure-core 1.30.0
azure-identity 1.15.0
azure-keyvault 4.2.0
azure-keyvault-certificates 4.7.0
azure-keyvault-keys 4.8.0
azure-keyvault-secrets 4.7.0
boto3 1.34.47
botocore 1.34.47
Brotli 1.1.0
cachetools 5.3.2
certifi 2038.12.31
cffi 1.16.0
channels 3.0.5
channels-redis 4.2.0
charset-normalizer 3.3.2
click 8.1.7
constantly 23.10.4
cryptography 42.0.8
Cython 3.1.3
daphne 3.0.2
defusedxml 0.7.1
Deprecated 1.2.14
distro 1.9.0
Django 4.2.24
django-ansible-base 2.6.20251001
django-auth-ldap 5.1.0
django-cors-headers 4.3.1
django-crum 0.7.9
django-extensions 3.2.3
django-flags 5.0.13
django-guid 3.2.1
django-oauth-toolkit 1.7.1
django-pglocks 1.0.4
django-polymorphic 3.1.0
django-radius 1.5.1
django-solo 2.2.0
djangorestframework 3.15.2
djangorestframework-yaml 2.0.0
dynaconf 3.2.10
enum-compat 0.0.3
et-xmlfile 1.1.0
filelock 3.13.1
frozenlist 1.4.1
gitdb 4.0.11
GitPython 3.1.42
google-auth 2.28.1
googleapis-common-protos 1.63.0
grpcio 1.68.1
hiredis 3.0.0
hyperlink 21.0.0
idna 3.10
importlib-metadata 6.2.1
incremental 24.7.2
inflect 7.0.0
inflection 0.5.1
irc 20.3.1
isodate 0.6.1
jaraco.collections 5.0.0
jaraco.context 4.3.0
jaraco.functools 4.0.0
jaraco.logging 3.3.0
jaraco.stream 3.0.3
jaraco.text 3.12.0
Jinja2 3.1.6
jmespath 1.0.1
jq 1.8.0
JSON-log-formatter 0.5.2
jsonschema 4.21.1
jsonschema-specifications 2023.12.1
jwcrypto 1.5.4
kubernetes 29.0.0
lockfile 0.12.2
lxml 4.9.4
Markdown 3.5.2
MarkupSafe 2.1.5
maturin 1.5.0
metrics-utility 0.6.0
more-itertools 10.2.0
msal 1.26.0
msal-extensions 1.1.0
msgpack 1.1.1
msrest 0.7.1
msrestazure 0.6.4
multidict 6.0.5
netaddr 1.2.1
numpy 1.26.4
oauthlib 3.2.2
opa-python-client 2.0.2
openpyxl 3.1.2
openshift 0.13.2
opentelemetry-api 1.24.0
opentelemetry-exporter-otlp 1.24.0
opentelemetry-exporter-otlp-proto-common 1.24.0
opentelemetry-exporter-otlp-proto-grpc 1.24.0
opentelemetry-exporter-otlp-proto-http 1.24.0
opentelemetry-instrumentation 0.45b0
opentelemetry-instrumentation-logging 0.45b0
opentelemetry-proto 1.24.0
opentelemetry-sdk 1.24.0
opentelemetry-semantic-conventions 0.45b0
packaging 25.0
pandas 2.2.1
pbr 6.0.0
pexpect 4.7.0
pip 21.2.4
pip 22.3.1
pkgconfig 1.5.5
portalocker 2.8.2
prometheus_client 0.20.0
propcache 0.2.0
protobuf 4.25.8
psutil 5.9.8
psycopg 3.1.18
ptyprocess 0.7.0
pyasn1 0.5.1
pyasn1-modules 0.3.0
pycares 4.5.0
pycparser 2.21
pydantic 2.5.0
pydantic_core 2.14.1
pygerduty 0.38.3
PyGithub 2.6.0
PyJWT 2.8.0
PyNaCl 1.5.0
pyOpenSSL 24.0.0
pyparsing 2.4.6
pyrad 2.4
python-daemon 3.1.2
python-dateutil 2.8.2
python-dsv-sdk 1.0.4
python-ldap 3.4.4
python-string-utils 1.0.0
python-tss-sdk 1.2.2
python3-openid 3.2.0
python3-saml 1.14.0
pytz 2024.1
PyYAML 6.0.2
pyzstd 0.15.10
receptorctl 1.5.7
redis 5.0.1
referencing 0.33.0
requests 2.32.3
requests-oauthlib 1.3.1
rpds-py 0.18.0
s3transfer 0.10.0
semantic-version 2.10.0
service-identity 24.1.0
setuptools 65.5.1
setuptools 80.9.0
setuptools-rust 1.8.1
setuptools-scm 8.0.4
six 1.16.0
slack_sdk 3.27.0
smmap 5.0.1
social-auth-app-django 5.4.2
social-auth-core 4.5.4
sqlparse 0.5.3
tacacs-plus 1.0
tempora 5.5.1
tomli 2.2.1
twilio 8.13.0
Twisted 24.7.0
txaio 23.1.1
typing_extensions 4.9.0
urllib3 1.26.20
uWSGI 2.0.28
uwsgitop 0.11
websocket-client 1.7.0
wheel 0.42.0
wrapt 1.16.0
xmlsec 1.3.13
yarl 1.17.2
zipp 3.17.0
zope.interface 6.2
```

</details>

[Back to top](#contents)

### de-supported-rhel9

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-26/de-supported-rhel9` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/de-supported-rhel9.tar.gz` |
| Labels `version` / `release` | `1.2.0` / `74` |
| Image ID | `sha256:e09120edc2cb6677db348fdc5085800310f721071329e2bbcf381f90f004b8e5` |
| Build date | 2025-09-24T01:54:32 |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.6 (Plow) |
| Python | 3.9, 3.11 |
| Ansible Core | 2.16.14 |

<details><summary>RPM packages (228)</summary>

```text
alsa-lib 1.2.13-2.el9
alternatives 1.24-2.el9
ansible-core 2.16.14-2.el9ap
ansible-rulebook 1.2.0-1.el9ap
ansible-runner 2.4.1-1.el9ap
audit-libs 3.1.5-4.el9
avahi-libs 0.8-22.el9_6.1
basesystem 11-13.el9
bash 5.1.8-9.el9
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
copy-jdk-configs 4.0-3.el9
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crypto-policies 20250128-1.git5269e22.el9
crypto-policies-scripts 20250128-1.git5269e22.el9
cups-libs 2.3.3op2-33.el9_6.1
curl-minimal 7.76.1-31.el9_6.1
cyrus-sasl-lib 2.1.27-21.el9
dbus-libs 1.12.20-8.el9
dejavu-sans-fonts 2.37-18.el9
dnf-data 4.14.0-25.el9
dumb-init 1.2.5-3.el9ap
expat 2.5.0-5.el9_6
file-libs 5.39-16.el9
filesystem 3.16-5.el9
findutils 4.8.0-7.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdbm-libs 1.23-1.el9
git-core 2.47.3-1.el9_6
glib2 2.68.4-16.el9_6.2
glibc 2.34-168.el9_6.23
glibc-common 2.34-168.el9_6.23
glibc-langpack-en 2.34-168.el9_6.23
glibc-minimal-langpack 2.34-168.el9_6.23
gmp 6.2.0-13.el9
gnupg2 2.3.3-4.el9
gnutls 3.8.3-6.el9_6.2
gobject-introspection 1.68.0-11.el9
gpg-pubkey 5a6340b3-6229229e
gpg-pubkey fd431d51-4ae0493b
gpgme 1.15.1-6.el9
grep 3.6-5.el9
gzip 1.12-1.el9
java-17-openjdk-headless 17.0.16.0.8-2.el9
javapackages-filesystem 6.4.0-1.el9
json-c 0.14-11.el9
json-glib 1.6.6-1.el9
keyutils-libs 1.6.3-1.el9
krb5-libs 1.21.1-8.el9_6
krb5-pkinit 1.21.1-8.el9_6
krb5-workstation 1.21.1-8.el9_6
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
less 590-5.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-6.el9_6
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9
libcap 2.48-9.el9_2
libcap-ng 0.8.2-7.el9
libcbor 0.7.0-5.el9
libcom_err 1.46.5-7.el9
libcurl-minimal 7.76.1-31.el9_6.1
libdb 5.3.28-57.el9_6
libdnf 0.69.0-13.el9
libeconf 0.4.1-4.el9
libedit 3.1-38.20210216cvs.el9
libevent 2.1.12-8.el9_4
libfdisk 2.37.4-21.el9
libffi 3.4.2-8.el9
libfido2 1.13.0-2.el9
libgcc 11.5.0-5.el9_5
libgcrypt 1.10.0-11.el9
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libkadm5 1.21.1-8.el9_6
libksba 1.5.1-7.el9
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9
libnghttp2 1.43.0-6.el9
libnsl2 2.0.0-1.el9
libpeas 1.30.0-4.el9
libpq 13.20-1.el9_5
libpwquality 1.4.4-8.el9
librepo 1.14.5-2.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libselinux 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-2.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9
libsolv 0.7.24-3.el9
libss 1.46.5-7.el9
libstdc++ 11.5.0-5.el9_5
libtasn1 4.16.0-9.el9
libtirpc 1.3.3-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libusbx 1.0.26-1.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-12.el9_6
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
lksctp-tools 1.0.19-3.el9_4
lua 5.4.4-4.el9
lua-libs 5.4.4-4.el9
lua-posix 35.0-8.el9
lz4-libs 1.9.3-5.el9
mailcap 2.1.49-5.el9
microdnf 3.9.1-3.el9
mpdecimal 2.5.1-3.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-10.20210508.el9_6.2
ncurses-libs 6.2-10.20210508.el9_6.2
nettle 3.10.1-1.el9
npth 1.6-8.el9
nspr 4.36.0-4.el9_4
nss 3.112.0-4.el9_4
nss-softokn 3.112.0-4.el9_4
nss-softokn-freebl 3.112.0-4.el9_4
nss-sysinit 3.112.0-4.el9_4
nss-util 3.112.0-4.el9_4
openldap 2.6.8-4.el9
openssh 8.7p1-45.el9
openssh-clients 8.7p1-45.el9
openssl 3.2.2-6.el9_5.1
openssl-fips-provider 3.0.7-6.el9_5
openssl-fips-provider-so 3.0.7-6.el9_5
openssl-libs 3.2.2-6.el9_5.1
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pam 1.5.1-26.el9_6
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
popt 1.18-8.el9
python3 3.9.21-2.el9_6.2
python3-libs 3.9.21-2.el9_6.2
python3-pip-wheel 21.3.1-1.el9
python3-setuptools-wheel 53.0.0-13.el9_6.1
python3.11 3.11.11-2.el9_6.2
python3.11-aiodns 3.2.0-1.el9ap
python3.11-aiohappyeyeballs 2.4.4-1.el9ap
python3.11-aiohttp 3.10.11-1.el9ap
python3.11-aiosignal 1.3.1-1.el9ap
python3.11-ansible-runner 2.4.1-1.el9ap
python3.11-async-timeout 4.0.3-2.el9ap
python3.11-attrs 22.2.0-1.el9ap
python3.11-azure-core 1.34.0-1.el9ap
python3.11-botocore 1.34.30-1.el9ap
python3.11-brotli 1.1.0-1.el9ap
python3.11-certifi 2023.5.7-1.el9ap
python3.11-cffi 1.15.1-1.el9
python3.11-charset-normalizer 2.1.0-1.el9
python3.11-cryptography 42.0.5-1.el9ap
python3.11-daemon 2.3.2-1.el9ap
python3.11-dateutil 2.8.2-2.el9ap
python3.11-docutils 0.20.1-2.el9ap
python3.11-dpath 2.1.6-1.el9ap
python3.11-drools-jpy 0.3.14-1.el9ap
python3.11-drools-jpy-jar 1.0.11-1.Final_redhat_00001.1.el9ap
python3.11-frozenlist 1.4.0-1.el9ap
python3.11-idna 3.4-1.el9
python3.11-isodate 0.6.1-2.el9ap
python3.11-janus 1.0.0-2.el9ap
python3.11-jinja2 3.1.6-1.el9ap
python3.11-jmespath 1.0.1-2.el9ap
python3.11-jpy 0.15.0-1.el9ap
python3.11-jsonschema 4.21.1-1.el9ap
python3.11-jsonschema-specifications 2023.12.1-1.el9ap
python3.11-libs 3.11.11-2.el9_6.2
python3.11-lockfile 0.12.2-2.el9ap
python3.11-markupsafe 2.1.5-1.el9ap
python3.11-multidict 6.0.4-1.el9ap
python3.11-packaging 23.2-1.el9ap
python3.11-pexpect 4.9.0-1.el9ap
python3.11-pip 22.3.1-5.el9
python3.11-pip-wheel 22.3.1-5.el9
python3.11-ply 3.11-1.el9
python3.11-psycopg 3.2.7-1.el9ap
python3.11-psycopg+c 3.2.7-1.el9ap
python3.11-psycopg-c 3.2.7-1.el9ap
python3.11-ptyprocess 0.7.0-1.el9ap
python3.11-pycares 4.4.0-2.el9ap
python3.11-pycparser 2.20-1.el9
python3.11-pyparsing 3.1.1-1.el9ap
python3.11-pyyaml 6.0-1.el9
python3.11-referencing 0.36.2-1.el9ap
python3.11-requests 2.31.0-2.el9ap
python3.11-resolvelib 1.0.1-1.el9ap
python3.11-rpds-py 0.18.1-1.el9ap
python3.11-setuptools 65.5.1-4.el9_6
python3.11-setuptools-wheel 65.5.1-4.el9_6
python3.11-six 1.16.0-1.el9
python3.11-typing-extensions 4.9.0-1.el9ap
python3.11-urllib3 1.26.20-1.el9ap
python3.11-watchdog 5.0.2-1.el9ap
python3.11-websockets 15.0-2.el9ap
python3.11-wrapt 1.16.0-1.el9ap
python3.11-xxhash 3.4.1-1.el9ap
python3.11-yarl 1.13.1-1.el9ap
readline 8.1-4.el9
redhat-release 9.6-0.1.el9
rootfiles 8.1-34.el9
rpm 4.16.1.3-37.el9
rpm-libs 4.16.1.3-37.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-12.el9
sqlite-libs 3.34.1-8.el9_6
sshpass 1.09-5.el9ap
systemd-libs 252-51.el9_6.2
tar 1.34-7.el9
tzdata 2025b-1.el9
tzdata-java 2025b-1.el9
util-linux 2.37.4-21.el9
util-linux-core 2.37.4-21.el9
xz-libs 5.2.5-8.el9_0
zlib 1.2.11-40.el9
```

</details>

<details><summary>Python packages: /usr (python3.11) (57)</summary>

```text
aiodns 3.2.0
aiohappyeyeballs 2.4.4
aiohttp 3.10.11
aiosignal 1.3.1
ansible-core 2.16.14
ansible-rulebook 1.2.0
ansible-runner 2.4.1
async-timeout 4.0.3
attrs 22.2.0
azure-core 1.34.0
botocore 1.34.30
Brotli 1.1.0
certifi 2023.5.7
cffi 1.15.1
charset-normalizer 2.1.0
cryptography 42.0.5
docutils 0.20.1
dpath 2.1.6
drools-jpy 0.3.14
frozenlist 1.4.0
idna 3.4
isodate 0.6.1
janus 1.0.0
Jinja2 3.1.6
jmespath 1.0.1
jpy 0.15.0
jsonschema 4.21.1
jsonschema-specifications 2023.12.1
lockfile 0.12.2
MarkupSafe 2.1.5
multidict 6.0.4
packaging 23.2
pexpect 4.9.0
pip 22.3.1
ply 3.11
psycopg 3.2.7
psycopg-c 3.2.7
ptyprocess 0.7.0
pycares 4.4.0
pycparser 2.20
pyparsing 3.1.1
python-daemon 2.3.2
python-dateutil 2.8.2
PyYAML 6.0
referencing 0.36.2
requests 2.31.0
resolvelib 1.0.1
rpds-py 0.18.1
setuptools 65.5.1
six 1.16.0
typing_extensions 4.9.0
urllib3 1.26.20
watchdog 5.0.2
websockets 15.0
wrapt 1.16.0
xxhash 3.4.1
yarl 1.13.1
```

</details>

<details><summary>Python packages: /usr/local (python3.11) (7)</summary>

```text
aiobotocore 2.11.2
aioitertools 0.11.0
aiokafka 0.10.0
azure-servicebus 7.12.1
decorator 5.2.1
gssapi 1.9.0
kafka-python 2.0.2
```

</details>

<details><summary>Ansible collections (1)</summary>

```text
ansible.eda 2.10.0
```

</details>

[Back to top](#contents)

### eda-controller-rhel9

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-26/eda-controller-rhel9` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/eda-controller-rhel9.tar.gz` |
| Labels `version` / `release` | `1.2.0` / `147` |
| Image ID | `sha256:3b8d9b8a8c8214ab07c82c66e2b940c2e465dbd5f8f34622677030f7876c1867` |
| Build date | 2025-09-23T21:40:50 |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.6 (Plow) |
| Python | 3.9, 3.11 |
| Ansible Core | 2.16.14 |

<details><summary>RPM packages (299)</summary>

```text
acl 2.3.1-4.el9
alternatives 1.24-2.el9
ansible-automation-platform-common 2.6-1.el9ap
ansible-automation-platform-selinux 0.2-3.el9ap
ansible-core 2.16.14-2.el9ap
audit-libs 3.1.5-4.el9
automation-eda-controller 1.2.0-1.el9ap
basesystem 11-13.el9
bash 5.1.8-9.el9
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crypto-policies 20250128-1.git5269e22.el9
curl-minimal 7.76.1-31.el9_6.1
cyrus-sasl-lib 2.1.27-21.el9
dbus 1.12.20-8.el9
dbus-broker 28-7.el9
dbus-common 1.12.20-8.el9
dejavu-sans-fonts 2.37-18.el9
diffutils 3.7-12.el9
dnf-data 4.14.0-25.el9
dumb-init 1.2.5-3.el9ap
expat 2.5.0-5.el9_6
file-libs 5.39-16.el9
filesystem 3.16-5.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdbm-libs 1.23-1.el9
git-core 2.47.3-1.el9_6
glib2 2.68.4-16.el9_6.2
glibc 2.34-168.el9_6.23
glibc-common 2.34-168.el9_6.23
glibc-langpack-en 2.34-168.el9_6.23
glibc-minimal-langpack 2.34-168.el9_6.23
gmp 6.2.0-13.el9
gnupg2 2.3.3-4.el9
gnutls 3.8.3-6.el9_6.2
gobject-introspection 1.68.0-11.el9
gpg-pubkey 5a6340b3-6229229e
gpg-pubkey fd431d51-4ae0493b
gpgme 1.15.1-6.el9
grep 3.6-5.el9
gzip 1.12-1.el9
json-c 0.14-11.el9
json-glib 1.6.6-1.el9
keyutils-libs 1.6.3-1.el9
kmod-libs 28-10.el9
krb5-libs 1.21.1-8.el9_6
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
less 590-5.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-6.el9_6
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9
libcap 2.48-9.el9_2
libcap-ng 0.8.2-7.el9
libcbor 0.7.0-5.el9
libcom_err 1.46.5-7.el9
libcurl-minimal 7.76.1-31.el9_6.1
libdb 5.3.28-57.el9_6
libdnf 0.69.0-13.el9
libeconf 0.4.1-4.el9
libedit 3.1-38.20210216cvs.el9
libevent 2.1.12-8.el9_4
libfdisk 2.37.4-21.el9
libffi 3.4.2-8.el9
libfido2 1.13.0-2.el9
libgcc 11.5.0-5.el9_5
libgcrypt 1.10.0-11.el9
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libksba 1.5.1-7.el9
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9
libnghttp2 1.43.0-6.el9
libnsl2 2.0.0-1.el9
libpeas 1.30.0-4.el9
libpq 13.20-1.el9_5
libpwquality 1.4.4-8.el9
librepo 1.14.5-2.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libseccomp 2.5.2-2.el9
libselinux 3.6-3.el9
libselinux-utils 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-2.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9
libsolv 0.7.24-3.el9
libstdc++ 11.5.0-5.el9_5
libtasn1 4.16.0-9.el9
libtirpc 1.3.3-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libusbx 1.0.26-1.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-12.el9_6
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
microdnf 3.9.1-3.el9
mpdecimal 2.5.1-3.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-10.20210508.el9_6.2
ncurses-libs 6.2-10.20210508.el9_6.2
nettle 3.10.1-1.el9
npth 1.6-8.el9
openldap 2.6.8-4.el9
openssh 8.7p1-45.el9
openssh-clients 8.7p1-45.el9
openssl 3.2.2-6.el9_5.1
openssl-fips-provider 3.0.7-6.el9_5
openssl-fips-provider-so 3.0.7-6.el9_5
openssl-libs 3.2.2-6.el9_5.1
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pam 1.5.1-26.el9_6
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
podman-remote 5.4.0-13.el9_6
policycoreutils 3.6-2.1.el9
popt 1.18-8.el9
postgresql 15.14-1.module+el9.6.0+23419+7863ab62
postgresql-private-libs 15.14-1.module+el9.6.0+23419+7863ab62
python3 3.9.21-2.el9_6.2
python3-cffi 1.15.0-3.el9ap
python3-cryptography 42.0.5-1.el9ap
python3-libs 3.9.21-2.el9_6.2
python3-pip-wheel 21.3.1-1.el9
python3-pycparser 2.21-2.el9pc
python3-setuptools 53.0.0-13.el9_6.1
python3-setuptools-wheel 53.0.0-13.el9_6.1
python3.11 3.11.11-2.el9_6.2
python3.11-Automat 22.10.0-3.el9ap
python3.11-adal 1.2.7-1.el9ap
python3.11-ansible-runner 2.4.1-1.el9ap
python3.11-asgiref 3.7.2-1.el9ap
python3.11-async-timeout 4.0.3-2.el9ap
python3.11-attrs 22.2.0-1.el9ap
python3.11-autobahn 24.4.2-1.el9ap
python3.11-awx-plugins-core 0.0.1~a10-1.el9ap
python3.11-awx-plugins-core+credentials-aim 0.0.1~a10-1.el9ap
python3.11-awx-plugins-core+credentials-aws-secretsmanager-credential 0.0.1~a10-1.el9ap
python3.11-awx-plugins-core+credentials-azure-kv 0.0.1~a10-1.el9ap
python3.11-awx-plugins-core+credentials-centrify-vault-kv 0.0.1~a10-1.el9ap
python3.11-awx-plugins-core+credentials-conjur 0.0.1~a10-1.el9ap
python3.11-awx-plugins-core+credentials-github-app 0.0.1~a10-1.el9ap
python3.11-awx-plugins-core+credentials-hashivault-kv 0.0.1~a10-1.el9ap
python3.11-awx-plugins-core+credentials-hashivault-ssh 0.0.1~a10-1.el9ap
python3.11-awx-plugins-core+credentials-thycotic-dsv 0.0.1~a10-1.el9ap
python3.11-awx-plugins-core+credentials-thycotic-tss 0.0.1~a10-1.el9ap
python3.11-awx-plugins-interfaces 0.0.1~a5-1.el9ap
python3.11-azure-core 1.34.0-1.el9ap
python3.11-azure-identity 1.23.0-1.el9ap
python3.11-azure-keyvault 4.2.0-1.el9ap
python3.11-azure-keyvault-certificates 4.10.0-1.el9ap
python3.11-azure-keyvault-keys 4.11.0-1.el9ap
python3.11-azure-keyvault-secrets 4.10.0-1.el9ap
python3.11-boto3 1.34.30-1.el9ap
python3.11-botocore 1.34.30-1.el9ap
python3.11-cachetools 5.3.2-1.el9ap
python3.11-certifi 2023.5.7-1.el9ap
python3.11-cffi 1.15.1-1.el9
python3.11-channels 4.0.0-3.el9ap
python3.11-channels+daphne 4.0.0-3.el9ap
python3.11-charset-normalizer 2.1.0-1.el9
python3.11-click 8.1.7-1.el9ap
python3.11-constantly 15.1.0-2.el9ap
python3.11-croniter 2.0.1-1.el9ap
python3.11-cryptography 42.0.5-1.el9ap
python3.11-daemon 2.3.2-1.el9ap
python3.11-daphne 4.0.0-3.el9ap
python3.11-dateutil 2.8.2-2.el9ap
python3.11-deprecated 1.2.14-1.el9ap
python3.11-dispatcherd 2025.5.19-2.el9ap
python3.11-dispatcherd+pg_notify 2025.5.19-2.el9ap
python3.11-distro 1.9.0-1.el9ap
python3.11-django 4.2.24-1.el9ap
python3.11-django-ansible-base 2.6.20251001-1.el9ap
python3.11-django-ansible-base+channel_auth 2.6.20251001-1.el9ap
python3.11-django-ansible-base+feature_flags 2.6.20251001-1.el9ap
python3.11-django-ansible-base+jwt_consumer 2.6.20251001-1.el9ap
python3.11-django-ansible-base+rbac 2.6.20251001-1.el9ap
python3.11-django-ansible-base+redis_client 2.6.20251001-1.el9ap
python3.11-django-ansible-base+resource_registry 2.6.20251001-1.el9ap
python3.11-django-ansible-base+rest_filters 2.6.20251001-1.el9ap
python3.11-django-crum 0.7.9-2.el9ap
python3.11-django-filter 23.5-1.el9ap
python3.11-django-flags 5.0.13-1.el9ap
python3.11-django-redis 5.4.0-1.el9ap
python3.11-django-rq 2.8.0-1.el9ap
python3.11-django-split-settings 1.2.0-2.el9ap
python3.11-djangorestframework 3.15.1-1.el9ap
python3.11-docutils 0.20.1-2.el9ap
python3.11-drf-spectacular 0.26.5-2.el9ap
python3.11-dsv-sdk 1.0.4-1.el9ap
python3.11-dynaconf 3.2.11-1.el9ap
python3.11-ecdsa 0.18.0-1.el9ap
python3.11-gnupg 0.5.2-1.el9ap
python3.11-google-auth 2.27.0-1.el9ap
python3.11-gunicorn 22.0.0-1.el9ap
python3.11-hyperlink 21.0.0-2.el9ap
python3.11-idna 3.4-1.el9
python3.11-incremental 24.7.2-1.el9ap
python3.11-inflection 0.5.1-4.el9ap
python3.11-insights-analytics-collector 0.3.2-2.el9ap
python3.11-isodate 0.6.1-2.el9ap
python3.11-jinja2 3.1.6-1.el9ap
python3.11-jmespath 1.0.1-2.el9ap
python3.11-jsonschema 4.21.1-1.el9ap
python3.11-jsonschema-specifications 2023.12.1-1.el9ap
python3.11-kubernetes 26.1.0-2.el9ap
python3.11-libs 3.11.11-2.el9_6.2
python3.11-lockfile 0.12.2-2.el9ap
python3.11-markupsafe 2.1.5-1.el9ap
python3.11-msal 1.32.3-1.el9ap
python3.11-msal-extensions 1.3.1-1.el9ap
python3.11-msrest 0.7.1-2.el9ap
python3.11-msrestazure 0.6.4-1.el9ap
python3.11-oauthlib 3.2.2-1.el9ap
python3.11-packaging 23.2-1.el9ap
python3.11-pexpect 4.9.0-1.el9ap
python3.11-pip-wheel 22.3.1-5.el9
python3.11-ply 3.11-1.el9
python3.11-podman 5.4.0.1-1.el9ap
python3.11-psycopg 3.2.7-1.el9ap
python3.11-ptyprocess 0.7.0-1.el9ap
python3.11-pyOpenSSL 24.1.0-1.el9ap
python3.11-pyasn1 0.5.1-1.el9ap
python3.11-pyasn1-modules 0.3.0-1.el9ap
python3.11-pycparser 2.20-1.el9
python3.11-pydantic 1.10.15-1.el9ap
python3.11-pygithub 2.6.1-1.el9ap
python3.11-pyjwt 2.7.0-2.el9ap
python3.11-pyjwt+crypto 2.7.0-2.el9ap
python3.11-pynacl 1.5.0-1.el9ap
python3.11-pytz 2024.1-1.el9ap
python3.11-pyyaml 6.0-1.el9
python3.11-redis 4.6.0-2.el9ap
python3.11-referencing 0.36.2-1.el9ap
python3.11-requests 2.31.0-2.el9ap
python3.11-requests-oauthlib 1.3.1-1.el9ap
python3.11-resolvelib 1.0.1-1.el9ap
python3.11-rpds-py 0.18.1-1.el9ap
python3.11-rq 1.13.0-3.el9ap
python3.11-rq-scheduler 0.10.0-3.el9ap
python3.11-rsa 4.9-2.el9ap
python3.11-s3transfer 0.10.0-1.el9ap
python3.11-service-identity 21.1.0-2.el9ap
python3.11-setuptools 65.5.1-4.el9_6
python3.11-setuptools-wheel 65.5.1-4.el9_6
python3.11-six 1.16.0-1.el9
python3.11-sqlparse 0.5.3-2.el9ap
python3.11-tss-sdk 1.2.3-1.el9ap
python3.11-twisted 24.7.0-1.el9ap
python3.11-twisted+tls 24.7.0-1.el9ap
python3.11-txaio 23.1.1-2.el9ap
python3.11-typing-extensions 4.9.0-1.el9ap
python3.11-uritemplate 4.1.1-3.el9ap
python3.11-urllib3 1.26.20-1.el9ap
python3.11-validators 0.34.0-1.el9ap
python3.11-websocket-client 1.7.0-2.el9ap
python3.11-wrapt 1.16.0-1.el9ap
python3.11-xxhash 3.4.1-1.el9ap
python3.11-zope-interface 6.1-1.el9ap
readline 8.1-4.el9
redhat-release 9.6-0.1.el9
rootfiles 8.1-34.el9
rpm 4.16.1.3-37.el9
rpm-libs 4.16.1.3-37.el9
rpm-plugin-selinux 4.16.1.3-37.el9
sed 4.8-9.el9
selinux-policy 38.1.53-5.el9_6
selinux-policy-targeted 38.1.53-5.el9_6
setup 2.13.7-10.el9
shadow-utils 4.9-12.el9
shadow-utils-subid 4.9-12.el9
sqlite-libs 3.34.1-8.el9_6
sshpass 1.09-5.el9ap
systemd 252-51.el9_6.2
systemd-libs 252-51.el9_6.2
systemd-pam 252-51.el9_6.2
systemd-rpm-macros 252-51.el9_6.2
tzdata 2025b-1.el9
util-linux 2.37.4-21.el9
util-linux-core 2.37.4-21.el9
xz-libs 5.2.5-8.el9_0
zlib 1.2.11-40.el9
```

</details>

<details><summary>Python packages: /usr (python3.11) (110)</summary>

```text
aap-eda 1.2.0
adal 1.2.7
ansible-core 2.16.14
ansible-runner 2.4.1
asgiref 3.7.2
async-timeout 4.0.3
attrs 22.2.0
autobahn 24.4.2
Automat 22.10.0
awx-plugins-core 0.0.1a10
awx-plugins.interfaces 0.0.1a5
azure-core 1.34.0
azure-identity 1.23.0
azure-keyvault 4.2.0
azure-keyvault-certificates 4.10.0
azure-keyvault-keys 4.11.0
azure-keyvault-secrets 4.10.0
boto3 1.34.30
botocore 1.34.30
cachetools 5.3.2
certifi 2023.5.7
cffi 1.15.1
channels 4.0.0
charset-normalizer 2.1.0
click 8.1.7
constantly 15.1.0
croniter 2.0.1
cryptography 42.0.5
daphne 4.0.0
Deprecated 1.2.14
dispatcherd 2025.5.19
distro 1.9.0
Django 4.2.24
django-ansible-base 2.6.20251001
django-crum 0.7.9
django-filter 23.5
django-flags 5.0.13
django-redis 5.4.0
django-rq 2.8.0
django-split-settings 1.2.0
djangorestframework 3.15.1
docutils 0.20.1
drf-spectacular 0.26.5
dynaconf 3.2.11
ecdsa 0.18.0
google-auth 2.27.0
gunicorn 22.0.0
hyperlink 21.0.0
idna 3.4
incremental 24.7.2
inflection 0.5.1
insights-analytics-collector 0.3.2
isodate 0.6.1
Jinja2 3.1.6
jmespath 1.0.1
jsonschema 4.21.1
jsonschema-specifications 2023.12.1
kubernetes 26.1.0
lockfile 0.12.2
MarkupSafe 2.1.5
msal 1.32.3
msal-extensions 1.3.1
msrest 0.7.1
msrestazure 0.6.4
oauthlib 3.2.2
packaging 23.2
pexpect 4.9.0
ply 3.11
podman 5.4.0.1
psycopg 3.2.7
ptyprocess 0.7.0
pyasn1 0.5.1
pyasn1-modules 0.3.0
pycparser 2.20
pydantic 1.10.15
PyGithub 2.6.1
PyJWT 2.7.0
PyNaCl 1.5.0
pyOpenSSL 24.1.0
python-daemon 2.3.2
python-dateutil 2.8.2
python-dsv-sdk 1.0.4
python-gnupg 0.5.2
python-tss-sdk 1.2.3
pytz 2024.1
PyYAML 6.0
redis 4.6.0
referencing 0.36.2
requests 2.31.0
requests-oauthlib 1.3.1
resolvelib 1.0.1
rpds-py 0.18.1
rq 1.13.0
rq-scheduler 0.10.0
rsa 4.9
s3transfer 0.10.0
service-identity 21.1.0
setuptools 65.5.1
six 1.16.0
sqlparse 0.5.3
Twisted 24.7.0
txaio 23.1.1
typing_extensions 4.9.0
uritemplate 4.1.1
urllib3 1.26.20
validators 0.34.0
websocket-client 1.7.0
wrapt 1.16.0
xxhash 3.4.1
zope.interface 6.1
```

</details>

<details><summary>Python packages: /usr (python3.9) (4)</summary>

```text
cffi 1.15.0
cryptography 42.0.5
pycparser 2.21
setuptools 53.0.0
```

</details>

[Back to top](#contents)

### eda-controller-ui-rhel9

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-26/eda-controller-ui-rhel9` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/eda-controller-ui-rhel9.tar.gz` |
| Labels `version` / `release` | `1.2.0` / `141` |
| Image ID | `sha256:5e8655027857c5ded40b09f5fade40afecab3672a9b9d0d5254153cd6a9fdf0f` |
| Build date | 2025-09-24T00:41:17 |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.6 (Plow) |
| Python | 3.9 |
| Ansible Core | N/A |

<details><summary>RPM packages (301)</summary>

```text
acl 2.3.1-4.el9
alternatives 1.24-2.el9
attr 2.5.1-3.el9
audit-libs 3.1.5-4.el9
basesystem 11-13.el9
bash 5.1.8-9.el9
bind9.18-libs 9.18.29-4.el9_6
bind9.18-utils 9.18.29-4.el9_6
bsdtar 3.5.3-6.el9_6
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crypto-policies 20250128-1.git5269e22.el9
crypto-policies-scripts 20250128-1.git5269e22.el9
curl-minimal 7.76.1-31.el9_6.1
cyrus-sasl-lib 2.1.27-21.el9
dbus 1.12.20-8.el9
dbus-broker 28-7.el9
dbus-common 1.12.20-8.el9
dbus-libs 1.12.20-8.el9
dejavu-sans-fonts 2.37-18.el9
dmidecode 3.6-1.el9
dnf 4.14.0-25.el9
dnf-data 4.14.0-25.el9
elfutils-default-yama-scope 0.192-6.el9_6
elfutils-libelf 0.192-6.el9_6
elfutils-libs 0.192-6.el9_6
environment-modules 5.3.0-1.el9
expat 2.5.0-5.el9_6
file-libs 5.39-16.el9
filesystem 3.16-5.el9
findutils 4.8.0-7.el9
fontconfig 2.14.0-2.el9_1
fonts-filesystem 2.0.5-7.el9.1
freetype 2.10.4-10.el9_5
fstrm 0.6.1-3.el9
gawk 5.1.0-6.el9
gd 2.3.2-3.el9
gdb-gdbserver 14.2-4.1.el9_6
gdbm-libs 1.23-1.el9
gettext 0.21-8.el9
gettext-libs 0.21-8.el9
glib2 2.68.4-16.el9_6.2
glibc 2.34-168.el9_6.23
glibc-common 2.34-168.el9_6.23
glibc-langpack-en 2.34-168.el9_6.23
glibc-locale-source 2.34-168.el9_6.23
glibc-minimal-langpack 2.34-168.el9_6.23
gmp 6.2.0-13.el9
gnupg2 2.3.3-4.el9
gnutls 3.8.3-6.el9_6.2
gobject-introspection 1.68.0-11.el9
gpg-pubkey 5a6340b3-6229229e
gpg-pubkey fd431d51-4ae0493b
gpgme 1.15.1-6.el9
graphite2 1.3.14-9.el9
grep 3.6-5.el9
groff-base 1.22.4-10.el9
gzip 1.12-1.el9
harfbuzz 2.7.4-10.el9
hostname 3.23-6.el9
ima-evm-utils 1.5-3.el9
iproute 6.11.0-1.el9
jbigkit-libs 2.1-23.el9
json-c 0.14-11.el9
json-glib 1.6.6-1.el9
keyutils 1.6.3-1.el9
keyutils-libs 1.6.3-1.el9
kmod-libs 28-10.el9
krb5-libs 1.21.1-8.el9_6
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
less 590-5.el9
libX11 1.7.0-11.el9
libX11-common 1.7.0-11.el9
libXau 1.0.9-8.el9
libXpm 3.5.13-10.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-6.el9_6
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9
libbpf 1.5.0-1.el9
libbrotli 1.0.9-7.el9_5
libcap 2.48-9.el9_2
libcap-ng 0.8.2-7.el9
libcom_err 1.46.5-7.el9
libcomps 0.1.18-1.el9
libcurl-minimal 7.76.1-31.el9_6.1
libdb 5.3.28-57.el9_6
libdnf 0.69.0-13.el9
libdnf-plugin-subscription-manager 1.29.45.1-1.el9_6
libeconf 0.4.1-4.el9
libevent 2.1.12-8.el9_4
libfdisk 2.37.4-21.el9
libffi 3.4.2-8.el9
libgcc 11.5.0-5.el9_5
libgcrypt 1.10.0-11.el9
libgomp 11.5.0-5.el9_5
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libjpeg-turbo 2.0.90-7.el9
libksba 1.5.1-7.el9
libmaxminddb 1.5.2-4.el9
libmnl 1.0.4-16.el9_4
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9
libnghttp2 1.43.0-6.el9
libpipeline 1.5.3-4.el9
libpng 1.6.37-12.el9
libpwquality 1.4.4-8.el9
librepo 1.14.5-2.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libseccomp 2.5.2-2.el9
libselinux 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-2.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9
libsolv 0.7.24-3.el9
libstdc++ 11.5.0-5.el9_5
libtasn1 4.16.0-9.el9
libtiff 4.4.0-13.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libuser 0.63-16.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9
libuv 1.42.0-2.el9_4
libverto 0.3.2-3.el9
libwebp 1.2.0-8.el9_3
libxcb 1.13.1-9.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-12.el9_6
libxslt 1.1.34-13.el9_6
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
lmdb-libs 0.9.29-3.el9
logrotate 3.18.0-9.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
man-db 2.9.3-7.el9
mpfr 4.1.0-7.el9
ncurses 6.2-10.20210508.el9_6.2
ncurses-base 6.2-10.20210508.el9_6.2
ncurses-libs 6.2-10.20210508.el9_6.2
nettle 3.10.1-1.el9
nginx 1.24.0-4.module+el9.5.0+22954+e2d70a1c.1
nginx-all-modules 1.24.0-4.module+el9.5.0+22954+e2d70a1c.1
nginx-core 1.24.0-4.module+el9.5.0+22954+e2d70a1c.1
nginx-filesystem 1.24.0-4.module+el9.5.0+22954+e2d70a1c.1
nginx-mod-http-image-filter 1.24.0-4.module+el9.5.0+22954+e2d70a1c.1
nginx-mod-http-perl 1.24.0-4.module+el9.5.0+22954+e2d70a1c.1
nginx-mod-http-xslt-filter 1.24.0-4.module+el9.5.0+22954+e2d70a1c.1
nginx-mod-mail 1.24.0-4.module+el9.5.0+22954+e2d70a1c.1
nginx-mod-stream 1.24.0-4.module+el9.5.0+22954+e2d70a1c.1
npth 1.6-8.el9
nss_wrapper-libs 1.1.13-1.el9
openldap 2.6.8-4.el9
openssl 3.2.2-6.el9_5.1
openssl-fips-provider 3.0.7-6.el9_5
openssl-fips-provider-so 3.0.7-6.el9_5
openssl-libs 3.2.2-6.el9_5.1
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pam 1.5.1-26.el9_6
passwd 0.80-12.el9
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
perl-AutoLoader 5.74-481.1.el9_6
perl-B 1.80-481.1.el9_6
perl-Carp 1.50-460.el9
perl-Class-Struct 0.66-481.1.el9_6
perl-Data-Dumper 2.174-462.el9
perl-Digest 1.19-4.el9
perl-Digest-MD5 2.58-4.el9
perl-Encode 3.08-462.el9
perl-Errno 1.30-481.1.el9_6
perl-Exporter 5.74-461.el9
perl-Fcntl 1.13-481.1.el9_6
perl-File-Basename 2.85-481.1.el9_6
perl-File-Path 2.18-4.el9
perl-File-Temp 0.231.100-4.el9
perl-File-stat 1.09-481.1.el9_6
perl-FileHandle 2.03-481.1.el9_6
perl-Getopt-Long 2.52-4.el9
perl-Getopt-Std 1.12-481.1.el9_6
perl-HTTP-Tiny 0.076-462.el9
perl-IO 1.43-481.1.el9_6
perl-IO-Socket-IP 0.41-5.el9
perl-IO-Socket-SSL 2.073-2.el9
perl-IPC-Open3 1.21-481.1.el9_6
perl-MIME-Base64 3.16-4.el9
perl-Mozilla-CA 20200520-6.el9
perl-NDBM_File 1.15-481.1.el9_6
perl-Net-SSLeay 1.94-1.el9
perl-POSIX 1.94-481.1.el9_6
perl-PathTools 3.78-461.el9
perl-Pod-Escapes 1.07-460.el9
perl-Pod-Perldoc 3.28.01-461.el9
perl-Pod-Simple 3.42-4.el9
perl-Pod-Usage 2.01-4.el9
perl-Scalar-List-Utils 1.56-462.el9
perl-SelectSaver 1.02-481.1.el9_6
perl-Socket 2.031-4.el9
perl-Storable 3.21-460.el9
perl-Symbol 1.08-481.1.el9_6
perl-Term-ANSIColor 5.01-461.el9
perl-Term-Cap 1.17-460.el9
perl-Text-ParseWords 3.30-460.el9
perl-Text-Tabs+Wrap 2013.0523-460.el9
perl-Time-Local 1.300-7.el9
perl-URI 5.09-3.el9
perl-base 2.27-481.1.el9_6
perl-constant 1.33-461.el9
perl-if 0.60.800-481.1.el9_6
perl-interpreter 5.32.1-481.1.el9_6
perl-libnet 3.13-4.el9
perl-libs 5.32.1-481.1.el9_6
perl-mro 1.23-481.1.el9_6
perl-overload 1.31-481.1.el9_6
perl-overloading 0.02-481.1.el9_6
perl-parent 0.238-460.el9
perl-podlators 4.14-460.el9
perl-subs 1.03-481.1.el9_6
perl-vars 1.05-481.1.el9_6
popt 1.18-8.el9
procps-ng 3.3.17-14.el9
protobuf-c 1.3.3-13.el9
psmisc 23.4-3.el9
python3 3.9.21-2.el9_6.2
python3-chardet 4.0.0-5.el9
python3-cloud-what 1.29.45.1-1.el9_6
python3-dateutil 2.8.1-7.el9
python3-dbus 1.2.18-2.el9
python3-decorator 4.4.2-6.el9
python3-dnf 4.14.0-25.el9
python3-dnf-plugins-core 4.3.0-20.el9
python3-gobject-base 3.40.1-6.el9
python3-gobject-base-noarch 3.40.1-6.el9
python3-gpg 1.15.1-6.el9
python3-hawkey 0.69.0-13.el9
python3-idna 2.10-7.el9_4.1
python3-iniparse 0.4-45.el9
python3-inotify 0.9.6-25.el9
python3-libcomps 0.1.18-1.el9
python3-libdnf 0.69.0-13.el9
python3-librepo 1.14.5-2.el9
python3-libs 3.9.21-2.el9_6.2
python3-pip-wheel 21.3.1-1.el9
python3-pysocks 1.7.1-12.el9
python3-requests 2.25.1-10.el9_6
python3-rpm 4.16.1.3-37.el9
python3-setuptools 53.0.0-13.el9_6.1
python3-setuptools-wheel 53.0.0-13.el9_6.1
python3-six 1.15.0-9.el9
python3-subscription-manager-rhsm 1.29.45.1-1.el9_6
python3-systemd 234-19.el9
python3-urllib3 1.26.5-6.el9
readline 8.1-4.el9
redhat-logos-httpd 90.5-1.el9_6.1
redhat-release 9.6-0.1.el9
rootfiles 8.1-34.el9
rpm 4.16.1.3-37.el9
rpm-build-libs 4.16.1.3-37.el9
rpm-libs 4.16.1.3-37.el9
rpm-sign-libs 4.16.1.3-37.el9
rsync 3.2.5-3.el9
scl-utils 2.0.3-4.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-12.el9
sqlite-libs 3.34.1-8.el9_6
subscription-manager 1.29.45.1-1.el9_6
subscription-manager-rhsm-certificates 20220623-1.el9
systemd 252-51.el9_6.2
systemd-libs 252-51.el9_6.2
systemd-pam 252-51.el9_6.2
systemd-rpm-macros 252-51.el9_6.2
tar 1.34-7.el9
tcl 8.6.10-7.el9
tpm2-tss 3.2.3-1.el9
tzdata 2025b-1.el9
unzip 6.0-58.el9_5
usermode 1.114-6.el9
util-linux 2.37.4-21.el9
util-linux-core 2.37.4-21.el9
vim-filesystem 8.2.2637-22.el9_6
vim-minimal 8.2.2637-22.el9_6
virt-what 1.27-1.el9
which 2.21-30.el9_6
xml-common 0.6.3-58.el9
xz 5.2.5-8.el9_0
xz-libs 5.2.5-8.el9_0
yum 4.14.0-25.el9
zlib 1.2.11-40.el9
```

</details>

<details><summary>Python packages: /usr (python3.9) (18)</summary>

```text
chardet 4.0.0
dbus-python 1.2.18
decorator 4.4.2
gpg 1.15.1
idna 2.10
iniparse 0.4
libcomps 0.1.18
PyGObject 3.40.1
pyinotify 0.9.6
PySocks 1.7.1
python-dateutil 2.8.1
requests 2.25.1
rpm 4.16.1.3
setuptools 53.0.0
six 1.15.0
subscription-manager 1.29.45.1
systemd-python 234
urllib3 1.26.5
```

</details>

[Back to top](#contents)

### ee-minimal-rhel9

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-26/ee-minimal-rhel9` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/ee-minimal-rhel9.tar.gz` |
| Labels `version` / `release` | `1.0.0` / `973` |
| Image ID | `sha256:e96a4d533cefd35e265af3b04a0de1a5bf85fde001dd368eb7a268e029ebe9ce` |
| Build date | 2025-09-24T00:54:55 |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.6 (Plow) |
| Python | 3.11 |
| Ansible Core | 2.16.14 |

<details><summary>RPM packages (199)</summary>

```text
alternatives 1.24-2.el9
ansible-core 2.16.14-2.el9ap
ansible-lint 25.8.2-1.el9ap
ansible-runner 2.4.1-1.el9ap
ansible-test 2.16.14-2.el9ap
audit-libs 3.1.5-4.el9
basesystem 11-13.el9
bash 5.1.8-9.el9
bzip2 1.0.8-10.el9_5
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crypto-policies 20250128-1.git5269e22.el9
curl-minimal 7.76.1-31.el9_6.1
cyrus-sasl-lib 2.1.27-21.el9
dejavu-sans-fonts 2.37-18.el9
dnf-data 4.14.0-25.el9
dumb-init 1.2.5-3.el9ap
expat 2.5.0-5.el9_6
file 5.39-16.el9
file-libs 5.39-16.el9
filesystem 3.16-5.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdbm-libs 1.23-1.el9
git-core 2.47.3-1.el9_6
glib2 2.68.4-16.el9_6.2
glibc 2.34-168.el9_6.23
glibc-common 2.34-168.el9_6.23
glibc-langpack-en 2.34-168.el9_6.23
glibc-minimal-langpack 2.34-168.el9_6.23
gmp 6.2.0-13.el9
gnupg2 2.3.3-4.el9
gnutls 3.8.3-6.el9_6.2
gobject-introspection 1.68.0-11.el9
gpg-pubkey 5a6340b3-6229229e
gpg-pubkey fd431d51-4ae0493b
gpgme 1.15.1-6.el9
grep 3.6-5.el9
gzip 1.12-1.el9
json-c 0.14-11.el9
json-glib 1.6.6-1.el9
keyutils-libs 1.6.3-1.el9
krb5-libs 1.21.1-8.el9_6
krb5-pkinit 1.21.1-8.el9_6
krb5-workstation 1.21.1-8.el9_6
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
less 590-5.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-6.el9_6
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9
libcap 2.48-9.el9_2
libcap-ng 0.8.2-7.el9
libcbor 0.7.0-5.el9
libcom_err 1.46.5-7.el9
libcurl-minimal 7.76.1-31.el9_6.1
libdb 5.3.28-57.el9_6
libdnf 0.69.0-13.el9
libeconf 0.4.1-4.el9
libedit 3.1-38.20210216cvs.el9
libevent 2.1.12-8.el9_4
libfdisk 2.37.4-21.el9
libffi 3.4.2-8.el9
libfido2 1.13.0-2.el9
libgcc 11.5.0-5.el9_5
libgcrypt 1.10.0-11.el9
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libkadm5 1.21.1-8.el9_6
libksba 1.5.1-7.el9
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9
libnghttp2 1.43.0-6.el9
libnsl2 2.0.0-1.el9
libpeas 1.30.0-4.el9
libpwquality 1.4.4-8.el9
librepo 1.14.5-2.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libselinux 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-2.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9
libsolv 0.7.24-3.el9
libss 1.46.5-7.el9
libstdc++ 11.5.0-5.el9_5
libtasn1 4.16.0-9.el9
libtirpc 1.3.3-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libusbx 1.0.26-1.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-12.el9_6
libxslt 1.1.34-13.el9_6
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
microdnf 3.9.1-3.el9
mpdecimal 2.5.1-3.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-10.20210508.el9_6.2
ncurses-libs 6.2-10.20210508.el9_6.2
nettle 3.10.1-1.el9
npth 1.6-8.el9
openldap 2.6.8-4.el9
openssh 8.7p1-45.el9
openssh-clients 8.7p1-45.el9
openssl 3.2.2-6.el9_5.1
openssl-fips-provider 3.0.7-6.el9_5
openssl-fips-provider-so 3.0.7-6.el9_5
openssl-libs 3.2.2-6.el9_5.1
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pam 1.5.1-26.el9_6
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
popt 1.18-8.el9
python3.11 3.11.11-2.el9_6.2
python3.11-ansible-compat 25.8.1-1.el9ap
python3.11-ansible-runner 2.4.1-1.el9ap
python3.11-attrs 22.2.0-1.el9ap
python3.11-black 24.4.2-2.el9ap
python3.11-bracex 2.4-1.el9ap
python3.11-cffi 1.15.1-1.el9
python3.11-charset-normalizer 2.1.0-1.el9
python3.11-click 8.1.7-1.el9ap
python3.11-cryptography 42.0.5-1.el9ap
python3.11-daemon 2.3.2-1.el9ap
python3.11-docutils 0.20.1-2.el9ap
python3.11-filelock 3.13.1-1.el9ap
python3.11-idna 3.4-1.el9
python3.11-importlib-metadata 6.0.1-2.el9ap
python3.11-jinja2 3.1.6-1.el9ap
python3.11-jsonschema 4.21.1-1.el9ap
python3.11-jsonschema-specifications 2023.12.1-1.el9ap
python3.11-libs 3.11.11-2.el9_6.2
python3.11-lockfile 0.12.2-2.el9ap
python3.11-lxml 4.9.2-4.el9
python3.11-markupsafe 2.1.5-1.el9ap
python3.11-mypy-extensions 1.0.0-1.el9ap
python3.11-packaging 23.2-1.el9ap
python3.11-pathspec 0.12.1-1.el9ap
python3.11-pexpect 4.9.0-1.el9ap
python3.11-pip 22.3.1-5.el9
python3.11-pip-wheel 22.3.1-5.el9
python3.11-platformdirs 4.2.0-1.el9ap
python3.11-ply 3.11-1.el9
python3.11-ptyprocess 0.7.0-1.el9ap
python3.11-pyOpenSSL 24.1.0-1.el9ap
python3.11-pycparser 2.20-1.el9
python3.11-pysocks 1.7.1-1.el9
python3.11-pyyaml 6.0-1.el9
python3.11-referencing 0.36.2-1.el9ap
python3.11-requests 2.28.1-1.el9
python3.11-resolvelib 1.0.1-1.el9ap
python3.11-rpds-py 0.18.1-1.el9ap
python3.11-ruamel-yaml 0.18.15-1.el9ap
python3.11-ruamel-yaml-clib 0.2.8-1.el9ap
python3.11-setuptools 65.5.1-4.el9_6
python3.11-setuptools-wheel 65.5.1-4.el9_6
python3.11-six 1.16.0-1.el9
python3.11-subprocess-tee 0.4.1-2.el9ap
python3.11-typing-extensions 4.9.0-1.el9ap
python3.11-urllib3 1.26.12-5.el9
python3.11-wcmatch 8.5-1.el9ap
python3.11-zipp 3.19.2-1.el9ap
readline 8.1-4.el9
redhat-release 9.6-0.1.el9
rootfiles 8.1-34.el9
rpm 4.16.1.3-37.el9
rpm-libs 4.16.1.3-37.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-12.el9
sqlite-libs 3.34.1-8.el9_6
sshpass 1.09-5.el9ap
systemd-libs 252-51.el9_6.2
tar 1.34-7.el9
tzdata 2025b-1.el9
unzip 6.0-58.el9_5
util-linux 2.37.4-21.el9
util-linux-core 2.37.4-21.el9
xz 5.2.5-8.el9_0
xz-libs 5.2.5-8.el9_0
yamllint 1.35.1-1.el9ap
zlib 1.2.11-40.el9
zstd 1.5.5-1.el9
```

</details>

<details><summary>Python packages: /usr (python3.11) (48)</summary>

```text
ansible-compat 25.8.1
ansible-core 2.16.14
ansible-lint 25.8.2
ansible-runner 2.4.1
attrs 22.2.0
black 24.4.2
bracex 2.4
cffi 1.15.1
charset-normalizer 2.1.0
click 8.1.7
cryptography 42.0.5
docutils 0.20.1
filelock 3.13.1
idna 3.4
importlib-metadata 6.0.1
Jinja2 3.1.6
jsonschema 4.21.1
jsonschema-specifications 2023.12.1
lockfile 0.12.2
lxml 4.9.2
MarkupSafe 2.1.5
mypy-extensions 1.0.0
packaging 23.2
pathspec 0.12.1
pexpect 4.9.0
pip 22.3.1
platformdirs 4.2.0
ply 3.11
ptyprocess 0.7.0
pycparser 2.20
pyOpenSSL 24.1.0
PySocks 1.7.1
python-daemon 2.3.2
PyYAML 6.0
referencing 0.36.2
requests 2.28.1
resolvelib 1.0.1
rpds-py 0.18.1
ruamel.yaml 0.18.15
ruamel.yaml.clib 0.2.8
setuptools 65.5.1
six 1.16.0
subprocess-tee 0.4.1
typing_extensions 4.9.0
urllib3 1.26.12
wcmatch 8.5
yamllint 1.35.1
zipp 3.19.2
```

</details>

<details><summary>Python packages: /usr/local (python3.11) (15)</summary>

```text
bcrypt 3.2.0
decorator 5.1.1
gssapi 1.8.2
ncclient 0.6.10
ntlm-auth 1.5.0
paramiko 2.8.1
pykerberos 1.2.4
PyNaCl 1.4.0
pypsrp 0.5.0
pyspnego 0.9.0
pywinrm 0.4.3
requests-credssp 2.0.0
requests-ntlm 1.1.0
toml 0.10.2
xmltodict 0.12.0
```

</details>

[Back to top](#contents)

### ee-supported-rhel9

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-26/ee-supported-rhel9` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/ee-supported-rhel9.tar.gz` |
| Labels `version` / `release` | `1.0.0` / `1096` |
| Image ID | `sha256:d590c7adac8e14046bea36be51874920b6b4931bb9a4a7810b7791cee90bbf10` |
| Build date | 2025-09-24T01:08:48 |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.6 (Plow) |
| Python | 3.9, 3.11 |
| Ansible Core | 2.16.14 |

<details><summary>RPM packages (311)</summary>

```text
acl 2.3.1-4.el9
alternatives 1.24-2.el9
ansible-core 2.16.14-2.el9ap
ansible-lint 25.8.2-1.el9ap
ansible-runner 2.4.1-1.el9ap
ansible-sign 0.1.2-1.el9ap
ansible-test 2.16.14-2.el9ap
apr 1.7.0-12.el9_3
apr-util 1.6.1-23.el9
apr-util-bdb 1.6.1-23.el9
audit-libs 3.1.5-4.el9
automation-controller-cli 4.7.1-1.el9ap
basesystem 11-13.el9
bash 5.1.8-9.el9
bash-completion 2.11-5.el9
bzip2 1.0.8-10.el9_5
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crypto-policies 20250128-1.git5269e22.el9
curl-minimal 7.76.1-31.el9_6.1
cyrus-sasl-lib 2.1.27-21.el9
dbus 1.12.20-8.el9
dbus-broker 28-7.el9
dbus-common 1.12.20-8.el9
dejavu-sans-fonts 2.37-18.el9
diffutils 3.7-12.el9
dnf-data 4.14.0-25.el9
dumb-init 1.2.5-3.el9ap
expat 2.5.0-5.el9_6
file 5.39-16.el9
file-libs 5.39-16.el9
filesystem 3.16-5.el9
findutils 4.8.0-7.el9
flexiblas 3.0.4-8.el9
flexiblas-netlib 3.0.4-8.el9
flexiblas-openblas-openmp 3.0.4-8.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdbm-libs 1.23-1.el9
git-core 2.47.3-1.el9_6
git-lfs 3.6.1-2.el9_6
glib2 2.68.4-16.el9_6.2
glibc 2.34-168.el9_6.23
glibc-common 2.34-168.el9_6.23
glibc-langpack-en 2.34-168.el9_6.23
glibc-minimal-langpack 2.34-168.el9_6.23
gmp 6.2.0-13.el9
gnupg2 2.3.3-4.el9
gnutls 3.8.3-6.el9_6.2
gobject-introspection 1.68.0-11.el9
gpg-pubkey 5a6340b3-6229229e
gpg-pubkey fd431d51-4ae0493b
gpgme 1.15.1-6.el9
grep 3.6-5.el9
gzip 1.12-1.el9
json-c 0.14-11.el9
json-glib 1.6.6-1.el9
keyutils-libs 1.6.3-1.el9
kmod-libs 28-10.el9
krb5-libs 1.21.1-8.el9_6
krb5-pkinit 1.21.1-8.el9_6
krb5-workstation 1.21.1-8.el9_6
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
less 590-5.el9
libacl 2.3.1-4.el9
libaio 0.3.111-13.el9
libarchive 3.5.3-6.el9_6
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9
libcap 2.48-9.el9_2
libcap-ng 0.8.2-7.el9
libcbor 0.7.0-5.el9
libcom_err 1.46.5-7.el9
libcurl-minimal 7.76.1-31.el9_6.1
libdb 5.3.28-57.el9_6
libdnf 0.69.0-13.el9
libeconf 0.4.1-4.el9
libedit 3.1-38.20210216cvs.el9
libevent 2.1.12-8.el9_4
libfdisk 2.37.4-21.el9
libffi 3.4.2-8.el9
libfido2 1.13.0-2.el9
libgcc 11.5.0-5.el9_5
libgcrypt 1.10.0-11.el9
libgfortran 11.5.0-5.el9_5
libgomp 11.5.0-5.el9_5
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libkadm5 1.21.1-8.el9_6
libksba 1.5.1-7.el9
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9
libnghttp2 1.43.0-6.el9
libnsl2 2.0.0-1.el9
libpeas 1.30.0-4.el9
libpkgconf 1.7.3-10.el9
libpq 13.20-1.el9_5
libpwquality 1.4.4-8.el9
libquadmath 11.5.0-5.el9_5
librepo 1.14.5-2.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libseccomp 2.5.2-2.el9
libselinux 3.6-3.el9
libselinux-utils 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-2.el9
libserf 1.3.9-27.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9
libsolv 0.7.24-3.el9
libss 1.46.5-7.el9
libssh 0.10.4-13.el9
libssh-config 0.10.4-13.el9
libstdc++ 11.5.0-5.el9_5
libtasn1 4.16.0-9.el9
libtirpc 1.3.3-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
liburing 2.5-1.el9
libusbx 1.0.26-1.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-12.el9_6
libxslt 1.1.34-13.el9_6
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
logrotate 3.18.0-9.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
mailcap 2.1.49-5.el9
microdnf 3.9.1-3.el9
mpdecimal 2.5.1-3.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-10.20210508.el9_6.2
ncurses-libs 6.2-10.20210508.el9_6.2
nettle 3.10.1-1.el9
npth 1.6-8.el9
numactl-libs 2.0.19-1.el9
openblas 0.3.26-2.el9
openblas-openmp 0.3.26-2.el9
openldap 2.6.8-4.el9
openshift-clients 4.14.0-202507050036.p0.g44b3ac2.assembly.stream.el9
openssh 8.7p1-45.el9
openssh-clients 8.7p1-45.el9
openssl 3.2.2-6.el9_5.1
openssl-fips-provider 3.0.7-6.el9_5
openssl-fips-provider-so 3.0.7-6.el9_5
openssl-libs 3.2.2-6.el9_5.1
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pam 1.5.1-26.el9_6
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
pkgconf 1.7.3-10.el9
pkgconf-m4 1.7.3-10.el9
pkgconf-pkg-config 1.7.3-10.el9
podman-remote 5.4.0-13.el9_6
policycoreutils 3.6-2.1.el9
popt 1.18-8.el9
python3 3.9.21-2.el9_6.2
python3-chardet 4.0.0-5.el9
python3-idna 2.10-7.el9_4.1
python3-libs 3.9.21-2.el9_6.2
python3-pexpect 4.8.0-7.el9
python3-pip-wheel 21.3.1-1.el9
python3-ptyprocess 0.6.0-12.el9
python3-pysocks 1.7.1-12.el9
python3-pyyaml 5.4.1-6.el9
python3-requests 2.25.1-10.el9_6
python3-setuptools 53.0.0-13.el9_6.1
python3-setuptools-wheel 53.0.0-13.el9_6.1
python3-six 1.15.0-9.el9
python3-urllib3 1.26.5-6.el9
python3.11 3.11.11-2.el9_6.2
python3.11-aiodns 3.2.0-1.el9ap
python3.11-aiohappyeyeballs 2.4.4-1.el9ap
python3.11-aiohttp 3.10.11-1.el9ap
python3.11-aiosignal 1.3.1-1.el9ap
python3.11-ansible-compat 25.8.1-1.el9ap
python3.11-ansible-pylibssh 1.2.2-1.el9ap
python3.11-ansible-runner 2.4.1-1.el9ap
python3.11-async-timeout 4.0.3-2.el9ap
python3.11-attrs 22.2.0-1.el9ap
python3.11-black 24.4.2-2.el9ap
python3.11-boto3 1.34.30-1.el9ap
python3.11-botocore 1.34.30-1.el9ap
python3.11-bracex 2.4-1.el9ap
python3.11-brotli 1.1.0-1.el9ap
python3.11-cachetools 5.3.2-1.el9ap
python3.11-certifi 2023.5.7-1.el9ap
python3.11-cffi 1.15.1-1.el9
python3.11-chardet 5.2.0-2.el9ap
python3.11-charset-normalizer 2.1.0-1.el9
python3.11-click 8.1.7-1.el9ap
python3.11-cryptography 42.0.5-1.el9ap
python3.11-daemon 2.3.2-1.el9ap
python3.11-dateutil 2.8.2-2.el9ap
python3.11-deprecated 1.2.14-1.el9ap
python3.11-distlib 0.3.8-1.el9ap
python3.11-distro 1.9.0-1.el9ap
python3.11-docutils 0.20.1-2.el9ap
python3.11-dpath 2.1.6-1.el9ap
python3.11-filelock 3.13.1-1.el9ap
python3.11-frozenlist 1.4.0-1.el9ap
python3.11-gnupg 0.5.2-1.el9ap
python3.11-google-auth 2.27.0-1.el9ap
python3.11-grpcio 1.58.3-1.el9ap
python3.11-idna 3.4-1.el9
python3.11-importlib-metadata 6.0.1-2.el9ap
python3.11-isodate 0.6.1-2.el9ap
python3.11-jinja2 3.1.6-1.el9ap
python3.11-jmespath 1.0.1-2.el9ap
python3.11-jsonschema 4.21.1-1.el9ap
python3.11-jsonschema-specifications 2023.12.1-1.el9ap
python3.11-libs 3.11.11-2.el9_6.2
python3.11-lockfile 0.12.2-2.el9ap
python3.11-lxml 4.9.2-4.el9
python3.11-markupsafe 2.1.5-1.el9ap
python3.11-multidict 6.0.4-1.el9ap
python3.11-mypy-extensions 1.0.0-1.el9ap
python3.11-netaddr 1.2.1-1.el9ap
python3.11-numpy 1.23.5-1.el9
python3.11-oauthlib 3.2.2-1.el9ap
python3.11-packaging 23.2-1.el9ap
python3.11-pathspec 0.12.1-1.el9ap
python3.11-pbr 6.0.0-2.el9ap
python3.11-pexpect 4.9.0-1.el9ap
python3.11-pip 22.3.1-5.el9
python3.11-pip-wheel 22.3.1-5.el9
python3.11-platformdirs 4.2.0-1.el9ap
python3.11-ply 3.11-1.el9
python3.11-protobuf 4.21.12-2.el9ap
python3.11-psycopg 3.2.7-1.el9ap
python3.11-ptyprocess 0.7.0-1.el9ap
python3.11-pyOpenSSL 24.1.0-1.el9ap
python3.11-pyasn1 0.5.1-1.el9ap
python3.11-pyasn1-modules 0.3.0-1.el9ap
python3.11-pycares 4.4.0-2.el9ap
python3.11-pycparser 2.20-1.el9
python3.11-pygments 2.17.2-2.el9ap
python3.11-pyjwt 2.7.0-2.el9ap
python3.11-pysocks 1.7.1-1.el9
python3.11-pytz 2024.1-1.el9ap
python3.11-pyyaml 6.0-1.el9
python3.11-referencing 0.36.2-1.el9ap
python3.11-requests 2.31.0-2.el9ap
python3.11-requests-oauthlib 1.3.1-1.el9ap
python3.11-resolvelib 1.0.1-1.el9ap
python3.11-rpds-py 0.18.1-1.el9ap
python3.11-rsa 4.9-2.el9ap
python3.11-ruamel-yaml 0.18.15-1.el9ap
python3.11-ruamel-yaml-clib 0.2.8-1.el9ap
python3.11-s3transfer 0.10.0-1.el9ap
python3.11-setuptools 65.5.1-4.el9_6
python3.11-setuptools-wheel 65.5.1-4.el9_6
python3.11-six 1.16.0-1.el9
python3.11-subprocess-tee 0.4.1-2.el9ap
python3.11-tabulate 0.9.0-3.el9ap
python3.11-typing-extensions 4.9.0-1.el9ap
python3.11-uamqp 1.6.8-1.el9ap
python3.11-urllib3 1.26.20-1.el9ap
python3.11-watchdog 5.0.2-1.el9ap
python3.11-wcmatch 8.5-1.el9ap
python3.11-websocket-client 1.7.0-2.el9ap
python3.11-wrapt 1.16.0-1.el9ap
python3.11-xxhash 3.4.1-1.el9ap
python3.11-yarl 1.13.1-1.el9ap
python3.11-zipp 3.19.2-1.el9ap
qemu-img 9.1.0-15.el9_6.9
readline 8.1-4.el9
receptor 1.5.7-2.el9ap
receptorctl 1.5.7-2.el9ap
redhat-release 9.6-0.1.el9
rootfiles 8.1-34.el9
rpm 4.16.1.3-37.el9
rpm-libs 4.16.1.3-37.el9
rsync 3.2.5-3.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-12.el9
shadow-utils-subid 4.9-12.el9
sos 4.9.2-1.el9_6
sqlite-libs 3.34.1-8.el9_6
sshpass 1.09-5.el9ap
subversion 1.14.1-5.el9_0
subversion-libs 1.14.1-5.el9_0
systemd 252-51.el9_6.2
systemd-libs 252-51.el9_6.2
systemd-pam 252-51.el9_6.2
systemd-rpm-macros 252-51.el9_6.2
tar 1.34-7.el9
tzdata 2025b-1.el9
unzip 6.0-58.el9_5
utf8proc 2.6.1-4.el9
util-linux 2.37.4-21.el9
util-linux-core 2.37.4-21.el9
xz 5.2.5-8.el9_0
xz-libs 5.2.5-8.el9_0
yamllint 1.35.1-1.el9ap
zlib 1.2.11-40.el9
zstd 1.5.5-1.el9
```

</details>

<details><summary>Python packages: /usr (python3.11) (97)</summary>

```text
aiodns 3.2.0
aiohappyeyeballs 2.4.4
aiohttp 3.10.11
aiosignal 1.3.1
ansible-compat 25.8.1
ansible-core 2.16.14
ansible-lint 25.8.2
ansible-pylibssh 1.2.2
ansible-runner 2.4.1
ansible-sign 0.1.2
async-timeout 4.0.3
attrs 22.2.0
awxkit 4.7.1
black 24.4.2
boto3 1.34.30
botocore 1.34.30
bracex 2.4
Brotli 1.1.0
cachetools 5.3.2
certifi 2023.5.7
cffi 1.15.1
chardet 5.2.0
charset-normalizer 2.1.0
click 8.1.7
cryptography 42.0.5
Deprecated 1.2.14
distlib 0.3.8
distro 1.9.0
docutils 0.20.1
dpath 2.1.6
filelock 3.13.1
frozenlist 1.4.0
google-auth 2.27.0
grpcio 1.58.3
idna 3.4
importlib-metadata 6.0.1
isodate 0.6.1
Jinja2 3.1.6
jmespath 1.0.1
jsonschema 4.21.1
jsonschema-specifications 2023.12.1
lockfile 0.12.2
lxml 4.9.2
MarkupSafe 2.1.5
multidict 6.0.4
mypy-extensions 1.0.0
netaddr 1.2.1
numpy 1.23.5
oauthlib 3.2.2
packaging 23.2
pathspec 0.12.1
pbr 6.0.0
pexpect 4.9.0
pip 22.3.1
platformdirs 4.2.0
ply 3.11
protobuf 4.21.12
psycopg 3.2.7
ptyprocess 0.7.0
pyasn1 0.5.1
pyasn1-modules 0.3.0
pycares 4.4.0
pycparser 2.20
Pygments 2.17.2
PyJWT 2.7.0
pyOpenSSL 24.1.0
PySocks 1.7.1
python-daemon 2.3.2
python-dateutil 2.8.2
python-gnupg 0.5.2
pytz 2024.1
PyYAML 6.0
receptorctl 1.5.7
referencing 0.36.2
requests 2.31.0
requests-oauthlib 1.3.1
resolvelib 1.0.1
rpds-py 0.18.1
rsa 4.9
ruamel.yaml 0.18.15
ruamel.yaml.clib 0.2.8
s3transfer 0.10.0
setuptools 65.5.1
six 1.16.0
subprocess-tee 0.4.1
tabulate 0.9.0
typing_extensions 4.9.0
uamqp 1.6.8
urllib3 1.26.20
watchdog 5.0.2
wcmatch 8.5
websocket-client 1.7.0
wrapt 1.16.0
xxhash 3.4.1
yamllint 1.35.1
yarl 1.13.1
zipp 3.19.2
```

</details>

<details><summary>Python packages: /usr (python3.9) (11)</summary>

```text
chardet 4.0.0
idna 2.10
pexpect 4.8.0
ptyprocess 0.6.0
PySocks 1.7.1
PyYAML 5.4.1
requests 2.25.1
setuptools 53.0.0
six 1.15.0
sos 4.9.2
urllib3 1.26.5
```

</details>

<details><summary>Python packages: /usr/local (python3.11) (159)</summary>

```text
adal 1.2.7
aiobotocore 2.11.2
aioitertools 0.11.0
aiokafka 0.10.0
anyio 4.4.0
appdirs 1.4.4
applicationinsights 0.11.10
argcomplete 3.5.3
azure-cli-core 2.74.0
azure-cli-telemetry 1.1.0
azure-common 1.1.28
azure-containerregistry 1.2.0
azure-core 1.31.0
azure-identity 1.19.0
azure-iot-hub 2.6.1
azure-keyvault 4.2.0
azure-keyvault-certificates 4.7.0
azure-keyvault-keys 4.8.0
azure-keyvault-secrets 4.7.0
azure-keyvault-securitydomain 1.0.0b1
azure-mgmt-apimanagement 4.0.1
azure-mgmt-authorization 4.0.0
azure-mgmt-automation 1.1.0b4
azure-mgmt-batch 17.3.0
azure-mgmt-cdn 13.1.1
azure-mgmt-compute 33.0.0
azure-mgmt-containerinstance 10.1.0
azure-mgmt-containerregistry 10.3.0
azure-mgmt-containerservice 32.1.0
azure-mgmt-core 1.4.0
azure-mgmt-cosmosdb 10.0.0b3
azure-mgmt-datafactory 9.0.0
azure-mgmt-devtestlabs 10.0.0b2
azure-mgmt-dns 8.1.0
azure-mgmt-eventhub 11.1.0
azure-mgmt-hdinsight 9.1.0b1
azure-mgmt-iothub 3.0.0
azure-mgmt-keyvault 10.3.1
azure-mgmt-loganalytics 13.0.0b7
azure-mgmt-managedservices 7.0.0b2
azure-mgmt-managementgroups 1.1.0b2
azure-mgmt-marketplaceordering 1.2.0b2
azure-mgmt-monitor 6.0.2
azure-mgmt-mysqlflexibleservers 1.0.0b3
azure-mgmt-network 28.0.0
azure-mgmt-notificationhubs 8.1.0b1
azure-mgmt-nspkg 3.0.2
azure-mgmt-postgresqlflexibleservers 1.1.0
azure-mgmt-privatedns 1.2.0
azure-mgmt-rdbms 10.2.0b17
azure-mgmt-recoveryservices 3.0.0
azure-mgmt-recoveryservicesbackup 9.1.0
azure-mgmt-redis 14.4.0
azure-mgmt-resource 23.2.0
azure-mgmt-resourcegraph 8.0.0
azure-mgmt-resourcehealth 1.0.0b6
azure-mgmt-search 9.2.0b2
azure-mgmt-servicebus 8.2.1
azure-mgmt-sql 4.0.0b19
azure-mgmt-storage 21.2.1
azure-mgmt-trafficmanager 1.1.0
azure-mgmt-web 7.3.1
azure-nspkg 3.0.2
azure-servicebus 7.14.2
azure-storage-blob 12.23.0b1
bcrypt 3.2.0
decorator 5.2.1
dnspython 2.6.1
dogpile.cache 1.1.2
dpapi-ng 0.2.0
google-api-core 2.25.1
google-cloud-core 2.4.3
google-cloud-storage 3.3.0
google-crc32c 1.7.1
google-resumable-media 2.7.2
googleapis-common-protos 1.70.0
gssapi 1.9.0
h11 0.16.0
h2 4.1.0
hpack 4.0.0
httpcore 1.0.9
httpx 0.27.0
humanfriendly 10.0
hyperframe 6.0.1
iso8601 0.1.14
jsonpatch 1.32
jsonpointer 2.1
jxmlease 1.0.3
kafka-python 2.0.2
keystoneauth1 4.3.1
knack 0.11.0
krb5 0.7.1
kubernetes 29.0.0
microsoft-kiota-abstractions 1.3.3
microsoft-kiota-authentication-azure 1.0.0
microsoft-kiota-http 1.3.1
microsoft-kiota-serialization-form 0.1.1
microsoft-kiota-serialization-json 1.3.3
microsoft-kiota-serialization-multipart 0.1.0
microsoft-kiota-serialization-text 1.0.0
microsoft-security-utilities-secret-masker 1.0.0b4
msal 1.32.3
msal-extensions 1.2.0
msgraph-core 1.1.0
msgraph-sdk 1.6.0
msrest 0.7.1
msrestazure 0.6.4
munch 2.5.0
ncclient 0.6.10
netifaces 0.10.9
nsx-policy-python-sdk 4.1.2.0.0
nsx-python-sdk 4.1.2.0.0
nsx-vmc-aws-integration-python-sdk 4.1.2.0.0
nsx-vmc-policy-python-sdk 4.1.2.0.0
ntlm-auth 1.5.0
openstacksdk 0.56.0
opentelemetry-api 1.25.0
opentelemetry-sdk 1.25.0
opentelemetry-semantic-conventions 0.46b0
oras 0.2.37
os-service-types 1.7.0
ovirt-engine-sdk-python 4.5.2
ovirt-imageio 2.4.6
pandas 2.3.2
paramiko 2.8.1
pendulum 3.0.0
pkginfo 1.7.0
portalocker 1.7.1
proto-plus 1.26.1
psutil 5.9.1
py-deviceid 0.1.1
pyang 2.5.3
pycurl 7.45.3
pykerberos 1.2.4
PyNaCl 1.4.0
pypsrp 0.5.0
pyspnego 0.9.0
pyvmomi 8.0.3.0.1
pywinrm 0.4.3
requests-credssp 2.0.0
requests-ntlm 1.1.0
requestsexceptions 1.4.0
sansldap 0.1.0
scp 0.13.3
sniffio 1.3.1
std-uritemplate 1.0.2
stevedore 3.3.0
textfsm 0.4.1
time-machine 2.14.2
toml 0.10.2
ttp 0.6.0
tzdata 2024.1
vapi-common-client 2.44.0
vapi-runtime 2.44.0
vcenter-bindings 4.2.0
vmwarecloud-aws 1.64.0
vmwarecloud-draas 1.23.0
vsphere-automation-sdk 1.86.0
xmltodict 0.12.0
```

</details>

<details><summary>Ansible collections (54)</summary>

```text
amazon.aws 9.5.1
ansible.controller 4.7.1
ansible.eda 2.10.0
ansible.hub 1.0.1
ansible.netcommon 8.1.0
ansible.network 5.0.0
ansible.platform 2.6.20250924
ansible.posix 2.1.0
ansible.scm 3.0.0
ansible.security 5.0.0
ansible.snmp 3.0.0
ansible.utils 6.0.0
ansible.windows 3.2.0
ansible.yang 3.0.0
arista.eos 12.0.0
azure.azcollection 3.7.0
cisco.intersight 2.2.0
cisco.ios 11.0.0
cisco.iosxr 12.0.0
cisco.nxos 11.0.0
cloud.common 5.0.0
cloud.terraform 4.0.0
community.vmware 1.9.0
google.cloud 1.7.0
junipernetworks.junos 11.0.0
kubernetes.core 6.1.0
microsoft.ad 1.9.2
microsoft.iis 1.0.3
openstack.cloud 1.5.0
redhat.amq_broker 2.3.4
redhat.amq_streams 1.0.0
redhat.data_grid 1.3.3
redhat.eap 1.5.7
redhat.insights 1.3.0
redhat.jbcs 1.1.2
redhat.jws 2.1.1
redhat.openshift 5.0.0
redhat.openshift_virtualization 2.2.3
redhat.redhat_csp_download 1.2.2
redhat.rhbk 3.0.1
redhat.rhel_idm 1.15.1
redhat.rhel_system_roles 1.95.7
redhat.rhv 2.4.2
redhat.runtimes_common 1.2.2
redhat.sap_install 1.7.1
redhat.satellite 5.5.0
redhat.satellite_operations 3.0.0
redhat.sso 2.0.0
sap.sap_operations 2.2.0
servicenow.itsm 2.11.0
splunk.es 4.0.0
trendmicro.deepsec 4.0.0
vmware.vmware 2.3.0
vmware.vmware_rest 4.8.1
```

</details>

[Back to top](#contents)

### gateway-proxy-rhel9

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-26/gateway-proxy-rhel9` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/gateway-proxy-rhel9.tar.gz` |
| Labels `version` / `release` | `2.6.6` / `5` |
| Image ID | `sha256:0a4ef1771371f28b8fe7d0086d96972ef062f1b7b6600d6827a5be24b588a47d` |
| Build date | 2025-09-23T21:40:39 |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.6 (Plow) |
| Python | N/A |
| Ansible Core | N/A |

<details><summary>RPM packages (113)</summary>

```text
alternatives 1.24-2.el9
audit-libs 3.1.5-4.el9
automation-gateway-config 2.6.20251001-1.el9ap
automation-gateway-proxy-server 2.6.6-3.el9ap
basesystem 11-13.el9
bash 5.1.8-9.el9
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
crypto-policies 20250128-1.git5269e22.el9
curl-minimal 7.76.1-31.el9_6.1
cyrus-sasl-lib 2.1.27-21.el9
dejavu-sans-fonts 2.37-18.el9
dnf-data 4.14.0-25.el9
dumb-init 1.2.5-3.el9ap
file-libs 5.39-16.el9
filesystem 3.16-5.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdbm-libs 1.23-1.el9
glib2 2.68.4-16.el9_6.2
glibc 2.34-168.el9_6.23
glibc-common 2.34-168.el9_6.23
glibc-langpack-en 2.34-168.el9_6.23
glibc-minimal-langpack 2.34-168.el9_6.23
gmp 6.2.0-13.el9
gnupg2 2.3.3-4.el9
gnutls 3.8.3-6.el9_6.2
gobject-introspection 1.68.0-11.el9
gpg-pubkey 5a6340b3-6229229e
gpg-pubkey fd431d51-4ae0493b
gpgme 1.15.1-6.el9
grep 3.6-5.el9
json-c 0.14-11.el9
json-glib 1.6.6-1.el9
keyutils-libs 1.6.3-1.el9
krb5-libs 1.21.1-8.el9_6
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-6.el9_6
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9
libcap 2.48-9.el9_2
libcap-ng 0.8.2-7.el9
libcom_err 1.46.5-7.el9
libcurl-minimal 7.76.1-31.el9_6.1
libdnf 0.69.0-13.el9
libevent 2.1.12-8.el9_4
libffi 3.4.2-8.el9
libgcc 11.5.0-5.el9_5
libgcrypt 1.10.0-11.el9
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libksba 1.5.1-7.el9
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9
libnghttp2 1.43.0-6.el9
libpeas 1.30.0-4.el9
librepo 1.14.5-2.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libselinux 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-2.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9
libsolv 0.7.24-3.el9
libstdc++ 11.5.0-5.el9_5
libtasn1 4.16.0-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libusbx 1.0.26-1.el9
libuuid 2.37.4-21.el9
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-12.el9_6
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
microdnf 3.9.1-3.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-10.20210508.el9_6.2
ncurses-libs 6.2-10.20210508.el9_6.2
nettle 3.10.1-1.el9
npth 1.6-8.el9
openldap 2.6.8-4.el9
openssl 3.2.2-6.el9_5.1
openssl-fips-provider 3.0.7-6.el9_5
openssl-fips-provider-so 3.0.7-6.el9_5
openssl-libs 3.2.2-6.el9_5.1
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
popt 1.18-8.el9
readline 8.1-4.el9
redhat-release 9.6-0.1.el9
rootfiles 8.1-34.el9
rpm 4.16.1.3-37.el9
rpm-libs 4.16.1.3-37.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-12.el9
sqlite-libs 3.34.1-8.el9_6
systemd-libs 252-51.el9_6.2
tzdata 2025b-1.el9
xz-libs 5.2.5-8.el9_0
zlib 1.2.11-40.el9
```

</details>

[Back to top](#contents)

### gateway-rhel9

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-26/gateway-rhel9` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/gateway-rhel9.tar.gz` |
| Labels `version` / `release` | `2.6.20251001` / `1` |
| Image ID | `sha256:effabbb5cae9cd431e27ed7a5a168d4fa61aec013e1396a8dfea32a9785d1d98` |
| Build date | 2025-09-23T21:40:53 |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.6 (Plow) |
| Python | 3.9, 3.11 |
| Ansible Core | N/A |

<details><summary>RPM packages (243)</summary>

```text
acl 2.3.1-4.el9
alternatives 1.24-2.el9
ansible-automation-platform-common 2.6-1.el9ap
ansible-automation-platform-selinux 0.2-3.el9ap
audit-libs 3.1.5-4.el9
automation-gateway-server 2.6.20251001-1.el9ap
automation-platform-ui 2.6.1-1.el9ap
basesystem 11-13.el9
bash 5.1.8-9.el9
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crypto-policies 20250128-1.git5269e22.el9
curl-minimal 7.76.1-31.el9_6.1
cyrus-sasl-lib 2.1.27-21.el9
dbus 1.12.20-8.el9
dbus-broker 28-7.el9
dbus-common 1.12.20-8.el9
dejavu-sans-fonts 2.37-18.el9
diffutils 3.7-12.el9
dnf-data 4.14.0-25.el9
dumb-init 1.2.5-3.el9ap
expat 2.5.0-5.el9_6
file-libs 5.39-16.el9
filesystem 3.16-5.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdbm-libs 1.23-1.el9
glib2 2.68.4-16.el9_6.2
glibc 2.34-168.el9_6.23
glibc-common 2.34-168.el9_6.23
glibc-langpack-en 2.34-168.el9_6.23
glibc-minimal-langpack 2.34-168.el9_6.23
gmp 6.2.0-13.el9
gnupg2 2.3.3-4.el9
gnutls 3.8.3-6.el9_6.2
gobject-introspection 1.68.0-11.el9
gpg-pubkey 5a6340b3-6229229e
gpg-pubkey fd431d51-4ae0493b
gpgme 1.15.1-6.el9
grep 3.6-5.el9
gzip 1.12-1.el9
json-c 0.14-11.el9
json-glib 1.6.6-1.el9
keyutils-libs 1.6.3-1.el9
kmod-libs 28-10.el9
krb5-libs 1.21.1-8.el9_6
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-6.el9_6
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9
libcap 2.48-9.el9_2
libcap-ng 0.8.2-7.el9
libcom_err 1.46.5-7.el9
libcurl-minimal 7.76.1-31.el9_6.1
libdb 5.3.28-57.el9_6
libdnf 0.69.0-13.el9
libeconf 0.4.1-4.el9
libevent 2.1.12-8.el9_4
libfdisk 2.37.4-21.el9
libffi 3.4.2-8.el9
libgcc 11.5.0-5.el9_5
libgcrypt 1.10.0-11.el9
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libksba 1.5.1-7.el9
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9
libnghttp2 1.43.0-6.el9
libnsl2 2.0.0-1.el9
libpeas 1.30.0-4.el9
libpq 13.20-1.el9_5
libpwquality 1.4.4-8.el9
librepo 1.14.5-2.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libseccomp 2.5.2-2.el9
libselinux 3.6-3.el9
libselinux-utils 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-2.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9
libsolv 0.7.24-3.el9
libstdc++ 11.5.0-5.el9_5
libtasn1 4.16.0-9.el9
libtirpc 1.3.3-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libusbx 1.0.26-1.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-12.el9_6
libxslt 1.1.34-13.el9_6
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
microdnf 3.9.1-3.el9
mpdecimal 2.5.1-3.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-10.20210508.el9_6.2
ncurses-libs 6.2-10.20210508.el9_6.2
nettle 3.10.1-1.el9
nginx 1.24.0-4.module+el9.5.0+22954+e2d70a1c.1
nginx-core 1.24.0-4.module+el9.5.0+22954+e2d70a1c.1
nginx-filesystem 1.24.0-4.module+el9.5.0+22954+e2d70a1c.1
npth 1.6-8.el9
openldap 2.6.8-4.el9
openssl 3.2.2-6.el9_5.1
openssl-fips-provider 3.0.7-6.el9_5
openssl-fips-provider-so 3.0.7-6.el9_5
openssl-libs 3.2.2-6.el9_5.1
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pam 1.5.1-26.el9_6
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
policycoreutils 3.6-2.1.el9
popt 1.18-8.el9
postgresql 15.14-1.module+el9.6.0+23419+7863ab62
postgresql-private-libs 15.14-1.module+el9.6.0+23419+7863ab62
python3 3.9.21-2.el9_6.2
python3-cffi 1.15.0-3.el9ap
python3-cryptography 42.0.5-1.el9ap
python3-libs 3.9.21-2.el9_6.2
python3-pip-wheel 21.3.1-1.el9
python3-pycparser 2.21-2.el9pc
python3-setuptools 53.0.0-13.el9_6.1
python3-setuptools-wheel 53.0.0-13.el9_6.1
python3.11 3.11.11-2.el9_6.2
python3.11-argon2-cffi 23.1.0-1.el9ap
python3.11-argon2-cffi-bindings 21.2.0-1.el9ap
python3.11-asgiref 3.7.2-1.el9ap
python3.11-async-timeout 4.0.3-2.el9ap
python3.11-attrs 22.2.0-1.el9ap
python3.11-certifi 2023.5.7-1.el9ap
python3.11-cffi 1.15.1-1.el9
python3.11-charset-normalizer 2.1.0-1.el9
python3.11-cryptography 42.0.5-1.el9ap
python3.11-defusedxml 0.7.1-4.el9ap
python3.11-django 4.2.24-1.el9ap
python3.11-django-ansible-base 2.6.20251001-1.el9ap
python3.11-django-ansible-base+activitystream 2.6.20251001-1.el9ap
python3.11-django-ansible-base+api_documentation 2.6.20251001-1.el9ap
python3.11-django-ansible-base+authentication 2.6.20251001-1.el9ap
python3.11-django-ansible-base+feature_flags 2.6.20251001-1.el9ap
python3.11-django-ansible-base+oauth2_provider 2.6.20251001-1.el9ap
python3.11-django-ansible-base+rbac 2.6.20251001-1.el9ap
python3.11-django-ansible-base+redis_client 2.6.20251001-1.el9ap
python3.11-django-ansible-base+rest_filters 2.6.20251001-1.el9ap
python3.11-django-auth-ldap 4.0.0-2.el9ap
python3.11-django-crum 0.7.9-2.el9ap
python3.11-django-dynamic-preferences 1.16.0-1.el9ap
python3.11-django-extensions 3.2.3-2.el9ap
python3.11-django-flags 5.0.13-1.el9ap
python3.11-django-oauth-toolkit 2.3.0-1.el9ap
python3.11-django-redis 5.4.0-1.el9ap
python3.11-djangorestframework 3.15.1-1.el9ap
python3.11-drf-spectacular 0.26.5-2.el9ap
python3.11-dynaconf 3.2.11-1.el9ap
python3.11-googleapis-common-protos 1.59.1-2.el9ap
python3.11-grpcio 1.58.3-1.el9ap
python3.11-grpcio-tools 1.58.3-1.el9ap
python3.11-idna 3.4-1.el9
python3.11-inflection 0.5.1-4.el9ap
python3.11-isodate 0.6.1-2.el9ap
python3.11-jsonschema 4.21.1-1.el9ap
python3.11-jsonschema-specifications 2023.12.1-1.el9ap
python3.11-jwcrypto 1.5.6-1.el9ap
python3.11-ldap 3.4.4-1.el9ap
python3.11-ldap-filter 1.0.1-1.el9ap
python3.11-libs 3.11.11-2.el9_6.2
python3.11-lxml 4.9.2-4.el9
python3.11-netaddr 1.2.1-1.el9ap
python3.11-oauthlib 3.2.2-1.el9ap
python3.11-opentelemetry-proto 1.18.0-2.el9ap
python3.11-persisting-theory 1.0-2.el9ap
python3.11-pip-wheel 22.3.1-5.el9
python3.11-ply 3.11-1.el9
python3.11-protobuf 4.21.12-2.el9ap
python3.11-psycopg 3.2.7-1.el9ap
python3.11-pyasn1 0.5.1-1.el9ap
python3.11-pyasn1-modules 0.3.0-1.el9ap
python3.11-pycparser 2.20-1.el9
python3.11-pyjwt 2.7.0-2.el9ap
python3.11-pyrad 2.4-2.el9ap
python3.11-python3-openid 3.2.0-3.el9ap
python3.11-python3-saml 1.16.0-2.el9ap
python3.11-pyyaml 6.0-1.el9
python3.11-redis 4.6.0-2.el9ap
python3.11-referencing 0.36.2-1.el9ap
python3.11-requests 2.31.0-2.el9ap
python3.11-requests-oauthlib 1.3.1-1.el9ap
python3.11-rpds-py 0.18.1-1.el9ap
python3.11-setuptools 65.5.1-4.el9_6
python3.11-setuptools-wheel 65.5.1-4.el9_6
python3.11-six 1.16.0-1.el9
python3.11-social-auth-app-django 5.4.1-1.el9ap
python3.11-social-auth-core 4.5.4-1.el9ap
python3.11-sqlparse 0.5.3-2.el9ap
python3.11-tabulate 0.9.0-3.el9ap
python3.11-tacacs-plus 2.6-2.el9ap
python3.11-typing-extensions 4.9.0-1.el9ap
python3.11-uritemplate 4.1.1-3.el9ap
python3.11-urllib3 1.26.20-1.el9ap
python3.11-xds-protos 1.58.0-2.el9ap
python3.11-xmlsec 1.3.13-2.el9ap
readline 8.1-4.el9
redhat-logos-httpd 90.5-1.el9_6.1
redhat-release 9.6-0.1.el9
rootfiles 8.1-34.el9
rpm 4.16.1.3-37.el9
rpm-libs 4.16.1.3-37.el9
rpm-plugin-selinux 4.16.1.3-37.el9
sed 4.8-9.el9
selinux-policy 38.1.53-5.el9_6
selinux-policy-targeted 38.1.53-5.el9_6
setup 2.13.7-10.el9
shadow-utils 4.9-12.el9
sqlite-libs 3.34.1-8.el9_6
supervisor 4.2.5-1.el9ap
systemd 252-51.el9_6.2
systemd-libs 252-51.el9_6.2
systemd-pam 252-51.el9_6.2
systemd-rpm-macros 252-51.el9_6.2
tzdata 2025b-1.el9
util-linux 2.37.4-21.el9
util-linux-core 2.37.4-21.el9
uwsgi 2.0.23-2.el9ap
xmlsec1 1.2.29-13.el9
xmlsec1-openssl 1.2.29-13.el9
xz-libs 5.2.5-8.el9_0
zlib 1.2.11-40.el9
```

</details>

<details><summary>Python packages: /usr (python3.11) (68)</summary>

```text
aap-gateway 2.6.20251001
argon2-cffi 23.1.0
argon2-cffi-bindings 21.2.0
asgiref 3.7.2
async-timeout 4.0.3
attrs 22.2.0
certifi 2023.5.7
cffi 1.15.1
charset-normalizer 2.1.0
cryptography 42.0.5
defusedxml 0.7.1
Django 4.2.24
django-ansible-base 2.6.20251001
django-auth-ldap 4.0.0
django-crum 0.7.9
django-dynamic-preferences 1.16.0
django-extensions 3.2.3
django-flags 5.0.13
django-oauth-toolkit 2.3.0
django-redis 5.4.0
djangorestframework 3.15.1
drf-spectacular 0.26.5
dynaconf 3.2.11
googleapis-common-protos 1.59.1
grpcio 1.58.3
grpcio-tools 1.58.3
idna 3.4
inflection 0.5.1
isodate 0.6.1
jsonschema 4.21.1
jsonschema-specifications 2023.12.1
jwcrypto 1.5.6
ldap-filter 1.0.1
lxml 4.9.2
netaddr 1.2.1
oauthlib 3.2.2
opentelemetry-proto 1.18.0
persisting-theory 1.0
ply 3.11
protobuf 4.21.12
psycopg 3.2.7
pyasn1 0.5.1
pyasn1-modules 0.3.0
pycparser 2.20
PyJWT 2.7.0
pyrad 2.4
python-ldap 3.4.4
python3-openid 3.2.0
python3-saml 1.16.0
PyYAML 6.0
redis 4.6.0
referencing 0.36.2
requests 2.31.0
requests-oauthlib 1.3.1
rpds-py 0.18.1
setuptools 65.5.1
six 1.16.0
social-auth-app-django 5.4.1
social-auth-core 4.5.4
sqlparse 0.5.3
supervisor 4.2.5
tabulate 0.9.0
tacacs-plus 2.6
typing_extensions 4.9.0
uritemplate 4.1.1
urllib3 1.26.20
xds-protos 1.58.0
xmlsec 1.3.13
```

</details>

<details><summary>Python packages: /usr (python3.9) (4)</summary>

```text
cffi 1.15.0
cryptography 42.0.5
pycparser 2.21
setuptools 53.0.0
```

</details>

[Back to top](#contents)

### hub-rhel9

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-26/hub-rhel9` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/hub-rhel9.tar.gz` |
| Labels `version` / `release` | `4.11.0` / `159` |
| Image ID | `sha256:ffbb3283c188888f4a7ef6a537d94b04cd13e498a95b193cc4431725c38831a5` |
| Build date | 2025-09-23T21:40:58 |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.6 (Plow) |
| Python | 3.9, 3.11 |
| Ansible Core | 2.16.14 |

<details><summary>RPM packages (362)</summary>

```text
acl 2.3.1-4.el9
alternatives 1.24-2.el9
ansible-automation-platform-common 2.6-1.el9ap
ansible-automation-platform-selinux 0.2-3.el9ap
ansible-builder 3.1.0-1.el9ap
ansible-core 2.16.14-2.el9ap
ansible-lint 25.8.2-1.el9ap
ansible-test 2.16.14-2.el9ap
audit-libs 3.1.5-4.el9
automation-hub 4.11.0-1.el9ap
basesystem 11-13.el9
bash 5.1.8-9.el9
bindep 2.11.0-2.el9ap
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
container-selinux 2.237.0-2.el9_6
containers-common 1-117.el9_6
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crun 1.23.1-2.el9_6
crypto-policies 20250128-1.git5269e22.el9
curl-minimal 7.76.1-31.el9_6.1
cyrus-sasl-lib 2.1.27-21.el9
dbus 1.12.20-8.el9
dbus-broker 28-7.el9
dbus-common 1.12.20-8.el9
dejavu-sans-fonts 2.37-18.el9
diffutils 3.7-12.el9
dnf-data 4.14.0-25.el9
expat 2.5.0-5.el9_6
file-libs 5.39-16.el9
filesystem 3.16-5.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdbm-libs 1.23-1.el9
git-core 2.47.3-1.el9_6
glib2 2.68.4-16.el9_6.2
glibc 2.34-168.el9_6.23
glibc-common 2.34-168.el9_6.23
glibc-minimal-langpack 2.34-168.el9_6.23
gmp 6.2.0-13.el9
gnupg2 2.3.3-4.el9
gnutls 3.8.3-6.el9_6.2
gobject-introspection 1.68.0-11.el9
gpg-pubkey 5a6340b3-6229229e
gpg-pubkey fd431d51-4ae0493b
gpgme 1.15.1-6.el9
grep 3.6-5.el9
gzip 1.12-1.el9
jq 1.6-17.el9_6.2
json-c 0.14-11.el9
json-glib 1.6.6-1.el9
keyutils-libs 1.6.3-1.el9
kmod-libs 28-10.el9
krb5-libs 1.21.1-8.el9_6
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
less 590-5.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-6.el9_6
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9
libcap 2.48-9.el9_2
libcap-ng 0.8.2-7.el9
libcbor 0.7.0-5.el9
libcom_err 1.46.5-7.el9
libcurl-minimal 7.76.1-31.el9_6.1
libdb 5.3.28-57.el9_6
libdnf 0.69.0-13.el9
libeconf 0.4.1-4.el9
libedit 3.1-38.20210216cvs.el9
libestr 0.1.11-4.el9
libevent 2.1.12-8.el9_4
libfastjson 0.99.9-5.el9
libfdisk 2.37.4-21.el9
libffi 3.4.2-8.el9
libfido2 1.13.0-2.el9
libgcc 11.5.0-5.el9_5
libgcrypt 1.10.0-11.el9
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libjpeg-turbo 2.0.90-7.el9
libksba 1.5.1-7.el9
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9
libnghttp2 1.43.0-6.el9
libnsl2 2.0.0-1.el9
libpeas 1.30.0-4.el9
libpq 13.20-1.el9_5
libpwquality 1.4.4-8.el9
librepo 1.14.5-2.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libseccomp 2.5.2-2.el9
libsecret 0.20.4-4.el9
libselinux 3.6-3.el9
libselinux-utils 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-2.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9
libsolv 0.7.24-3.el9
libstdc++ 11.5.0-5.el9_5
libtasn1 4.16.0-9.el9
libtirpc 1.3.3-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libusbx 1.0.26-1.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-12.el9_6
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
logrotate 3.18.0-9.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
mailcap 2.1.49-5.el9
microdnf 3.9.1-3.el9
mpdecimal 2.5.1-3.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-10.20210508.el9_6.2
ncurses-libs 6.2-10.20210508.el9_6.2
nettle 3.10.1-1.el9
npth 1.6-8.el9
oniguruma 6.9.6-1.el9.6
openldap 2.6.8-4.el9
openssh 8.7p1-45.el9
openssh-clients 8.7p1-45.el9
openssl 3.2.2-6.el9_5.1
openssl-fips-provider 3.0.7-6.el9_5
openssl-fips-provider-so 3.0.7-6.el9_5
openssl-libs 3.2.2-6.el9_5.1
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pam 1.5.1-26.el9_6
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
pinentry 1.1.1-8.el9
policycoreutils 3.6-2.1.el9
popt 1.18-8.el9
pulpcore-selinux 2.0.1-1.el9ap
python3 3.9.21-2.el9_6.2
python3-cffi 1.15.0-3.el9ap
python3-chardet 4.0.0-5.el9
python3-cryptography 42.0.5-1.el9ap
python3-idna 2.10-7.el9_4.1
python3-libs 3.9.21-2.el9_6.2
python3-pexpect 4.8.0-7.el9
python3-pip-wheel 21.3.1-1.el9
python3-ptyprocess 0.6.0-12.el9
python3-pycparser 2.21-2.el9pc
python3-pysocks 1.7.1-12.el9
python3-pyyaml 5.4.1-6.el9
python3-requests 2.25.1-10.el9_6
python3-setuptools 53.0.0-13.el9_6.1
python3-setuptools-wheel 53.0.0-13.el9_6.1
python3-six 1.15.0-9.el9
python3-urllib3 1.26.5-6.el9
python3.11 3.11.11-2.el9_6.2
python3.11-aiodns 3.2.0-1.el9ap
python3.11-aiofiles 23.2.1-1.el9ap
python3.11-aiohappyeyeballs 2.4.4-1.el9ap
python3.11-aiohttp 3.10.11-1.el9ap
python3.11-aiosignal 1.3.1-1.el9ap
python3.11-ansible-compat 25.8.1-1.el9ap
python3.11-asgiref 3.7.2-1.el9ap
python3.11-async-lru 2.0.4-1.el9ap
python3.11-async-timeout 4.0.3-2.el9ap
python3.11-asyncio-throttle 1.0.2-4.el9ap
python3.11-attrs 22.2.0-1.el9ap
python3.11-azure-core 1.34.0-1.el9ap
python3.11-azure-storage-blob 12.19.0-1.el9ap
python3.11-backoff 2.2.1-1.el9ap
python3.11-black 24.4.2-2.el9ap
python3.11-boto3 1.34.30-1.el9ap
python3.11-botocore 1.34.30-1.el9ap
python3.11-bracex 2.4-1.el9ap
python3.11-brotli 1.1.0-1.el9ap
python3.11-certifi 2023.5.7-1.el9ap
python3.11-cffi 1.15.1-1.el9
python3.11-charset-normalizer 2.1.0-1.el9
python3.11-click 8.1.7-1.el9ap
python3.11-cryptography 42.0.5-1.el9ap
python3.11-dateutil 2.8.2-2.el9ap
python3.11-defusedxml 0.7.1-4.el9ap
python3.11-deprecated 1.2.14-1.el9ap
python3.11-diff-match-patch 20230430-1.el9ap
python3.11-distro 1.9.0-1.el9ap
python3.11-django 4.2.24-1.el9ap
python3.11-django-ansible-base 2.6.20251001-1.el9ap
python3.11-django-ansible-base+feature_flags 2.6.20251001-1.el9ap
python3.11-django-ansible-base+jwt_consumer 2.6.20251001-1.el9ap
python3.11-django-auth-ldap 4.0.0-2.el9ap
python3.11-django-automated-logging 6.2.2-1.el9ap
python3.11-django-crum 0.7.9-2.el9ap
python3.11-django-filter 23.5-1.el9ap
python3.11-django-flags 5.0.13-1.el9ap
python3.11-django-guid 3.4.0-1.el9ap
python3.11-django-import-export 3.3.6-2.el9ap
python3.11-django-ipware 6.0.5-1.el9ap
python3.11-django-lifecycle 1.1.2-1.el9ap
python3.11-django-picklefield 3.1-1.el9ap
python3.11-django-prometheus 2.3.1-2.el9ap
python3.11-django-storages 1.14.2-2.el9ap
python3.11-django-storages+azure 1.14.2-2.el9ap
python3.11-django-storages+s3 1.14.2-2.el9ap
python3.11-djangorestframework 3.15.1-1.el9ap
python3.11-djangorestframework-queryfields 1.1.0-1.el9ap
python3.11-drf-access-policy 1.5.0-1.el9ap
python3.11-drf-nested-routers 0.93.5-1.el9ap
python3.11-drf-spectacular 0.26.5-2.el9ap
python3.11-dynaconf 3.2.11-1.el9ap
python3.11-et-xmlfile 1.1.0-3.el9ap
python3.11-filelock 3.13.1-1.el9ap
python3.11-flake8 6.1.0-2.el9ap
python3.11-frozenlist 1.4.0-1.el9ap
python3.11-galaxy-importer 0.4.33-1.el9ap
python3.11-galaxy-ng 4.11.0-1.el9ap
python3.11-gitdb 4.0.11-1.el9ap
python3.11-gitpython 3.1.41-1.el9ap
python3.11-gnupg 0.5.2-1.el9ap
python3.11-googleapis-common-protos 1.59.1-2.el9ap
python3.11-grpcio 1.58.3-1.el9ap
python3.11-gunicorn 22.0.0-1.el9ap
python3.11-idna 3.4-1.el9
python3.11-importlib-metadata 6.0.1-2.el9ap
python3.11-inflection 0.5.1-4.el9ap
python3.11-insights-analytics-collector 0.3.2-2.el9ap
python3.11-ipware 3.0.0-1.el9ap
python3.11-isodate 0.6.1-2.el9ap
python3.11-jinja2 3.1.6-1.el9ap
python3.11-jmespath 1.0.1-2.el9ap
python3.11-jq 1.6.0-1.el9ap
python3.11-json-stream 2.3.2-1.el9ap
python3.11-json-stream-rs-tokenizer 0.4.26-1.el9ap
python3.11-jsonschema 4.21.1-1.el9ap
python3.11-jsonschema-specifications 2023.12.1-1.el9ap
python3.11-ldap 3.4.4-1.el9ap
python3.11-libs 3.11.11-2.el9_6.2
python3.11-markdown 3.5.2-1.el9ap
python3.11-markuppy 1.14-4.el9ap
python3.11-markupsafe 2.1.5-1.el9ap
python3.11-marshmallow 3.26.1-1.el9ap
python3.11-mccabe 0.7.0-2.el9ap
python3.11-multidict 6.0.4-1.el9ap
python3.11-mypy-extensions 1.0.0-1.el9ap
python3.11-nh3 0.2.18-1.el9ap
python3.11-oauthlib 3.2.2-1.el9ap
python3.11-odfpy 1.4.1-8.el9ap
python3.11-openpyxl 3.1.2-1.el9ap
python3.11-opentelemetry-api 1.18.0-2.el9ap
python3.11-opentelemetry-distro 0.39b0-6.el9ap
python3.11-opentelemetry-distro+otlp 0.39b0-6.el9ap
python3.11-opentelemetry-exporter-otlp 1.18.0-2.el9ap
python3.11-opentelemetry-exporter-otlp-proto-common 1.18.0-2.el9ap
python3.11-opentelemetry-exporter-otlp-proto-grpc 1.18.0-2.el9ap
python3.11-opentelemetry-exporter-otlp-proto-http 1.18.0-2.el9ap
python3.11-opentelemetry-instrumentation 0.39b0-6.el9ap
python3.11-opentelemetry-instrumentation-django 0.39b0-6.el9ap
python3.11-opentelemetry-instrumentation-wsgi 0.39b0-6.el9ap
python3.11-opentelemetry-proto 1.18.0-2.el9ap
python3.11-opentelemetry-sdk 1.18.0-2.el9ap
python3.11-opentelemetry-semantic-conventions 0.39b0-2.el9ap
python3.11-opentelemetry-util-http 0.39b0-6.el9ap
python3.11-packaging 23.2-1.el9ap
python3.11-parsley 1.3-3.el9ap
python3.11-pathspec 0.12.1-1.el9ap
python3.11-pbr 6.0.0-2.el9ap
python3.11-pillow 10.3.0-1.el9ap
python3.11-pip-wheel 22.3.1-5.el9
python3.11-platformdirs 4.2.0-1.el9ap
python3.11-ply 3.11-1.el9
python3.11-prometheus-client 0.19.0-1.el9ap
python3.11-protobuf 4.21.12-2.el9ap
python3.11-psycopg 3.2.7-1.el9ap
python3.11-pulp-ansible 0.25.1-1.el9ap
python3.11-pulp-container 2.19.3-1.el9ap
python3.11-pulp-glue 0.23.2-1.el9ap
python3.11-pulpcore 3.49.42-1.el9ap
python3.11-pyOpenSSL 24.1.0-1.el9ap
python3.11-pyasn1 0.5.1-1.el9ap
python3.11-pyasn1-modules 0.3.0-1.el9ap
python3.11-pycares 4.4.0-2.el9ap
python3.11-pycodestyle 2.11.1-1.el9ap
python3.11-pycparser 2.20-1.el9
python3.11-pyflakes 3.1.0-1.el9ap
python3.11-pygtrie 2.5.0-2.el9ap
python3.11-pyjwt 2.7.0-2.el9ap
python3.11-pyparsing 3.1.1-1.el9ap
python3.11-python3-openid 3.2.0-3.el9ap
python3.11-pyyaml 6.0-1.el9
python3.11-redis 4.6.0-2.el9ap
python3.11-referencing 0.36.2-1.el9ap
python3.11-requests 2.31.0-2.el9ap
python3.11-requests-oauthlib 1.3.1-1.el9ap
python3.11-resolvelib 1.0.1-1.el9ap
python3.11-rpds-py 0.18.1-1.el9ap
python3.11-ruamel-yaml 0.18.15-1.el9ap
python3.11-ruamel-yaml-clib 0.2.8-1.el9ap
python3.11-s3transfer 0.10.0-1.el9ap
python3.11-semantic-version 2.10.0-2.el9ap
python3.11-setuptools 65.5.1-4.el9_6
python3.11-setuptools-wheel 65.5.1-4.el9_6
python3.11-six 1.16.0-1.el9
python3.11-smmap 5.0.1-1.el9ap
python3.11-social-auth-app-django 5.4.1-1.el9ap
python3.11-social-auth-core 4.5.4-1.el9ap
python3.11-sqlparse 0.5.3-2.el9ap
python3.11-subprocess-tee 0.4.1-2.el9ap
python3.11-tablib 3.5.0-1.el9ap
python3.11-tablib+html 3.5.0-1.el9ap
python3.11-tablib+ods 3.5.0-1.el9ap
python3.11-tablib+xls 3.5.0-1.el9ap
python3.11-tablib+xlsx 3.5.0-1.el9ap
python3.11-tablib+yaml 3.5.0-1.el9ap
python3.11-typing-extensions 4.9.0-1.el9ap
python3.11-uritemplate 4.1.1-3.el9ap
python3.11-url-normalize 1.4.3-5.el9ap
python3.11-urllib3 1.26.20-1.el9ap
python3.11-uuid6 2024.1.12-1.el9ap
python3.11-wcmatch 8.5-1.el9ap
python3.11-whitenoise 6.6.0-1.el9ap
python3.11-wrapt 1.16.0-1.el9ap
python3.11-xlrd 2.0.1-6.el9ap
python3.11-xlwt 1.3.0-4.el9ap
python3.11-yarl 1.13.1-1.el9ap
python3.11-zipp 3.19.2-1.el9ap
readline 8.1-4.el9
redhat-release 9.6-0.1.el9
rootfiles 8.1-34.el9
rpm 4.16.1.3-37.el9
rpm-libs 4.16.1.3-37.el9
rpm-plugin-selinux 4.16.1.3-37.el9
rsyslog 8.2412.0-1.el9
sed 4.8-9.el9
selinux-policy 38.1.53-5.el9_6
selinux-policy-targeted 38.1.53-5.el9_6
setup 2.13.7-10.el9
shadow-utils 4.9-12.el9
shadow-utils-subid 4.9-12.el9
skopeo 1.18.1-2.el9_6
sos 4.9.2-1.el9_6
sqlite-libs 3.34.1-8.el9_6
sshpass 1.09-5.el9ap
systemd 252-51.el9_6.2
systemd-libs 252-51.el9_6.2
systemd-pam 252-51.el9_6.2
systemd-rpm-macros 252-51.el9_6.2
tar 1.34-7.el9
tzdata 2025b-1.el9
util-linux 2.37.4-21.el9
util-linux-core 2.37.4-21.el9
xz-libs 5.2.5-8.el9_0
yajl 2.1.0-25.el9
yamllint 1.35.1-1.el9ap
zlib 1.2.11-40.el9
```

</details>

<details><summary>Python packages: /usr (python3.11) (160)</summary>

```text
aiodns 3.2.0
aiofiles 23.2.1
aiohappyeyeballs 2.4.4
aiohttp 3.10.11
aiosignal 1.3.1
ansible-builder 3.1.0
ansible-compat 25.8.1
ansible-core 2.16.14
ansible-lint 25.8.2
asgiref 3.7.2
async-lru 2.0.4
async-timeout 4.0.3
asyncio-throttle 1.0.2
attrs 22.2.0
azure-core 1.34.0
azure-storage-blob 12.19.0
backoff 2.2.1
bindep 2.11.0
black 24.4.2
boto3 1.34.30
botocore 1.34.30
bracex 2.4
Brotli 1.1.0
certifi 2023.5.7
cffi 1.15.1
charset-normalizer 2.1.0
click 8.1.7
cryptography 42.0.5
defusedxml 0.7.1
Deprecated 1.2.14
diff-match-patch 20230430
distro 1.9.0
Django 4.2.24
django-ansible-base 2.6.20251001
django-auth-ldap 4.0.0
django-automated-logging 6.2.2
django-crum 0.7.9
django-filter 23.5
django-flags 5.0.13
django-guid 3.4.0
django-import-export 3.3.6
django-ipware 6.0.5
django-lifecycle 1.1.2
django-picklefield 3.1
django-prometheus 2.3.1
django-storages 1.14.2
djangorestframework 3.15.1
djangorestframework-queryfields 1.1.0
drf-access-policy 1.5.0
drf-nested-routers 0.93.5
drf-spectacular 0.26.5
dynaconf 3.2.11
et-xmlfile 1.1.0
filelock 3.13.1
flake8 6.1.0
frozenlist 1.4.0
galaxy-importer 0.4.33
galaxy-ng 4.11.0.dev0
gitdb 4.0.11
GitPython 3.1.41
googleapis-common-protos 1.59.1
grpcio 1.58.3
gunicorn 22.0.0
idna 3.4
importlib-metadata 6.0.1
inflection 0.5.1
insights-analytics-collector 0.3.2
isodate 0.6.1
Jinja2 3.1.6
jmespath 1.0.1
jq 1.6.0
json-stream 2.3.2
json-stream-rs-tokenizer 0.4.26
jsonschema 4.21.1
jsonschema-specifications 2023.12.1
Markdown 3.5.2
MarkupPy 1.14
MarkupSafe 2.1.5
marshmallow 3.26.1
mccabe 0.7.0
multidict 6.0.4
mypy-extensions 1.0.0
nh3 0.2.18
oauthlib 3.2.2
odfpy 1.4.1
openpyxl 3.1.2
opentelemetry-api 1.18.0
opentelemetry-distro 0.39b0
opentelemetry-exporter-otlp 1.18.0
opentelemetry-exporter-otlp-proto-common 1.18.0
opentelemetry-exporter-otlp-proto-grpc 1.18.0
opentelemetry-exporter-otlp-proto-http 1.18.0
opentelemetry-instrumentation 0.39b0
opentelemetry-instrumentation-django 0.39b0
opentelemetry-instrumentation-wsgi 0.39b0
opentelemetry-proto 1.18.0
opentelemetry-sdk 1.18.0
opentelemetry-semantic-conventions 0.39b0
opentelemetry-util-http 0.39b0
packaging 23.2
Parsley 1.3
pathspec 0.12.1
pbr 6.0.0
pillow 10.3.0
platformdirs 4.2.0
ply 3.11
prometheus-client 0.19.0
protobuf 4.21.12
psycopg 3.2.7
pulp-ansible 0.25.1
pulp-container 2.19.3
pulp-glue 0.23.2
pulpcore 3.49.42
pyasn1 0.5.1
pyasn1-modules 0.3.0
pycares 4.4.0
pycodestyle 2.11.1
pycparser 2.20
pyflakes 3.1.0
pygtrie 2.5.0
PyJWT 2.7.0
pyOpenSSL 24.1.0
pyparsing 3.1.1
python-dateutil 2.8.2
python-gnupg 0.5.2
python-ipware 3.0.0
python-ldap 3.4.4
python3-openid 3.2.0
PyYAML 6.0
redis 4.6.0
referencing 0.36.2
requests 2.31.0
requests-oauthlib 1.3.1
resolvelib 1.0.1
rpds-py 0.18.1
ruamel.yaml 0.18.15
ruamel.yaml.clib 0.2.8
s3transfer 0.10.0
semantic-version 2.10.0
setuptools 65.5.1
six 1.16.0
smmap 5.0.1
social-auth-app-django 5.4.1
social-auth-core 4.5.4
sqlparse 0.5.3
subprocess-tee 0.4.1
tablib 3.5.0
typing_extensions 4.9.0
uritemplate 4.1.1
url-normalize 1.4.3
urllib3 1.26.20
uuid6 2024.1.12
wcmatch 8.5
whitenoise 6.6.0
wrapt 1.16.0
xlrd 2.0.1
xlwt 1.3.0
yamllint 1.35.1
yarl 1.13.1
zipp 3.19.2
```

</details>

<details><summary>Python packages: /usr (python3.9) (14)</summary>

```text
cffi 1.15.0
chardet 4.0.0
cryptography 42.0.5
idna 2.10
pexpect 4.8.0
ptyprocess 0.6.0
pycparser 2.21
PySocks 1.7.1
PyYAML 5.4.1
requests 2.25.1
setuptools 53.0.0
six 1.15.0
sos 4.9.2
urllib3 1.26.5
```

</details>

[Back to top](#contents)

### hub-web-rhel9

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-26/hub-web-rhel9` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/hub-web-rhel9.tar.gz` |
| Labels `version` / `release` | `4.11.0` / `150` |
| Image ID | `sha256:8852c4dcca6f23398c65040a4a5a5d24998fc102a447efbb35815426badd2f1e` |
| Build date | 2025-09-24T00:41:14 |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.6 (Plow) |
| Python | 3.9 |
| Ansible Core | N/A |

<details><summary>RPM packages (301)</summary>

```text
acl 2.3.1-4.el9
alternatives 1.24-2.el9
attr 2.5.1-3.el9
audit-libs 3.1.5-4.el9
basesystem 11-13.el9
bash 5.1.8-9.el9
bind9.18-libs 9.18.29-4.el9_6
bind9.18-utils 9.18.29-4.el9_6
bsdtar 3.5.3-6.el9_6
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crypto-policies 20250128-1.git5269e22.el9
crypto-policies-scripts 20250128-1.git5269e22.el9
curl-minimal 7.76.1-31.el9_6.1
cyrus-sasl-lib 2.1.27-21.el9
dbus 1.12.20-8.el9
dbus-broker 28-7.el9
dbus-common 1.12.20-8.el9
dbus-libs 1.12.20-8.el9
dejavu-sans-fonts 2.37-18.el9
dmidecode 3.6-1.el9
dnf 4.14.0-25.el9
dnf-data 4.14.0-25.el9
elfutils-default-yama-scope 0.192-6.el9_6
elfutils-libelf 0.192-6.el9_6
elfutils-libs 0.192-6.el9_6
environment-modules 5.3.0-1.el9
expat 2.5.0-5.el9_6
file-libs 5.39-16.el9
filesystem 3.16-5.el9
findutils 4.8.0-7.el9
fontconfig 2.14.0-2.el9_1
fonts-filesystem 2.0.5-7.el9.1
freetype 2.10.4-10.el9_5
fstrm 0.6.1-3.el9
gawk 5.1.0-6.el9
gd 2.3.2-3.el9
gdb-gdbserver 14.2-4.1.el9_6
gdbm-libs 1.23-1.el9
gettext 0.21-8.el9
gettext-libs 0.21-8.el9
glib2 2.68.4-16.el9_6.2
glibc 2.34-168.el9_6.23
glibc-common 2.34-168.el9_6.23
glibc-langpack-en 2.34-168.el9_6.23
glibc-locale-source 2.34-168.el9_6.23
glibc-minimal-langpack 2.34-168.el9_6.23
gmp 6.2.0-13.el9
gnupg2 2.3.3-4.el9
gnutls 3.8.3-6.el9_6.2
gobject-introspection 1.68.0-11.el9
gpg-pubkey 5a6340b3-6229229e
gpg-pubkey fd431d51-4ae0493b
gpgme 1.15.1-6.el9
graphite2 1.3.14-9.el9
grep 3.6-5.el9
groff-base 1.22.4-10.el9
gzip 1.12-1.el9
harfbuzz 2.7.4-10.el9
hostname 3.23-6.el9
ima-evm-utils 1.5-3.el9
iproute 6.11.0-1.el9
jbigkit-libs 2.1-23.el9
json-c 0.14-11.el9
json-glib 1.6.6-1.el9
keyutils 1.6.3-1.el9
keyutils-libs 1.6.3-1.el9
kmod-libs 28-10.el9
krb5-libs 1.21.1-8.el9_6
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
less 590-5.el9
libX11 1.7.0-11.el9
libX11-common 1.7.0-11.el9
libXau 1.0.9-8.el9
libXpm 3.5.13-10.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-6.el9_6
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9
libbpf 1.5.0-1.el9
libbrotli 1.0.9-7.el9_5
libcap 2.48-9.el9_2
libcap-ng 0.8.2-7.el9
libcom_err 1.46.5-7.el9
libcomps 0.1.18-1.el9
libcurl-minimal 7.76.1-31.el9_6.1
libdb 5.3.28-57.el9_6
libdnf 0.69.0-13.el9
libdnf-plugin-subscription-manager 1.29.45.1-1.el9_6
libeconf 0.4.1-4.el9
libevent 2.1.12-8.el9_4
libfdisk 2.37.4-21.el9
libffi 3.4.2-8.el9
libgcc 11.5.0-5.el9_5
libgcrypt 1.10.0-11.el9
libgomp 11.5.0-5.el9_5
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libjpeg-turbo 2.0.90-7.el9
libksba 1.5.1-7.el9
libmaxminddb 1.5.2-4.el9
libmnl 1.0.4-16.el9_4
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9
libnghttp2 1.43.0-6.el9
libpipeline 1.5.3-4.el9
libpng 1.6.37-12.el9
libpwquality 1.4.4-8.el9
librepo 1.14.5-2.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libseccomp 2.5.2-2.el9
libselinux 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-2.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9
libsolv 0.7.24-3.el9
libstdc++ 11.5.0-5.el9_5
libtasn1 4.16.0-9.el9
libtiff 4.4.0-13.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libuser 0.63-16.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9
libuv 1.42.0-2.el9_4
libverto 0.3.2-3.el9
libwebp 1.2.0-8.el9_3
libxcb 1.13.1-9.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-12.el9_6
libxslt 1.1.34-13.el9_6
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
lmdb-libs 0.9.29-3.el9
logrotate 3.18.0-9.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
man-db 2.9.3-7.el9
mpfr 4.1.0-7.el9
ncurses 6.2-10.20210508.el9_6.2
ncurses-base 6.2-10.20210508.el9_6.2
ncurses-libs 6.2-10.20210508.el9_6.2
nettle 3.10.1-1.el9
nginx 1.24.0-4.module+el9.5.0+22954+e2d70a1c.1
nginx-all-modules 1.24.0-4.module+el9.5.0+22954+e2d70a1c.1
nginx-core 1.24.0-4.module+el9.5.0+22954+e2d70a1c.1
nginx-filesystem 1.24.0-4.module+el9.5.0+22954+e2d70a1c.1
nginx-mod-http-image-filter 1.24.0-4.module+el9.5.0+22954+e2d70a1c.1
nginx-mod-http-perl 1.24.0-4.module+el9.5.0+22954+e2d70a1c.1
nginx-mod-http-xslt-filter 1.24.0-4.module+el9.5.0+22954+e2d70a1c.1
nginx-mod-mail 1.24.0-4.module+el9.5.0+22954+e2d70a1c.1
nginx-mod-stream 1.24.0-4.module+el9.5.0+22954+e2d70a1c.1
npth 1.6-8.el9
nss_wrapper-libs 1.1.13-1.el9
openldap 2.6.8-4.el9
openssl 3.2.2-6.el9_5.1
openssl-fips-provider 3.0.7-6.el9_5
openssl-fips-provider-so 3.0.7-6.el9_5
openssl-libs 3.2.2-6.el9_5.1
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pam 1.5.1-26.el9_6
passwd 0.80-12.el9
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
perl-AutoLoader 5.74-481.1.el9_6
perl-B 1.80-481.1.el9_6
perl-Carp 1.50-460.el9
perl-Class-Struct 0.66-481.1.el9_6
perl-Data-Dumper 2.174-462.el9
perl-Digest 1.19-4.el9
perl-Digest-MD5 2.58-4.el9
perl-Encode 3.08-462.el9
perl-Errno 1.30-481.1.el9_6
perl-Exporter 5.74-461.el9
perl-Fcntl 1.13-481.1.el9_6
perl-File-Basename 2.85-481.1.el9_6
perl-File-Path 2.18-4.el9
perl-File-Temp 0.231.100-4.el9
perl-File-stat 1.09-481.1.el9_6
perl-FileHandle 2.03-481.1.el9_6
perl-Getopt-Long 2.52-4.el9
perl-Getopt-Std 1.12-481.1.el9_6
perl-HTTP-Tiny 0.076-462.el9
perl-IO 1.43-481.1.el9_6
perl-IO-Socket-IP 0.41-5.el9
perl-IO-Socket-SSL 2.073-2.el9
perl-IPC-Open3 1.21-481.1.el9_6
perl-MIME-Base64 3.16-4.el9
perl-Mozilla-CA 20200520-6.el9
perl-NDBM_File 1.15-481.1.el9_6
perl-Net-SSLeay 1.94-1.el9
perl-POSIX 1.94-481.1.el9_6
perl-PathTools 3.78-461.el9
perl-Pod-Escapes 1.07-460.el9
perl-Pod-Perldoc 3.28.01-461.el9
perl-Pod-Simple 3.42-4.el9
perl-Pod-Usage 2.01-4.el9
perl-Scalar-List-Utils 1.56-462.el9
perl-SelectSaver 1.02-481.1.el9_6
perl-Socket 2.031-4.el9
perl-Storable 3.21-460.el9
perl-Symbol 1.08-481.1.el9_6
perl-Term-ANSIColor 5.01-461.el9
perl-Term-Cap 1.17-460.el9
perl-Text-ParseWords 3.30-460.el9
perl-Text-Tabs+Wrap 2013.0523-460.el9
perl-Time-Local 1.300-7.el9
perl-URI 5.09-3.el9
perl-base 2.27-481.1.el9_6
perl-constant 1.33-461.el9
perl-if 0.60.800-481.1.el9_6
perl-interpreter 5.32.1-481.1.el9_6
perl-libnet 3.13-4.el9
perl-libs 5.32.1-481.1.el9_6
perl-mro 1.23-481.1.el9_6
perl-overload 1.31-481.1.el9_6
perl-overloading 0.02-481.1.el9_6
perl-parent 0.238-460.el9
perl-podlators 4.14-460.el9
perl-subs 1.03-481.1.el9_6
perl-vars 1.05-481.1.el9_6
popt 1.18-8.el9
procps-ng 3.3.17-14.el9
protobuf-c 1.3.3-13.el9
psmisc 23.4-3.el9
python3 3.9.21-2.el9_6.2
python3-chardet 4.0.0-5.el9
python3-cloud-what 1.29.45.1-1.el9_6
python3-dateutil 2.8.1-7.el9
python3-dbus 1.2.18-2.el9
python3-decorator 4.4.2-6.el9
python3-dnf 4.14.0-25.el9
python3-dnf-plugins-core 4.3.0-20.el9
python3-gobject-base 3.40.1-6.el9
python3-gobject-base-noarch 3.40.1-6.el9
python3-gpg 1.15.1-6.el9
python3-hawkey 0.69.0-13.el9
python3-idna 2.10-7.el9_4.1
python3-iniparse 0.4-45.el9
python3-inotify 0.9.6-25.el9
python3-libcomps 0.1.18-1.el9
python3-libdnf 0.69.0-13.el9
python3-librepo 1.14.5-2.el9
python3-libs 3.9.21-2.el9_6.2
python3-pip-wheel 21.3.1-1.el9
python3-pysocks 1.7.1-12.el9
python3-requests 2.25.1-10.el9_6
python3-rpm 4.16.1.3-37.el9
python3-setuptools 53.0.0-13.el9_6.1
python3-setuptools-wheel 53.0.0-13.el9_6.1
python3-six 1.15.0-9.el9
python3-subscription-manager-rhsm 1.29.45.1-1.el9_6
python3-systemd 234-19.el9
python3-urllib3 1.26.5-6.el9
readline 8.1-4.el9
redhat-logos-httpd 90.5-1.el9_6.1
redhat-release 9.6-0.1.el9
rootfiles 8.1-34.el9
rpm 4.16.1.3-37.el9
rpm-build-libs 4.16.1.3-37.el9
rpm-libs 4.16.1.3-37.el9
rpm-sign-libs 4.16.1.3-37.el9
rsync 3.2.5-3.el9
scl-utils 2.0.3-4.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-12.el9
sqlite-libs 3.34.1-8.el9_6
subscription-manager 1.29.45.1-1.el9_6
subscription-manager-rhsm-certificates 20220623-1.el9
systemd 252-51.el9_6.2
systemd-libs 252-51.el9_6.2
systemd-pam 252-51.el9_6.2
systemd-rpm-macros 252-51.el9_6.2
tar 1.34-7.el9
tcl 8.6.10-7.el9
tpm2-tss 3.2.3-1.el9
tzdata 2025b-1.el9
unzip 6.0-58.el9_5
usermode 1.114-6.el9
util-linux 2.37.4-21.el9
util-linux-core 2.37.4-21.el9
vim-filesystem 8.2.2637-22.el9_6
vim-minimal 8.2.2637-22.el9_6
virt-what 1.27-1.el9
which 2.21-30.el9_6
xml-common 0.6.3-58.el9
xz 5.2.5-8.el9_0
xz-libs 5.2.5-8.el9_0
yum 4.14.0-25.el9
zlib 1.2.11-40.el9
```

</details>

<details><summary>Python packages: /usr (python3.9) (18)</summary>

```text
chardet 4.0.0
dbus-python 1.2.18
decorator 4.4.2
gpg 1.15.1
idna 2.10
iniparse 0.4
libcomps 0.1.18
PyGObject 3.40.1
pyinotify 0.9.6
PySocks 1.7.1
python-dateutil 2.8.1
requests 2.25.1
rpm 4.16.1.3
setuptools 53.0.0
six 1.15.0
subscription-manager 1.29.45.1
systemd-python 234
urllib3 1.26.5
```

</details>

[Back to top](#contents)

### receptor-rhel9

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-26/receptor-rhel9` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/receptor-rhel9.tar.gz` |
| Labels `version` / `release` | `1.5.7` / `11` |
| Image ID | `sha256:920342a88459db4fb4ab12fd3fedfaab752fccb12a6a3e2c25565e0dd8138750` |
| Build date | 2025-09-23T21:40:42 |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.6 (Plow) |
| Python | 3.9, 3.11 |
| Ansible Core | N/A |

<details><summary>RPM packages (174)</summary>

```text
acl 2.3.1-4.el9
alternatives 1.24-2.el9
ansible-runner 2.4.1-1.el9ap
audit-libs 3.1.5-4.el9
basesystem 11-13.el9
bash 5.1.8-9.el9
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crypto-policies 20250128-1.git5269e22.el9
curl-minimal 7.76.1-31.el9_6.1
cyrus-sasl-lib 2.1.27-21.el9
dbus 1.12.20-8.el9
dbus-broker 28-7.el9
dbus-common 1.12.20-8.el9
dejavu-sans-fonts 2.37-18.el9
diffutils 3.7-12.el9
dnf-data 4.14.0-25.el9
dumb-init 1.2.5-3.el9ap
expat 2.5.0-5.el9_6
file-libs 5.39-16.el9
filesystem 3.16-5.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdbm-libs 1.23-1.el9
glib2 2.68.4-16.el9_6.2
glibc 2.34-168.el9_6.23
glibc-common 2.34-168.el9_6.23
glibc-minimal-langpack 2.34-168.el9_6.23
gmp 6.2.0-13.el9
gnupg2 2.3.3-4.el9
gnutls 3.8.3-6.el9_6.2
gobject-introspection 1.68.0-11.el9
gpg-pubkey 5a6340b3-6229229e
gpg-pubkey fd431d51-4ae0493b
gpgme 1.15.1-6.el9
grep 3.6-5.el9
gzip 1.12-1.el9
json-c 0.14-11.el9
json-glib 1.6.6-1.el9
keyutils-libs 1.6.3-1.el9
kmod-libs 28-10.el9
krb5-libs 1.21.1-8.el9_6
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-6.el9_6
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9
libcap 2.48-9.el9_2
libcap-ng 0.8.2-7.el9
libcom_err 1.46.5-7.el9
libcurl-minimal 7.76.1-31.el9_6.1
libdb 5.3.28-57.el9_6
libdnf 0.69.0-13.el9
libeconf 0.4.1-4.el9
libevent 2.1.12-8.el9_4
libfdisk 2.37.4-21.el9
libffi 3.4.2-8.el9
libgcc 11.5.0-5.el9_5
libgcrypt 1.10.0-11.el9
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libksba 1.5.1-7.el9
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9
libnghttp2 1.43.0-6.el9
libnsl2 2.0.0-1.el9
libpeas 1.30.0-4.el9
libpwquality 1.4.4-8.el9
librepo 1.14.5-2.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libseccomp 2.5.2-2.el9
libselinux 3.6-3.el9
libselinux-utils 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-2.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9
libsolv 0.7.24-3.el9
libstdc++ 11.5.0-5.el9_5
libtasn1 4.16.0-9.el9
libtirpc 1.3.3-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libusbx 1.0.26-1.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-12.el9_6
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
logrotate 3.18.0-9.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
microdnf 3.9.1-3.el9
mpdecimal 2.5.1-3.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-10.20210508.el9_6.2
ncurses-libs 6.2-10.20210508.el9_6.2
nettle 3.10.1-1.el9
npth 1.6-8.el9
openldap 2.6.8-4.el9
openssl 3.2.2-6.el9_5.1
openssl-fips-provider 3.0.7-6.el9_5
openssl-fips-provider-so 3.0.7-6.el9_5
openssl-libs 3.2.2-6.el9_5.1
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pam 1.5.1-26.el9_6
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
podman-remote 5.4.0-13.el9_6
policycoreutils 3.6-2.1.el9
popt 1.18-8.el9
python3 3.9.21-2.el9_6.2
python3-chardet 4.0.0-5.el9
python3-idna 2.10-7.el9_4.1
python3-libs 3.9.21-2.el9_6.2
python3-pexpect 4.8.0-7.el9
python3-pip-wheel 21.3.1-1.el9
python3-ptyprocess 0.6.0-12.el9
python3-pysocks 1.7.1-12.el9
python3-pyyaml 5.4.1-6.el9
python3-requests 2.25.1-10.el9_6
python3-setuptools 53.0.0-13.el9_6.1
python3-setuptools-wheel 53.0.0-13.el9_6.1
python3-six 1.15.0-9.el9
python3-urllib3 1.26.5-6.el9
python3.11 3.11.11-2.el9_6.2
python3.11-ansible-runner 2.4.1-1.el9ap
python3.11-click 8.1.7-1.el9ap
python3.11-daemon 2.3.2-1.el9ap
python3.11-dateutil 2.8.2-2.el9ap
python3.11-docutils 0.20.1-2.el9ap
python3.11-libs 3.11.11-2.el9_6.2
python3.11-lockfile 0.12.2-2.el9ap
python3.11-packaging 23.2-1.el9ap
python3.11-pexpect 4.9.0-1.el9ap
python3.11-pip-wheel 22.3.1-5.el9
python3.11-ptyprocess 0.7.0-1.el9ap
python3.11-pyyaml 6.0-1.el9
python3.11-setuptools 65.5.1-4.el9_6
python3.11-setuptools-wheel 65.5.1-4.el9_6
python3.11-six 1.16.0-1.el9
readline 8.1-4.el9
receptor 1.5.7-2.el9ap
receptorctl 1.5.7-2.el9ap
redhat-release 9.6-0.1.el9
rootfiles 8.1-34.el9
rpm 4.16.1.3-37.el9
rpm-libs 4.16.1.3-37.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-12.el9
shadow-utils-subid 4.9-12.el9
sos 4.9.2-1.el9_6
sqlite-libs 3.34.1-8.el9_6
systemd 252-51.el9_6.2
systemd-libs 252-51.el9_6.2
systemd-pam 252-51.el9_6.2
systemd-rpm-macros 252-51.el9_6.2
tzdata 2025b-1.el9
util-linux 2.37.4-21.el9
util-linux-core 2.37.4-21.el9
xz-libs 5.2.5-8.el9_0
zlib 1.2.11-40.el9
```

</details>

<details><summary>Python packages: /usr (python3.11) (13)</summary>

```text
ansible-runner 2.4.1
click 8.1.7
docutils 0.20.1
lockfile 0.12.2
packaging 23.2
pexpect 4.9.0
ptyprocess 0.7.0
python-daemon 2.3.2
python-dateutil 2.8.2
PyYAML 6.0
receptorctl 1.5.7
setuptools 65.5.1
six 1.16.0
```

</details>

<details><summary>Python packages: /usr (python3.9) (11)</summary>

```text
chardet 4.0.0
idna 2.10
pexpect 4.8.0
ptyprocess 0.6.0
PySocks 1.7.1
PyYAML 5.4.1
requests 2.25.1
setuptools 53.0.0
six 1.15.0
sos 4.9.2
urllib3 1.26.5
```

</details>

[Back to top](#contents)

### pcp

| Field | Value |
|---|---|
| Image | `registry.redhat.io/rhel9/pcp` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/pcp.tar.gz` |
| Labels `version` / `release` | `6` / `1758530508` |
| Image ID | `sha256:8322c3ef2c6f781dd8573b0d6728c5116ef349775d46611cb9d0045c91a1f24a` |
| Build date | 2025-09-22T08:42:21Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.6 (Plow) |
| Python | 3.9 |
| Ansible Core | N/A |

<details><summary>RPM packages (212)</summary>

```text
acl 2.3.1-4.el9
alternatives 1.24-2.el9
attr 2.5.1-3.el9
audit-libs 3.1.5-4.el9
avahi-libs 0.8-22.el9_6.1
basesystem 11-13.el9
bash 5.1.8-9.el9
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crypto-policies 20250128-1.git5269e22.el9
crypto-policies-scripts 20250128-1.git5269e22.el9
curl-minimal 7.76.1-31.el9_6.1
cyrus-sasl-lib 2.1.27-21.el9
dbus 1.12.20-8.el9
dbus-broker 28-7.el9
dbus-common 1.12.20-8.el9
dbus-libs 1.12.20-8.el9
dejavu-sans-fonts 2.37-18.el9
device-mapper 1.02.202-6.el9
device-mapper-libs 1.02.202-6.el9
diffutils 3.7-12.el9
dmidecode 3.6-1.el9
dnf 4.14.0-25.el9
dnf-data 4.14.0-25.el9
elfutils-default-yama-scope 0.192-6.el9_6
elfutils-libelf 0.192-6.el9_6
elfutils-libs 0.192-6.el9_6
expat 2.5.0-5.el9_6
file-libs 5.39-16.el9
filesystem 3.16-5.el9
findutils 4.8.0-7.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdb-gdbserver 14.2-4.1.el9_6
gdbm-libs 1.23-1.el9
gettext 0.21-8.el9
gettext-libs 0.21-8.el9
glib2 2.68.4-16.el9_6.2
glibc 2.34-168.el9_6.23
glibc-common 2.34-168.el9_6.23
glibc-minimal-langpack 2.34-168.el9_6.23
gmp 6.2.0-13.el9
gnupg2 2.3.3-4.el9
gnutls 3.8.3-6.el9_6.2
gobject-introspection 1.68.0-11.el9
gpg-pubkey 5a6340b3-6229229e
gpg-pubkey fd431d51-4ae0493b
gpgme 1.15.1-6.el9
grep 3.6-5.el9
gzip 1.12-1.el9
hostname 3.23-6.el9
ima-evm-utils 1.5-3.el9
iproute 6.11.0-1.el9
json-c 0.14-11.el9
json-glib 1.6.6-1.el9
keyutils 1.6.3-1.el9
keyutils-libs 1.6.3-1.el9
kmod-libs 28-10.el9
krb5-libs 1.21.1-8.el9_6
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-6.el9_6
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9
libbpf 1.5.0-1.el9
libcap 2.48-9.el9_2
libcap-ng 0.8.2-7.el9
libcom_err 1.46.5-7.el9
libcomps 0.1.18-1.el9
libcurl-minimal 7.76.1-31.el9_6.1
libdb 5.3.28-57.el9_6
libdnf 0.69.0-13.el9
libdnf-plugin-subscription-manager 1.29.45.1-1.el9_6
libeconf 0.4.1-4.el9
libevent 2.1.12-8.el9_4
libfdisk 2.37.4-21.el9
libffi 3.4.2-8.el9
libgcc 11.5.0-5.el9_5
libgcrypt 1.10.0-11.el9
libgomp 11.5.0-5.el9_5
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libksba 1.5.1-7.el9
libmnl 1.0.4-16.el9_4
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9
libnghttp2 1.43.0-6.el9
libpkgconf 1.7.3-10.el9
libpwquality 1.4.4-8.el9
librepo 1.14.5-2.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libseccomp 2.5.2-2.el9
libselinux 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-2.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9
libsolv 0.7.24-3.el9
libstdc++ 11.5.0-5.el9_5
libtasn1 4.16.0-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libuser 0.63-16.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9
libuv 1.42.0-2.el9_4
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-12.el9_6
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-10.20210508.el9_6.2
ncurses-libs 6.2-10.20210508.el9_6.2
nettle 3.10.1-1.el9
npth 1.6-8.el9
openldap 2.6.8-4.el9
openssl 3.2.2-6.el9_5.1
openssl-fips-provider 3.0.7-6.el9_5
openssl-fips-provider-so 3.0.7-6.el9_5
openssl-libs 3.2.2-6.el9_5.1
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pam 1.5.1-26.el9_6
passwd 0.80-12.el9
pcp 6.3.7-1.el9_6
pcp-conf 6.3.7-1.el9_6
pcp-doc 6.3.7-1.el9_6
pcp-libs 6.3.7-1.el9_6
pcp-pmda-dm 6.3.7-1.el9_6
pcp-pmda-nfsclient 6.3.7-1.el9_6
pcp-pmda-openmetrics 6.3.7-1.el9_6
pcp-system-tools 6.3.7-1.el9_6
pcp-zeroconf 6.3.7-1.el9_6
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
pkgconf 1.7.3-10.el9
pkgconf-m4 1.7.3-10.el9
pkgconf-pkg-config 1.7.3-10.el9
popt 1.18-8.el9
procps-ng 3.3.17-14.el9
psmisc 23.4-3.el9
python3 3.9.21-2.el9_6.2
python3-chardet 4.0.0-5.el9
python3-cloud-what 1.29.45.1-1.el9_6
python3-dateutil 2.8.1-7.el9
python3-dbus 1.2.18-2.el9
python3-decorator 4.4.2-6.el9
python3-dnf 4.14.0-25.el9
python3-dnf-plugins-core 4.3.0-20.el9
python3-gobject-base 3.40.1-6.el9
python3-gobject-base-noarch 3.40.1-6.el9
python3-gpg 1.15.1-6.el9
python3-hawkey 0.69.0-13.el9
python3-idna 2.10-7.el9_4.1
python3-iniparse 0.4-45.el9
python3-inotify 0.9.6-25.el9
python3-libcomps 0.1.18-1.el9
python3-libdnf 0.69.0-13.el9
python3-librepo 1.14.5-2.el9
python3-libs 3.9.21-2.el9_6.2
python3-pcp 6.3.7-1.el9_6
python3-pip-wheel 21.3.1-1.el9
python3-pysocks 1.7.1-12.el9
python3-requests 2.25.1-10.el9_6
python3-rpm 4.16.1.3-37.el9
python3-setuptools 53.0.0-13.el9_6.1
python3-setuptools-wheel 53.0.0-13.el9_6.1
python3-six 1.15.0-9.el9
python3-subscription-manager-rhsm 1.29.45.1-1.el9_6
python3-systemd 234-19.el9
python3-urllib3 1.26.5-6.el9
readline 8.1-4.el9
redhat-release 9.6-0.1.el9
rootfiles 8.1-34.el9
rpm 4.16.1.3-37.el9
rpm-build-libs 4.16.1.3-37.el9
rpm-libs 4.16.1.3-37.el9
rpm-sign-libs 4.16.1.3-37.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-12.el9
sqlite-libs 3.34.1-8.el9_6
subscription-manager 1.29.45.1-1.el9_6
subscription-manager-rhsm-certificates 20220623-1.el9
systemd 252-51.el9_6.2
systemd-libs 252-51.el9_6.2
systemd-pam 252-51.el9_6.2
systemd-rpm-macros 252-51.el9_6.2
tar 1.34-7.el9
tpm2-tss 3.2.3-1.el9
tzdata 2025b-1.el9
usermode 1.114-6.el9
util-linux 2.37.4-21.el9
util-linux-core 2.37.4-21.el9
vim-minimal 8.2.2637-22.el9_6
virt-what 1.27-1.el9
which 2.21-30.el9_6
xz 5.2.5-8.el9_0
xz-libs 5.2.5-8.el9_0
yum 4.14.0-25.el9
zlib 1.2.11-40.el9
```

</details>

<details><summary>Python packages: /usr (python3.9) (19)</summary>

```text
chardet 4.0.0
dbus-python 1.2.18
decorator 4.4.2
gpg 1.15.1
idna 2.10
iniparse 0.4
libcomps 0.1.18
pcp 5.0
PyGObject 3.40.1
pyinotify 0.9.6
PySocks 1.7.1
python-dateutil 2.8.1
requests 2.25.1
rpm 4.16.1.3
setuptools 53.0.0
six 1.15.0
subscription-manager 1.29.45.1
systemd-python 234
urllib3 1.26.5
```

</details>

[Back to top](#contents)

### postgresql-15

| Field | Value |
|---|---|
| Image | `registry.redhat.io/rhel9/postgresql-15` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/postgresql-15.tar.gz` |
| Labels `version` / `release` | `1` / `1758514462` |
| Image ID | `sha256:473f17c83f4be1d45173b45d14ca57a97be30f9c7fb51c150195d1b1a3dddd8a` |
| Build date | 2025-09-22T04:19:30Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.6 (Plow) |
| Python | 3.9 |
| Ansible Core | N/A |

<details><summary>RPM packages (280)</summary>

```text
acl 2.3.1-4.el9
alternatives 1.24-2.el9
attr 2.5.1-3.el9
audit-libs 3.1.5-4.el9
basesystem 11-13.el9
bash 5.1.8-9.el9
bind9.18-libs 9.18.29-4.el9_6
bind9.18-utils 9.18.29-4.el9_6
bsdtar 3.5.3-6.el9_6
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crypto-policies 20250128-1.git5269e22.el9
crypto-policies-scripts 20250128-1.git5269e22.el9
curl-minimal 7.76.1-31.el9_6.1
cyrus-sasl-lib 2.1.27-21.el9
dbus 1.12.20-8.el9
dbus-broker 28-7.el9
dbus-common 1.12.20-8.el9
dbus-libs 1.12.20-8.el9
dejavu-sans-fonts 2.37-18.el9
dmidecode 3.6-1.el9
dnf 4.14.0-25.el9
dnf-data 4.14.0-25.el9
elfutils-default-yama-scope 0.192-6.el9_6
elfutils-libelf 0.192-6.el9_6
elfutils-libs 0.192-6.el9_6
environment-modules 5.3.0-1.el9
expat 2.5.0-5.el9_6
file-libs 5.39-16.el9
filesystem 3.16-5.el9
findutils 4.8.0-7.el9
fonts-filesystem 2.0.5-7.el9.1
fstrm 0.6.1-3.el9
gawk 5.1.0-6.el9
gdb-gdbserver 14.2-4.1.el9_6
gdbm-libs 1.23-1.el9
gettext 0.21-8.el9
gettext-libs 0.21-8.el9
glib2 2.68.4-16.el9_6.2
glibc 2.34-168.el9_6.23
glibc-common 2.34-168.el9_6.23
glibc-langpack-en 2.34-168.el9_6.23
glibc-locale-source 2.34-168.el9_6.23
glibc-minimal-langpack 2.34-168.el9_6.23
gmp 6.2.0-13.el9
gnupg2 2.3.3-4.el9
gnutls 3.8.3-6.el9_6.2
gobject-introspection 1.68.0-11.el9
gpg-pubkey 5a6340b3-6229229e
gpg-pubkey fd431d51-4ae0493b
gpgme 1.15.1-6.el9
grep 3.6-5.el9
groff-base 1.22.4-10.el9
gzip 1.12-1.el9
ima-evm-utils 1.5-3.el9
iproute 6.11.0-1.el9
json-c 0.14-11.el9
json-glib 1.6.6-1.el9
keyutils 1.6.3-1.el9
keyutils-libs 1.6.3-1.el9
kmod-libs 28-10.el9
krb5-libs 1.21.1-8.el9_6
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
less 590-5.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-6.el9_6
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9
libbpf 1.5.0-1.el9
libcap 2.48-9.el9_2
libcap-ng 0.8.2-7.el9
libcom_err 1.46.5-7.el9
libcomps 0.1.18-1.el9
libcurl-minimal 7.76.1-31.el9_6.1
libdb 5.3.28-57.el9_6
libdnf 0.69.0-13.el9
libdnf-plugin-subscription-manager 1.29.45.1-1.el9_6
libeconf 0.4.1-4.el9
libevent 2.1.12-8.el9_4
libfdisk 2.37.4-21.el9
libffi 3.4.2-8.el9
libgcc 11.5.0-5.el9_5
libgcrypt 1.10.0-11.el9
libgomp 11.5.0-5.el9_5
libgpg-error 1.42-5.el9
libicu 67.1-10.el9_6
libidn2 2.3.0-7.el9
libksba 1.5.1-7.el9
libmaxminddb 1.5.2-4.el9
libmnl 1.0.4-16.el9_4
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9
libnghttp2 1.43.0-6.el9
libpipeline 1.5.3-4.el9
libpwquality 1.4.4-8.el9
librepo 1.14.5-2.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libseccomp 2.5.2-2.el9
libselinux 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-2.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9
libsolv 0.7.24-3.el9
libstdc++ 11.5.0-5.el9_5
libtasn1 4.16.0-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libuser 0.63-16.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9
libuv 1.42.0-2.el9_4
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-12.el9_6
libxslt 1.1.34-13.el9_6
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
lmdb-libs 0.9.29-3.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
man-db 2.9.3-7.el9
mpfr 4.1.0-7.el9
ncurses 6.2-10.20210508.el9_6.2
ncurses-base 6.2-10.20210508.el9_6.2
ncurses-libs 6.2-10.20210508.el9_6.2
nettle 3.10.1-1.el9
npth 1.6-8.el9
nss_wrapper-libs 1.1.13-1.el9
openldap 2.6.8-4.el9
openssl 3.2.2-6.el9_5.1
openssl-fips-provider 3.0.7-6.el9_5
openssl-fips-provider-so 3.0.7-6.el9_5
openssl-libs 3.2.2-6.el9_5.1
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pam 1.5.1-26.el9_6
passwd 0.80-12.el9
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
perl-AutoLoader 5.74-481.1.el9_6
perl-B 1.80-481.1.el9_6
perl-Carp 1.50-460.el9
perl-Class-Struct 0.66-481.1.el9_6
perl-Data-Dumper 2.174-462.el9
perl-Digest 1.19-4.el9
perl-Digest-MD5 2.58-4.el9
perl-Encode 3.08-462.el9
perl-Errno 1.30-481.1.el9_6
perl-Exporter 5.74-461.el9
perl-Fcntl 1.13-481.1.el9_6
perl-File-Basename 2.85-481.1.el9_6
perl-File-Path 2.18-4.el9
perl-File-Temp 0.231.100-4.el9
perl-File-stat 1.09-481.1.el9_6
perl-FileHandle 2.03-481.1.el9_6
perl-Getopt-Long 2.52-4.el9
perl-Getopt-Std 1.12-481.1.el9_6
perl-HTTP-Tiny 0.076-462.el9
perl-IO 1.43-481.1.el9_6
perl-IO-Socket-IP 0.41-5.el9
perl-IO-Socket-SSL 2.073-2.el9
perl-IPC-Open3 1.21-481.1.el9_6
perl-MIME-Base64 3.16-4.el9
perl-Mozilla-CA 20200520-6.el9
perl-NDBM_File 1.15-481.1.el9_6
perl-Net-SSLeay 1.94-1.el9
perl-POSIX 1.94-481.1.el9_6
perl-PathTools 3.78-461.el9
perl-Pod-Escapes 1.07-460.el9
perl-Pod-Perldoc 3.28.01-461.el9
perl-Pod-Simple 3.42-4.el9
perl-Pod-Usage 2.01-4.el9
perl-Scalar-List-Utils 1.56-462.el9
perl-SelectSaver 1.02-481.1.el9_6
perl-Socket 2.031-4.el9
perl-Storable 3.21-460.el9
perl-Symbol 1.08-481.1.el9_6
perl-Term-ANSIColor 5.01-461.el9
perl-Term-Cap 1.17-460.el9
perl-Text-ParseWords 3.30-460.el9
perl-Text-Tabs+Wrap 2013.0523-460.el9
perl-Time-Local 1.300-7.el9
perl-URI 5.09-3.el9
perl-base 2.27-481.1.el9_6
perl-constant 1.33-461.el9
perl-if 0.60.800-481.1.el9_6
perl-interpreter 5.32.1-481.1.el9_6
perl-libnet 3.13-4.el9
perl-libs 5.32.1-481.1.el9_6
perl-mro 1.23-481.1.el9_6
perl-overload 1.31-481.1.el9_6
perl-overloading 0.02-481.1.el9_6
perl-parent 0.238-460.el9
perl-podlators 4.14-460.el9
perl-subs 1.03-481.1.el9_6
perl-vars 1.05-481.1.el9_6
pgaudit 1.7.0-1.module+el9.2.0+17405+aeb9ec60
popt 1.18-8.el9
postgresql 15.14-1.module+el9.6.0+23419+7863ab62
postgresql-contrib 15.14-1.module+el9.6.0+23419+7863ab62
postgresql-private-libs 15.14-1.module+el9.6.0+23419+7863ab62
postgresql-server 15.14-1.module+el9.6.0+23419+7863ab62
postgresql-upgrade 15.14-1.module+el9.6.0+23419+7863ab62
procps-ng 3.3.17-14.el9
protobuf-c 1.3.3-13.el9
psmisc 23.4-3.el9
python3 3.9.21-2.el9_6.2
python3-chardet 4.0.0-5.el9
python3-cloud-what 1.29.45.1-1.el9_6
python3-dateutil 2.8.1-7.el9
python3-dbus 1.2.18-2.el9
python3-decorator 4.4.2-6.el9
python3-dnf 4.14.0-25.el9
python3-dnf-plugins-core 4.3.0-20.el9
python3-gobject-base 3.40.1-6.el9
python3-gobject-base-noarch 3.40.1-6.el9
python3-gpg 1.15.1-6.el9
python3-hawkey 0.69.0-13.el9
python3-idna 2.10-7.el9_4.1
python3-iniparse 0.4-45.el9
python3-inotify 0.9.6-25.el9
python3-libcomps 0.1.18-1.el9
python3-libdnf 0.69.0-13.el9
python3-librepo 1.14.5-2.el9
python3-libs 3.9.21-2.el9_6.2
python3-pip-wheel 21.3.1-1.el9
python3-pysocks 1.7.1-12.el9
python3-requests 2.25.1-10.el9_6
python3-rpm 4.16.1.3-37.el9
python3-setuptools 53.0.0-13.el9_6.1
python3-setuptools-wheel 53.0.0-13.el9_6.1
python3-six 1.15.0-9.el9
python3-subscription-manager-rhsm 1.29.45.1-1.el9_6
python3-systemd 234-19.el9
python3-urllib3 1.26.5-6.el9
readline 8.1-4.el9
redhat-release 9.6-0.1.el9
rootfiles 8.1-34.el9
rpm 4.16.1.3-37.el9
rpm-build-libs 4.16.1.3-37.el9
rpm-libs 4.16.1.3-37.el9
rpm-sign-libs 4.16.1.3-37.el9
rsync 3.2.5-3.el9
scl-utils 2.0.3-4.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-12.el9
sqlite-libs 3.34.1-8.el9_6
subscription-manager 1.29.45.1-1.el9_6
subscription-manager-rhsm-certificates 20220623-1.el9
systemd 252-51.el9_6.2
systemd-libs 252-51.el9_6.2
systemd-pam 252-51.el9_6.2
systemd-rpm-macros 252-51.el9_6.2
tar 1.34-7.el9
tcl 8.6.10-7.el9
tpm2-tss 3.2.3-1.el9
tzdata 2025b-1.el9
unzip 6.0-58.el9_5
usermode 1.114-6.el9
util-linux 2.37.4-21.el9
util-linux-core 2.37.4-21.el9
uuid 1.6.2-55.el9
vim-filesystem 8.2.2637-22.el9_6
vim-minimal 8.2.2637-22.el9_6
virt-what 1.27-1.el9
which 2.21-30.el9_6
xz 5.2.5-8.el9_0
xz-libs 5.2.5-8.el9_0
yum 4.14.0-25.el9
zlib 1.2.11-40.el9
```

</details>

<details><summary>Python packages: /usr (python3.9) (18)</summary>

```text
chardet 4.0.0
dbus-python 1.2.18
decorator 4.4.2
gpg 1.15.1
idna 2.10
iniparse 0.4
libcomps 0.1.18
PyGObject 3.40.1
pyinotify 0.9.6
PySocks 1.7.1
python-dateutil 2.8.1
requests 2.25.1
rpm 4.16.1.3
setuptools 53.0.0
six 1.15.0
subscription-manager 1.29.45.1
systemd-python 234
urllib3 1.26.5
```

</details>

[Back to top](#contents)

### redis-6

| Field | Value |
|---|---|
| Image | `registry.redhat.io/rhel9/redis-6` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/redis-6.tar.gz` |
| Labels `version` / `release` | `1` / `1758530358` |
| Image ID | `sha256:66c15d0ce52bba473498fc69142ab3c61bd2f6354c7d9f4805a002f735954ed0` |
| Build date | 2025-09-22T08:39:40Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.6 (Plow) |
| Python | 3.9 |
| Ansible Core | N/A |

<details><summary>RPM packages (210)</summary>

```text
acl 2.3.1-4.el9
alternatives 1.24-2.el9
attr 2.5.1-3.el9
audit-libs 3.1.5-4.el9
basesystem 11-13.el9
bash 5.1.8-9.el9
bsdtar 3.5.3-6.el9_6
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crypto-policies 20250128-1.git5269e22.el9
crypto-policies-scripts 20250128-1.git5269e22.el9
curl-minimal 7.76.1-31.el9_6.1
cyrus-sasl-lib 2.1.27-21.el9
dbus 1.12.20-8.el9
dbus-broker 28-7.el9
dbus-common 1.12.20-8.el9
dbus-libs 1.12.20-8.el9
dejavu-sans-fonts 2.37-18.el9
diffutils 3.7-12.el9
dmidecode 3.6-1.el9
dnf 4.14.0-25.el9
dnf-data 4.14.0-25.el9
elfutils-default-yama-scope 0.192-6.el9_6
elfutils-libelf 0.192-6.el9_6
elfutils-libs 0.192-6.el9_6
environment-modules 5.3.0-1.el9
expat 2.5.0-5.el9_6
file-libs 5.39-16.el9
filesystem 3.16-5.el9
findutils 4.8.0-7.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdb-gdbserver 14.2-4.1.el9_6
gdbm-libs 1.23-1.el9
gettext 0.21-8.el9
gettext-libs 0.21-8.el9
glib2 2.68.4-16.el9_6.2
glibc 2.34-168.el9_6.23
glibc-common 2.34-168.el9_6.23
glibc-langpack-en 2.34-168.el9_6.23
glibc-locale-source 2.34-168.el9_6.23
glibc-minimal-langpack 2.34-168.el9_6.23
gmp 6.2.0-13.el9
gnupg2 2.3.3-4.el9
gnutls 3.8.3-6.el9_6.2
gobject-introspection 1.68.0-11.el9
gpg-pubkey 5a6340b3-6229229e
gpg-pubkey fd431d51-4ae0493b
gpgme 1.15.1-6.el9
grep 3.6-5.el9
groff-base 1.22.4-10.el9
gzip 1.12-1.el9
ima-evm-utils 1.5-3.el9
iproute 6.11.0-1.el9
json-c 0.14-11.el9
json-glib 1.6.6-1.el9
keyutils 1.6.3-1.el9
keyutils-libs 1.6.3-1.el9
kmod-libs 28-10.el9
krb5-libs 1.21.1-8.el9_6
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
less 590-5.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-6.el9_6
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9
libbpf 1.5.0-1.el9
libcap 2.48-9.el9_2
libcap-ng 0.8.2-7.el9
libcom_err 1.46.5-7.el9
libcomps 0.1.18-1.el9
libcurl-minimal 7.76.1-31.el9_6.1
libdb 5.3.28-57.el9_6
libdnf 0.69.0-13.el9
libdnf-plugin-subscription-manager 1.29.45.1-1.el9_6
libeconf 0.4.1-4.el9
libevent 2.1.12-8.el9_4
libfdisk 2.37.4-21.el9
libffi 3.4.2-8.el9
libgcc 11.5.0-5.el9_5
libgcrypt 1.10.0-11.el9
libgomp 11.5.0-5.el9_5
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libksba 1.5.1-7.el9
libmnl 1.0.4-16.el9_4
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9
libnghttp2 1.43.0-6.el9
libpipeline 1.5.3-4.el9
libpwquality 1.4.4-8.el9
librepo 1.14.5-2.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libseccomp 2.5.2-2.el9
libselinux 3.6-3.el9
libselinux-utils 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-2.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9
libsolv 0.7.24-3.el9
libstdc++ 11.5.0-5.el9_5
libtasn1 4.16.0-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libuser 0.63-16.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-12.el9_6
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
logrotate 3.18.0-9.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
man-db 2.9.3-7.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-10.20210508.el9_6.2
ncurses-libs 6.2-10.20210508.el9_6.2
nettle 3.10.1-1.el9
npth 1.6-8.el9
openldap 2.6.8-4.el9
openssl 3.2.2-6.el9_5.1
openssl-fips-provider 3.0.7-6.el9_5
openssl-fips-provider-so 3.0.7-6.el9_5
openssl-libs 3.2.2-6.el9_5.1
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pam 1.5.1-26.el9_6
passwd 0.80-12.el9
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
policycoreutils 3.6-2.1.el9
popt 1.18-8.el9
procps-ng 3.3.17-14.el9
psmisc 23.4-3.el9
python3 3.9.21-2.el9_6.2
python3-chardet 4.0.0-5.el9
python3-cloud-what 1.29.45.1-1.el9_6
python3-dateutil 2.8.1-7.el9
python3-dbus 1.2.18-2.el9
python3-decorator 4.4.2-6.el9
python3-dnf 4.14.0-25.el9
python3-dnf-plugins-core 4.3.0-20.el9
python3-gobject-base 3.40.1-6.el9
python3-gobject-base-noarch 3.40.1-6.el9
python3-gpg 1.15.1-6.el9
python3-hawkey 0.69.0-13.el9
python3-idna 2.10-7.el9_4.1
python3-iniparse 0.4-45.el9
python3-inotify 0.9.6-25.el9
python3-libcomps 0.1.18-1.el9
python3-libdnf 0.69.0-13.el9
python3-librepo 1.14.5-2.el9
python3-libs 3.9.21-2.el9_6.2
python3-pip-wheel 21.3.1-1.el9
python3-pysocks 1.7.1-12.el9
python3-requests 2.25.1-10.el9_6
python3-rpm 4.16.1.3-37.el9
python3-setuptools 53.0.0-13.el9_6.1
python3-setuptools-wheel 53.0.0-13.el9_6.1
python3-six 1.15.0-9.el9
python3-subscription-manager-rhsm 1.29.45.1-1.el9_6
python3-systemd 234-19.el9
python3-urllib3 1.26.5-6.el9
readline 8.1-4.el9
redhat-release 9.6-0.1.el9
redis 6.2.19-1.el9_6
rootfiles 8.1-34.el9
rpm 4.16.1.3-37.el9
rpm-build-libs 4.16.1.3-37.el9
rpm-libs 4.16.1.3-37.el9
rpm-sign-libs 4.16.1.3-37.el9
rsync 3.2.5-3.el9
scl-utils 2.0.3-4.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-12.el9
sqlite-libs 3.34.1-8.el9_6
subscription-manager 1.29.45.1-1.el9_6
subscription-manager-rhsm-certificates 20220623-1.el9
systemd 252-51.el9_6.2
systemd-libs 252-51.el9_6.2
systemd-pam 252-51.el9_6.2
systemd-rpm-macros 252-51.el9_6.2
tar 1.34-7.el9
tcl 8.6.10-7.el9
tpm2-tss 3.2.3-1.el9
tzdata 2025b-1.el9
unzip 6.0-58.el9_5
usermode 1.114-6.el9
util-linux 2.37.4-21.el9
util-linux-core 2.37.4-21.el9
vim-filesystem 8.2.2637-22.el9_6
vim-minimal 8.2.2637-22.el9_6
virt-what 1.27-1.el9
which 2.21-30.el9_6
xz 5.2.5-8.el9_0
xz-libs 5.2.5-8.el9_0
yum 4.14.0-25.el9
zlib 1.2.11-40.el9
```

</details>

<details><summary>Python packages: /usr (python3.9) (18)</summary>

```text
chardet 4.0.0
dbus-python 1.2.18
decorator 4.4.2
gpg 1.15.1
idna 2.10
iniparse 0.4
libcomps 0.1.18
PyGObject 3.40.1
pyinotify 0.9.6
PySocks 1.7.1
python-dateutil 2.8.1
requests 2.25.1
rpm 4.16.1.3
setuptools 53.0.0
six 1.15.0
subscription-manager 1.29.45.1
systemd-python 234
urllib3 1.26.5
```

</details>

[Back to top](#contents)

## Installer Collections

Collections shipped with the installer itself (`collections/ansible_collections`).

- `ansible.posix 1.5.4`
- `community.crypto 2.26.5`
- `community.postgresql 3.4.0`
- `containers.podman 1.17.0`
- `infra.ah_configuration 2.0.6`
- `infra.controller_configuration 2.9.0`

## Bundled Collections

Collection tarballs under `bundle/collections/` (uploaded to Automation Hub during install).

<details><summary>Bundled collections (90)</summary>

```text
amazon.aws 9.5.1 (certified)
ansible.controller 4.7.1 (certified)
ansible.eda 2.10.0 (certified)
ansible.hub 1.0.1 (certified)
ansible.netcommon 8.1.0 (certified)
ansible.network 5.0.0 (certified)
ansible.platform 2.6.20250924 (certified)
ansible.posix 2.1.0 (certified)
ansible.scm 3.0.0 (certified)
ansible.security 5.0.0 (certified)
ansible.snmp 3.0.0 (certified)
ansible.utils 6.0.0 (certified)
ansible.windows 3.2.0 (certified)
ansible.yang 3.0.0 (certified)
arista.eos 12.0.0 (certified)
azure.azcollection 3.7.0 (certified)
cisco.cvd_compute 1.1.0 (validated)
cisco.intersight 2.2.0 (certified)
cisco.ios 11.0.0 (certified)
cisco.iosxr 12.0.0 (certified)
cisco.nxos 11.0.0 (certified)
cloud.aws_ops 3.0.0 (validated)
cloud.aws_troubleshooting 4.0.0 (validated)
cloud.azure_ops 6.0.0 (validated)
cloud.common 5.0.0 (certified)
cloud.gcp_ops 2.0.0 (validated)
cloud.terraform 4.0.0 (certified)
cloud.terraform_ops 1.0.0 (validated)
cloud.vmware_ops 1.9.0 (validated)
edge.microshift 1.0.3 (validated)
f5networks.f5_eda_security 1.0.1 (validated)
google.cloud 1.7.0 (certified)
infra.aap_configuration 3.5.1 (validated)
infra.aap_configuration_extended 2.0.0 (validated)
infra.aap_utilities 2.8.0 (validated)
infra.ah_configuration 2.1.0 (validated)
infra.ai 1.2.0 (validated)
infra.ansible_rekey_variables 1.1.4 (validated)
infra.controller_configuration 3.1.2 (validated)
infra.convert2rhel 1.2.1 (validated)
infra.eda_configuration 1.1.0 (validated)
infra.ee_utilities 4.0.4 (validated)
infra.leapp 1.6.1 (validated)
infra.lvm_snapshots 2.1.3 (validated)
infra.middleware_ocpv 1.0.0 (validated)
infra.openshift_virtualization_migration 1.21.1 (validated)
infra.openshift_virtualization_ops 1.0.1 (validated)
infra.osbuild 2.3.0 (validated)
junipernetworks.junos 11.0.0 (certified)
kubernetes.core 6.1.0 (certified)
microsoft.ad 1.9.2 (certified)
microsoft.iis 1.0.3 (certified)
network.acls 4.0.0 (validated)
network.backup 3.0.0 (validated)
network.base 8.0.0 (validated)
network.bgp 8.0.0 (validated)
network.healthchecks 2.0.0 (validated)
network.interfaces 7.0.0 (validated)
network.inventory_reports 2.0.0 (validated)
network.meraki_ops 1.0.0 (validated)
network.offline_migration_sdn_to_ovnk 1.0.3 (validated)
network.ospf 7.0.0 (validated)
network.telemetry 3.0.0 (validated)
network.vpn 6.0.0 (validated)
redhat.amq_broker 2.3.4 (certified)
redhat.amq_streams 1.0.0 (certified)
redhat.data_grid 1.3.3 (certified)
redhat.eap 1.5.7 (certified)
redhat.insights 1.3.0 (certified)
redhat.insights_eda 1.2.0 (certified)
redhat.jbcs 1.1.2 (certified)
redhat.jws 2.1.1 (certified)
redhat.openshift 5.0.0 (certified)
redhat.openshift_virtualization 2.2.3 (certified)
redhat.redhat_csp_download 1.2.2 (certified)
redhat.rhbk 3.0.1 (certified)
redhat.rhel_idm 1.15.1 (certified)
redhat.rhel_system_roles 1.95.7 (certified)
redhat.rhv 2.4.2 (certified)
redhat.runtimes_common 1.2.2 (certified)
redhat.sap_install 1.7.1 (certified)
redhat.satellite 5.5.0 (certified)
redhat.satellite_operations 3.0.0 (certified)
redhat.sso 2.0.0 (certified)
sap.sap_operations 2.2.0 (certified)
servicenow.itsm 2.11.0 (certified)
splunk.es 4.0.0 (certified)
trendmicro.deepsec 4.0.0 (certified)
vmware.vmware 2.3.0 (certified)
vmware.vmware_rest 4.8.1 (certified)
```

</details>
