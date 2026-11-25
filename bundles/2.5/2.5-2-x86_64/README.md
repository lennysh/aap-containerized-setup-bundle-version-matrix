[All AAP versions](../../../README.md) / [AAP 2.5](../README.md) / 2.5-2

# AAP Containerized Setup Bundle 2.5-2 (x86_64)

- **Bundle file:** `ansible-automation-platform-containerized-setup-bundle-2.5-2-x86_64.tar.gz`
- **AAP version:** 2.5
- **Bundle created:** 2024-10-07 19:08:24 UTC
- **Container images:** 14
- **Distinct RPM package versions:** 657
- **Distinct Python package versions:** 520

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
  - [controller-rhel8](#controller-rhel8)
  - [de-supported-rhel8](#de-supported-rhel8)
  - [eda-controller-rhel8](#eda-controller-rhel8)
  - [eda-controller-ui-rhel8](#eda-controller-ui-rhel8)
  - [ee-minimal-rhel8](#ee-minimal-rhel8)
  - [ee-supported-rhel8](#ee-supported-rhel8)
  - [gateway-proxy-rhel8](#gateway-proxy-rhel8)
  - [gateway-rhel8](#gateway-rhel8)
  - [hub-rhel8](#hub-rhel8)
  - [hub-web-rhel8](#hub-web-rhel8)
  - [receptor-rhel8](#receptor-rhel8)
  - [pcp](#pcp)
  - [postgresql-15](#postgresql-15)
  - [redis-6](#redis-6)
- [Installer Collections](#installer-collections)
- [Bundled Collections](#bundled-collections)

## Container Images

| Image | Tag in Bundle | Version | Release | Image ID | RHEL Version | Python | Ansible Core | RPMs | Python Pkgs | Collections |
|---|---|---|---|---|---|---|---|--:|--:|--:|
| [registry.redhat.io/ansible-automation-platform-25/controller-rhel8](#controller-rhel8) | `latest` | 4.6.1 | 3 | `3d0cb3204030` | Red Hat Enterprise Linux 8.10 (Ootpa) | 3.11 | N/A | 256 | 215 | 0 |
| [registry.redhat.io/ansible-automation-platform-25/de-supported-rhel8](#de-supported-rhel8) | `latest` | 1.1.1 | 16 | `a9c8cec645c0` | Red Hat Enterprise Linux 8.10 (Ootpa) | 3.11 | 2.16.11 | 215 | 61 | 2 |
| [registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8](#eda-controller-rhel8) | `latest` | 1.1.1 | 2 | `1f5b20f9596d` | Red Hat Enterprise Linux 8.10 (Ootpa) | 3.11 | 2.16.11 | 262 | 91 | 0 |
| [registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8](#eda-controller-ui-rhel8) | `latest` | 1.1.1 | 2 | `04ae1753b4d7` | Red Hat Enterprise Linux 8.10 (Ootpa) | N/A | N/A | 277 | 22 | 0 |
| [registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8](#ee-minimal-rhel8) | `latest` | 1.0.0 | 747 | `a64b9fc48094` | Red Hat Enterprise Linux 8.10 (Ootpa) | 3.11 | 2.16.11 | 191 | 65 | 0 |
| [registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8](#ee-supported-rhel8) | `latest` | 1.0.0 | 812 | `59d1bc680a7c` | Red Hat Enterprise Linux 8.10 (Ootpa) | 3.11 | 2.16.11 | 295 | 247 | 57 |
| [registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8](#gateway-proxy-rhel8) | `latest` | 2.5.0 | 22 | `6e53887286a7` | Red Hat Enterprise Linux 8.10 (Ootpa) | N/A | N/A | 162 | 9 | 0 |
| [registry.redhat.io/ansible-automation-platform-25/gateway-rhel8](#gateway-rhel8) | `latest` | 2.5.0 | 58 | `f768a98a64be` | Red Hat Enterprise Linux 8.10 (Ootpa) | 3.11 | N/A | 248 | 75 | 0 |
| [registry.redhat.io/ansible-automation-platform-25/hub-rhel8](#hub-rhel8) | `latest` | 4.10.0 | 207 | `b9a82993ab1c` | Red Hat Enterprise Linux 8.10 (Ootpa) | 3.11 | 2.16.11 | 362 | 172 | 0 |
| [registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8](#hub-web-rhel8) | `latest` | 4.10.0 | 196 | `741a253ea19e` | Red Hat Enterprise Linux 8.10 (Ootpa) | N/A | N/A | 277 | 22 | 0 |
| [registry.redhat.io/ansible-automation-platform-25/receptor-rhel8](#receptor-rhel8) | `latest` | 1.4.8 | 34 | `ae9c0820d61d` | Red Hat Enterprise Linux 8.10 (Ootpa) | 3.11 | N/A | 172 | 20 | 0 |
| [registry.redhat.io/rhel8/pcp](#pcp) | `latest` | 5 | 233.1727149332 | `3d7083e69527` | Red Hat Enterprise Linux 8.10 (Ootpa) | 3.6 | N/A | 215 | 22 | 0 |
| [registry.redhat.io/rhel8/postgresql-15](#postgresql-15) | `latest` | 1 | 82 | `2392b56e6b5e` | Red Hat Enterprise Linux 8.10 (Ootpa) | N/A | N/A | 280 | 22 | 0 |
| [registry.redhat.io/rhel8/redis-6](#redis-6) | `latest` | 1 | 204 | `c99cedb5e4c1` | Red Hat Enterprise Linux 8.10 (Ootpa) | N/A | N/A | 208 | 20 | 0 |

## RPM Packages (all images)

Every RPM installed in any image of this bundle (`name version-release`). Search this table for a
package named in a CVE to see which containers ship which version.

| Package | Version-Release | Images |
|---|---|---|
| `aap-metrics-utility` | `0.3.0-2.el8ap` | controller-rhel8 |
| `acl` | `2.2.53-3.el8` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `alsa-lib` | `1.2.10-2.el8` | de-supported-rhel8 |
| `ansible-automation-platform-common` | `2.5-2.el8ap` | controller-rhel8, eda-controller-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8 |
| `ansible-automation-platform-selinux` | `0.2-3.el8ap` | controller-rhel8, eda-controller-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8 |
| `ansible-builder` | `3.1.0-1.el8ap` | hub-rhel8 |
| `ansible-core` | `2.16.11-1.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `ansible-lint` | `24.9.0-1.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `ansible-rulebook` | `1.1.1-1.el8ap` | de-supported-rhel8 |
| `ansible-runner` | `2.4.0-1.el8ap` | de-supported-rhel8, ee-minimal-rhel8, ee-supported-rhel8, receptor-rhel8 |
| `ansible-sign` | `0.1.1-2.el8ap` | ee-supported-rhel8 |
| `ansible-test` | `2.16.11-1.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `apr` | `1.6.3-12.el8` | controller-rhel8, ee-supported-rhel8 |
| `apr-util` | `1.6.1-9.el8` | controller-rhel8, ee-supported-rhel8 |
| `audit-libs` | `3.1.2-1.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `automation-controller` | `4.6.1-1.el8ap` | controller-rhel8 |
| `automation-controller-cli` | `4.6.1-1.el8ap` | ee-supported-rhel8 |
| `automation-controller-server` | `4.6.1-1.el8ap` | controller-rhel8 |
| `automation-controller-ui` | `4.6.1-1.el8ap` | controller-rhel8 |
| `automation-controller-venv-tower` | `4.6.1-1.el8ap` | controller-rhel8 |
| `automation-eda-controller` | `1.1.1-1.el8ap` | eda-controller-rhel8 |
| `automation-gateway-config` | `2.5.0-1.1.el8ap` | gateway-proxy-rhel8 |
| `automation-gateway-proxy-server` | `2.5.0-1.el8ap` | gateway-proxy-rhel8 |
| `automation-gateway-server` | `2.5.0-1.1.el8ap` | gateway-rhel8 |
| `automation-hub` | `4.10.0-1.el8ap` | hub-rhel8 |
| `avahi-libs` | `0.7-27.el8_10.1` | de-supported-rhel8, pcp |
| `basesystem` | `11-5.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `bash` | `4.4.20-5.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `bash-completion` | `2.7-5.el8` | ee-supported-rhel8 |
| `bind-libs` | `9.11.36-16.el8_10.2` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `bind-libs-lite` | `9.11.36-16.el8_10.2` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `bind-license` | `9.11.36-16.el8_10.2` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `bind-utils` | `9.11.36-16.el8_10.2` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `bindep` | `2.11.0-2.el8ap` | hub-rhel8 |
| `brotli` | `1.0.6-3.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `bsdtar` | `3.3.3-5.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15, redis-6 |
| `bzip2` | `1.0.6-26.el8` | ee-minimal-rhel8, ee-supported-rhel8 |
| `bzip2-libs` | `1.0.6-26.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `ca-certificates` | `2024.2.69_v8.0.303-80.0.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `checkpolicy` | `2.9-1.el8` | controller-rhel8, eda-controller-rhel8, gateway-proxy-rhel8, gateway-rhel8 |
| `chkconfig` | `1.19.2-1.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `cmake` | `3.26.5-2.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `cmake-data` | `3.26.5-2.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `cmake-filesystem` | `3.26.5-2.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `cmake-rpm-macros` | `3.26.5-2.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `container-selinux` | `2.229.0-2.module+el8.10.0+22283+6d6d094a` | hub-rhel8 |
| `containers-common` | `1-82.module+el8.10.0+22283+6d6d094a` | hub-rhel8 |
| `copy-jdk-configs` | `4.0-2.el8` | de-supported-rhel8 |
| `coreutils-single` | `8.30-15.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `cracklib` | `2.9.6-15.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `cracklib-dicts` | `2.9.6-15.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `criu` | `3.18-5.module+el8.10.0+22283+6d6d094a` | hub-rhel8 |
| `crontabs` | `1.11-17.20190603git.el8` | controller-rhel8 |
| `crun` | `1.14.3-2.module+el8.10.0+22283+6d6d094a` | controller-rhel8 |
| `crypto-policies` | `20230731-1.git3177e06.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `crypto-policies-scripts` | `20230731-1.git3177e06.el8` | de-supported-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `cryptsetup-libs` | `2.3.7-7.el8` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `cups-libs` | `2.2.6-60.el8_10` | de-supported-rhel8 |
| `curl` | `7.61.1-34.el8_10.2` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `cyrus-sasl-lib` | `2.1.27-6.el8_5` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `dbus` | `1.12.8-26.el8` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `dbus-common` | `1.12.8-26.el8` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `dbus-daemon` | `1.12.8-26.el8` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `dbus-glib` | `0.110-2.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `dbus-libs` | `1.12.8-26.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `dbus-tools` | `1.12.8-26.el8` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `device-mapper` | `1.02.181-14.el8` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `device-mapper-libs` | `1.02.181-14.el8` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `diffutils` | `3.6-6.el8` | controller-rhel8, eda-controller-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, receptor-rhel8, pcp, redis-6 |
| `dmidecode` | `3.5-1.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `dnf` | `4.7.0-20.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `dnf-data` | `4.7.0-20.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `dnf-plugin-subscription-manager` | `1.28.42-1.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `dumb-init` | `1.2.5-3.el8ap` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, receptor-rhel8 |
| `elfutils-default-yama-scope` | `0.190-2.el8` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `elfutils-libelf` | `0.190-2.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `elfutils-libs` | `0.190-2.el8` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `emacs-filesystem` | `26.1-12.el8_10` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `environment-modules` | `4.5.2-4.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15, redis-6 |
| `expat` | `2.2.5-15.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `file-libs` | `5.33-26.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `filesystem` | `3.8-6.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `findutils` | `4.6.0-23.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `fstrm` | `0.6.1-3.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `gawk` | `4.2.1-4.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `gdb-gdbserver` | `8.2-20.el8` | eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `gdbm` | `1.18-2.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `gdbm-libs` | `1.18-2.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `geolite2-city` | `20180605-1.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `geolite2-country` | `20180605-1.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `gettext` | `0.19.8.1-17.el8` | eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `gettext-libs` | `0.19.8.1-17.el8` | eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `git-core` | `2.43.5-1.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `git-lfs` | `3.4.1-3.el8_10` | controller-rhel8, ee-supported-rhel8 |
| `glib2` | `2.56.4-162.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `glibc` | `2.28-251.el8_10.5` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `glibc-common` | `2.28-251.el8_10.5` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `glibc-langpack-en` | `2.28-251.el8_10.5` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-web-rhel8, postgresql-15, redis-6 |
| `glibc-locale-source` | `2.28-251.el8_10.5` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15, redis-6 |
| `glibc-minimal-langpack` | `2.28-251.el8_10.5` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `gmp` | `6.1.2-11.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `gnupg2` | `2.2.20-3.el8_6` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `gnutls` | `3.6.16-8.el8_9.3` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `gobject-introspection` | `1.56.1-1.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `gpg-pubkey` | `d4082792-5b32db75` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `gpg-pubkey` | `fd431d51-4ae0493b` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `gpgme` | `1.13.1-12.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `grep` | `3.1-6.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `groff-base` | `1.22.3-18.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15, redis-6 |
| `gzip` | `1.9-13.el8_5` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `hostname` | `3.20-6.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp |
| `ima-evm-utils` | `1.3.2-12.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `info` | `6.5-7.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `java-17-openjdk-headless` | `17.0.12.0.7-2.el8` | de-supported-rhel8 |
| `javapackages-filesystem` | `5.3.0-2.module+el8+2598+06babf2e` | de-supported-rhel8 |
| `jq` | `1.6-9.el8_10` | hub-rhel8 |
| `json-c` | `0.13.1-3.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `json-glib` | `1.4.4-1.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `keyutils-libs` | `1.5.10-9.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `kmod-libs` | `25-20.el8` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `krb5-libs` | `1.18.2-29.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `krb5-workstation` | `1.18.2-29.el8_10` | controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8 |
| `langpacks-en` | `1.0-12.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `less` | `530-3.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8, hub-web-rhel8, postgresql-15, redis-6 |
| `libacl` | `2.2.53-3.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libaio` | `0.3.112-1.el8` | ee-supported-rhel8 |
| `libarchive` | `3.3.3-5.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libassuan` | `2.5.1-3.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libattr` | `2.4.48-3.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libblkid` | `2.32.1-46.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libcap` | `2.48-6.el8_9` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libcap-ng` | `0.7.11-1.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libcom_err` | `1.45.6-5.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libcomps` | `0.1.18-1.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `libcroco` | `0.6.12-4.el8_2.1` | eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `libcurl` | `7.61.1-34.el8_10.2` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libdb` | `5.3.28-42.el8_4` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libdb-utils` | `5.3.28-42.el8_4` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libdnf` | `0.63.0-20.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libedit` | `3.1-23.20170329cvs.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `libestr` | `0.1.10-3.el8` | controller-rhel8, hub-rhel8 |
| `libfastjson` | `0.99.9-2.el8` | controller-rhel8, hub-rhel8 |
| `libfdisk` | `2.32.1-46.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libffi` | `3.1-24.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libgcc` | `8.5.0-22.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libgcrypt` | `1.8.5-7.el8_6` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libgfortran` | `8.5.0-22.el8_10` | controller-rhel8 |
| `libgomp` | `8.5.0-22.el8_10` | eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `libgpg-error` | `1.31-1.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libicu` | `60.3-2.el8_1` | postgresql-15 |
| `libidn2` | `2.2.0-1.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libjpeg-turbo` | `1.5.3-12.el8` | hub-rhel8 |
| `libkadm5` | `1.18.2-29.el8_10` | controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8 |
| `libksba` | `1.3.5-9.el8_7` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libmaxminddb` | `1.2.0-10.el8_9.1` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `libmodulemd` | `2.13.0-1.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libmount` | `2.32.1-46.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libnet` | `1.1.6-15.el8` | hub-rhel8 |
| `libnghttp2` | `1.33.0-6.el8_10.1` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libnl3` | `3.7.0-1.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `libnsl2` | `1.2.0-2.20180605git4a062cf.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libpeas` | `1.22.0-6.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, receptor-rhel8 |
| `libpipeline` | `1.5.0-2.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15, redis-6 |
| `libpkgconf` | `1.4.2-1.el8` | eda-controller-ui-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `libpq` | `13.11-1.el8` | de-supported-rhel8, eda-controller-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `libpsl` | `0.20.2-6.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libpwquality` | `1.4.4-6.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libquadmath` | `8.5.0-22.el8_10` | controller-rhel8 |
| `librepo` | `1.14.2-5.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libreport-filesystem` | `2.9.5-15.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `librhsm` | `0.0.3-5.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libseccomp` | `2.5.2-1.el8` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libsecret` | `0.18.6-1.el8` | hub-rhel8 |
| `libselinux` | `2.9-8.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libselinux-utils` | `2.9-8.el8` | controller-rhel8, eda-controller-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, receptor-rhel8, redis-6 |
| `libsemanage` | `2.9-9.el8` | postgresql-15, redis-6 |
| `libsemanage` | `2.9-9.el8_6` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp |
| `libsepol` | `2.9-3.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libserf` | `1.3.9-9.module+el8.3.0+6671+2675c974` | controller-rhel8, ee-supported-rhel8 |
| `libsigsegv` | `2.11-5.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libsmartcols` | `2.32.1-46.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libsolv` | `0.7.20-6.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libss` | `1.45.6-5.el8` | controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8 |
| `libssh` | `0.9.6-14.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libssh-config` | `0.9.6-14.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libstdc++` | `8.5.0-22.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libtasn1` | `4.13-4.el8_7` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libtirpc` | `1.1.4-12.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libtool-ltdl` | `2.4.6-25.el8` | controller-rhel8, gateway-rhel8 |
| `libunistring` | `0.9.9-3.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libusbx` | `1.0.23-4.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libuser` | `0.62-26.el8_10` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `libutempter` | `1.1.6-14.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libuuid` | `2.32.1-46.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libuv` | `1.41.1-2.el8_10` | eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15 |
| `libverto` | `0.3.2-2.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libxcrypt` | `4.1.1-6.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libxml2` | `2.9.7-18.el8_10.1` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libxslt` | `1.1.32-6.el8` | controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, postgresql-15 |
| `libyaml` | `0.1.7-5.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libzstd` | `1.4.4-1.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `lksctp-tools` | `1.0.18-3.el8` | de-supported-rhel8 |
| `logrotate` | `3.14.0-6.el8` | controller-rhel8, ee-supported-rhel8, hub-rhel8, receptor-rhel8, redis-6 |
| `lua` | `5.3.4-12.el8` | de-supported-rhel8 |
| `lua-libs` | `5.3.4-12.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `lz4-libs` | `1.8.3-3.el8_4` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `mailcap` | `2.1.48-3.el8` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `make` | `4.2.1-11.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `man-db` | `2.7.6.1-18.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15, redis-6 |
| `microdnf` | `3.8.0-2.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, receptor-rhel8 |
| `mpdecimal` | `2.5.1-3.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, receptor-rhel8 |
| `mpfr` | `3.1.6-1.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `ncurses` | `6.1-10.20180224.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `ncurses-base` | `6.1-10.20180224.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `ncurses-libs` | `6.1-10.20180224.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `nettle` | `3.4.1-7.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `nginx` | `1.22.1-1.module+el8.8.0+20355+6d9c8a63.1` | controller-rhel8, eda-controller-ui-rhel8, gateway-rhel8, hub-web-rhel8 |
| `nginx-filesystem` | `1.22.1-1.module+el8.8.0+20355+6d9c8a63.1` | controller-rhel8, eda-controller-ui-rhel8, gateway-rhel8, hub-web-rhel8 |
| `nginx-mod-http-perl` | `1.22.1-1.module+el8.8.0+20355+6d9c8a63.1` | eda-controller-ui-rhel8, hub-web-rhel8 |
| `nginx-mod-stream` | `1.22.1-1.module+el8.8.0+20355+6d9c8a63.1` | eda-controller-ui-rhel8, hub-web-rhel8 |
| `npth` | `1.5-4.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `nspr` | `4.35.0-1.el8_8` | de-supported-rhel8, pcp |
| `nss` | `3.101.0-7.el8_8` | de-supported-rhel8, pcp |
| `nss-softokn` | `3.101.0-7.el8_8` | de-supported-rhel8, pcp |
| `nss-softokn-freebl` | `3.101.0-7.el8_8` | de-supported-rhel8, pcp |
| `nss-sysinit` | `3.101.0-7.el8_8` | de-supported-rhel8, pcp |
| `nss-util` | `3.101.0-7.el8_8` | de-supported-rhel8, pcp |
| `nss_wrapper` | `1.1.13-1.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `nss_wrapper-libs` | `1.1.13-1.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `oniguruma` | `6.9.7.1-2.el8ap` | hub-rhel8 |
| `openblas` | `0.3.15-6.el8` | controller-rhel8 |
| `openldap` | `2.4.46-19.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `openshift-clients` | `4.12.0-202404161006.p0.gd691257.assembly.stream.el8` | ee-supported-rhel8 |
| `openssh` | `8.0p1-25.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `openssh-clients` | `8.0p1-25.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `openssl` | `1.1.1k-12.el8_9` | controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, postgresql-15 |
| `openssl-libs` | `1.1.1k-12.el8_9` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `p11-kit` | `0.23.22-2.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `p11-kit-trust` | `0.23.22-2.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `pam` | `1.3.1-34.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `passwd` | `0.80-4.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `pcp` | `5.3.7-22.el8_10` | pcp |
| `pcp-conf` | `5.3.7-22.el8_10` | pcp |
| `pcp-doc` | `5.3.7-22.el8_10` | pcp |
| `pcp-libs` | `5.3.7-22.el8_10` | pcp |
| `pcp-pmda-dm` | `5.3.7-22.el8_10` | pcp |
| `pcp-pmda-nfsclient` | `5.3.7-22.el8_10` | pcp |
| `pcp-pmda-openmetrics` | `5.3.7-22.el8_10` | pcp |
| `pcp-system-tools` | `5.3.7-22.el8_10` | pcp |
| `pcp-zeroconf` | `5.3.7-22.el8_10` | pcp |
| `pcre` | `8.42-6.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `pcre2` | `10.32-3.el8_6` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `perl-Carp` | `1.42-396.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-constant` | `1.33-396.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Data-Dumper` | `2.167-399.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Digest` | `1.17-395.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Digest-MD5` | `2.55-396.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Encode` | `2.97-3.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Errno` | `1.28-422.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Exporter` | `5.72-396.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-File-Path` | `2.15-2.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-File-Temp` | `0.230.600-1.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Getopt-Long` | `2.50-4.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-HTTP-Tiny` | `0.074-3.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-interpreter` | `5.26.3-422.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-IO` | `1.38-422.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-IO-Socket-IP` | `0.39-5.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-IO-Socket-SSL` | `2.066-4.module+el8.3.0+6446+594cad75` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-libnet` | `3.11-3.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-libs` | `5.26.3-422.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-macros` | `5.26.3-422.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-MIME-Base64` | `3.15-396.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Mozilla-CA` | `20160104-7.module+el8.3.0+6498+9eecfe51` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Net-SSLeay` | `1.88-2.module+el8.6.0+13392+f0897f98` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-parent` | `0.237-1.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-PathTools` | `3.74-1.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Pod-Escapes` | `1.07-395.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Pod-Perldoc` | `3.28-396.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Pod-Simple` | `3.35-395.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Pod-Usage` | `1.69-395.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-podlators` | `4.11-1.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Scalar-List-Utils` | `1.49-2.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Socket` | `2.027-3.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Storable` | `3.11-3.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Term-ANSIColor` | `4.06-396.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Term-Cap` | `1.17-395.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Text-ParseWords` | `3.30-395.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Text-Tabs+Wrap` | `2013.0523-395.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-threads` | `2.21-2.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-threads-shared` | `1.58-2.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Time-Local` | `1.280-1.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Unicode-Normalize` | `1.25-396.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-URI` | `1.73-3.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `pgaudit` | `1.7.0-1.module+el8.9.0+19797+c4ce5969` | postgresql-15 |
| `pinentry` | `1.1.0-2.el8` | hub-rhel8 |
| `pkgconf` | `1.4.2-1.el8` | eda-controller-ui-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `pkgconf-m4` | `1.4.2-1.el8` | eda-controller-ui-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `pkgconf-pkg-config` | `1.4.2-1.el8` | eda-controller-ui-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `platform-python` | `3.6.8-67.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `platform-python-pip` | `9.0.3-24.el8` | pcp |
| `platform-python-setuptools` | `39.2.0-8.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `podman-remote` | `4.9.4-13.module+el8.10.0+22283+6d6d094a` | eda-controller-rhel8, ee-supported-rhel8, receptor-rhel8 |
| `policycoreutils` | `2.9-26.el8_10` | controller-rhel8, eda-controller-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, receptor-rhel8, redis-6 |
| `policycoreutils-python-utils` | `2.9-26.el8_10` | controller-rhel8, eda-controller-rhel8, gateway-proxy-rhel8, gateway-rhel8 |
| `popt` | `1.18-1.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `postgresql` | `15.8-1.module+el8.10.0+22212+a51fe170` | controller-rhel8, gateway-rhel8, postgresql-15 |
| `postgresql-contrib` | `15.8-1.module+el8.10.0+22212+a51fe170` | postgresql-15 |
| `postgresql-private-libs` | `15.8-1.module+el8.10.0+22212+a51fe170` | controller-rhel8, gateway-rhel8, postgresql-15 |
| `postgresql-server` | `15.8-1.module+el8.10.0+22212+a51fe170` | postgresql-15 |
| `postgresql-upgrade` | `15.8-1.module+el8.10.0+22212+a51fe170` | postgresql-15 |
| `procps-ng` | `3.3.15-14.el8` | eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `protobuf-c` | `1.3.0-8.el8` | eda-controller-ui-rhel8, hub-rhel8, hub-web-rhel8, postgresql-15 |
| `publicsuffix-list-dafsa` | `20180723-1.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `pulpcore-selinux` | `2.0.1-1.el8ap` | hub-rhel8 |
| `python3-audit` | `3.1.2-1.el8` | controller-rhel8, eda-controller-rhel8, gateway-proxy-rhel8, gateway-rhel8 |
| `python3-bind` | `9.11.36-16.el8_10.2` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `python3-cffi` | `1.11.5-6.el8` | controller-rhel8, eda-controller-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8 |
| `python3-chardet` | `3.0.4-7.el8` | controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `python3-cloud-what` | `1.28.42-1.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-cryptography` | `3.2.1-7.el8_9` | controller-rhel8, eda-controller-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8 |
| `python3-dateutil` | `2.6.1-6.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-dbus` | `1.2.4-15.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-decorator` | `4.2.1-2.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-dnf` | `4.7.0-20.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-dnf-plugins-core` | `4.0.21-25.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-ethtool` | `0.14-5.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-gobject-base` | `3.28.3-2.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-gpg` | `1.13.1-12.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-hawkey` | `0.63.0-20.el8_10` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-idna` | `2.5-7.el8_10` | controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `python3-iniparse` | `0.4-31.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-inotify` | `0.9.6-13.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-libcomps` | `0.1.18-1.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-libdnf` | `0.63.0-20.el8_10` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-librepo` | `1.14.2-5.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-libs` | `3.6.8-67.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `python3-libselinux` | `2.9-8.el8` | controller-rhel8, eda-controller-rhel8, gateway-proxy-rhel8, gateway-rhel8 |
| `python3-libsemanage` | `2.9-9.el8_6` | controller-rhel8, eda-controller-rhel8, gateway-proxy-rhel8, gateway-rhel8 |
| `python3-pcp` | `5.3.7-22.el8_10` | pcp |
| `python3-pip` | `9.0.3-24.el8` | pcp |
| `python3-pip-wheel` | `9.0.3-24.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `python3-ply` | `3.9-9.el8` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, postgresql-15 |
| `python3-policycoreutils` | `2.9-26.el8_10` | controller-rhel8, eda-controller-rhel8, gateway-proxy-rhel8, gateway-rhel8 |
| `python3-pycparser` | `2.14-14.el8` | controller-rhel8, eda-controller-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8 |
| `python3-pysocks` | `1.6.8-3.el8` | controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `python3-requests` | `2.20.0-3.el8_8` | controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `python3-rpm` | `4.14.3-31.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-setools` | `4.3.0-5.el8` | controller-rhel8, eda-controller-rhel8, gateway-proxy-rhel8, gateway-rhel8 |
| `python3-setuptools` | `39.2.0-8.el8_10` | controller-rhel8, ee-supported-rhel8, hub-rhel8, receptor-rhel8, pcp |
| `python3-setuptools-wheel` | `39.2.0-8.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `python3-six` | `1.11.0-8.el8` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `python3-subscription-manager-rhsm` | `1.28.42-1.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-syspurpose` | `1.28.42-1.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-systemd` | `234-8.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-urllib3` | `1.24.2-8.el8_10` | controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `python3.11` | `3.11.9-7.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, receptor-rhel8 |
| `python3.11-aiodns` | `3.1.1-1.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-aiofiles` | `23.2.1-1.el8ap` | hub-rhel8 |
| `python3.11-aiohttp` | `3.9.5-1.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-aiosignal` | `1.3.1-1.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-ansible-compat` | `24.9.0-1.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-ansible-pylibssh` | `1.2.2-1.el8ap` | ee-supported-rhel8 |
| `python3.11-ansible-runner` | `2.4.0-1.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, receptor-rhel8 |
| `python3.11-argon2-cffi` | `23.1.0-1.el8ap` | gateway-rhel8 |
| `python3.11-argon2-cffi-bindings` | `21.2.0-1.el8ap` | gateway-rhel8 |
| `python3.11-asgiref` | `3.7.2-1.el8ap` | eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-async-lru` | `2.0.4-1.el8ap` | hub-rhel8 |
| `python3.11-async-timeout` | `4.0.3-2.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-asyncio-throttle` | `1.0.2-4.el8ap` | hub-rhel8 |
| `python3.11-attrs` | `22.2.0-1.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-autobahn` | `23.6.2-2.el8ap` | eda-controller-rhel8 |
| `python3.11-Automat` | `22.10.0-3.el8ap` | eda-controller-rhel8 |
| `python3.11-azure-core` | `1.29.7-1.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-azure-storage-blob` | `12.19.0-1.el8ap` | hub-rhel8 |
| `python3.11-backoff` | `2.2.1-1.el8ap` | hub-rhel8 |
| `python3.11-black` | `24.4.2-2.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-boto3` | `1.34.30-1.el8ap` | ee-supported-rhel8, hub-rhel8 |
| `python3.11-botocore` | `1.34.30-1.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-bracex` | `2.4-1.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-brotli` | `1.1.0-1.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-cachetools` | `5.3.2-1.el8ap` | eda-controller-rhel8, ee-supported-rhel8 |
| `python3.11-certifi` | `2023.5.7-1.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-cffi` | `1.15.1-1.el8` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-channels` | `4.0.0-3.el8ap` | eda-controller-rhel8 |
| `python3.11-channels+daphne` | `4.0.0-3.el8ap` | eda-controller-rhel8 |
| `python3.11-chardet` | `5.2.0-2.el8ap` | ee-supported-rhel8 |
| `python3.11-charset-normalizer` | `2.1.0-1.el8` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-click` | `8.1.7-1.el8ap` | eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8, receptor-rhel8 |
| `python3.11-commonmark` | `0.9.1-6.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-constantly` | `15.1.0-2.el8ap` | eda-controller-rhel8 |
| `python3.11-croniter` | `2.0.1-1.el8ap` | eda-controller-rhel8 |
| `python3.11-cryptography` | `42.0.5-1.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-daemon` | `2.3.2-1.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, receptor-rhel8 |
| `python3.11-daphne` | `4.0.0-3.el8ap` | eda-controller-rhel8 |
| `python3.11-dateutil` | `2.8.2-2.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-supported-rhel8, hub-rhel8, receptor-rhel8 |
| `python3.11-defusedxml` | `0.7.1-4.el8ap` | gateway-rhel8, hub-rhel8 |
| `python3.11-deprecated` | `1.2.14-1.el8ap` | ee-supported-rhel8, hub-rhel8 |
| `python3.11-diff-match-patch` | `20230430-1.el8ap` | hub-rhel8 |
| `python3.11-distlib` | `0.3.8-1.el8ap` | ee-supported-rhel8 |
| `python3.11-distro` | `1.9.0-1.el8ap` | ee-supported-rhel8, hub-rhel8 |
| `python3.11-django` | `4.2.16-1.el8ap` | eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-django-ansible-base` | `2.5.1-1.el8ap` | eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-django-ansible-base+api_documentation` | `2.5.1-1.el8ap` | gateway-rhel8 |
| `python3.11-django-ansible-base+authentication` | `2.5.1-1.el8ap` | gateway-rhel8 |
| `python3.11-django-ansible-base+channel_auth` | `2.5.1-1.el8ap` | eda-controller-rhel8 |
| `python3.11-django-ansible-base+jwt_consumer` | `2.5.1-1.el8ap` | hub-rhel8 |
| `python3.11-django-ansible-base+oauth2_provider` | `2.5.1-1.el8ap` | gateway-rhel8 |
| `python3.11-django-ansible-base+rbac` | `2.5.1-1.el8ap` | eda-controller-rhel8 |
| `python3.11-django-ansible-base+redis_client` | `2.5.1-1.el8ap` | eda-controller-rhel8, gateway-rhel8 |
| `python3.11-django-ansible-base+rest_filters` | `2.5.1-1.el8ap` | gateway-rhel8 |
| `python3.11-django-auth-ldap` | `4.0.0-2.el8ap` | gateway-rhel8, hub-rhel8 |
| `python3.11-django-crum` | `0.7.9-2.el8ap` | eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-django-dynamic-preferences` | `1.16.0-1.el8ap` | gateway-rhel8 |
| `python3.11-django-extensions` | `3.2.3-2.el8ap` | gateway-rhel8 |
| `python3.11-django-filter` | `23.5-1.el8ap` | eda-controller-rhel8, hub-rhel8 |
| `python3.11-django-guid` | `3.4.0-1.el8ap` | hub-rhel8 |
| `python3.11-django-import-export` | `3.3.6-2.el8ap` | hub-rhel8 |
| `python3.11-django-ipware` | `3.0.7-3.el8ap` | hub-rhel8 |
| `python3.11-django-lifecycle` | `1.1.2-1.el8ap` | hub-rhel8 |
| `python3.11-django-oauth-toolkit` | `2.3.0-1.el8ap` | gateway-rhel8 |
| `python3.11-django-picklefield` | `3.1-1.el8ap` | hub-rhel8 |
| `python3.11-django-prometheus` | `2.3.1-2.el8ap` | hub-rhel8 |
| `python3.11-django-redis` | `5.4.0-1.el8ap` | eda-controller-rhel8, gateway-rhel8 |
| `python3.11-django-rq` | `2.8.0-1.el8ap` | eda-controller-rhel8 |
| `python3.11-django-split-settings` | `1.2.0-2.el8ap` | eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-django-storages` | `1.14.2-2.el8ap` | hub-rhel8 |
| `python3.11-django-storages+azure` | `1.14.2-2.el8ap` | hub-rhel8 |
| `python3.11-django-storages+s3` | `1.14.2-2.el8ap` | hub-rhel8 |
| `python3.11-djangorestframework` | `3.15.1-1.el8ap` | eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-djangorestframework-queryfields` | `1.1.0-1.el8ap` | hub-rhel8 |
| `python3.11-docutils` | `0.20.1-2.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, receptor-rhel8 |
| `python3.11-dpath` | `2.1.6-1.el8ap` | de-supported-rhel8, ee-supported-rhel8 |
| `python3.11-drf-access-policy` | `1.5.0-1.el8ap` | hub-rhel8 |
| `python3.11-drf-nested-routers` | `0.93.5-1.el8ap` | hub-rhel8 |
| `python3.11-drf-spectacular` | `0.26.5-2.el8ap` | eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-drools-jpy` | `0.3.9-2.el8ap` | de-supported-rhel8 |
| `python3.11-drools-jpy-jar` | `1.0.6-2.Final_redhat_00001.1.el8ap` | de-supported-rhel8 |
| `python3.11-dynaconf` | `3.2.6-1.el8ap` | eda-controller-rhel8, hub-rhel8 |
| `python3.11-ecdsa` | `0.18.0-1.el8ap` | eda-controller-rhel8 |
| `python3.11-et-xmlfile` | `1.1.0-3.el8ap` | hub-rhel8 |
| `python3.11-filelock` | `3.13.1-1.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-flake8` | `6.1.0-2.el8ap` | hub-rhel8 |
| `python3.11-frozenlist` | `1.4.0-1.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-galaxy-importer` | `0.4.25-1.el8ap` | hub-rhel8 |
| `python3.11-galaxy-ng` | `4.10.0-1.el8ap` | hub-rhel8 |
| `python3.11-gitdb` | `4.0.11-1.el8ap` | hub-rhel8 |
| `python3.11-gitpython` | `3.1.41-1.el8ap` | hub-rhel8 |
| `python3.11-gnupg` | `0.5.2-1.el8ap` | eda-controller-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-google-auth` | `2.27.0-1.el8ap` | eda-controller-rhel8, ee-supported-rhel8 |
| `python3.11-googleapis-common-protos` | `1.59.1-2.el8ap` | gateway-rhel8, hub-rhel8 |
| `python3.11-grpcio` | `1.58.3-1.el8ap` | ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-grpcio-tools` | `1.58.3-1.el8ap` | gateway-rhel8 |
| `python3.11-gunicorn` | `22.0.0-1.el8ap` | eda-controller-rhel8, hub-rhel8 |
| `python3.11-hyperlink` | `21.0.0-2.el8ap` | eda-controller-rhel8 |
| `python3.11-idna` | `3.4-1.el8` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-importlib-metadata` | `6.0.1-2.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-incremental` | `24.7.2-1.el8ap` | eda-controller-rhel8 |
| `python3.11-inflection` | `0.5.1-4.el8ap` | eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-insights-analytics-collector` | `0.3.2-2.el8ap` | hub-rhel8 |
| `python3.11-isodate` | `0.6.1-2.el8ap` | de-supported-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-janus` | `1.0.0-2.el8ap` | de-supported-rhel8 |
| `python3.11-jinja2` | `3.1.4-1.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-jmespath` | `1.0.1-2.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-jpy` | `0.15.0-1.el8ap` | de-supported-rhel8 |
| `python3.11-jq` | `1.6.0-1.el8ap` | hub-rhel8 |
| `python3.11-json-stream` | `2.3.2-1.el8ap` | hub-rhel8 |
| `python3.11-json-stream-rs-tokenizer` | `0.4.26-1.el8ap` | hub-rhel8 |
| `python3.11-jsonschema` | `4.21.1-1.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-jsonschema-specifications` | `2023.12.1-1.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-jwcrypto` | `1.5.6-1.el8ap` | gateway-rhel8 |
| `python3.11-kubernetes` | `26.1.0-2.el8ap` | eda-controller-rhel8 |
| `python3.11-ldap` | `3.4.4-1.el8ap` | gateway-rhel8, hub-rhel8 |
| `python3.11-libs` | `3.11.9-7.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, receptor-rhel8 |
| `python3.11-lockfile` | `0.12.2-2.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, receptor-rhel8 |
| `python3.11-lxml` | `4.9.2-4.el8` | ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8 |
| `python3.11-markdown` | `3.5.2-1.el8ap` | hub-rhel8 |
| `python3.11-markuppy` | `1.14-4.el8ap` | hub-rhel8 |
| `python3.11-markupsafe` | `2.1.5-1.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-marshmallow` | `3.20.2-1.el8ap` | hub-rhel8 |
| `python3.11-mccabe` | `0.7.0-2.el8ap` | hub-rhel8 |
| `python3.11-multidict` | `6.0.4-1.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-mypy-extensions` | `1.0.0-1.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-netaddr` | `1.2.1-1.el8ap` | ee-supported-rhel8, gateway-rhel8 |
| `python3.11-nh3` | `0.2.18-1.el8ap` | hub-rhel8 |
| `python3.11-oauthlib` | `3.2.2-1.el8ap` | eda-controller-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-odfpy` | `1.4.1-8.el8ap` | hub-rhel8 |
| `python3.11-openpyxl` | `3.1.2-1.el8ap` | hub-rhel8 |
| `python3.11-opentelemetry-api` | `1.18.0-2.el8ap` | hub-rhel8 |
| `python3.11-opentelemetry-distro` | `0.39b0-6.el8ap` | hub-rhel8 |
| `python3.11-opentelemetry-distro+otlp` | `0.39b0-6.el8ap` | hub-rhel8 |
| `python3.11-opentelemetry-exporter-otlp` | `1.18.0-2.el8ap` | hub-rhel8 |
| `python3.11-opentelemetry-exporter-otlp-proto-common` | `1.18.0-2.el8ap` | hub-rhel8 |
| `python3.11-opentelemetry-exporter-otlp-proto-grpc` | `1.18.0-2.el8ap` | hub-rhel8 |
| `python3.11-opentelemetry-exporter-otlp-proto-http` | `1.18.0-2.el8ap` | hub-rhel8 |
| `python3.11-opentelemetry-instrumentation` | `0.39b0-6.el8ap` | hub-rhel8 |
| `python3.11-opentelemetry-instrumentation-django` | `0.39b0-6.el8ap` | hub-rhel8 |
| `python3.11-opentelemetry-instrumentation-wsgi` | `0.39b0-6.el8ap` | hub-rhel8 |
| `python3.11-opentelemetry-proto` | `1.18.0-2.el8ap` | gateway-rhel8, hub-rhel8 |
| `python3.11-opentelemetry-sdk` | `1.18.0-2.el8ap` | hub-rhel8 |
| `python3.11-opentelemetry-semantic-conventions` | `0.39b0-2.el8ap` | hub-rhel8 |
| `python3.11-opentelemetry-util-http` | `0.39b0-6.el8ap` | hub-rhel8 |
| `python3.11-packaging` | `23.2-1.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8, receptor-rhel8 |
| `python3.11-parsley` | `1.3-3.el8ap` | hub-rhel8 |
| `python3.11-pathspec` | `0.12.1-1.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-pbr` | `6.0.0-2.el8ap` | ee-supported-rhel8, hub-rhel8 |
| `python3.11-persisting-theory` | `1.0-2.el8ap` | gateway-rhel8 |
| `python3.11-pexpect` | `4.9.0-1.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, receptor-rhel8 |
| `python3.11-pillow` | `10.3.0-1.el8ap` | hub-rhel8 |
| `python3.11-pip` | `22.3.1-5.el8` | de-supported-rhel8, ee-minimal-rhel8, ee-supported-rhel8 |
| `python3.11-pip-wheel` | `22.3.1-5.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, receptor-rhel8 |
| `python3.11-platformdirs` | `4.2.0-1.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-ply` | `3.11-1.el8` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-podman` | `4.9.0-1.el8ap` | eda-controller-rhel8 |
| `python3.11-prometheus-client` | `0.19.0-1.el8ap` | hub-rhel8 |
| `python3.11-protobuf` | `4.21.12-2.el8ap` | ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-psycopg` | `3.1.17-3.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-psycopg+c` | `3.1.17-3.el8ap` | de-supported-rhel8 |
| `python3.11-psycopg-c` | `3.1.17-3.el8ap` | de-supported-rhel8 |
| `python3.11-ptyprocess` | `0.7.0-1.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, receptor-rhel8 |
| `python3.11-pulp-ansible` | `0.21.7-1.el8ap` | hub-rhel8 |
| `python3.11-pulp-container` | `2.19.3-1.el8ap` | hub-rhel8 |
| `python3.11-pulp-glue` | `0.23.2-1.el8ap` | hub-rhel8 |
| `python3.11-pulpcore` | `3.49.19-1.el8ap` | hub-rhel8 |
| `python3.11-pyasn1` | `0.5.1-1.el8ap` | eda-controller-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-pyasn1-modules` | `0.3.0-1.el8ap` | eda-controller-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-pycares` | `4.4.0-2.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-pycodestyle` | `2.11.1-1.el8ap` | hub-rhel8 |
| `python3.11-pycparser` | `2.20-1.el8` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-pydantic` | `1.10.15-1.el8ap` | eda-controller-rhel8 |
| `python3.11-pyflakes` | `3.1.0-1.el8ap` | hub-rhel8 |
| `python3.11-pygments` | `2.17.2-2.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-pygtrie` | `2.5.0-2.el8ap` | hub-rhel8 |
| `python3.11-pyjwt` | `2.7.0-2.el8ap` | eda-controller-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-pyjwt+crypto` | `2.7.0-2.el8ap` | eda-controller-rhel8 |
| `python3.11-pyOpenSSL` | `24.1.0-1.el8ap` | eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-pyparsing` | `3.1.1-1.el8ap` | de-supported-rhel8, hub-rhel8 |
| `python3.11-pyrad` | `2.4-2.el8ap` | gateway-rhel8 |
| `python3.11-pysocks` | `1.7.1-1.el8` | ee-supported-rhel8 |
| `python3.11-python3-openid` | `3.2.0-3.el8ap` | gateway-rhel8, hub-rhel8 |
| `python3.11-python3-saml` | `1.16.0-2.el8ap` | gateway-rhel8 |
| `python3.11-pytz` | `2024.1-1.el8ap` | eda-controller-rhel8, ee-supported-rhel8 |
| `python3.11-pyxdg` | `0.28-1.el8ap` | eda-controller-rhel8 |
| `python3.11-pyyaml` | `6.0-1.el8` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, receptor-rhel8 |
| `python3.11-redis` | `4.6.0-2.el8ap` | eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-referencing` | `0.35.1-1.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-requests` | `2.31.0-2.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-requests-oauthlib` | `1.3.1-1.el8ap` | eda-controller-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-resolvelib` | `1.0.1-1.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-rich` | `13.1.0-1.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-rpds-py` | `0.18.1-1.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-rq` | `1.13.0-3.el8ap` | eda-controller-rhel8 |
| `python3.11-rq-scheduler` | `0.10.0-3.el8ap` | eda-controller-rhel8 |
| `python3.11-rsa` | `4.9-2.el8ap` | eda-controller-rhel8, ee-supported-rhel8 |
| `python3.11-ruamel-yaml` | `0.18.6-1.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-ruamel-yaml-clib` | `0.2.8-1.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-s3transfer` | `0.10.0-1.el8ap` | ee-supported-rhel8, hub-rhel8 |
| `python3.11-semantic-version` | `2.10.0-2.el8ap` | hub-rhel8 |
| `python3.11-service-identity` | `21.1.0-2.el8ap` | eda-controller-rhel8 |
| `python3.11-setuptools` | `65.5.1-3.el8_10` | controller-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-setuptools-wheel` | `65.5.1-3.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, receptor-rhel8 |
| `python3.11-six` | `1.16.0-1.el8` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, receptor-rhel8 |
| `python3.11-smmap` | `5.0.1-1.el8ap` | hub-rhel8 |
| `python3.11-social-auth-app-django` | `5.4.1-1.el8ap` | gateway-rhel8, hub-rhel8 |
| `python3.11-social-auth-core` | `4.5.4-1.el8ap` | gateway-rhel8, hub-rhel8 |
| `python3.11-sqlparse` | `0.5.0-1.el8ap` | eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-subprocess-tee` | `0.4.1-2.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-tablib` | `3.5.0-1.el8ap` | hub-rhel8 |
| `python3.11-tablib+html` | `3.5.0-1.el8ap` | hub-rhel8 |
| `python3.11-tablib+ods` | `3.5.0-1.el8ap` | hub-rhel8 |
| `python3.11-tablib+xls` | `3.5.0-1.el8ap` | hub-rhel8 |
| `python3.11-tablib+xlsx` | `3.5.0-1.el8ap` | hub-rhel8 |
| `python3.11-tablib+yaml` | `3.5.0-1.el8ap` | hub-rhel8 |
| `python3.11-tabulate` | `0.9.0-3.el8ap` | ee-supported-rhel8, gateway-rhel8 |
| `python3.11-tacacs-plus` | `2.6-2.el8ap` | gateway-rhel8 |
| `python3.11-twisted` | `24.7.0-1.el8ap` | eda-controller-rhel8 |
| `python3.11-twisted+tls` | `24.7.0-1.el8ap` | eda-controller-rhel8 |
| `python3.11-txaio` | `23.1.1-2.el8ap` | eda-controller-rhel8 |
| `python3.11-typing-extensions` | `4.9.0-1.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-uamqp` | `1.6.8-1.el8ap` | ee-supported-rhel8 |
| `python3.11-uritemplate` | `4.1.1-3.el8ap` | eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-url-normalize` | `1.4.3-5.el8ap` | hub-rhel8 |
| `python3.11-urllib3` | `1.26.20-1.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.11-uuid6` | `2024.1.12-1.el8ap` | hub-rhel8 |
| `python3.11-watchdog` | `5.0.2-1.el8ap` | de-supported-rhel8, ee-supported-rhel8 |
| `python3.11-wcmatch` | `8.5-1.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-websocket-client` | `1.7.0-2.el8ap` | eda-controller-rhel8, ee-supported-rhel8 |
| `python3.11-websockets` | `10.4-2.el8ap` | de-supported-rhel8 |
| `python3.11-whitenoise` | `6.6.0-1.el8ap` | hub-rhel8 |
| `python3.11-wrapt` | `1.16.0-1.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-xds-protos` | `1.58.0-2.el8ap` | gateway-rhel8 |
| `python3.11-xlrd` | `2.0.1-6.el8ap` | hub-rhel8 |
| `python3.11-xlwt` | `1.3.0-4.el8ap` | hub-rhel8 |
| `python3.11-xmlsec` | `1.3.13-2.el8ap` | gateway-rhel8 |
| `python3.11-xxhash` | `3.4.1-1.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-supported-rhel8 |
| `python3.11-yarl` | `1.9.2-1.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-zipp` | `3.19.2-1.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.11-zope-interface` | `6.1-1.el8ap` | eda-controller-rhel8 |
| `python36` | `3.6.8-39.module+el8.10.0+20784+edafcd43` | pcp |
| `qemu-img` | `6.2.0-53.module+el8.10.0+22268+f82ccd96` | ee-supported-rhel8 |
| `readline` | `7.0-10.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `receptor` | `1.4.8-3.el8ap` | ee-supported-rhel8, receptor-rhel8 |
| `receptorctl` | `1.4.8-3.el8ap` | ee-supported-rhel8, receptor-rhel8 |
| `redhat-logos-httpd` | `84.5-2.el8` | controller-rhel8, eda-controller-ui-rhel8, gateway-rhel8, hub-web-rhel8 |
| `redhat-release` | `8.10-0.3.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `redis` | `6.2.7-1.module+el8.7.0+15197+cc495aeb` | controller-rhel8, redis-6 |
| `rootfiles` | `8.1-22.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `rpm` | `4.14.3-31.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `rpm-build-libs` | `4.14.3-31.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `rpm-libs` | `4.14.3-31.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `rpm-plugin-selinux` | `4.14.3-31.el8` | controller-rhel8, eda-controller-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8 |
| `rsync` | `3.1.3-19.el8_7.1` | controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15, redis-6 |
| `rsyslog` | `8.2102.0-15.el8` | controller-rhel8, hub-rhel8 |
| `runc` | `1.1.12-4.module+el8.10.0+22283+6d6d094a` | hub-rhel8 |
| `scl-utils` | `2.0.2-16.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15, redis-6 |
| `sed` | `4.5-5.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `selinux-policy` | `3.14.3-139.el8_10` | controller-rhel8, eda-controller-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8 |
| `selinux-policy-minimum` | `3.14.3-139.el8_10` | controller-rhel8, eda-controller-rhel8, gateway-proxy-rhel8, gateway-rhel8 |
| `selinux-policy-targeted` | `3.14.3-139.el8_10` | hub-rhel8 |
| `setup` | `2.12.2-9.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `shadow-utils` | `4.6-22.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `shadow-utils-subid` | `4.6-22.el8` | eda-controller-rhel8, ee-supported-rhel8, receptor-rhel8 |
| `skopeo` | `1.14.5-3.module+el8.10.0+22283+6d6d094a` | hub-rhel8 |
| `sos` | `4.7.2-2.el8_10` | controller-rhel8, ee-supported-rhel8, hub-rhel8, receptor-rhel8 |
| `sqlite-libs` | `3.26.0-19.el8_9` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `sshpass` | `1.09-5.el8ap` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `subscription-manager` | `1.28.42-1.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `subscription-manager-rhsm-certificates` | `20220623-1.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `subversion` | `1.10.2-5.module+el8.6.0+15157+188c9801` | controller-rhel8, ee-supported-rhel8 |
| `subversion-libs` | `1.10.2-5.module+el8.6.0+15157+188c9801` | controller-rhel8, ee-supported-rhel8 |
| `supervisor` | `4.2.5-1.el8ap` | controller-rhel8, gateway-rhel8 |
| `systemd` | `239-82.el8_10.2` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `systemd-libs` | `239-82.el8_10.2` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `systemd-pam` | `239-82.el8_10.2` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `tar` | `1.30-9.el8` | de-supported-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `tcl` | `8.6.8-2.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15, redis-6 |
| `tpm2-tss` | `2.3.2-6.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `tzdata` | `2024a-1.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `tzdata-java` | `2024a-1.el8` | de-supported-rhel8 |
| `unzip` | `6.0-46.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15, redis-6 |
| `usermode` | `1.113-2.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `utf8proc` | `2.6.1-3.module+el8.7.0+15837+7cfc8c53` | controller-rhel8, ee-supported-rhel8 |
| `util-linux` | `2.32.1-46.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `uuid` | `1.6.2-43.el8` | postgresql-15 |
| `uwsgi` | `2.0.23-1.el8ap` | gateway-rhel8 |
| `vim-filesystem` | `8.0.1763-19.el8_6.4` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `vim-minimal` | `8.0.1763-19.el8_6.4` | eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `virt-what` | `1.25-4.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `which` | `2.21-20.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `xmlsec1` | `1.2.25-8.el8_10` | controller-rhel8, gateway-rhel8 |
| `xmlsec1-openssl` | `1.2.25-8.el8_10` | controller-rhel8, gateway-rhel8 |
| `xz` | `5.2.4-4.el8_6` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `xz-libs` | `5.2.4-4.el8_6` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `yajl` | `2.1.0-12.el8` | controller-rhel8 |
| `yamllint` | `1.35.1-1.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `yum` | `4.7.0-20.el8` | eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `zlib` | `1.2.11-25.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `zstd` | `1.4.4-1.el8` | ee-minimal-rhel8, ee-supported-rhel8 |

## Python Packages (all images)

Every Python distribution found in any image (`image:environment prefix (python)`), from
`*.dist-info`/`*.egg-info` metadata. Names are normalized (PEP 503: lowercase, `-` separators). This covers system Python, `/usr/local` and application venvs.

| Package | Version | Images |
|---|---|---|
| `aap-eda` | `1.1.1` | eda-controller-rhel8:/usr (python3.11) |
| `aap-gateway` | `2.5.0.dev1` | gateway-rhel8:/usr (python3.11) |
| `adal` | `1.2.7` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `aiobotocore` | `2.11.2` | de-supported-rhel8:/usr/local (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `aiodns` | `3.1.1` | de-supported-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `aiofiles` | `23.2.1` | hub-rhel8:/usr (python3.11) |
| `aiohttp` | `3.9.5` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), de-supported-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `aiohttp-retry` | `2.8.3` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `aioitertools` | `0.11.0` | de-supported-rhel8:/usr/local (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `aiokafka` | `0.10.0` | de-supported-rhel8:/usr/local (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `aiosignal` | `1.3.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), de-supported-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `annotated-types` | `0.6.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `ansible-builder` | `3.1.0` | hub-rhel8:/usr (python3.11) |
| `ansible-compat` | `24.9.0` | ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `ansible-core` | `2.16.11` | de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `ansible-lint` | `24.9.0` | ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `ansible-pylibssh` | `1.2.2` | ee-supported-rhel8:/usr (python3.11) |
| `ansible-rulebook` | `1.1.1` | de-supported-rhel8:/usr (python3.11) |
| `ansible-runner` | `2.4.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), receptor-rhel8:/usr (python3.11) |
| `ansible-sign` | `0.1.1` | ee-supported-rhel8:/usr (python3.11) |
| `ansiconv` | `1.0.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `anyio` | `4.4.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `appdirs` | `1.4.4` | ee-supported-rhel8:/usr/local (python3.11) |
| `applicationinsights` | `0.11.10` | ee-supported-rhel8:/usr/local (python3.11) |
| `argcomplete` | `3.3.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `argon2-cffi` | `23.1.0` | gateway-rhel8:/usr (python3.11) |
| `argon2-cffi-bindings` | `21.2.0` | gateway-rhel8:/usr (python3.11) |
| `asciichartpy` | `1.5.25` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `asgiref` | `3.7.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `asn1` | `2.7.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `async-lru` | `2.0.4` | hub-rhel8:/usr (python3.11) |
| `async-timeout` | `4.0.3` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `asyncio-throttle` | `1.0.2` | hub-rhel8:/usr (python3.11) |
| `attrs` | `22.2.0` | de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `attrs` | `23.2.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `autobahn` | `23.6.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel8:/usr (python3.11) |
| `autocommand` | `2.2.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `automat` | `22.10.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel8:/usr (python3.11) |
| `awx` | `4.6.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `awxkit` | `4.6.1` | ee-supported-rhel8:/usr (python3.11) |
| `azure-cli-core` | `2.61.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-cli-telemetry` | `1.1.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-common` | `1.1.11` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-common` | `1.1.28` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `azure-containerregistry` | `1.1.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-core` | `1.28.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-core` | `1.29.7` | de-supported-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `azure-core` | `1.30.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `azure-identity` | `1.15.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `azure-identity` | `1.16.1` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-iot-hub` | `2.6.1` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-keyvault` | `4.2.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `azure-keyvault-certificates` | `4.7.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `azure-keyvault-keys` | `4.8.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `azure-keyvault-secrets` | `4.7.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-apimanagement` | `3.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-authorization` | `2.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-automation` | `1.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-batch` | `16.2.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-cdn` | `11.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-compute` | `30.6.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-containerinstance` | `9.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-containerregistry` | `9.1.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-containerservice` | `20.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-core` | `1.4.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-cosmosdb` | `6.4.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-datafactory` | `2.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-devtestlabs` | `9.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-dns` | `8.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-eventhub` | `10.1.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-hdinsight` | `9.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-iothub` | `2.2.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-keyvault` | `10.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-loganalytics` | `12.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-managedservices` | `6.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-managementgroups` | `1.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-marketplaceordering` | `1.1.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-monitor` | `3.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-network` | `19.1.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-notificationhubs` | `7.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-nspkg` | `2.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-privatedns` | `1.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-rdbms` | `10.2.0b12` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-recoveryservices` | `2.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-recoveryservicesbackup` | `3.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-redis` | `13.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-resource` | `21.1.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-search` | `8.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-servicebus` | `7.1.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-sql` | `3.0.1` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-storage` | `19.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-trafficmanager` | `1.0.0b1` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-mgmt-web` | `6.1.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-nspkg` | `2.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-servicebus` | `7.12.1` | de-supported-rhel8:/usr/local (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `azure-storage-blob` | `12.13.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `azure-storage-blob` | `12.19.0` | hub-rhel8:/usr (python3.11) |
| `backoff` | `2.2.1` | hub-rhel8:/usr (python3.11) |
| `bcrypt` | `3.2.0` | ee-minimal-rhel8:/usr/local (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `bindep` | `2.11.0` | hub-rhel8:/usr (python3.11) |
| `black` | `24.4.2` | ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `boto3` | `1.34.30` | ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `boto3` | `1.34.47` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `botocore` | `1.34.30` | de-supported-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `botocore` | `1.34.47` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `bracex` | `2.4` | ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `brotli` | `1.1.0` | de-supported-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `cachetools` | `5.3.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11) |
| `certifi` | `2023.5.7` | de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `certifi` | `2038.12.31` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `cffi` | `1.11.5` | controller-rhel8:/usr (python3.6), eda-controller-rhel8:/usr (python3.6), gateway-proxy-rhel8:/usr (python3.6), gateway-rhel8:/usr (python3.6), hub-rhel8:/usr (python3.6) |
| `cffi` | `1.15.1` | de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `cffi` | `1.16.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `channels` | `3.0.5` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `channels` | `4.0.0` | eda-controller-rhel8:/usr (python3.11) |
| `channels-redis` | `4.2.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `chardet` | `3.0.4` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), ee-supported-rhel8:/usr (python3.6), hub-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), receptor-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `chardet` | `5.2.0` | ee-supported-rhel8:/usr (python3.11) |
| `charset-normalizer` | `2.1.0` | de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `charset-normalizer` | `3.3.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `click` | `8.1.7` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11), receptor-rhel8:/usr (python3.11) |
| `commonmark` | `0.9.1` | ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `constantly` | `15.1.0` | eda-controller-rhel8:/usr (python3.11) |
| `constantly` | `23.10.4` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `croniter` | `2.0.1` | eda-controller-rhel8:/usr (python3.11) |
| `cryptography` | `3.2.1` | controller-rhel8:/usr (python3.6), eda-controller-rhel8:/usr (python3.6), gateway-proxy-rhel8:/usr (python3.6), gateway-rhel8:/usr (python3.6), hub-rhel8:/usr (python3.6) |
| `cryptography` | `41.0.7` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `cryptography` | `42.0.5` | de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `cython` | `0.29.37` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `daphne` | `3.0.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `daphne` | `4.0.0` | eda-controller-rhel8:/usr (python3.11) |
| `dbus-python` | `1.2.4` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `decorator` | `4.2.1` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `decorator` | `5.1.1` | ee-minimal-rhel8:/usr/local (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `defusedxml` | `0.7.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `deprecated` | `1.2.14` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `diff-match-patch` | `20230430` | hub-rhel8:/usr (python3.11) |
| `distlib` | `0.3.8` | ee-supported-rhel8:/usr (python3.11) |
| `distro` | `1.9.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `django` | `4.2.15` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `django` | `4.2.16` | eda-controller-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `django-ansible-base` | `1.0.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `django-ansible-base` | `2.5.1` | eda-controller-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `django-auth-ldap` | `4.0.0` | gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `django-auth-ldap` | `4.6.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `django-cors-headers` | `4.3.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `django-crum` | `0.7.9` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `django-dynamic-preferences` | `1.16.0` | gateway-rhel8:/usr (python3.11) |
| `django-extensions` | `3.2.3` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), gateway-rhel8:/usr (python3.11) |
| `django-filter` | `23.5` | eda-controller-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `django-guid` | `3.2.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `django-guid` | `3.4.0` | hub-rhel8:/usr (python3.11) |
| `django-import-export` | `3.3.6` | hub-rhel8:/usr (python3.11) |
| `django-ipware` | `3.0.7` | hub-rhel8:/usr (python3.11) |
| `django-lifecycle` | `1.1.2` | hub-rhel8:/usr (python3.11) |
| `django-oauth-toolkit` | `1.7.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `django-oauth-toolkit` | `2.3.0` | gateway-rhel8:/usr (python3.11) |
| `django-pglocks` | `1.0.4` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `django-picklefield` | `3.1` | hub-rhel8:/usr (python3.11) |
| `django-polymorphic` | `3.1.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `django-prometheus` | `2.3.1` | hub-rhel8:/usr (python3.11) |
| `django-radius` | `1.5.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `django-redis` | `5.4.0` | eda-controller-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11) |
| `django-rq` | `2.8.0` | eda-controller-rhel8:/usr (python3.11) |
| `django-solo` | `2.2.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `django-split-settings` | `1.0.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `django-split-settings` | `1.2.0` | eda-controller-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `django-storages` | `1.14.2` | hub-rhel8:/usr (python3.11) |
| `djangorestframework` | `3.15.1` | eda-controller-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `djangorestframework` | `3.15.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `djangorestframework-queryfields` | `1.1.0` | hub-rhel8:/usr (python3.11) |
| `djangorestframework-yaml` | `2.0.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `dnspython` | `2.6.1` | ee-supported-rhel8:/usr/local (python3.11) |
| `docutils` | `0.20.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), receptor-rhel8:/usr (python3.11) |
| `dogpile-cache` | `1.1.2` | ee-supported-rhel8:/usr/local (python3.11) |
| `dpath` | `2.1.6` | de-supported-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11) |
| `drf-access-policy` | `1.5.0` | hub-rhel8:/usr (python3.11) |
| `drf-nested-routers` | `0.93.5` | hub-rhel8:/usr (python3.11) |
| `drf-spectacular` | `0.26.5` | eda-controller-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `drools-jpy` | `0.3.9` | de-supported-rhel8:/usr (python3.11) |
| `dynaconf` | `3.2.6` | eda-controller-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `ecdsa` | `0.18.0` | eda-controller-rhel8:/usr (python3.11) |
| `enum-compat` | `0.0.3` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `et-xmlfile` | `1.1.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), hub-rhel8:/usr (python3.11) |
| `ethtool` | `0.14` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `filelock` | `3.13.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `flake8` | `6.1.0` | hub-rhel8:/usr (python3.11) |
| `frozenlist` | `1.4.0` | de-supported-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `frozenlist` | `1.4.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `galaxy-importer` | `0.4.25` | hub-rhel8:/usr (python3.11) |
| `galaxy-ng` | `4.10.0` | hub-rhel8:/usr (python3.11) |
| `gitdb` | `4.0.11` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), hub-rhel8:/usr (python3.11) |
| `gitpython` | `3.1.41` | hub-rhel8:/usr (python3.11) |
| `gitpython` | `3.1.42` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `google-auth` | `2.27.0` | eda-controller-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11) |
| `google-auth` | `2.28.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `googleapis-common-protos` | `1.59.1` | gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `googleapis-common-protos` | `1.63.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `gpg` | `1.13.1` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `grpcio` | `1.58.3` | ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `grpcio` | `1.62.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `grpcio-tools` | `1.58.3` | gateway-rhel8:/usr (python3.11) |
| `gssapi` | `1.8.2` | ee-minimal-rhel8:/usr/local (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `gunicorn` | `22.0.0` | eda-controller-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `h11` | `0.14.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `h2` | `4.1.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `hiredis` | `3.0.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `hpack` | `4.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `httpcore` | `1.0.5` | ee-supported-rhel8:/usr/local (python3.11) |
| `httpx` | `0.27.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `humanfriendly` | `10.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `hyperframe` | `6.0.1` | ee-supported-rhel8:/usr/local (python3.11) |
| `hyperlink` | `21.0.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel8:/usr (python3.11) |
| `idna` | `2.5` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), ee-supported-rhel8:/usr (python3.6), hub-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), receptor-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `idna` | `3.4` | de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `idna` | `3.6` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `importlib-metadata` | `6.0.1` | ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `importlib-metadata` | `6.2.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `incremental` | `24.7.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel8:/usr (python3.11) |
| `inflect` | `7.0.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `inflection` | `0.5.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `iniparse` | `0.4` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `insights-analytics-collector` | `0.3.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), hub-rhel8:/usr (python3.11) |
| `irc` | `20.3.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `isc` | `2.0` | eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), postgresql-15:/usr (python3.6) |
| `iso8601` | `0.1.14` | ee-supported-rhel8:/usr/local (python3.11) |
| `isodate` | `0.6.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), de-supported-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `janus` | `1.0.0` | de-supported-rhel8:/usr (python3.11) |
| `jaraco-collections` | `5.0.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `jaraco-context` | `4.3.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `jaraco-functools` | `4.0.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `jaraco-logging` | `3.3.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `jaraco-stream` | `3.0.3` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `jaraco-text` | `3.12.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `jinja2` | `3.1.3` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `jinja2` | `3.1.4` | de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `jmespath` | `1.0.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), de-supported-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `jpy` | `0.15.0` | de-supported-rhel8:/usr (python3.11) |
| `jq` | `1.6.0` | hub-rhel8:/usr (python3.11) |
| `json-log-formatter` | `0.5.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `json-stream` | `2.3.2` | hub-rhel8:/usr (python3.11) |
| `json-stream-rs-tokenizer` | `0.4.26` | hub-rhel8:/usr (python3.11) |
| `jsonpatch` | `1.32` | ee-supported-rhel8:/usr/local (python3.11) |
| `jsonpointer` | `2.1` | ee-supported-rhel8:/usr/local (python3.11) |
| `jsonschema` | `4.21.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `jsonschema-specifications` | `2023.12.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `jwcrypto` | `1.5.4` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `jwcrypto` | `1.5.6` | gateway-rhel8:/usr (python3.11) |
| `jxmlease` | `1.0.3` | ee-supported-rhel8:/usr/local (python3.11) |
| `kafka-python` | `2.0.2` | de-supported-rhel8:/usr/local (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `keystoneauth1` | `4.3.1` | ee-supported-rhel8:/usr/local (python3.11) |
| `knack` | `0.11.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `krb5` | `0.5.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `kubernetes` | `26.1.0` | eda-controller-rhel8:/usr (python3.11) |
| `kubernetes` | `29.0.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `libcomps` | `0.1.18` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `lockfile` | `0.12.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), receptor-rhel8:/usr (python3.11) |
| `lxml` | `4.9.2` | ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11) |
| `lxml` | `4.9.4` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `markdown` | `3.5.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), hub-rhel8:/usr (python3.11) |
| `markuppy` | `1.14` | hub-rhel8:/usr (python3.11) |
| `markupsafe` | `2.1.5` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `marshmallow` | `3.20.2` | hub-rhel8:/usr (python3.11) |
| `maturin` | `1.5.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `mccabe` | `0.7.0` | hub-rhel8:/usr (python3.11) |
| `metrics-utility` | `0.3.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `microsoft-kiota-abstractions` | `1.3.3` | ee-supported-rhel8:/usr/local (python3.11) |
| `microsoft-kiota-authentication-azure` | `1.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `microsoft-kiota-http` | `1.3.1` | ee-supported-rhel8:/usr/local (python3.11) |
| `microsoft-kiota-serialization-json` | `1.2.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `microsoft-kiota-serialization-text` | `1.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `more-itertools` | `10.2.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `msal` | `1.26.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `msal` | `1.28.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `msal-extensions` | `1.1.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `msal-extensions` | `1.2.0b1` | ee-supported-rhel8:/usr/local (python3.11) |
| `msgpack` | `1.0.5` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `msgraph-core` | `1.1.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `msgraph-sdk` | `1.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `msrest` | `0.6.21` | ee-supported-rhel8:/usr/local (python3.11) |
| `msrest` | `0.7.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `msrestazure` | `0.6.4` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `multidict` | `6.0.4` | de-supported-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `multidict` | `6.0.5` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `munch` | `2.5.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `mypy-extensions` | `1.0.0` | ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `ncclient` | `0.6.10` | ee-minimal-rhel8:/usr/local (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `netaddr` | `1.2.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11) |
| `netifaces` | `0.10.9` | ee-supported-rhel8:/usr/local (python3.11) |
| `nh3` | `0.2.18` | hub-rhel8:/usr (python3.11) |
| `nsx-policy-python-sdk` | `3.1.5.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `nsx-python-sdk` | `3.1.5.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `nsx-vmc-aws-integration-python-sdk` | `3.1.5.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `nsx-vmc-policy-python-sdk` | `3.1.5.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `ntlm-auth` | `1.5.0` | ee-minimal-rhel8:/usr/local (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `numpy` | `1.26.4` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `oauthlib` | `3.2.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `odfpy` | `1.4.1` | hub-rhel8:/usr (python3.11) |
| `openpyxl` | `3.1.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), hub-rhel8:/usr (python3.11) |
| `openshift` | `0.13.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `openstacksdk` | `0.56.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `opentelemetry-api` | `1.18.0` | hub-rhel8:/usr (python3.11) |
| `opentelemetry-api` | `1.24.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `opentelemetry-api` | `1.25.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `opentelemetry-distro` | `0.39b0` | hub-rhel8:/usr (python3.11) |
| `opentelemetry-exporter-otlp` | `1.18.0` | hub-rhel8:/usr (python3.11) |
| `opentelemetry-exporter-otlp` | `1.24.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `opentelemetry-exporter-otlp-proto-common` | `1.18.0` | hub-rhel8:/usr (python3.11) |
| `opentelemetry-exporter-otlp-proto-common` | `1.24.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `opentelemetry-exporter-otlp-proto-grpc` | `1.18.0` | hub-rhel8:/usr (python3.11) |
| `opentelemetry-exporter-otlp-proto-grpc` | `1.24.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `opentelemetry-exporter-otlp-proto-http` | `1.18.0` | hub-rhel8:/usr (python3.11) |
| `opentelemetry-exporter-otlp-proto-http` | `1.24.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `opentelemetry-instrumentation` | `0.39b0` | hub-rhel8:/usr (python3.11) |
| `opentelemetry-instrumentation` | `0.45b0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `opentelemetry-instrumentation-django` | `0.39b0` | hub-rhel8:/usr (python3.11) |
| `opentelemetry-instrumentation-logging` | `0.45b0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `opentelemetry-instrumentation-wsgi` | `0.39b0` | hub-rhel8:/usr (python3.11) |
| `opentelemetry-proto` | `1.18.0` | gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `opentelemetry-proto` | `1.24.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `opentelemetry-sdk` | `1.18.0` | hub-rhel8:/usr (python3.11) |
| `opentelemetry-sdk` | `1.24.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `opentelemetry-sdk` | `1.25.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `opentelemetry-semantic-conventions` | `0.39b0` | hub-rhel8:/usr (python3.11) |
| `opentelemetry-semantic-conventions` | `0.45b0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `opentelemetry-semantic-conventions` | `0.46b0` | ee-supported-rhel8:/usr/local (python3.11) |
| `opentelemetry-util-http` | `0.39b0` | hub-rhel8:/usr (python3.11) |
| `os-service-types` | `1.7.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `ovirt-engine-sdk-python` | `4.5.2` | ee-supported-rhel8:/usr/local (python3.11) |
| `ovirt-imageio` | `2.4.6` | ee-supported-rhel8:/usr/local (python3.11) |
| `packaging` | `23.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11), receptor-rhel8:/usr (python3.11) |
| `pandas` | `2.2.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `paramiko` | `2.8.1` | ee-minimal-rhel8:/usr/local (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `parsley` | `1.3` | hub-rhel8:/usr (python3.11) |
| `pathspec` | `0.12.1` | ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `pbr` | `6.0.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `pcp` | `5.0` | pcp:/usr (python3.6) |
| `pendulum` | `3.0.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `persisting-theory` | `1.0` | gateway-rhel8:/usr (python3.11) |
| `pexpect` | `4.7.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `pexpect` | `4.9.0` | de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), receptor-rhel8:/usr (python3.11) |
| `pillow` | `10.3.0` | hub-rhel8:/usr (python3.11) |
| `pip` | `21.2.4` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `pip` | `22.3.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), de-supported-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11) |
| `pip` | `9.0.3` | pcp:/usr (python3.6) |
| `pkgconfig` | `1.5.5` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `pkginfo` | `1.7.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `platformdirs` | `4.2.0` | ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `ply` | `3.11` | de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `ply` | `3.9` | controller-rhel8:/usr (python3.6), eda-controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), gateway-proxy-rhel8:/usr (python3.6), gateway-rhel8:/usr (python3.6), hub-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), postgresql-15:/usr (python3.6) |
| `podman` | `4.9.0` | eda-controller-rhel8:/usr (python3.11) |
| `portalocker` | `1.7.1` | ee-supported-rhel8:/usr/local (python3.11) |
| `portalocker` | `2.8.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `prometheus-client` | `0.19.0` | hub-rhel8:/usr (python3.11) |
| `prometheus-client` | `0.20.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `protobuf` | `4.21.12` | ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `protobuf` | `4.25.3` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `psutil` | `5.9.1` | ee-supported-rhel8:/usr/local (python3.11) |
| `psutil` | `5.9.8` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `psycopg` | `3.1.17` | de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `psycopg` | `3.1.18` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `psycopg-c` | `3.1.17` | de-supported-rhel8:/usr (python3.11) |
| `ptyprocess` | `0.7.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), receptor-rhel8:/usr (python3.11) |
| `pulp-ansible` | `0.21.7` | hub-rhel8:/usr (python3.11) |
| `pulp-container` | `2.19.3` | hub-rhel8:/usr (python3.11) |
| `pulp-glue` | `0.23.2` | hub-rhel8:/usr (python3.11) |
| `pulpcore` | `3.49.19` | hub-rhel8:/usr (python3.11) |
| `pyang` | `2.5.3` | ee-supported-rhel8:/usr/local (python3.11) |
| `pyasn1` | `0.5.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `pyasn1-modules` | `0.3.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `pycares` | `4.4.0` | de-supported-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `pycodestyle` | `2.11.1` | hub-rhel8:/usr (python3.11) |
| `pycparser` | `2.14` | controller-rhel8:/usr (python3.6), eda-controller-rhel8:/usr (python3.6), gateway-proxy-rhel8:/usr (python3.6), gateway-rhel8:/usr (python3.6), hub-rhel8:/usr (python3.6) |
| `pycparser` | `2.20` | de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `pycparser` | `2.21` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `pycurl` | `7.45.3` | ee-supported-rhel8:/usr/local (python3.11) |
| `pydantic` | `1.10.15` | eda-controller-rhel8:/usr (python3.11) |
| `pydantic` | `2.5.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `pydantic-core` | `2.14.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `pyflakes` | `3.1.0` | hub-rhel8:/usr (python3.11) |
| `pygerduty` | `0.38.3` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `pygments` | `2.17.2` | ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `pygobject` | `3.28.3` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `pygtrie` | `2.5.0` | hub-rhel8:/usr (python3.11) |
| `pyinotify` | `0.9.6` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `pyjwt` | `2.7.0` | eda-controller-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `pyjwt` | `2.8.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `pykerberos` | `1.2.1` | ee-minimal-rhel8:/usr/local (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `pynacl` | `1.4.0` | ee-minimal-rhel8:/usr/local (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `pyopenssl` | `24.0.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `pyopenssl` | `24.1.0` | eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `pyparsing` | `2.4.6` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `pyparsing` | `3.1.1` | de-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `pypsrp` | `0.5.0` | ee-minimal-rhel8:/usr/local (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `pyrad` | `2.4` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), gateway-rhel8:/usr (python3.11) |
| `pysocks` | `1.6.8` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), ee-supported-rhel8:/usr (python3.6), hub-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), receptor-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `pysocks` | `1.7.1` | ee-supported-rhel8:/usr (python3.11) |
| `pyspnego` | `0.9.0` | ee-minimal-rhel8:/usr/local (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `python-daemon` | `2.3.2` | de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), receptor-rhel8:/usr (python3.11) |
| `python-daemon` | `3.0.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `python-dateutil` | `2.6.1` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `python-dateutil` | `2.8.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11), receptor-rhel8:/usr (python3.11) |
| `python-dsv-sdk` | `1.0.4` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `python-gnupg` | `0.5.2` | eda-controller-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `python-ldap` | `3.4.4` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `python-string-utils` | `1.0.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `python-tss-sdk` | `1.2.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `python3-openid` | `3.2.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `python3-saml` | `1.14.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `python3-saml` | `1.16.0` | gateway-rhel8:/usr (python3.11) |
| `pytz` | `2024.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11) |
| `pyvmomi` | `7.0.2` | ee-supported-rhel8:/usr/local (python3.11) |
| `pywinrm` | `0.4.1` | ee-minimal-rhel8:/usr/local (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `pyxdg` | `0.28` | eda-controller-rhel8:/usr (python3.11) |
| `pyyaml` | `6.0` | de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11), receptor-rhel8:/usr (python3.11) |
| `pyyaml` | `6.0.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `pyzstd` | `0.15.10` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `receptorctl` | `1.4.8` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), ee-supported-rhel8:/usr (python3.11), receptor-rhel8:/usr (python3.11) |
| `redis` | `4.6.0` | eda-controller-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `redis` | `5.0.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `referencing` | `0.33.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `referencing` | `0.35.1` | de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `requests` | `2.20.0` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), ee-supported-rhel8:/usr (python3.6), hub-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), receptor-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `requests` | `2.31.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `requests-credssp` | `2.0.0` | ee-minimal-rhel8:/usr/local (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `requests-ntlm` | `1.1.0` | ee-minimal-rhel8:/usr/local (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `requests-oauthlib` | `1.3.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `requestsexceptions` | `1.4.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `resolvelib` | `1.0.1` | de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `rich` | `13.1.0` | ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `rpds-py` | `0.18.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `rpds-py` | `0.18.1` | de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `rpm` | `4.14.3` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `rq` | `1.13.0` | eda-controller-rhel8:/usr (python3.11) |
| `rq-scheduler` | `0.10.0` | eda-controller-rhel8:/usr (python3.11) |
| `rsa` | `4.9` | eda-controller-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11) |
| `ruamel-yaml` | `0.18.6` | ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `ruamel-yaml-clib` | `0.2.8` | ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `s3transfer` | `0.10.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `sansldap` | `0.1.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `scp` | `0.13.3` | ee-supported-rhel8:/usr/local (python3.11) |
| `selinux` | `2.9` | controller-rhel8:/usr (python3.6), eda-controller-rhel8:/usr (python3.6), gateway-proxy-rhel8:/usr (python3.6), gateway-rhel8:/usr (python3.6) |
| `semantic-version` | `2.10.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), hub-rhel8:/usr (python3.11) |
| `sepolicy` | `1.1` | controller-rhel8:/usr (python3.6), eda-controller-rhel8:/usr (python3.6), gateway-proxy-rhel8:/usr (python3.6), gateway-rhel8:/usr (python3.6) |
| `service-identity` | `21.1.0` | eda-controller-rhel8:/usr (python3.11) |
| `service-identity` | `24.1.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `setools` | `4.3.0` | controller-rhel8:/usr (python3.6), eda-controller-rhel8:/usr (python3.6), gateway-proxy-rhel8:/usr (python3.6), gateway-rhel8:/usr (python3.6) |
| `setuptools` | `39.2.0` | controller-rhel8:/usr (python3.6), de-supported-rhel8:/usr (python3.6), eda-controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), ee-supported-rhel8:/usr (python3.6), gateway-proxy-rhel8:/usr (python3.6), gateway-rhel8:/usr (python3.6), hub-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), receptor-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `setuptools` | `65.5.1` | controller-rhel8:/usr (python3.11), controller-rhel8:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `setuptools` | `69.0.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `setuptools-rust` | `1.8.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `setuptools-scm` | `8.0.4` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `six` | `1.11.0` | controller-rhel8:/usr (python3.6), eda-controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), ee-supported-rhel8:/usr (python3.6), gateway-proxy-rhel8:/usr (python3.6), gateway-rhel8:/usr (python3.6), hub-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), receptor-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `six` | `1.16.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11), receptor-rhel8:/usr (python3.11) |
| `slack-sdk` | `3.27.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `smmap` | `5.0.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), hub-rhel8:/usr (python3.11) |
| `sniffio` | `1.3.1` | ee-supported-rhel8:/usr/local (python3.11) |
| `social-auth-app-django` | `5.4.1` | gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `social-auth-app-django` | `5.4.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `social-auth-core` | `4.5.4` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `sos` | `4.7.2` | controller-rhel8:/usr (python3.6), ee-supported-rhel8:/usr (python3.6), hub-rhel8:/usr (python3.6), receptor-rhel8:/usr (python3.6) |
| `sqlparse` | `0.4.4` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `sqlparse` | `0.5.0` | eda-controller-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `std-uritemplate` | `1.0.2` | ee-supported-rhel8:/usr/local (python3.11) |
| `stevedore` | `3.3.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `subprocess-tee` | `0.4.1` | ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `subscription-manager` | `1.28.42` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `suds` | `1.1.2` | ee-supported-rhel8:/usr/local (python3.11) |
| `supervisor` | `4.2.5` | controller-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11) |
| `syspurpose` | `1.28.42` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `systemd-python` | `234` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `tablib` | `3.5.0` | hub-rhel8:/usr (python3.11) |
| `tabulate` | `0.9.0` | ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11) |
| `tacacs-plus` | `1.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `tacacs-plus` | `2.6` | gateway-rhel8:/usr (python3.11) |
| `tempora` | `5.5.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `textfsm` | `0.4.1` | ee-supported-rhel8:/usr/local (python3.11) |
| `time-machine` | `2.14.2` | ee-supported-rhel8:/usr/local (python3.11) |
| `toml` | `0.10.2` | ee-minimal-rhel8:/usr/local (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `tomli` | `2.0.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `ttp` | `0.6.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `twilio` | `8.13.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `twisted` | `24.7.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel8:/usr (python3.11) |
| `txaio` | `23.1.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel8:/usr (python3.11) |
| `typing-extensions` | `4.9.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `tzdata` | `2024.1` | ee-supported-rhel8:/usr/local (python3.11) |
| `uamqp` | `1.6.8` | ee-supported-rhel8:/usr (python3.11) |
| `uritemplate` | `4.1.1` | eda-controller-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `url-normalize` | `1.4.3` | hub-rhel8:/usr (python3.11) |
| `urllib3` | `1.24.2` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), ee-supported-rhel8:/usr (python3.6), hub-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), receptor-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `urllib3` | `1.26.20` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), gateway-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `uuid6` | `2024.1.12` | hub-rhel8:/usr (python3.11) |
| `uwsgi` | `2.0.24` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `uwsgitop` | `0.11` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `vapi-client-bindings` | `3.8.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `vapi-common-client` | `2.34.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `vapi-runtime` | `2.34.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `vmc-client-bindings` | `1.59.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `vmc-draas-client-bindings` | `1.18.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `vsphere-automation-sdk` | `1.76.0` | ee-supported-rhel8:/usr/local (python3.11) |
| `watchdog` | `5.0.2` | de-supported-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11) |
| `wcmatch` | `8.5` | ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `websocket-client` | `1.7.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), eda-controller-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11) |
| `websockets` | `10.4` | de-supported-rhel8:/usr (python3.11) |
| `wheel` | `0.42.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `whitenoise` | `6.6.0` | hub-rhel8:/usr (python3.11) |
| `wrapt` | `1.16.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), de-supported-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `xds-protos` | `1.58.0` | gateway-rhel8:/usr (python3.11) |
| `xlrd` | `2.0.1` | hub-rhel8:/usr (python3.11) |
| `xlwt` | `1.3.0` | hub-rhel8:/usr (python3.11) |
| `xmlsec` | `1.3.13` | controller-rhel8:/var/lib/awx/venv/awx (python3.11), gateway-rhel8:/usr (python3.11) |
| `xmltodict` | `0.12.0` | ee-minimal-rhel8:/usr/local (python3.11), ee-supported-rhel8:/usr/local (python3.11) |
| `xxhash` | `3.4.1` | de-supported-rhel8:/usr (python3.11), eda-controller-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11) |
| `yamllint` | `1.35.1` | ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `yarl` | `1.9.2` | de-supported-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `yarl` | `1.9.4` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `zipp` | `3.17.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |
| `zipp` | `3.19.2` | ee-minimal-rhel8:/usr (python3.11), ee-supported-rhel8:/usr (python3.11), hub-rhel8:/usr (python3.11) |
| `zope-interface` | `6.1` | eda-controller-rhel8:/usr (python3.11) |
| `zope-interface` | `6.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.11) |

## Image Details

### controller-rhel8

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/controller-rhel8.tar.gz` |
| Labels `version` / `release` | `4.6.1` / `3` |
| Image ID | `sha256:3d0cb32040307b37692a9ff0fa138428de641ae3081ee8a00e2c90b940738120` |
| Build date | 2024-10-02T00:26:51 |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | 3.11 |
| Ansible Core | N/A |

<details><summary>RPM packages (256)</summary>

```text
aap-metrics-utility 0.3.0-2.el8ap
acl 2.2.53-3.el8
ansible-automation-platform-common 2.5-2.el8ap
ansible-automation-platform-selinux 0.2-3.el8ap
apr 1.6.3-12.el8
apr-util 1.6.1-9.el8
audit-libs 3.1.2-1.el8
automation-controller 4.6.1-1.el8ap
automation-controller-server 4.6.1-1.el8ap
automation-controller-ui 4.6.1-1.el8ap
automation-controller-venv-tower 4.6.1-1.el8ap
basesystem 11-5.el8
bash 4.4.20-5.el8
brotli 1.0.6-3.el8
bzip2-libs 1.0.6-26.el8
ca-certificates 2024.2.69_v8.0.303-80.0.el8_10
checkpolicy 2.9-1.el8
chkconfig 1.19.2-1.el8
coreutils-single 8.30-15.el8
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crontabs 1.11-17.20190603git.el8
crun 1.14.3-2.module+el8.10.0+22283+6d6d094a
crypto-policies 20230731-1.git3177e06.el8
cryptsetup-libs 2.3.7-7.el8
curl 7.61.1-34.el8_10.2
cyrus-sasl-lib 2.1.27-6.el8_5
dbus 1.12.8-26.el8
dbus-common 1.12.8-26.el8
dbus-daemon 1.12.8-26.el8
dbus-glib 0.110-2.el8
dbus-libs 1.12.8-26.el8
dbus-tools 1.12.8-26.el8
device-mapper 1.02.181-14.el8
device-mapper-libs 1.02.181-14.el8
diffutils 3.6-6.el8
dmidecode 3.5-1.el8
dnf 4.7.0-20.el8
dnf-data 4.7.0-20.el8
dnf-plugin-subscription-manager 1.28.42-1.el8
dumb-init 1.2.5-3.el8ap
elfutils-default-yama-scope 0.190-2.el8
elfutils-libelf 0.190-2.el8
elfutils-libs 0.190-2.el8
expat 2.2.5-15.el8_10
file-libs 5.33-26.el8
filesystem 3.8-6.el8
findutils 4.6.0-23.el8_10
gawk 4.2.1-4.el8
gdbm 1.18-2.el8
gdbm-libs 1.18-2.el8
git-core 2.43.5-1.el8_10
git-lfs 3.4.1-3.el8_10
glib2 2.56.4-162.el8
glibc 2.28-251.el8_10.5
glibc-common 2.28-251.el8_10.5
glibc-langpack-en 2.28-251.el8_10.5
glibc-minimal-langpack 2.28-251.el8_10.5
gmp 6.1.2-11.el8
gnupg2 2.2.20-3.el8_6
gnutls 3.6.16-8.el8_9.3
gobject-introspection 1.56.1-1.el8
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
gzip 1.9-13.el8_5
hostname 3.20-6.el8
ima-evm-utils 1.3.2-12.el8
info 6.5-7.el8
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
kmod-libs 25-20.el8
krb5-libs 1.18.2-29.el8_10
krb5-workstation 1.18.2-29.el8_10
langpacks-en 1.0-12.el8
less 530-3.el8_10
libacl 2.2.53-3.el8
libarchive 3.3.3-5.el8
libassuan 2.5.1-3.el8
libattr 2.4.48-3.el8
libblkid 2.32.1-46.el8
libcap 2.48-6.el8_9
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-5.el8
libcomps 0.1.18-1.el8
libcurl 7.61.1-34.el8_10.2
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-20.el8_10
libedit 3.1-23.20170329cvs.el8
libestr 0.1.10-3.el8
libfastjson 0.99.9-2.el8
libfdisk 2.32.1-46.el8
libffi 3.1-24.el8
libgcc 8.5.0-22.el8_10
libgcrypt 1.8.5-7.el8_6
libgfortran 8.5.0-22.el8_10
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libkadm5 1.18.2-29.el8_10
libksba 1.3.5-9.el8_7
libmodulemd 2.13.0-1.el8
libmount 2.32.1-46.el8
libnghttp2 1.33.0-6.el8_10.1
libnl3 3.7.0-1.el8
libnsl2 1.2.0-2.20180605git4a062cf.el8
libpeas 1.22.0-6.el8
libpsl 0.20.2-6.el8
libpwquality 1.4.4-6.el8
libquadmath 8.5.0-22.el8_10
librepo 1.14.2-5.el8
libreport-filesystem 2.9.5-15.el8
librhsm 0.0.3-5.el8
libseccomp 2.5.2-1.el8
libselinux 2.9-8.el8
libselinux-utils 2.9-8.el8
libsemanage 2.9-9.el8_6
libsepol 2.9-3.el8
libserf 1.3.9-9.module+el8.3.0+6671+2675c974
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-46.el8
libsolv 0.7.20-6.el8
libss 1.45.6-5.el8
libssh 0.9.6-14.el8
libssh-config 0.9.6-14.el8
libstdc++ 8.5.0-22.el8_10
libtasn1 4.13-4.el8_7
libtirpc 1.1.4-12.el8_10
libtool-ltdl 2.4.6-25.el8
libunistring 0.9.9-3.el8
libusbx 1.0.23-4.el8
libuser 0.62-26.el8_10
libutempter 1.1.6-14.el8
libuuid 2.32.1-46.el8
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-18.el8_10.1
libxslt 1.1.32-6.el8
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
logrotate 3.14.0-6.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-3.el8_4
microdnf 3.8.0-2.el8
mpdecimal 2.5.1-3.el8
mpfr 3.1.6-1.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
nginx 1.22.1-1.module+el8.8.0+20355+6d9c8a63.1
nginx-filesystem 1.22.1-1.module+el8.8.0+20355+6d9c8a63.1
npth 1.5-4.el8
openblas 0.3.15-6.el8
openldap 2.4.46-19.el8_10
openssh 8.0p1-25.el8_10
openssh-clients 8.0p1-25.el8_10
openssl 1.1.1k-12.el8_9
openssl-libs 1.1.1k-12.el8_9
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-34.el8_10
passwd 0.80-4.el8
pcre 8.42-6.el8
pcre2 10.32-3.el8_6
platform-python 3.6.8-67.el8_10
platform-python-setuptools 39.2.0-8.el8_10
policycoreutils 2.9-26.el8_10
policycoreutils-python-utils 2.9-26.el8_10
popt 1.18-1.el8
postgresql 15.8-1.module+el8.10.0+22212+a51fe170
postgresql-private-libs 15.8-1.module+el8.10.0+22212+a51fe170
publicsuffix-list-dafsa 20180723-1.el8
python3-audit 3.1.2-1.el8
python3-cffi 1.11.5-6.el8
python3-chardet 3.0.4-7.el8
python3-cloud-what 1.28.42-1.el8
python3-cryptography 3.2.1-7.el8_9
python3-dateutil 2.6.1-6.el8
python3-dbus 1.2.4-15.el8
python3-decorator 4.2.1-2.el8
python3-dnf 4.7.0-20.el8
python3-dnf-plugins-core 4.0.21-25.el8
python3-ethtool 0.14-5.el8
python3-gobject-base 3.28.3-2.el8
python3-gpg 1.13.1-12.el8
python3-hawkey 0.63.0-20.el8_10
python3-idna 2.5-7.el8_10
python3-iniparse 0.4-31.el8
python3-inotify 0.9.6-13.el8
python3-libcomps 0.1.18-1.el8
python3-libdnf 0.63.0-20.el8_10
python3-librepo 1.14.2-5.el8
python3-libs 3.6.8-67.el8_10
python3-libselinux 2.9-8.el8
python3-libsemanage 2.9-9.el8_6
python3-pip-wheel 9.0.3-24.el8
python3-ply 3.9-9.el8
python3-policycoreutils 2.9-26.el8_10
python3-pycparser 2.14-14.el8
python3-pysocks 1.6.8-3.el8
python3-requests 2.20.0-3.el8_8
python3-rpm 4.14.3-31.el8
python3-setools 4.3.0-5.el8
python3-setuptools 39.2.0-8.el8_10
python3-setuptools-wheel 39.2.0-8.el8_10
python3-six 1.11.0-8.el8
python3-subscription-manager-rhsm 1.28.42-1.el8
python3-syspurpose 1.28.42-1.el8
python3-systemd 234-8.el8
python3-urllib3 1.24.2-8.el8_10
python3.11 3.11.9-7.el8_10
python3.11-libs 3.11.9-7.el8_10
python3.11-pip-wheel 22.3.1-5.el8
python3.11-setuptools 65.5.1-3.el8_10
python3.11-setuptools-wheel 65.5.1-3.el8_10
readline 7.0-10.el8
redhat-logos-httpd 84.5-2.el8
redhat-release 8.10-0.3.el8
redis 6.2.7-1.module+el8.7.0+15197+cc495aeb
rootfiles 8.1-22.el8
rpm 4.14.3-31.el8
rpm-build-libs 4.14.3-31.el8
rpm-libs 4.14.3-31.el8
rpm-plugin-selinux 4.14.3-31.el8
rsync 3.1.3-19.el8_7.1
rsyslog 8.2102.0-15.el8
sed 4.5-5.el8
selinux-policy 3.14.3-139.el8_10
selinux-policy-minimum 3.14.3-139.el8_10
setup 2.12.2-9.el8
shadow-utils 4.6-22.el8
sos 4.7.2-2.el8_10
sqlite-libs 3.26.0-19.el8_9
sshpass 1.09-5.el8ap
subscription-manager 1.28.42-1.el8
subscription-manager-rhsm-certificates 20220623-1.el8
subversion 1.10.2-5.module+el8.6.0+15157+188c9801
subversion-libs 1.10.2-5.module+el8.6.0+15157+188c9801
supervisor 4.2.5-1.el8ap
systemd 239-82.el8_10.2
systemd-libs 239-82.el8_10.2
systemd-pam 239-82.el8_10.2
tpm2-tss 2.3.2-6.el8
tzdata 2024a-1.el8
usermode 1.113-2.el8
utf8proc 2.6.1-3.module+el8.7.0+15837+7cfc8c53
util-linux 2.32.1-46.el8
virt-what 1.25-4.el8
which 2.21-20.el8
xmlsec1 1.2.25-8.el8_10
xmlsec1-openssl 1.2.25-8.el8_10
xz-libs 5.2.4-4.el8_6
yajl 2.1.0-12.el8
zlib 1.2.11-25.el8
```

</details>

<details><summary>Python packages: /usr (python3.11) (2)</summary>

```text
setuptools 65.5.1
supervisor 4.2.5
```

</details>

<details><summary>Python packages: /usr (python3.6) (28)</summary>

```text
cffi 1.11.5
chardet 3.0.4
cryptography 3.2.1
dbus-python 1.2.4
decorator 4.2.1
ethtool 0.14
gpg 1.13.1
idna 2.5
iniparse 0.4
libcomps 0.1.18
ply 3.9
pycparser 2.14
PyGObject 3.28.3
pyinotify 0.9.6
PySocks 1.6.8
python-dateutil 2.6.1
requests 2.20.0
rpm 4.14.3
selinux 2.9
sepolicy 1.1
setools 4.3.0
setuptools 39.2.0
six 1.11.0
sos 4.7.2
subscription-manager 1.28.42
syspurpose 1.28.42
systemd-python 234
urllib3 1.24.2
```

</details>

<details><summary>Python packages: /var/lib/awx/venv/awx (python3.11) (185)</summary>

```text
adal 1.2.7
aiohttp 3.9.5
aiohttp-retry 2.8.3
aiosignal 1.3.1
annotated-types 0.6.0
ansible-runner 2.4.0
ansiconv 1.0.0
asciichartpy 1.5.25
asgiref 3.7.2
asn1 2.7.0
async-timeout 4.0.3
attrs 23.2.0
autobahn 23.6.2
autocommand 2.2.2
Automat 22.10.0
awx 4.6.1
azure-common 1.1.28
azure-core 1.30.0
azure-identity 1.15.0
azure-keyvault 4.2.0
azure-keyvault-certificates 4.7.0
azure-keyvault-keys 4.8.0
azure-keyvault-secrets 4.7.0
boto3 1.34.47
botocore 1.34.47
cachetools 5.3.2
certifi 2038.12.31
cffi 1.16.0
channels 3.0.5
channels-redis 4.2.0
charset-normalizer 3.3.2
click 8.1.7
constantly 23.10.4
cryptography 41.0.7
Cython 0.29.37
daphne 3.0.2
defusedxml 0.7.1
Deprecated 1.2.14
distro 1.9.0
Django 4.2.15
django-ansible-base 1.0.0
django-auth-ldap 4.6.0
django-cors-headers 4.3.1
django-crum 0.7.9
django-extensions 3.2.3
django-guid 3.2.1
django-oauth-toolkit 1.7.1
django-pglocks 1.0.4
django-polymorphic 3.1.0
django-radius 1.5.1
django-solo 2.2.0
django-split-settings 1.0.0
djangorestframework 3.15.2
djangorestframework-yaml 2.0.0
docutils 0.20.1
enum-compat 0.0.3
et-xmlfile 1.1.0
filelock 3.13.1
frozenlist 1.4.1
gitdb 4.0.11
GitPython 3.1.42
google-auth 2.28.1
googleapis-common-protos 1.63.0
grpcio 1.62.2
hiredis 3.0.0
hyperlink 21.0.0
idna 3.6
importlib-metadata 6.2.1
incremental 24.7.2
inflect 7.0.0
inflection 0.5.1
insights-analytics-collector 0.3.2
irc 20.3.1
isodate 0.6.1
jaraco.collections 5.0.0
jaraco.context 4.3.0
jaraco.functools 4.0.0
jaraco.logging 3.3.0
jaraco.stream 3.0.3
jaraco.text 3.12.0
Jinja2 3.1.3
jmespath 1.0.1
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
metrics-utility 0.3.0
more-itertools 10.2.0
msal 1.26.0
msal-extensions 1.1.0
msgpack 1.0.5
msrest 0.7.1
msrestazure 0.6.4
multidict 6.0.5
netaddr 1.2.1
numpy 1.26.4
oauthlib 3.2.2
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
packaging 23.2
pandas 2.2.1
pbr 6.0.0
pexpect 4.7.0
pip 21.2.4
pip 22.3.1
pkgconfig 1.5.5
portalocker 2.8.2
prometheus_client 0.20.0
protobuf 4.25.3
psutil 5.9.8
psycopg 3.1.18
ptyprocess 0.7.0
pyasn1 0.5.1
pyasn1-modules 0.3.0
pycparser 2.21
pydantic 2.5.0
pydantic_core 2.14.1
pygerduty 0.38.3
PyJWT 2.8.0
pyOpenSSL 24.0.0
pyparsing 2.4.6
pyrad 2.4
python-daemon 3.0.1
python-dateutil 2.8.2
python-dsv-sdk 1.0.4
python-ldap 3.4.4
python-string-utils 1.0.0
python-tss-sdk 1.2.2
python3-openid 3.2.0
python3-saml 1.14.0
pytz 2024.1
PyYAML 6.0.1
pyzstd 0.15.10
receptorctl 1.4.8
redis 5.0.1
referencing 0.33.0
requests 2.31.0
requests-oauthlib 1.3.1
rpds-py 0.18.0
s3transfer 0.10.0
semantic-version 2.10.0
service-identity 24.1.0
setuptools 65.5.1
setuptools 69.0.2
setuptools-rust 1.8.1
setuptools-scm 8.0.4
six 1.16.0
slack_sdk 3.27.0
smmap 5.0.1
social-auth-app-django 5.4.2
social-auth-core 4.5.4
sqlparse 0.4.4
tacacs-plus 1.0
tempora 5.5.1
tomli 2.0.1
twilio 8.13.0
Twisted 24.7.0
txaio 23.1.1
typing_extensions 4.9.0
urllib3 1.26.20
uWSGI 2.0.24
uwsgitop 0.11
websocket-client 1.7.0
wheel 0.42.0
wrapt 1.16.0
xmlsec 1.3.13
yarl 1.9.4
zipp 3.17.0
zope.interface 6.2
```

</details>

[Back to top](#contents)

### de-supported-rhel8

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-25/de-supported-rhel8` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/de-supported-rhel8.tar.gz` |
| Labels `version` / `release` | `1.1.1` / `16` |
| Image ID | `sha256:a9c8cec645c0d070de761405094caadd6969799d85a2b859233e0569a23fb774` |
| Build date | 2024-10-02T02:03:35 |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | 3.11 |
| Ansible Core | 2.16.11 |

<details><summary>RPM packages (215)</summary>

```text
alsa-lib 1.2.10-2.el8
ansible-core 2.16.11-1.el8ap
ansible-rulebook 1.1.1-1.el8ap
ansible-runner 2.4.0-1.el8ap
audit-libs 3.1.2-1.el8
avahi-libs 0.7-27.el8_10.1
basesystem 11-5.el8
bash 4.4.20-5.el8
brotli 1.0.6-3.el8
bzip2-libs 1.0.6-26.el8
ca-certificates 2024.2.69_v8.0.303-80.0.el8_10
chkconfig 1.19.2-1.el8
copy-jdk-configs 4.0-2.el8
coreutils-single 8.30-15.el8
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crypto-policies 20230731-1.git3177e06.el8
crypto-policies-scripts 20230731-1.git3177e06.el8
cups-libs 2.2.6-60.el8_10
curl 7.61.1-34.el8_10.2
cyrus-sasl-lib 2.1.27-6.el8_5
dbus-libs 1.12.8-26.el8
dumb-init 1.2.5-3.el8ap
elfutils-libelf 0.190-2.el8
expat 2.2.5-15.el8_10
file-libs 5.33-26.el8
filesystem 3.8-6.el8
findutils 4.6.0-23.el8_10
gawk 4.2.1-4.el8
gdbm 1.18-2.el8
gdbm-libs 1.18-2.el8
git-core 2.43.5-1.el8_10
glib2 2.56.4-162.el8
glibc 2.28-251.el8_10.5
glibc-common 2.28-251.el8_10.5
glibc-langpack-en 2.28-251.el8_10.5
glibc-minimal-langpack 2.28-251.el8_10.5
gmp 6.1.2-11.el8
gnupg2 2.2.20-3.el8_6
gnutls 3.6.16-8.el8_9.3
gobject-introspection 1.56.1-1.el8
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
gzip 1.9-13.el8_5
info 6.5-7.el8
java-17-openjdk-headless 17.0.12.0.7-2.el8
javapackages-filesystem 5.3.0-2.module+el8+2598+06babf2e
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
krb5-libs 1.18.2-29.el8_10
langpacks-en 1.0-12.el8
less 530-3.el8_10
libacl 2.2.53-3.el8
libarchive 3.3.3-5.el8
libassuan 2.5.1-3.el8
libattr 2.4.48-3.el8
libblkid 2.32.1-46.el8
libcap 2.48-6.el8_9
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-5.el8
libcurl 7.61.1-34.el8_10.2
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-20.el8_10
libedit 3.1-23.20170329cvs.el8
libfdisk 2.32.1-46.el8
libffi 3.1-24.el8
libgcc 8.5.0-22.el8_10
libgcrypt 1.8.5-7.el8_6
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libksba 1.3.5-9.el8_7
libmodulemd 2.13.0-1.el8
libmount 2.32.1-46.el8
libnghttp2 1.33.0-6.el8_10.1
libnsl2 1.2.0-2.20180605git4a062cf.el8
libpeas 1.22.0-6.el8
libpq 13.11-1.el8
libpsl 0.20.2-6.el8
libpwquality 1.4.4-6.el8
librepo 1.14.2-5.el8
librhsm 0.0.3-5.el8
libselinux 2.9-8.el8
libsemanage 2.9-9.el8_6
libsepol 2.9-3.el8
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-46.el8
libsolv 0.7.20-6.el8
libssh 0.9.6-14.el8
libssh-config 0.9.6-14.el8
libstdc++ 8.5.0-22.el8_10
libtasn1 4.13-4.el8_7
libtirpc 1.1.4-12.el8_10
libunistring 0.9.9-3.el8
libusbx 1.0.23-4.el8
libutempter 1.1.6-14.el8
libuuid 2.32.1-46.el8
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-18.el8_10.1
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
lksctp-tools 1.0.18-3.el8
lua 5.3.4-12.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-3.el8_4
mailcap 2.1.48-3.el8
microdnf 3.8.0-2.el8
mpdecimal 2.5.1-3.el8
mpfr 3.1.6-1.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
npth 1.5-4.el8
nspr 4.35.0-1.el8_8
nss 3.101.0-7.el8_8
nss-softokn 3.101.0-7.el8_8
nss-softokn-freebl 3.101.0-7.el8_8
nss-sysinit 3.101.0-7.el8_8
nss-util 3.101.0-7.el8_8
openldap 2.4.46-19.el8_10
openssh 8.0p1-25.el8_10
openssh-clients 8.0p1-25.el8_10
openssl-libs 1.1.1k-12.el8_9
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-34.el8_10
pcre 8.42-6.el8
pcre2 10.32-3.el8_6
platform-python 3.6.8-67.el8_10
platform-python-setuptools 39.2.0-8.el8_10
popt 1.18-1.el8
publicsuffix-list-dafsa 20180723-1.el8
python3-libs 3.6.8-67.el8_10
python3-pip-wheel 9.0.3-24.el8
python3-setuptools-wheel 39.2.0-8.el8_10
python3.11 3.11.9-7.el8_10
python3.11-aiodns 3.1.1-1.el8ap
python3.11-aiohttp 3.9.5-1.el8ap
python3.11-aiosignal 1.3.1-1.el8ap
python3.11-ansible-runner 2.4.0-1.el8ap
python3.11-async-timeout 4.0.3-2.el8ap
python3.11-attrs 22.2.0-1.el8ap
python3.11-azure-core 1.29.7-1.el8ap
python3.11-botocore 1.34.30-1.el8ap
python3.11-brotli 1.1.0-1.el8ap
python3.11-certifi 2023.5.7-1.el8ap
python3.11-cffi 1.15.1-1.el8
python3.11-charset-normalizer 2.1.0-1.el8
python3.11-cryptography 42.0.5-1.el8ap
python3.11-daemon 2.3.2-1.el8ap
python3.11-dateutil 2.8.2-2.el8ap
python3.11-docutils 0.20.1-2.el8ap
python3.11-dpath 2.1.6-1.el8ap
python3.11-drools-jpy 0.3.9-2.el8ap
python3.11-drools-jpy-jar 1.0.6-2.Final_redhat_00001.1.el8ap
python3.11-frozenlist 1.4.0-1.el8ap
python3.11-idna 3.4-1.el8
python3.11-isodate 0.6.1-2.el8ap
python3.11-janus 1.0.0-2.el8ap
python3.11-jinja2 3.1.4-1.el8ap
python3.11-jmespath 1.0.1-2.el8ap
python3.11-jpy 0.15.0-1.el8ap
python3.11-jsonschema 4.21.1-1.el8ap
python3.11-jsonschema-specifications 2023.12.1-1.el8ap
python3.11-libs 3.11.9-7.el8_10
python3.11-lockfile 0.12.2-2.el8ap
python3.11-markupsafe 2.1.5-1.el8ap
python3.11-multidict 6.0.4-1.el8ap
python3.11-packaging 23.2-1.el8ap
python3.11-pexpect 4.9.0-1.el8ap
python3.11-pip 22.3.1-5.el8
python3.11-pip-wheel 22.3.1-5.el8
python3.11-ply 3.11-1.el8
python3.11-psycopg 3.1.17-3.el8ap
python3.11-psycopg+c 3.1.17-3.el8ap
python3.11-psycopg-c 3.1.17-3.el8ap
python3.11-ptyprocess 0.7.0-1.el8ap
python3.11-pycares 4.4.0-2.el8ap
python3.11-pycparser 2.20-1.el8
python3.11-pyparsing 3.1.1-1.el8ap
python3.11-pyyaml 6.0-1.el8
python3.11-referencing 0.35.1-1.el8ap
python3.11-requests 2.31.0-2.el8ap
python3.11-resolvelib 1.0.1-1.el8ap
python3.11-rpds-py 0.18.1-1.el8ap
python3.11-setuptools-wheel 65.5.1-3.el8_10
python3.11-six 1.16.0-1.el8
python3.11-typing-extensions 4.9.0-1.el8ap
python3.11-urllib3 1.26.20-1.el8ap
python3.11-watchdog 5.0.2-1.el8ap
python3.11-websockets 10.4-2.el8ap
python3.11-wrapt 1.16.0-1.el8ap
python3.11-xxhash 3.4.1-1.el8ap
python3.11-yarl 1.9.2-1.el8ap
readline 7.0-10.el8
redhat-release 8.10-0.3.el8
rootfiles 8.1-22.el8
rpm 4.14.3-31.el8
rpm-libs 4.14.3-31.el8
sed 4.5-5.el8
setup 2.12.2-9.el8
shadow-utils 4.6-22.el8
sqlite-libs 3.26.0-19.el8_9
sshpass 1.09-5.el8ap
systemd-libs 239-82.el8_10.2
tar 1.30-9.el8
tzdata 2024a-1.el8
tzdata-java 2024a-1.el8
util-linux 2.32.1-46.el8
xz-libs 5.2.4-4.el8_6
zlib 1.2.11-25.el8
```

</details>

<details><summary>Python packages: /usr (python3.11) (55)</summary>

```text
aiodns 3.1.1
aiohttp 3.9.5
aiosignal 1.3.1
ansible-core 2.16.11
ansible-rulebook 1.1.1
ansible-runner 2.4.0
async-timeout 4.0.3
attrs 22.2.0
azure-core 1.29.7
botocore 1.34.30
Brotli 1.1.0
certifi 2023.5.7
cffi 1.15.1
charset-normalizer 2.1.0
cryptography 42.0.5
docutils 0.20.1
dpath 2.1.6
drools-jpy 0.3.9
frozenlist 1.4.0
idna 3.4
isodate 0.6.1
janus 1.0.0
Jinja2 3.1.4
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
psycopg 3.1.17
psycopg-c 3.1.17
ptyprocess 0.7.0
pycares 4.4.0
pycparser 2.20
pyparsing 3.1.1
python-daemon 2.3.2
python-dateutil 2.8.2
PyYAML 6.0
referencing 0.35.1
requests 2.31.0
resolvelib 1.0.1
rpds-py 0.18.1
six 1.16.0
typing_extensions 4.9.0
urllib3 1.26.20
watchdog 5.0.2
websockets 10.4
wrapt 1.16.0
xxhash 3.4.1
yarl 1.9.2
```

</details>

<details><summary>Python packages: /usr (python3.6) (1)</summary>

```text
setuptools 39.2.0
```

</details>

<details><summary>Python packages: /usr/local (python3.11) (5)</summary>

```text
aiobotocore 2.11.2
aioitertools 0.11.0
aiokafka 0.10.0
azure-servicebus 7.12.1
kafka-python 2.0.2
```

</details>

<details><summary>Ansible collections (2)</summary>

```text
ansible.eda 2.1.0
redhat.insights_eda 1.2.0
```

</details>

[Back to top](#contents)

### eda-controller-rhel8

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/eda-controller-rhel8.tar.gz` |
| Labels `version` / `release` | `1.1.1` / `2` |
| Image ID | `sha256:1f5b20f9596d229fd174a532d84150174c3c85e124cd1ce822bf813797dc02e6` |
| Build date | 2024-10-02T00:27:36 |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | 3.11 |
| Ansible Core | 2.16.11 |

<details><summary>RPM packages (262)</summary>

```text
acl 2.2.53-3.el8
ansible-automation-platform-common 2.5-2.el8ap
ansible-automation-platform-selinux 0.2-3.el8ap
ansible-core 2.16.11-1.el8ap
audit-libs 3.1.2-1.el8
automation-eda-controller 1.1.1-1.el8ap
basesystem 11-5.el8
bash 4.4.20-5.el8
brotli 1.0.6-3.el8
bzip2-libs 1.0.6-26.el8
ca-certificates 2024.2.69_v8.0.303-80.0.el8_10
checkpolicy 2.9-1.el8
chkconfig 1.19.2-1.el8
coreutils-single 8.30-15.el8
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crypto-policies 20230731-1.git3177e06.el8
cryptsetup-libs 2.3.7-7.el8
curl 7.61.1-34.el8_10.2
cyrus-sasl-lib 2.1.27-6.el8_5
dbus 1.12.8-26.el8
dbus-common 1.12.8-26.el8
dbus-daemon 1.12.8-26.el8
dbus-libs 1.12.8-26.el8
dbus-tools 1.12.8-26.el8
device-mapper 1.02.181-14.el8
device-mapper-libs 1.02.181-14.el8
diffutils 3.6-6.el8
dumb-init 1.2.5-3.el8ap
elfutils-default-yama-scope 0.190-2.el8
elfutils-libelf 0.190-2.el8
elfutils-libs 0.190-2.el8
expat 2.2.5-15.el8_10
file-libs 5.33-26.el8
filesystem 3.8-6.el8
gawk 4.2.1-4.el8
gdbm 1.18-2.el8
gdbm-libs 1.18-2.el8
git-core 2.43.5-1.el8_10
glib2 2.56.4-162.el8
glibc 2.28-251.el8_10.5
glibc-common 2.28-251.el8_10.5
glibc-langpack-en 2.28-251.el8_10.5
glibc-minimal-langpack 2.28-251.el8_10.5
gmp 6.1.2-11.el8
gnupg2 2.2.20-3.el8_6
gnutls 3.6.16-8.el8_9.3
gobject-introspection 1.56.1-1.el8
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
gzip 1.9-13.el8_5
info 6.5-7.el8
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
kmod-libs 25-20.el8
krb5-libs 1.18.2-29.el8_10
langpacks-en 1.0-12.el8
less 530-3.el8_10
libacl 2.2.53-3.el8
libarchive 3.3.3-5.el8
libassuan 2.5.1-3.el8
libattr 2.4.48-3.el8
libblkid 2.32.1-46.el8
libcap 2.48-6.el8_9
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-5.el8
libcurl 7.61.1-34.el8_10.2
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-20.el8_10
libedit 3.1-23.20170329cvs.el8
libfdisk 2.32.1-46.el8
libffi 3.1-24.el8
libgcc 8.5.0-22.el8_10
libgcrypt 1.8.5-7.el8_6
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libksba 1.3.5-9.el8_7
libmodulemd 2.13.0-1.el8
libmount 2.32.1-46.el8
libnghttp2 1.33.0-6.el8_10.1
libnsl2 1.2.0-2.20180605git4a062cf.el8
libpeas 1.22.0-6.el8
libpq 13.11-1.el8
libpsl 0.20.2-6.el8
libpwquality 1.4.4-6.el8
librepo 1.14.2-5.el8
librhsm 0.0.3-5.el8
libseccomp 2.5.2-1.el8
libselinux 2.9-8.el8
libselinux-utils 2.9-8.el8
libsemanage 2.9-9.el8_6
libsepol 2.9-3.el8
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-46.el8
libsolv 0.7.20-6.el8
libssh 0.9.6-14.el8
libssh-config 0.9.6-14.el8
libstdc++ 8.5.0-22.el8_10
libtasn1 4.13-4.el8_7
libtirpc 1.1.4-12.el8_10
libunistring 0.9.9-3.el8
libusbx 1.0.23-4.el8
libutempter 1.1.6-14.el8
libuuid 2.32.1-46.el8
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-18.el8_10.1
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-3.el8_4
microdnf 3.8.0-2.el8
mpdecimal 2.5.1-3.el8
mpfr 3.1.6-1.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
npth 1.5-4.el8
openldap 2.4.46-19.el8_10
openssh 8.0p1-25.el8_10
openssh-clients 8.0p1-25.el8_10
openssl-libs 1.1.1k-12.el8_9
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-34.el8_10
pcre 8.42-6.el8
pcre2 10.32-3.el8_6
platform-python 3.6.8-67.el8_10
platform-python-setuptools 39.2.0-8.el8_10
podman-remote 4.9.4-13.module+el8.10.0+22283+6d6d094a
policycoreutils 2.9-26.el8_10
policycoreutils-python-utils 2.9-26.el8_10
popt 1.18-1.el8
publicsuffix-list-dafsa 20180723-1.el8
python3-audit 3.1.2-1.el8
python3-cffi 1.11.5-6.el8
python3-cryptography 3.2.1-7.el8_9
python3-libs 3.6.8-67.el8_10
python3-libselinux 2.9-8.el8
python3-libsemanage 2.9-9.el8_6
python3-pip-wheel 9.0.3-24.el8
python3-ply 3.9-9.el8
python3-policycoreutils 2.9-26.el8_10
python3-pycparser 2.14-14.el8
python3-setools 4.3.0-5.el8
python3-setuptools-wheel 39.2.0-8.el8_10
python3-six 1.11.0-8.el8
python3.11 3.11.9-7.el8_10
python3.11-Automat 22.10.0-3.el8ap
python3.11-ansible-runner 2.4.0-1.el8ap
python3.11-asgiref 3.7.2-1.el8ap
python3.11-async-timeout 4.0.3-2.el8ap
python3.11-attrs 22.2.0-1.el8ap
python3.11-autobahn 23.6.2-2.el8ap
python3.11-cachetools 5.3.2-1.el8ap
python3.11-certifi 2023.5.7-1.el8ap
python3.11-cffi 1.15.1-1.el8
python3.11-channels 4.0.0-3.el8ap
python3.11-channels+daphne 4.0.0-3.el8ap
python3.11-charset-normalizer 2.1.0-1.el8
python3.11-click 8.1.7-1.el8ap
python3.11-constantly 15.1.0-2.el8ap
python3.11-croniter 2.0.1-1.el8ap
python3.11-cryptography 42.0.5-1.el8ap
python3.11-daemon 2.3.2-1.el8ap
python3.11-daphne 4.0.0-3.el8ap
python3.11-dateutil 2.8.2-2.el8ap
python3.11-django 4.2.16-1.el8ap
python3.11-django-ansible-base 2.5.1-1.el8ap
python3.11-django-ansible-base+channel_auth 2.5.1-1.el8ap
python3.11-django-ansible-base+rbac 2.5.1-1.el8ap
python3.11-django-ansible-base+redis_client 2.5.1-1.el8ap
python3.11-django-crum 0.7.9-2.el8ap
python3.11-django-filter 23.5-1.el8ap
python3.11-django-redis 5.4.0-1.el8ap
python3.11-django-rq 2.8.0-1.el8ap
python3.11-django-split-settings 1.2.0-2.el8ap
python3.11-djangorestframework 3.15.1-1.el8ap
python3.11-docutils 0.20.1-2.el8ap
python3.11-drf-spectacular 0.26.5-2.el8ap
python3.11-dynaconf 3.2.6-1.el8ap
python3.11-ecdsa 0.18.0-1.el8ap
python3.11-gnupg 0.5.2-1.el8ap
python3.11-google-auth 2.27.0-1.el8ap
python3.11-gunicorn 22.0.0-1.el8ap
python3.11-hyperlink 21.0.0-2.el8ap
python3.11-idna 3.4-1.el8
python3.11-incremental 24.7.2-1.el8ap
python3.11-inflection 0.5.1-4.el8ap
python3.11-jinja2 3.1.4-1.el8ap
python3.11-jsonschema 4.21.1-1.el8ap
python3.11-jsonschema-specifications 2023.12.1-1.el8ap
python3.11-kubernetes 26.1.0-2.el8ap
python3.11-libs 3.11.9-7.el8_10
python3.11-lockfile 0.12.2-2.el8ap
python3.11-markupsafe 2.1.5-1.el8ap
python3.11-oauthlib 3.2.2-1.el8ap
python3.11-packaging 23.2-1.el8ap
python3.11-pexpect 4.9.0-1.el8ap
python3.11-pip-wheel 22.3.1-5.el8
python3.11-ply 3.11-1.el8
python3.11-podman 4.9.0-1.el8ap
python3.11-psycopg 3.1.17-3.el8ap
python3.11-ptyprocess 0.7.0-1.el8ap
python3.11-pyOpenSSL 24.1.0-1.el8ap
python3.11-pyasn1 0.5.1-1.el8ap
python3.11-pyasn1-modules 0.3.0-1.el8ap
python3.11-pycparser 2.20-1.el8
python3.11-pydantic 1.10.15-1.el8ap
python3.11-pyjwt 2.7.0-2.el8ap
python3.11-pyjwt+crypto 2.7.0-2.el8ap
python3.11-pytz 2024.1-1.el8ap
python3.11-pyxdg 0.28-1.el8ap
python3.11-pyyaml 6.0-1.el8
python3.11-redis 4.6.0-2.el8ap
python3.11-referencing 0.35.1-1.el8ap
python3.11-requests 2.31.0-2.el8ap
python3.11-requests-oauthlib 1.3.1-1.el8ap
python3.11-resolvelib 1.0.1-1.el8ap
python3.11-rpds-py 0.18.1-1.el8ap
python3.11-rq 1.13.0-3.el8ap
python3.11-rq-scheduler 0.10.0-3.el8ap
python3.11-rsa 4.9-2.el8ap
python3.11-service-identity 21.1.0-2.el8ap
python3.11-setuptools 65.5.1-3.el8_10
python3.11-setuptools-wheel 65.5.1-3.el8_10
python3.11-six 1.16.0-1.el8
python3.11-sqlparse 0.5.0-1.el8ap
python3.11-twisted 24.7.0-1.el8ap
python3.11-twisted+tls 24.7.0-1.el8ap
python3.11-txaio 23.1.1-2.el8ap
python3.11-typing-extensions 4.9.0-1.el8ap
python3.11-uritemplate 4.1.1-3.el8ap
python3.11-urllib3 1.26.20-1.el8ap
python3.11-websocket-client 1.7.0-2.el8ap
python3.11-xxhash 3.4.1-1.el8ap
python3.11-zope-interface 6.1-1.el8ap
readline 7.0-10.el8
redhat-release 8.10-0.3.el8
rootfiles 8.1-22.el8
rpm 4.14.3-31.el8
rpm-libs 4.14.3-31.el8
rpm-plugin-selinux 4.14.3-31.el8
sed 4.5-5.el8
selinux-policy 3.14.3-139.el8_10
selinux-policy-minimum 3.14.3-139.el8_10
setup 2.12.2-9.el8
shadow-utils 4.6-22.el8
shadow-utils-subid 4.6-22.el8
sqlite-libs 3.26.0-19.el8_9
sshpass 1.09-5.el8ap
systemd 239-82.el8_10.2
systemd-libs 239-82.el8_10.2
systemd-pam 239-82.el8_10.2
tzdata 2024a-1.el8
util-linux 2.32.1-46.el8
xz-libs 5.2.4-4.el8_6
zlib 1.2.11-25.el8
```

</details>

<details><summary>Python packages: /usr (python3.11) (82)</summary>

```text
aap-eda 1.1.1
ansible-core 2.16.11
ansible-runner 2.4.0
asgiref 3.7.2
async-timeout 4.0.3
attrs 22.2.0
autobahn 23.6.2
Automat 22.10.0
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
Django 4.2.16
django-ansible-base 2.5.1
django-crum 0.7.9
django-filter 23.5
django-redis 5.4.0
django-rq 2.8.0
django-split-settings 1.2.0
djangorestframework 3.15.1
docutils 0.20.1
drf-spectacular 0.26.5
dynaconf 3.2.6
ecdsa 0.18.0
google-auth 2.27.0
gunicorn 22.0.0
hyperlink 21.0.0
idna 3.4
incremental 24.7.2
inflection 0.5.1
Jinja2 3.1.4
jsonschema 4.21.1
jsonschema-specifications 2023.12.1
kubernetes 26.1.0
lockfile 0.12.2
MarkupSafe 2.1.5
oauthlib 3.2.2
packaging 23.2
pexpect 4.9.0
ply 3.11
podman 4.9.0
psycopg 3.1.17
ptyprocess 0.7.0
pyasn1 0.5.1
pyasn1-modules 0.3.0
pycparser 2.20
pydantic 1.10.15
PyJWT 2.7.0
pyOpenSSL 24.1.0
python-daemon 2.3.2
python-dateutil 2.8.2
python-gnupg 0.5.2
pytz 2024.1
pyxdg 0.28
PyYAML 6.0
redis 4.6.0
referencing 0.35.1
requests 2.31.0
requests-oauthlib 1.3.1
resolvelib 1.0.1
rpds-py 0.18.1
rq 1.13.0
rq-scheduler 0.10.0
rsa 4.9
service-identity 21.1.0
setuptools 65.5.1
six 1.16.0
sqlparse 0.5.0
Twisted 24.7.0
txaio 23.1.1
typing_extensions 4.9.0
uritemplate 4.1.1
urllib3 1.26.20
websocket-client 1.7.0
xxhash 3.4.1
zope.interface 6.1
```

</details>

<details><summary>Python packages: /usr (python3.6) (9)</summary>

```text
cffi 1.11.5
cryptography 3.2.1
ply 3.9
pycparser 2.14
selinux 2.9
sepolicy 1.1
setools 4.3.0
setuptools 39.2.0
six 1.11.0
```

</details>

[Back to top](#contents)

### eda-controller-ui-rhel8

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/eda-controller-ui-rhel8.tar.gz` |
| Labels `version` / `release` | `1.1.1` / `2` |
| Image ID | `sha256:04ae1753b4d7bc385e9bb5c0383fb9cdbe0544c693f636a71b4f80751bf61877` |
| Build date | 2024-10-02T01:15:44 |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | N/A |
| Ansible Core | N/A |

<details><summary>RPM packages (277)</summary>

```text
acl 2.2.53-3.el8
audit-libs 3.1.2-1.el8
basesystem 11-5.el8
bash 4.4.20-5.el8
bind-libs 9.11.36-16.el8_10.2
bind-libs-lite 9.11.36-16.el8_10.2
bind-license 9.11.36-16.el8_10.2
bind-utils 9.11.36-16.el8_10.2
brotli 1.0.6-3.el8
bsdtar 3.3.3-5.el8
bzip2-libs 1.0.6-26.el8
ca-certificates 2024.2.69_v8.0.303-80.0.el8_10
chkconfig 1.19.2-1.el8
cmake 3.26.5-2.el8
cmake-data 3.26.5-2.el8
cmake-filesystem 3.26.5-2.el8
cmake-rpm-macros 3.26.5-2.el8
coreutils-single 8.30-15.el8
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crypto-policies 20230731-1.git3177e06.el8
crypto-policies-scripts 20230731-1.git3177e06.el8
cryptsetup-libs 2.3.7-7.el8
curl 7.61.1-34.el8_10.2
cyrus-sasl-lib 2.1.27-6.el8_5
dbus 1.12.8-26.el8
dbus-common 1.12.8-26.el8
dbus-daemon 1.12.8-26.el8
dbus-glib 0.110-2.el8
dbus-libs 1.12.8-26.el8
dbus-tools 1.12.8-26.el8
device-mapper 1.02.181-14.el8
device-mapper-libs 1.02.181-14.el8
dmidecode 3.5-1.el8
dnf 4.7.0-20.el8
dnf-data 4.7.0-20.el8
dnf-plugin-subscription-manager 1.28.42-1.el8
elfutils-default-yama-scope 0.190-2.el8
elfutils-libelf 0.190-2.el8
elfutils-libs 0.190-2.el8
emacs-filesystem 26.1-12.el8_10
environment-modules 4.5.2-4.el8
expat 2.2.5-15.el8_10
file-libs 5.33-26.el8
filesystem 3.8-6.el8
findutils 4.6.0-23.el8_10
fstrm 0.6.1-3.el8
gawk 4.2.1-4.el8
gdb-gdbserver 8.2-20.el8
gdbm 1.18-2.el8
gdbm-libs 1.18-2.el8
geolite2-city 20180605-1.el8
geolite2-country 20180605-1.el8
gettext 0.19.8.1-17.el8
gettext-libs 0.19.8.1-17.el8
glib2 2.56.4-162.el8
glibc 2.28-251.el8_10.5
glibc-common 2.28-251.el8_10.5
glibc-langpack-en 2.28-251.el8_10.5
glibc-locale-source 2.28-251.el8_10.5
glibc-minimal-langpack 2.28-251.el8_10.5
gmp 6.1.2-11.el8
gnupg2 2.2.20-3.el8_6
gnutls 3.6.16-8.el8_9.3
gobject-introspection 1.56.1-1.el8
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
groff-base 1.22.3-18.el8
gzip 1.9-13.el8_5
hostname 3.20-6.el8
ima-evm-utils 1.3.2-12.el8
info 6.5-7.el8
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
kmod-libs 25-20.el8
krb5-libs 1.18.2-29.el8_10
langpacks-en 1.0-12.el8
less 530-3.el8_10
libacl 2.2.53-3.el8
libarchive 3.3.3-5.el8
libassuan 2.5.1-3.el8
libattr 2.4.48-3.el8
libblkid 2.32.1-46.el8
libcap 2.48-6.el8_9
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-5.el8
libcomps 0.1.18-1.el8
libcroco 0.6.12-4.el8_2.1
libcurl 7.61.1-34.el8_10.2
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-20.el8_10
libfdisk 2.32.1-46.el8
libffi 3.1-24.el8
libgcc 8.5.0-22.el8_10
libgcrypt 1.8.5-7.el8_6
libgomp 8.5.0-22.el8_10
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libksba 1.3.5-9.el8_7
libmaxminddb 1.2.0-10.el8_9.1
libmodulemd 2.13.0-1.el8
libmount 2.32.1-46.el8
libnghttp2 1.33.0-6.el8_10.1
libnl3 3.7.0-1.el8
libnsl2 1.2.0-2.20180605git4a062cf.el8
libpipeline 1.5.0-2.el8
libpkgconf 1.4.2-1.el8
libpsl 0.20.2-6.el8
libpwquality 1.4.4-6.el8
librepo 1.14.2-5.el8
libreport-filesystem 2.9.5-15.el8
librhsm 0.0.3-5.el8
libseccomp 2.5.2-1.el8
libselinux 2.9-8.el8
libsemanage 2.9-9.el8_6
libsepol 2.9-3.el8
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-46.el8
libsolv 0.7.20-6.el8
libssh 0.9.6-14.el8
libssh-config 0.9.6-14.el8
libstdc++ 8.5.0-22.el8_10
libtasn1 4.13-4.el8_7
libtirpc 1.1.4-12.el8_10
libunistring 0.9.9-3.el8
libusbx 1.0.23-4.el8
libuser 0.62-26.el8_10
libutempter 1.1.6-14.el8
libuuid 2.32.1-46.el8
libuv 1.41.1-2.el8_10
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-18.el8_10.1
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-3.el8_4
make 4.2.1-11.el8
man-db 2.7.6.1-18.el8
mpfr 3.1.6-1.el8
ncurses 6.1-10.20180224.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
nginx 1.22.1-1.module+el8.8.0+20355+6d9c8a63.1
nginx-filesystem 1.22.1-1.module+el8.8.0+20355+6d9c8a63.1
nginx-mod-http-perl 1.22.1-1.module+el8.8.0+20355+6d9c8a63.1
nginx-mod-stream 1.22.1-1.module+el8.8.0+20355+6d9c8a63.1
npth 1.5-4.el8
nss_wrapper 1.1.13-1.el8
nss_wrapper-libs 1.1.13-1.el8
openldap 2.4.46-19.el8_10
openssl 1.1.1k-12.el8_9
openssl-libs 1.1.1k-12.el8_9
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-34.el8_10
passwd 0.80-4.el8
pcre 8.42-6.el8
pcre2 10.32-3.el8_6
perl-Carp 1.42-396.el8
perl-Data-Dumper 2.167-399.el8
perl-Digest 1.17-395.el8
perl-Digest-MD5 2.55-396.el8
perl-Encode 2.97-3.el8
perl-Errno 1.28-422.el8
perl-Exporter 5.72-396.el8
perl-File-Path 2.15-2.el8
perl-File-Temp 0.230.600-1.el8
perl-Getopt-Long 2.50-4.el8
perl-HTTP-Tiny 0.074-3.el8
perl-IO 1.38-422.el8
perl-IO-Socket-IP 0.39-5.el8
perl-IO-Socket-SSL 2.066-4.module+el8.3.0+6446+594cad75
perl-MIME-Base64 3.15-396.el8
perl-Mozilla-CA 20160104-7.module+el8.3.0+6498+9eecfe51
perl-Net-SSLeay 1.88-2.module+el8.6.0+13392+f0897f98
perl-PathTools 3.74-1.el8
perl-Pod-Escapes 1.07-395.el8
perl-Pod-Perldoc 3.28-396.el8
perl-Pod-Simple 3.35-395.el8
perl-Pod-Usage 1.69-395.el8
perl-Scalar-List-Utils 1.49-2.el8
perl-Socket 2.027-3.el8
perl-Storable 3.11-3.el8
perl-Term-ANSIColor 4.06-396.el8
perl-Term-Cap 1.17-395.el8
perl-Text-ParseWords 3.30-395.el8
perl-Text-Tabs+Wrap 2013.0523-395.el8
perl-Time-Local 1.280-1.el8
perl-URI 1.73-3.el8
perl-Unicode-Normalize 1.25-396.el8
perl-constant 1.33-396.el8
perl-interpreter 5.26.3-422.el8
perl-libnet 3.11-3.el8
perl-libs 5.26.3-422.el8
perl-macros 5.26.3-422.el8
perl-parent 0.237-1.el8
perl-podlators 4.11-1.el8
perl-threads 2.21-2.el8
perl-threads-shared 1.58-2.el8
pkgconf 1.4.2-1.el8
pkgconf-m4 1.4.2-1.el8
pkgconf-pkg-config 1.4.2-1.el8
platform-python 3.6.8-67.el8_10
platform-python-setuptools 39.2.0-8.el8_10
popt 1.18-1.el8
procps-ng 3.3.15-14.el8
protobuf-c 1.3.0-8.el8
publicsuffix-list-dafsa 20180723-1.el8
python3-bind 9.11.36-16.el8_10.2
python3-chardet 3.0.4-7.el8
python3-cloud-what 1.28.42-1.el8
python3-dateutil 2.6.1-6.el8
python3-dbus 1.2.4-15.el8
python3-decorator 4.2.1-2.el8
python3-dnf 4.7.0-20.el8
python3-dnf-plugins-core 4.0.21-25.el8
python3-ethtool 0.14-5.el8
python3-gobject-base 3.28.3-2.el8
python3-gpg 1.13.1-12.el8
python3-hawkey 0.63.0-20.el8_10
python3-idna 2.5-7.el8_10
python3-iniparse 0.4-31.el8
python3-inotify 0.9.6-13.el8
python3-libcomps 0.1.18-1.el8
python3-libdnf 0.63.0-20.el8_10
python3-librepo 1.14.2-5.el8
python3-libs 3.6.8-67.el8_10
python3-pip-wheel 9.0.3-24.el8
python3-ply 3.9-9.el8
python3-pysocks 1.6.8-3.el8
python3-requests 2.20.0-3.el8_8
python3-rpm 4.14.3-31.el8
python3-setuptools-wheel 39.2.0-8.el8_10
python3-six 1.11.0-8.el8
python3-subscription-manager-rhsm 1.28.42-1.el8
python3-syspurpose 1.28.42-1.el8
python3-systemd 234-8.el8
python3-urllib3 1.24.2-8.el8_10
readline 7.0-10.el8
redhat-logos-httpd 84.5-2.el8
redhat-release 8.10-0.3.el8
rootfiles 8.1-22.el8
rpm 4.14.3-31.el8
rpm-build-libs 4.14.3-31.el8
rpm-libs 4.14.3-31.el8
rsync 3.1.3-19.el8_7.1
scl-utils 2.0.2-16.el8
sed 4.5-5.el8
setup 2.12.2-9.el8
shadow-utils 4.6-22.el8
sqlite-libs 3.26.0-19.el8_9
subscription-manager 1.28.42-1.el8
subscription-manager-rhsm-certificates 20220623-1.el8
systemd 239-82.el8_10.2
systemd-libs 239-82.el8_10.2
systemd-pam 239-82.el8_10.2
tar 1.30-9.el8
tcl 8.6.8-2.el8
tpm2-tss 2.3.2-6.el8
tzdata 2024a-1.el8
unzip 6.0-46.el8
usermode 1.113-2.el8
util-linux 2.32.1-46.el8
vim-filesystem 8.0.1763-19.el8_6.4
vim-minimal 8.0.1763-19.el8_6.4
virt-what 1.25-4.el8
which 2.21-20.el8
xz 5.2.4-4.el8_6
xz-libs 5.2.4-4.el8_6
yum 4.7.0-20.el8
zlib 1.2.11-25.el8
```

</details>

<details><summary>Python packages: /usr (python3.6) (22)</summary>

```text
chardet 3.0.4
dbus-python 1.2.4
decorator 4.2.1
ethtool 0.14
gpg 1.13.1
idna 2.5
iniparse 0.4
isc 2.0
libcomps 0.1.18
ply 3.9
PyGObject 3.28.3
pyinotify 0.9.6
PySocks 1.6.8
python-dateutil 2.6.1
requests 2.20.0
rpm 4.14.3
setuptools 39.2.0
six 1.11.0
subscription-manager 1.28.42
syspurpose 1.28.42
systemd-python 234
urllib3 1.24.2
```

</details>

[Back to top](#contents)

### ee-minimal-rhel8

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/ee-minimal-rhel8.tar.gz` |
| Labels `version` / `release` | `1.0.0` / `747` |
| Image ID | `sha256:a64b9fc4809444fd038346b5f1ea4bf2f1f560147e8a79f563a99e059b919906` |
| Build date | 2024-10-01T22:36:50 |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | 3.11 |
| Ansible Core | 2.16.11 |

<details><summary>RPM packages (191)</summary>

```text
ansible-core 2.16.11-1.el8ap
ansible-lint 24.9.0-1.el8ap
ansible-runner 2.4.0-1.el8ap
ansible-test 2.16.11-1.el8ap
audit-libs 3.1.2-1.el8
basesystem 11-5.el8
bash 4.4.20-5.el8
brotli 1.0.6-3.el8
bzip2 1.0.6-26.el8
bzip2-libs 1.0.6-26.el8
ca-certificates 2024.2.69_v8.0.303-80.0.el8_10
chkconfig 1.19.2-1.el8
coreutils-single 8.30-15.el8
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crypto-policies 20230731-1.git3177e06.el8
curl 7.61.1-34.el8_10.2
cyrus-sasl-lib 2.1.27-6.el8_5
dumb-init 1.2.5-3.el8ap
elfutils-libelf 0.190-2.el8
expat 2.2.5-15.el8_10
file-libs 5.33-26.el8
filesystem 3.8-6.el8
gawk 4.2.1-4.el8
gdbm-libs 1.18-2.el8
git-core 2.43.5-1.el8_10
glib2 2.56.4-162.el8
glibc 2.28-251.el8_10.5
glibc-common 2.28-251.el8_10.5
glibc-langpack-en 2.28-251.el8_10.5
glibc-minimal-langpack 2.28-251.el8_10.5
gmp 6.1.2-11.el8
gnupg2 2.2.20-3.el8_6
gnutls 3.6.16-8.el8_9.3
gobject-introspection 1.56.1-1.el8
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
gzip 1.9-13.el8_5
info 6.5-7.el8
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
krb5-libs 1.18.2-29.el8_10
krb5-workstation 1.18.2-29.el8_10
langpacks-en 1.0-12.el8
less 530-3.el8_10
libacl 2.2.53-3.el8
libarchive 3.3.3-5.el8
libassuan 2.5.1-3.el8
libattr 2.4.48-3.el8
libblkid 2.32.1-46.el8
libcap 2.48-6.el8_9
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-5.el8
libcurl 7.61.1-34.el8_10.2
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-20.el8_10
libedit 3.1-23.20170329cvs.el8
libfdisk 2.32.1-46.el8
libffi 3.1-24.el8
libgcc 8.5.0-22.el8_10
libgcrypt 1.8.5-7.el8_6
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libkadm5 1.18.2-29.el8_10
libksba 1.3.5-9.el8_7
libmodulemd 2.13.0-1.el8
libmount 2.32.1-46.el8
libnghttp2 1.33.0-6.el8_10.1
libnsl2 1.2.0-2.20180605git4a062cf.el8
libpeas 1.22.0-6.el8
libpsl 0.20.2-6.el8
libpwquality 1.4.4-6.el8
librepo 1.14.2-5.el8
librhsm 0.0.3-5.el8
libselinux 2.9-8.el8
libsemanage 2.9-9.el8_6
libsepol 2.9-3.el8
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-46.el8
libsolv 0.7.20-6.el8
libss 1.45.6-5.el8
libssh 0.9.6-14.el8
libssh-config 0.9.6-14.el8
libstdc++ 8.5.0-22.el8_10
libtasn1 4.13-4.el8_7
libtirpc 1.1.4-12.el8_10
libunistring 0.9.9-3.el8
libusbx 1.0.23-4.el8
libutempter 1.1.6-14.el8
libuuid 2.32.1-46.el8
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-18.el8_10.1
libxslt 1.1.32-6.el8
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-3.el8_4
microdnf 3.8.0-2.el8
mpdecimal 2.5.1-3.el8
mpfr 3.1.6-1.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
npth 1.5-4.el8
openldap 2.4.46-19.el8_10
openssh 8.0p1-25.el8_10
openssh-clients 8.0p1-25.el8_10
openssl-libs 1.1.1k-12.el8_9
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-34.el8_10
pcre 8.42-6.el8
pcre2 10.32-3.el8_6
popt 1.18-1.el8
publicsuffix-list-dafsa 20180723-1.el8
python3.11 3.11.9-7.el8_10
python3.11-ansible-compat 24.9.0-1.el8ap
python3.11-ansible-runner 2.4.0-1.el8ap
python3.11-attrs 22.2.0-1.el8ap
python3.11-black 24.4.2-2.el8ap
python3.11-bracex 2.4-1.el8ap
python3.11-certifi 2023.5.7-1.el8ap
python3.11-cffi 1.15.1-1.el8
python3.11-charset-normalizer 2.1.0-1.el8
python3.11-click 8.1.7-1.el8ap
python3.11-commonmark 0.9.1-6.el8ap
python3.11-cryptography 42.0.5-1.el8ap
python3.11-daemon 2.3.2-1.el8ap
python3.11-docutils 0.20.1-2.el8ap
python3.11-filelock 3.13.1-1.el8ap
python3.11-idna 3.4-1.el8
python3.11-importlib-metadata 6.0.1-2.el8ap
python3.11-jinja2 3.1.4-1.el8ap
python3.11-jsonschema 4.21.1-1.el8ap
python3.11-jsonschema-specifications 2023.12.1-1.el8ap
python3.11-libs 3.11.9-7.el8_10
python3.11-lockfile 0.12.2-2.el8ap
python3.11-lxml 4.9.2-4.el8
python3.11-markupsafe 2.1.5-1.el8ap
python3.11-mypy-extensions 1.0.0-1.el8ap
python3.11-packaging 23.2-1.el8ap
python3.11-pathspec 0.12.1-1.el8ap
python3.11-pexpect 4.9.0-1.el8ap
python3.11-pip 22.3.1-5.el8
python3.11-pip-wheel 22.3.1-5.el8
python3.11-platformdirs 4.2.0-1.el8ap
python3.11-ply 3.11-1.el8
python3.11-ptyprocess 0.7.0-1.el8ap
python3.11-pyOpenSSL 24.1.0-1.el8ap
python3.11-pycparser 2.20-1.el8
python3.11-pygments 2.17.2-2.el8ap
python3.11-pyyaml 6.0-1.el8
python3.11-referencing 0.35.1-1.el8ap
python3.11-requests 2.31.0-2.el8ap
python3.11-resolvelib 1.0.1-1.el8ap
python3.11-rich 13.1.0-1.el8ap
python3.11-rpds-py 0.18.1-1.el8ap
python3.11-ruamel-yaml 0.18.6-1.el8ap
python3.11-ruamel-yaml-clib 0.2.8-1.el8ap
python3.11-setuptools 65.5.1-3.el8_10
python3.11-setuptools-wheel 65.5.1-3.el8_10
python3.11-six 1.16.0-1.el8
python3.11-subprocess-tee 0.4.1-2.el8ap
python3.11-urllib3 1.26.20-1.el8ap
python3.11-wcmatch 8.5-1.el8ap
python3.11-zipp 3.19.2-1.el8ap
readline 7.0-10.el8
redhat-release 8.10-0.3.el8
rootfiles 8.1-22.el8
rpm 4.14.3-31.el8
rpm-libs 4.14.3-31.el8
sed 4.5-5.el8
setup 2.12.2-9.el8
shadow-utils 4.6-22.el8
sqlite-libs 3.26.0-19.el8_9
sshpass 1.09-5.el8ap
systemd-libs 239-82.el8_10.2
tar 1.30-9.el8
tzdata 2024a-1.el8
unzip 6.0-46.el8
util-linux 2.32.1-46.el8
xz 5.2.4-4.el8_6
xz-libs 5.2.4-4.el8_6
yamllint 1.35.1-1.el8ap
zlib 1.2.11-25.el8
zstd 1.4.4-1.el8
```

</details>

<details><summary>Python packages: /usr (python3.11) (50)</summary>

```text
ansible-compat 24.9.0
ansible-core 2.16.11
ansible-lint 24.9.0
ansible-runner 2.4.0
attrs 22.2.0
black 24.4.2
bracex 2.4
certifi 2023.5.7
cffi 1.15.1
charset-normalizer 2.1.0
click 8.1.7
commonmark 0.9.1
cryptography 42.0.5
docutils 0.20.1
filelock 3.13.1
idna 3.4
importlib-metadata 6.0.1
Jinja2 3.1.4
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
Pygments 2.17.2
pyOpenSSL 24.1.0
python-daemon 2.3.2
PyYAML 6.0
referencing 0.35.1
requests 2.31.0
resolvelib 1.0.1
rich 13.1.0
rpds-py 0.18.1
ruamel.yaml 0.18.6
ruamel.yaml.clib 0.2.8
setuptools 65.5.1
six 1.16.0
subprocess-tee 0.4.1
urllib3 1.26.20
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
pykerberos 1.2.1
PyNaCl 1.4.0
pypsrp 0.5.0
pyspnego 0.9.0
pywinrm 0.4.1
requests-credssp 2.0.0
requests-ntlm 1.1.0
toml 0.10.2
xmltodict 0.12.0
```

</details>

[Back to top](#contents)

### ee-supported-rhel8

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/ee-supported-rhel8.tar.gz` |
| Labels `version` / `release` | `1.0.0` / `812` |
| Image ID | `sha256:59d1bc680a7c6d8c48dd649e90ad2dfa4dc03ab53f2f7d88aff2ce7090a584bd` |
| Build date | 2024-10-02T02:03:59 |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | 3.11 |
| Ansible Core | 2.16.11 |

<details><summary>RPM packages (295)</summary>

```text
acl 2.2.53-3.el8
ansible-core 2.16.11-1.el8ap
ansible-lint 24.9.0-1.el8ap
ansible-runner 2.4.0-1.el8ap
ansible-sign 0.1.1-2.el8ap
ansible-test 2.16.11-1.el8ap
apr 1.6.3-12.el8
apr-util 1.6.1-9.el8
audit-libs 3.1.2-1.el8
automation-controller-cli 4.6.1-1.el8ap
basesystem 11-5.el8
bash 4.4.20-5.el8
bash-completion 2.7-5.el8
brotli 1.0.6-3.el8
bzip2 1.0.6-26.el8
bzip2-libs 1.0.6-26.el8
ca-certificates 2024.2.69_v8.0.303-80.0.el8_10
chkconfig 1.19.2-1.el8
coreutils-single 8.30-15.el8
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crypto-policies 20230731-1.git3177e06.el8
cryptsetup-libs 2.3.7-7.el8
curl 7.61.1-34.el8_10.2
cyrus-sasl-lib 2.1.27-6.el8_5
dbus 1.12.8-26.el8
dbus-common 1.12.8-26.el8
dbus-daemon 1.12.8-26.el8
dbus-libs 1.12.8-26.el8
dbus-tools 1.12.8-26.el8
device-mapper 1.02.181-14.el8
device-mapper-libs 1.02.181-14.el8
diffutils 3.6-6.el8
dumb-init 1.2.5-3.el8ap
elfutils-default-yama-scope 0.190-2.el8
elfutils-libelf 0.190-2.el8
elfutils-libs 0.190-2.el8
expat 2.2.5-15.el8_10
file-libs 5.33-26.el8
filesystem 3.8-6.el8
findutils 4.6.0-23.el8_10
gawk 4.2.1-4.el8
gdbm 1.18-2.el8
gdbm-libs 1.18-2.el8
git-core 2.43.5-1.el8_10
git-lfs 3.4.1-3.el8_10
glib2 2.56.4-162.el8
glibc 2.28-251.el8_10.5
glibc-common 2.28-251.el8_10.5
glibc-langpack-en 2.28-251.el8_10.5
glibc-minimal-langpack 2.28-251.el8_10.5
gmp 6.1.2-11.el8
gnupg2 2.2.20-3.el8_6
gnutls 3.6.16-8.el8_9.3
gobject-introspection 1.56.1-1.el8
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
gzip 1.9-13.el8_5
info 6.5-7.el8
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
kmod-libs 25-20.el8
krb5-libs 1.18.2-29.el8_10
krb5-workstation 1.18.2-29.el8_10
langpacks-en 1.0-12.el8
less 530-3.el8_10
libacl 2.2.53-3.el8
libaio 0.3.112-1.el8
libarchive 3.3.3-5.el8
libassuan 2.5.1-3.el8
libattr 2.4.48-3.el8
libblkid 2.32.1-46.el8
libcap 2.48-6.el8_9
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-5.el8
libcurl 7.61.1-34.el8_10.2
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-20.el8_10
libedit 3.1-23.20170329cvs.el8
libfdisk 2.32.1-46.el8
libffi 3.1-24.el8
libgcc 8.5.0-22.el8_10
libgcrypt 1.8.5-7.el8_6
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libkadm5 1.18.2-29.el8_10
libksba 1.3.5-9.el8_7
libmodulemd 2.13.0-1.el8
libmount 2.32.1-46.el8
libnghttp2 1.33.0-6.el8_10.1
libnsl2 1.2.0-2.20180605git4a062cf.el8
libpeas 1.22.0-6.el8
libpkgconf 1.4.2-1.el8
libpq 13.11-1.el8
libpsl 0.20.2-6.el8
libpwquality 1.4.4-6.el8
librepo 1.14.2-5.el8
librhsm 0.0.3-5.el8
libseccomp 2.5.2-1.el8
libselinux 2.9-8.el8
libselinux-utils 2.9-8.el8
libsemanage 2.9-9.el8_6
libsepol 2.9-3.el8
libserf 1.3.9-9.module+el8.3.0+6671+2675c974
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-46.el8
libsolv 0.7.20-6.el8
libss 1.45.6-5.el8
libssh 0.9.6-14.el8
libssh-config 0.9.6-14.el8
libstdc++ 8.5.0-22.el8_10
libtasn1 4.13-4.el8_7
libtirpc 1.1.4-12.el8_10
libunistring 0.9.9-3.el8
libusbx 1.0.23-4.el8
libutempter 1.1.6-14.el8
libuuid 2.32.1-46.el8
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-18.el8_10.1
libxslt 1.1.32-6.el8
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
logrotate 3.14.0-6.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-3.el8_4
mailcap 2.1.48-3.el8
microdnf 3.8.0-2.el8
mpdecimal 2.5.1-3.el8
mpfr 3.1.6-1.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
npth 1.5-4.el8
openldap 2.4.46-19.el8_10
openshift-clients 4.12.0-202404161006.p0.gd691257.assembly.stream.el8
openssh 8.0p1-25.el8_10
openssh-clients 8.0p1-25.el8_10
openssl 1.1.1k-12.el8_9
openssl-libs 1.1.1k-12.el8_9
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-34.el8_10
pcre 8.42-6.el8
pcre2 10.32-3.el8_6
pkgconf 1.4.2-1.el8
pkgconf-m4 1.4.2-1.el8
pkgconf-pkg-config 1.4.2-1.el8
platform-python 3.6.8-67.el8_10
platform-python-setuptools 39.2.0-8.el8_10
podman-remote 4.9.4-13.module+el8.10.0+22283+6d6d094a
policycoreutils 2.9-26.el8_10
popt 1.18-1.el8
publicsuffix-list-dafsa 20180723-1.el8
python3-chardet 3.0.4-7.el8
python3-idna 2.5-7.el8_10
python3-libs 3.6.8-67.el8_10
python3-pip-wheel 9.0.3-24.el8
python3-pysocks 1.6.8-3.el8
python3-requests 2.20.0-3.el8_8
python3-setuptools 39.2.0-8.el8_10
python3-setuptools-wheel 39.2.0-8.el8_10
python3-six 1.11.0-8.el8
python3-urllib3 1.24.2-8.el8_10
python3.11 3.11.9-7.el8_10
python3.11-aiodns 3.1.1-1.el8ap
python3.11-aiohttp 3.9.5-1.el8ap
python3.11-aiosignal 1.3.1-1.el8ap
python3.11-ansible-compat 24.9.0-1.el8ap
python3.11-ansible-pylibssh 1.2.2-1.el8ap
python3.11-ansible-runner 2.4.0-1.el8ap
python3.11-async-timeout 4.0.3-2.el8ap
python3.11-attrs 22.2.0-1.el8ap
python3.11-azure-core 1.29.7-1.el8ap
python3.11-black 24.4.2-2.el8ap
python3.11-boto3 1.34.30-1.el8ap
python3.11-botocore 1.34.30-1.el8ap
python3.11-bracex 2.4-1.el8ap
python3.11-brotli 1.1.0-1.el8ap
python3.11-cachetools 5.3.2-1.el8ap
python3.11-certifi 2023.5.7-1.el8ap
python3.11-cffi 1.15.1-1.el8
python3.11-chardet 5.2.0-2.el8ap
python3.11-charset-normalizer 2.1.0-1.el8
python3.11-click 8.1.7-1.el8ap
python3.11-commonmark 0.9.1-6.el8ap
python3.11-cryptography 42.0.5-1.el8ap
python3.11-daemon 2.3.2-1.el8ap
python3.11-dateutil 2.8.2-2.el8ap
python3.11-deprecated 1.2.14-1.el8ap
python3.11-distlib 0.3.8-1.el8ap
python3.11-distro 1.9.0-1.el8ap
python3.11-docutils 0.20.1-2.el8ap
python3.11-dpath 2.1.6-1.el8ap
python3.11-filelock 3.13.1-1.el8ap
python3.11-frozenlist 1.4.0-1.el8ap
python3.11-gnupg 0.5.2-1.el8ap
python3.11-google-auth 2.27.0-1.el8ap
python3.11-grpcio 1.58.3-1.el8ap
python3.11-idna 3.4-1.el8
python3.11-importlib-metadata 6.0.1-2.el8ap
python3.11-isodate 0.6.1-2.el8ap
python3.11-jinja2 3.1.4-1.el8ap
python3.11-jmespath 1.0.1-2.el8ap
python3.11-jsonschema 4.21.1-1.el8ap
python3.11-jsonschema-specifications 2023.12.1-1.el8ap
python3.11-libs 3.11.9-7.el8_10
python3.11-lockfile 0.12.2-2.el8ap
python3.11-lxml 4.9.2-4.el8
python3.11-markupsafe 2.1.5-1.el8ap
python3.11-multidict 6.0.4-1.el8ap
python3.11-mypy-extensions 1.0.0-1.el8ap
python3.11-netaddr 1.2.1-1.el8ap
python3.11-oauthlib 3.2.2-1.el8ap
python3.11-packaging 23.2-1.el8ap
python3.11-pathspec 0.12.1-1.el8ap
python3.11-pbr 6.0.0-2.el8ap
python3.11-pexpect 4.9.0-1.el8ap
python3.11-pip 22.3.1-5.el8
python3.11-pip-wheel 22.3.1-5.el8
python3.11-platformdirs 4.2.0-1.el8ap
python3.11-ply 3.11-1.el8
python3.11-protobuf 4.21.12-2.el8ap
python3.11-psycopg 3.1.17-3.el8ap
python3.11-ptyprocess 0.7.0-1.el8ap
python3.11-pyOpenSSL 24.1.0-1.el8ap
python3.11-pyasn1 0.5.1-1.el8ap
python3.11-pyasn1-modules 0.3.0-1.el8ap
python3.11-pycares 4.4.0-2.el8ap
python3.11-pycparser 2.20-1.el8
python3.11-pygments 2.17.2-2.el8ap
python3.11-pyjwt 2.7.0-2.el8ap
python3.11-pysocks 1.7.1-1.el8
python3.11-pytz 2024.1-1.el8ap
python3.11-pyyaml 6.0-1.el8
python3.11-referencing 0.35.1-1.el8ap
python3.11-requests 2.31.0-2.el8ap
python3.11-requests-oauthlib 1.3.1-1.el8ap
python3.11-resolvelib 1.0.1-1.el8ap
python3.11-rich 13.1.0-1.el8ap
python3.11-rpds-py 0.18.1-1.el8ap
python3.11-rsa 4.9-2.el8ap
python3.11-ruamel-yaml 0.18.6-1.el8ap
python3.11-ruamel-yaml-clib 0.2.8-1.el8ap
python3.11-s3transfer 0.10.0-1.el8ap
python3.11-setuptools 65.5.1-3.el8_10
python3.11-setuptools-wheel 65.5.1-3.el8_10
python3.11-six 1.16.0-1.el8
python3.11-subprocess-tee 0.4.1-2.el8ap
python3.11-tabulate 0.9.0-3.el8ap
python3.11-typing-extensions 4.9.0-1.el8ap
python3.11-uamqp 1.6.8-1.el8ap
python3.11-urllib3 1.26.20-1.el8ap
python3.11-watchdog 5.0.2-1.el8ap
python3.11-wcmatch 8.5-1.el8ap
python3.11-websocket-client 1.7.0-2.el8ap
python3.11-wrapt 1.16.0-1.el8ap
python3.11-xxhash 3.4.1-1.el8ap
python3.11-yarl 1.9.2-1.el8ap
python3.11-zipp 3.19.2-1.el8ap
qemu-img 6.2.0-53.module+el8.10.0+22268+f82ccd96
readline 7.0-10.el8
receptor 1.4.8-3.el8ap
receptorctl 1.4.8-3.el8ap
redhat-release 8.10-0.3.el8
rootfiles 8.1-22.el8
rpm 4.14.3-31.el8
rpm-libs 4.14.3-31.el8
rsync 3.1.3-19.el8_7.1
sed 4.5-5.el8
setup 2.12.2-9.el8
shadow-utils 4.6-22.el8
shadow-utils-subid 4.6-22.el8
sos 4.7.2-2.el8_10
sqlite-libs 3.26.0-19.el8_9
sshpass 1.09-5.el8ap
subversion 1.10.2-5.module+el8.6.0+15157+188c9801
subversion-libs 1.10.2-5.module+el8.6.0+15157+188c9801
systemd 239-82.el8_10.2
systemd-libs 239-82.el8_10.2
systemd-pam 239-82.el8_10.2
tar 1.30-9.el8
tzdata 2024a-1.el8
unzip 6.0-46.el8
utf8proc 2.6.1-3.module+el8.7.0+15837+7cfc8c53
util-linux 2.32.1-46.el8
xz 5.2.4-4.el8_6
xz-libs 5.2.4-4.el8_6
yamllint 1.35.1-1.el8ap
zlib 1.2.11-25.el8
zstd 1.4.4-1.el8
```

</details>

<details><summary>Python packages: /usr (python3.11) (98)</summary>

```text
aiodns 3.1.1
aiohttp 3.9.5
aiosignal 1.3.1
ansible-compat 24.9.0
ansible-core 2.16.11
ansible-lint 24.9.0
ansible-pylibssh 1.2.2
ansible-runner 2.4.0
ansible-sign 0.1.1
async-timeout 4.0.3
attrs 22.2.0
awxkit 4.6.1
azure-core 1.29.7
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
commonmark 0.9.1
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
Jinja2 3.1.4
jmespath 1.0.1
jsonschema 4.21.1
jsonschema-specifications 2023.12.1
lockfile 0.12.2
lxml 4.9.2
MarkupSafe 2.1.5
multidict 6.0.4
mypy-extensions 1.0.0
netaddr 1.2.1
oauthlib 3.2.2
packaging 23.2
pathspec 0.12.1
pbr 6.0.0
pexpect 4.9.0
pip 22.3.1
platformdirs 4.2.0
ply 3.11
protobuf 4.21.12
psycopg 3.1.17
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
receptorctl 1.4.8
referencing 0.35.1
requests 2.31.0
requests-oauthlib 1.3.1
resolvelib 1.0.1
rich 13.1.0
rpds-py 0.18.1
rsa 4.9
ruamel.yaml 0.18.6
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
yarl 1.9.2
zipp 3.19.2
```

</details>

<details><summary>Python packages: /usr (python3.6) (8)</summary>

```text
chardet 3.0.4
idna 2.5
PySocks 1.6.8
requests 2.20.0
setuptools 39.2.0
six 1.11.0
sos 4.7.2
urllib3 1.24.2
```

</details>

<details><summary>Python packages: /usr/local (python3.11) (141)</summary>

```text
adal 1.2.7
aiobotocore 2.11.2
aioitertools 0.11.0
aiokafka 0.10.0
anyio 4.4.0
appdirs 1.4.4
applicationinsights 0.11.10
argcomplete 3.3.0
azure-cli-core 2.61.0
azure-cli-telemetry 1.1.0
azure-common 1.1.11
azure-containerregistry 1.1.0
azure-core 1.28.0
azure-identity 1.16.1
azure-iot-hub 2.6.1
azure-keyvault 4.2.0
azure-keyvault-certificates 4.7.0
azure-keyvault-keys 4.8.0
azure-keyvault-secrets 4.7.0
azure-mgmt-apimanagement 3.0.0
azure-mgmt-authorization 2.0.0
azure-mgmt-automation 1.0.0
azure-mgmt-batch 16.2.0
azure-mgmt-cdn 11.0.0
azure-mgmt-compute 30.6.0
azure-mgmt-containerinstance 9.0.0
azure-mgmt-containerregistry 9.1.0
azure-mgmt-containerservice 20.0.0
azure-mgmt-core 1.4.0
azure-mgmt-cosmosdb 6.4.0
azure-mgmt-datafactory 2.0.0
azure-mgmt-devtestlabs 9.0.0
azure-mgmt-dns 8.0.0
azure-mgmt-eventhub 10.1.0
azure-mgmt-hdinsight 9.0.0
azure-mgmt-iothub 2.2.0
azure-mgmt-keyvault 10.0.0
azure-mgmt-loganalytics 12.0.0
azure-mgmt-managedservices 6.0.0
azure-mgmt-managementgroups 1.0.0
azure-mgmt-marketplaceordering 1.1.0
azure-mgmt-monitor 3.0.0
azure-mgmt-network 19.1.0
azure-mgmt-notificationhubs 7.0.0
azure-mgmt-nspkg 2.0.0
azure-mgmt-privatedns 1.0.0
azure-mgmt-rdbms 10.2.0b12
azure-mgmt-recoveryservices 2.0.0
azure-mgmt-recoveryservicesbackup 3.0.0
azure-mgmt-redis 13.0.0
azure-mgmt-resource 21.1.0
azure-mgmt-search 8.0.0
azure-mgmt-servicebus 7.1.0
azure-mgmt-sql 3.0.1
azure-mgmt-storage 19.0.0
azure-mgmt-trafficmanager 1.0.0b1
azure-mgmt-web 6.1.0
azure-nspkg 2.0.0
azure-servicebus 7.12.1
azure-storage-blob 12.13.0
bcrypt 3.2.0
decorator 5.1.1
dnspython 2.6.1
dogpile.cache 1.1.2
gssapi 1.8.2
h11 0.14.0
h2 4.1.0
hpack 4.0.0
httpcore 1.0.5
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
krb5 0.5.0
kubernetes 29.0.0
microsoft-kiota-abstractions 1.3.3
microsoft-kiota-authentication-azure 1.0.0
microsoft-kiota-http 1.3.1
microsoft-kiota-serialization-json 1.2.0
microsoft-kiota-serialization-text 1.0.0
msal 1.28.0
msal-extensions 1.2.0b1
msgraph-core 1.1.0
msgraph-sdk 1.0.0
msrest 0.6.21
msrestazure 0.6.4
munch 2.5.0
ncclient 0.6.10
netifaces 0.10.9
nsx-policy-python-sdk 3.1.5.0.0
nsx-python-sdk 3.1.5.0.0
nsx-vmc-aws-integration-python-sdk 3.1.5.0.0
nsx-vmc-policy-python-sdk 3.1.5.0.0
ntlm-auth 1.5.0
openstacksdk 0.56.0
opentelemetry-api 1.25.0
opentelemetry-sdk 1.25.0
opentelemetry-semantic-conventions 0.46b0
os-service-types 1.7.0
ovirt-engine-sdk-python 4.5.2
ovirt-imageio 2.4.6
paramiko 2.8.1
pendulum 3.0.0
pkginfo 1.7.0
portalocker 1.7.1
psutil 5.9.1
pyang 2.5.3
pycurl 7.45.3
pykerberos 1.2.1
PyNaCl 1.4.0
pypsrp 0.5.0
pyspnego 0.9.0
pyvmomi 7.0.2
pywinrm 0.4.1
requests-credssp 2.0.0
requests-ntlm 1.1.0
requestsexceptions 1.4.0
sansldap 0.1.0
scp 0.13.3
sniffio 1.3.1
std-uritemplate 1.0.2
stevedore 3.3.0
suds 1.1.2
textfsm 0.4.1
time-machine 2.14.2
toml 0.10.2
ttp 0.6.0
tzdata 2024.1
vapi-client-bindings 3.8.0
vapi-common-client 2.34.0
vapi-runtime 2.34.0
vmc-client-bindings 1.59.0
vmc-draas-client-bindings 1.18.0
vSphere-Automation-SDK 1.76.0
xmltodict 0.12.0
```

</details>

<details><summary>Ansible collections (57)</summary>

```text
amazon.aws 7.4.0
ansible.controller 4.6.1
ansible.eda 2.1.0
ansible.hub 1.0.0
ansible.netcommon 7.1.0
ansible.network 4.0.0
ansible.platform 2.5.0
ansible.posix 1.5.4
ansible.scm 3.0.0
ansible.security 3.0.0
ansible.snmp 3.0.0
ansible.utils 5.1.0
ansible.windows 1.14.0
ansible.yang 3.0.0
arista.eos 10.0.0
azure.azcollection 2.5.0
cisco.asa 6.0.0
cisco.ios 9.0.1
cisco.iosxr 10.1.0
cisco.nxos 9.2.1
cloud.common 3.0.0
cloud.terraform 2.0.0
community.vmware 1.9.0
frr.frr 2.0.2
google.cloud 1.0.2
ibm.qradar 4.0.0
junipernetworks.junos 9.1.0
kubernetes.core 3.0.1
microsoft.ad 1.1.0
openstack.cloud 1.5.0
openvswitch.openvswitch 2.1.1
redhat.amq_broker 1.3.0
redhat.amq_streams 1.0.0
redhat.data_grid 1.3.1
redhat.eap 1.3.1
redhat.insights 1.2.2
redhat.jbcs 1.0.1
redhat.jws 2.0.0
redhat.openshift 3.0.1
redhat.openshift_virtualization 1.2.3
redhat.redhat_csp_download 1.2.2
redhat.rhbk 2.2.2
redhat.rhel_idm 1.10.0
redhat.rhel_system_roles 1.21.1
redhat.rhv 2.4.2
redhat.runtimes_common 1.1.3
redhat.sap_install 1.2.1
redhat.satellite 3.10.0
redhat.satellite_operations 1.3.0
redhat.sso 1.3.0
sap.sap_operations 1.0.4
servicenow.itsm 2.6.3
splunk.es 4.0.0
trendmicro.deepsec 4.0.0
vmware.vmware 1.3.0
vmware.vmware_rest 3.0.1
vyos.vyos 4.0.2
```

</details>

[Back to top](#contents)

### gateway-proxy-rhel8

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/gateway-proxy-rhel8.tar.gz` |
| Labels `version` / `release` | `2.5.0` / `22` |
| Image ID | `sha256:6e53887286a75ce1f566ac21b4e92c3a755e6000925461767a18b9f595adf2bb` |
| Build date | 2024-10-02T00:26:48 |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | N/A |
| Ansible Core | N/A |

<details><summary>RPM packages (162)</summary>

```text
acl 2.2.53-3.el8
ansible-automation-platform-common 2.5-2.el8ap
ansible-automation-platform-selinux 0.2-3.el8ap
audit-libs 3.1.2-1.el8
automation-gateway-config 2.5.0-1.1.el8ap
automation-gateway-proxy-server 2.5.0-1.el8ap
basesystem 11-5.el8
bash 4.4.20-5.el8
brotli 1.0.6-3.el8
bzip2-libs 1.0.6-26.el8
ca-certificates 2024.2.69_v8.0.303-80.0.el8_10
checkpolicy 2.9-1.el8
chkconfig 1.19.2-1.el8
coreutils-single 8.30-15.el8
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crypto-policies 20230731-1.git3177e06.el8
cryptsetup-libs 2.3.7-7.el8
curl 7.61.1-34.el8_10.2
cyrus-sasl-lib 2.1.27-6.el8_5
dbus 1.12.8-26.el8
dbus-common 1.12.8-26.el8
dbus-daemon 1.12.8-26.el8
dbus-libs 1.12.8-26.el8
dbus-tools 1.12.8-26.el8
device-mapper 1.02.181-14.el8
device-mapper-libs 1.02.181-14.el8
diffutils 3.6-6.el8
dumb-init 1.2.5-3.el8ap
elfutils-default-yama-scope 0.190-2.el8
elfutils-libelf 0.190-2.el8
elfutils-libs 0.190-2.el8
expat 2.2.5-15.el8_10
file-libs 5.33-26.el8
filesystem 3.8-6.el8
gawk 4.2.1-4.el8
gdbm 1.18-2.el8
gdbm-libs 1.18-2.el8
glib2 2.56.4-162.el8
glibc 2.28-251.el8_10.5
glibc-common 2.28-251.el8_10.5
glibc-langpack-en 2.28-251.el8_10.5
glibc-minimal-langpack 2.28-251.el8_10.5
gmp 6.1.2-11.el8
gnupg2 2.2.20-3.el8_6
gnutls 3.6.16-8.el8_9.3
gobject-introspection 1.56.1-1.el8
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
gzip 1.9-13.el8_5
info 6.5-7.el8
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
kmod-libs 25-20.el8
krb5-libs 1.18.2-29.el8_10
langpacks-en 1.0-12.el8
libacl 2.2.53-3.el8
libarchive 3.3.3-5.el8
libassuan 2.5.1-3.el8
libattr 2.4.48-3.el8
libblkid 2.32.1-46.el8
libcap 2.48-6.el8_9
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-5.el8
libcurl 7.61.1-34.el8_10.2
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-20.el8_10
libfdisk 2.32.1-46.el8
libffi 3.1-24.el8
libgcc 8.5.0-22.el8_10
libgcrypt 1.8.5-7.el8_6
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libksba 1.3.5-9.el8_7
libmodulemd 2.13.0-1.el8
libmount 2.32.1-46.el8
libnghttp2 1.33.0-6.el8_10.1
libnsl2 1.2.0-2.20180605git4a062cf.el8
libpeas 1.22.0-6.el8
libpsl 0.20.2-6.el8
libpwquality 1.4.4-6.el8
librepo 1.14.2-5.el8
librhsm 0.0.3-5.el8
libseccomp 2.5.2-1.el8
libselinux 2.9-8.el8
libselinux-utils 2.9-8.el8
libsemanage 2.9-9.el8_6
libsepol 2.9-3.el8
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-46.el8
libsolv 0.7.20-6.el8
libssh 0.9.6-14.el8
libssh-config 0.9.6-14.el8
libstdc++ 8.5.0-22.el8_10
libtasn1 4.13-4.el8_7
libtirpc 1.1.4-12.el8_10
libunistring 0.9.9-3.el8
libusbx 1.0.23-4.el8
libutempter 1.1.6-14.el8
libuuid 2.32.1-46.el8
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-18.el8_10.1
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-3.el8_4
microdnf 3.8.0-2.el8
mpfr 3.1.6-1.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
npth 1.5-4.el8
openldap 2.4.46-19.el8_10
openssl-libs 1.1.1k-12.el8_9
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-34.el8_10
pcre 8.42-6.el8
pcre2 10.32-3.el8_6
platform-python 3.6.8-67.el8_10
platform-python-setuptools 39.2.0-8.el8_10
policycoreutils 2.9-26.el8_10
policycoreutils-python-utils 2.9-26.el8_10
popt 1.18-1.el8
publicsuffix-list-dafsa 20180723-1.el8
python3-audit 3.1.2-1.el8
python3-cffi 1.11.5-6.el8
python3-cryptography 3.2.1-7.el8_9
python3-libs 3.6.8-67.el8_10
python3-libselinux 2.9-8.el8
python3-libsemanage 2.9-9.el8_6
python3-pip-wheel 9.0.3-24.el8
python3-ply 3.9-9.el8
python3-policycoreutils 2.9-26.el8_10
python3-pycparser 2.14-14.el8
python3-setools 4.3.0-5.el8
python3-setuptools-wheel 39.2.0-8.el8_10
python3-six 1.11.0-8.el8
readline 7.0-10.el8
redhat-release 8.10-0.3.el8
rootfiles 8.1-22.el8
rpm 4.14.3-31.el8
rpm-libs 4.14.3-31.el8
rpm-plugin-selinux 4.14.3-31.el8
sed 4.5-5.el8
selinux-policy 3.14.3-139.el8_10
selinux-policy-minimum 3.14.3-139.el8_10
setup 2.12.2-9.el8
shadow-utils 4.6-22.el8
sqlite-libs 3.26.0-19.el8_9
systemd 239-82.el8_10.2
systemd-libs 239-82.el8_10.2
systemd-pam 239-82.el8_10.2
tzdata 2024a-1.el8
util-linux 2.32.1-46.el8
xz-libs 5.2.4-4.el8_6
zlib 1.2.11-25.el8
```

</details>

<details><summary>Python packages: /usr (python3.6) (9)</summary>

```text
cffi 1.11.5
cryptography 3.2.1
ply 3.9
pycparser 2.14
selinux 2.9
sepolicy 1.1
setools 4.3.0
setuptools 39.2.0
six 1.11.0
```

</details>

[Back to top](#contents)

### gateway-rhel8

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/gateway-rhel8.tar.gz` |
| Labels `version` / `release` | `2.5.0` / `58` |
| Image ID | `sha256:f768a98a64be61d4c7a9d8624f0b9efacfa617f1a3c0d29907eb7a5cc77de20b` |
| Build date | 2024-10-02T00:27:42 |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | 3.11 |
| Ansible Core | N/A |

<details><summary>RPM packages (248)</summary>

```text
acl 2.2.53-3.el8
ansible-automation-platform-common 2.5-2.el8ap
ansible-automation-platform-selinux 0.2-3.el8ap
audit-libs 3.1.2-1.el8
automation-gateway-server 2.5.0-1.1.el8ap
basesystem 11-5.el8
bash 4.4.20-5.el8
brotli 1.0.6-3.el8
bzip2-libs 1.0.6-26.el8
ca-certificates 2024.2.69_v8.0.303-80.0.el8_10
checkpolicy 2.9-1.el8
chkconfig 1.19.2-1.el8
coreutils-single 8.30-15.el8
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crypto-policies 20230731-1.git3177e06.el8
cryptsetup-libs 2.3.7-7.el8
curl 7.61.1-34.el8_10.2
cyrus-sasl-lib 2.1.27-6.el8_5
dbus 1.12.8-26.el8
dbus-common 1.12.8-26.el8
dbus-daemon 1.12.8-26.el8
dbus-libs 1.12.8-26.el8
dbus-tools 1.12.8-26.el8
device-mapper 1.02.181-14.el8
device-mapper-libs 1.02.181-14.el8
diffutils 3.6-6.el8
dumb-init 1.2.5-3.el8ap
elfutils-default-yama-scope 0.190-2.el8
elfutils-libelf 0.190-2.el8
elfutils-libs 0.190-2.el8
expat 2.2.5-15.el8_10
file-libs 5.33-26.el8
filesystem 3.8-6.el8
gawk 4.2.1-4.el8
gdbm 1.18-2.el8
gdbm-libs 1.18-2.el8
glib2 2.56.4-162.el8
glibc 2.28-251.el8_10.5
glibc-common 2.28-251.el8_10.5
glibc-langpack-en 2.28-251.el8_10.5
glibc-minimal-langpack 2.28-251.el8_10.5
gmp 6.1.2-11.el8
gnupg2 2.2.20-3.el8_6
gnutls 3.6.16-8.el8_9.3
gobject-introspection 1.56.1-1.el8
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
gzip 1.9-13.el8_5
info 6.5-7.el8
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
kmod-libs 25-20.el8
krb5-libs 1.18.2-29.el8_10
langpacks-en 1.0-12.el8
libacl 2.2.53-3.el8
libarchive 3.3.3-5.el8
libassuan 2.5.1-3.el8
libattr 2.4.48-3.el8
libblkid 2.32.1-46.el8
libcap 2.48-6.el8_9
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-5.el8
libcurl 7.61.1-34.el8_10.2
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-20.el8_10
libfdisk 2.32.1-46.el8
libffi 3.1-24.el8
libgcc 8.5.0-22.el8_10
libgcrypt 1.8.5-7.el8_6
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libksba 1.3.5-9.el8_7
libmodulemd 2.13.0-1.el8
libmount 2.32.1-46.el8
libnghttp2 1.33.0-6.el8_10.1
libnsl2 1.2.0-2.20180605git4a062cf.el8
libpeas 1.22.0-6.el8
libpq 13.11-1.el8
libpsl 0.20.2-6.el8
libpwquality 1.4.4-6.el8
librepo 1.14.2-5.el8
librhsm 0.0.3-5.el8
libseccomp 2.5.2-1.el8
libselinux 2.9-8.el8
libselinux-utils 2.9-8.el8
libsemanage 2.9-9.el8_6
libsepol 2.9-3.el8
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-46.el8
libsolv 0.7.20-6.el8
libssh 0.9.6-14.el8
libssh-config 0.9.6-14.el8
libstdc++ 8.5.0-22.el8_10
libtasn1 4.13-4.el8_7
libtirpc 1.1.4-12.el8_10
libtool-ltdl 2.4.6-25.el8
libunistring 0.9.9-3.el8
libusbx 1.0.23-4.el8
libutempter 1.1.6-14.el8
libuuid 2.32.1-46.el8
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-18.el8_10.1
libxslt 1.1.32-6.el8
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-3.el8_4
microdnf 3.8.0-2.el8
mpdecimal 2.5.1-3.el8
mpfr 3.1.6-1.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
nginx 1.22.1-1.module+el8.8.0+20355+6d9c8a63.1
nginx-filesystem 1.22.1-1.module+el8.8.0+20355+6d9c8a63.1
npth 1.5-4.el8
openldap 2.4.46-19.el8_10
openssl 1.1.1k-12.el8_9
openssl-libs 1.1.1k-12.el8_9
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-34.el8_10
pcre 8.42-6.el8
pcre2 10.32-3.el8_6
platform-python 3.6.8-67.el8_10
platform-python-setuptools 39.2.0-8.el8_10
policycoreutils 2.9-26.el8_10
policycoreutils-python-utils 2.9-26.el8_10
popt 1.18-1.el8
postgresql 15.8-1.module+el8.10.0+22212+a51fe170
postgresql-private-libs 15.8-1.module+el8.10.0+22212+a51fe170
publicsuffix-list-dafsa 20180723-1.el8
python3-audit 3.1.2-1.el8
python3-cffi 1.11.5-6.el8
python3-cryptography 3.2.1-7.el8_9
python3-libs 3.6.8-67.el8_10
python3-libselinux 2.9-8.el8
python3-libsemanage 2.9-9.el8_6
python3-pip-wheel 9.0.3-24.el8
python3-ply 3.9-9.el8
python3-policycoreutils 2.9-26.el8_10
python3-pycparser 2.14-14.el8
python3-setools 4.3.0-5.el8
python3-setuptools-wheel 39.2.0-8.el8_10
python3-six 1.11.0-8.el8
python3.11 3.11.9-7.el8_10
python3.11-argon2-cffi 23.1.0-1.el8ap
python3.11-argon2-cffi-bindings 21.2.0-1.el8ap
python3.11-asgiref 3.7.2-1.el8ap
python3.11-async-timeout 4.0.3-2.el8ap
python3.11-attrs 22.2.0-1.el8ap
python3.11-certifi 2023.5.7-1.el8ap
python3.11-cffi 1.15.1-1.el8
python3.11-charset-normalizer 2.1.0-1.el8
python3.11-cryptography 42.0.5-1.el8ap
python3.11-defusedxml 0.7.1-4.el8ap
python3.11-django 4.2.16-1.el8ap
python3.11-django-ansible-base 2.5.1-1.el8ap
python3.11-django-ansible-base+api_documentation 2.5.1-1.el8ap
python3.11-django-ansible-base+authentication 2.5.1-1.el8ap
python3.11-django-ansible-base+oauth2_provider 2.5.1-1.el8ap
python3.11-django-ansible-base+redis_client 2.5.1-1.el8ap
python3.11-django-ansible-base+rest_filters 2.5.1-1.el8ap
python3.11-django-auth-ldap 4.0.0-2.el8ap
python3.11-django-crum 0.7.9-2.el8ap
python3.11-django-dynamic-preferences 1.16.0-1.el8ap
python3.11-django-extensions 3.2.3-2.el8ap
python3.11-django-oauth-toolkit 2.3.0-1.el8ap
python3.11-django-redis 5.4.0-1.el8ap
python3.11-django-split-settings 1.2.0-2.el8ap
python3.11-djangorestframework 3.15.1-1.el8ap
python3.11-drf-spectacular 0.26.5-2.el8ap
python3.11-googleapis-common-protos 1.59.1-2.el8ap
python3.11-grpcio 1.58.3-1.el8ap
python3.11-grpcio-tools 1.58.3-1.el8ap
python3.11-idna 3.4-1.el8
python3.11-inflection 0.5.1-4.el8ap
python3.11-isodate 0.6.1-2.el8ap
python3.11-jsonschema 4.21.1-1.el8ap
python3.11-jsonschema-specifications 2023.12.1-1.el8ap
python3.11-jwcrypto 1.5.6-1.el8ap
python3.11-ldap 3.4.4-1.el8ap
python3.11-libs 3.11.9-7.el8_10
python3.11-lxml 4.9.2-4.el8
python3.11-netaddr 1.2.1-1.el8ap
python3.11-oauthlib 3.2.2-1.el8ap
python3.11-opentelemetry-proto 1.18.0-2.el8ap
python3.11-persisting-theory 1.0-2.el8ap
python3.11-pip-wheel 22.3.1-5.el8
python3.11-ply 3.11-1.el8
python3.11-protobuf 4.21.12-2.el8ap
python3.11-psycopg 3.1.17-3.el8ap
python3.11-pyasn1 0.5.1-1.el8ap
python3.11-pyasn1-modules 0.3.0-1.el8ap
python3.11-pycparser 2.20-1.el8
python3.11-pyjwt 2.7.0-2.el8ap
python3.11-pyrad 2.4-2.el8ap
python3.11-python3-openid 3.2.0-3.el8ap
python3.11-python3-saml 1.16.0-2.el8ap
python3.11-pyyaml 6.0-1.el8
python3.11-redis 4.6.0-2.el8ap
python3.11-referencing 0.35.1-1.el8ap
python3.11-requests 2.31.0-2.el8ap
python3.11-requests-oauthlib 1.3.1-1.el8ap
python3.11-rpds-py 0.18.1-1.el8ap
python3.11-setuptools 65.5.1-3.el8_10
python3.11-setuptools-wheel 65.5.1-3.el8_10
python3.11-six 1.16.0-1.el8
python3.11-social-auth-app-django 5.4.1-1.el8ap
python3.11-social-auth-core 4.5.4-1.el8ap
python3.11-sqlparse 0.5.0-1.el8ap
python3.11-tabulate 0.9.0-3.el8ap
python3.11-tacacs-plus 2.6-2.el8ap
python3.11-typing-extensions 4.9.0-1.el8ap
python3.11-uritemplate 4.1.1-3.el8ap
python3.11-urllib3 1.26.20-1.el8ap
python3.11-xds-protos 1.58.0-2.el8ap
python3.11-xmlsec 1.3.13-2.el8ap
readline 7.0-10.el8
redhat-logos-httpd 84.5-2.el8
redhat-release 8.10-0.3.el8
rootfiles 8.1-22.el8
rpm 4.14.3-31.el8
rpm-libs 4.14.3-31.el8
rpm-plugin-selinux 4.14.3-31.el8
sed 4.5-5.el8
selinux-policy 3.14.3-139.el8_10
selinux-policy-minimum 3.14.3-139.el8_10
setup 2.12.2-9.el8
shadow-utils 4.6-22.el8
sqlite-libs 3.26.0-19.el8_9
supervisor 4.2.5-1.el8ap
systemd 239-82.el8_10.2
systemd-libs 239-82.el8_10.2
systemd-pam 239-82.el8_10.2
tzdata 2024a-1.el8
util-linux 2.32.1-46.el8
uwsgi 2.0.23-1.el8ap
xmlsec1 1.2.25-8.el8_10
xmlsec1-openssl 1.2.25-8.el8_10
xz-libs 5.2.4-4.el8_6
zlib 1.2.11-25.el8
```

</details>

<details><summary>Python packages: /usr (python3.11) (66)</summary>

```text
aap-gateway 2.5.0.dev1
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
Django 4.2.16
django-ansible-base 2.5.1
django-auth-ldap 4.0.0
django-crum 0.7.9
django-dynamic-preferences 1.16.0
django-extensions 3.2.3
django-oauth-toolkit 2.3.0
django-redis 5.4.0
django-split-settings 1.2.0
djangorestframework 3.15.1
drf-spectacular 0.26.5
googleapis-common-protos 1.59.1
grpcio 1.58.3
grpcio-tools 1.58.3
idna 3.4
inflection 0.5.1
isodate 0.6.1
jsonschema 4.21.1
jsonschema-specifications 2023.12.1
jwcrypto 1.5.6
lxml 4.9.2
netaddr 1.2.1
oauthlib 3.2.2
opentelemetry-proto 1.18.0
persisting-theory 1.0
ply 3.11
protobuf 4.21.12
psycopg 3.1.17
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
referencing 0.35.1
requests 2.31.0
requests-oauthlib 1.3.1
rpds-py 0.18.1
setuptools 65.5.1
six 1.16.0
social-auth-app-django 5.4.1
social-auth-core 4.5.4
sqlparse 0.5.0
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

<details><summary>Python packages: /usr (python3.6) (9)</summary>

```text
cffi 1.11.5
cryptography 3.2.1
ply 3.9
pycparser 2.14
selinux 2.9
sepolicy 1.1
setools 4.3.0
setuptools 39.2.0
six 1.11.0
```

</details>

[Back to top](#contents)

### hub-rhel8

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/hub-rhel8.tar.gz` |
| Labels `version` / `release` | `4.10.0` / `207` |
| Image ID | `sha256:b9a82993ab1cac226de8e16700dc751096f8fc5a385db703bec2e7af9467af45` |
| Build date | 2024-10-02T00:27:43 |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | 3.11 |
| Ansible Core | 2.16.11 |

<details><summary>RPM packages (362)</summary>

```text
acl 2.2.53-3.el8
ansible-automation-platform-common 2.5-2.el8ap
ansible-automation-platform-selinux 0.2-3.el8ap
ansible-builder 3.1.0-1.el8ap
ansible-core 2.16.11-1.el8ap
ansible-lint 24.9.0-1.el8ap
ansible-test 2.16.11-1.el8ap
audit-libs 3.1.2-1.el8
automation-hub 4.10.0-1.el8ap
basesystem 11-5.el8
bash 4.4.20-5.el8
bindep 2.11.0-2.el8ap
brotli 1.0.6-3.el8
bzip2-libs 1.0.6-26.el8
ca-certificates 2024.2.69_v8.0.303-80.0.el8_10
chkconfig 1.19.2-1.el8
container-selinux 2.229.0-2.module+el8.10.0+22283+6d6d094a
containers-common 1-82.module+el8.10.0+22283+6d6d094a
coreutils-single 8.30-15.el8
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
criu 3.18-5.module+el8.10.0+22283+6d6d094a
crypto-policies 20230731-1.git3177e06.el8
cryptsetup-libs 2.3.7-7.el8
curl 7.61.1-34.el8_10.2
cyrus-sasl-lib 2.1.27-6.el8_5
dbus 1.12.8-26.el8
dbus-common 1.12.8-26.el8
dbus-daemon 1.12.8-26.el8
dbus-libs 1.12.8-26.el8
dbus-tools 1.12.8-26.el8
device-mapper 1.02.181-14.el8
device-mapper-libs 1.02.181-14.el8
diffutils 3.6-6.el8
elfutils-default-yama-scope 0.190-2.el8
elfutils-libelf 0.190-2.el8
elfutils-libs 0.190-2.el8
expat 2.2.5-15.el8_10
file-libs 5.33-26.el8
filesystem 3.8-6.el8
gawk 4.2.1-4.el8
gdbm 1.18-2.el8
gdbm-libs 1.18-2.el8
git-core 2.43.5-1.el8_10
glib2 2.56.4-162.el8
glibc 2.28-251.el8_10.5
glibc-common 2.28-251.el8_10.5
glibc-minimal-langpack 2.28-251.el8_10.5
gmp 6.1.2-11.el8
gnupg2 2.2.20-3.el8_6
gnutls 3.6.16-8.el8_9.3
gobject-introspection 1.56.1-1.el8
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
gzip 1.9-13.el8_5
info 6.5-7.el8
jq 1.6-9.el8_10
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
kmod-libs 25-20.el8
krb5-libs 1.18.2-29.el8_10
langpacks-en 1.0-12.el8
less 530-3.el8_10
libacl 2.2.53-3.el8
libarchive 3.3.3-5.el8
libassuan 2.5.1-3.el8
libattr 2.4.48-3.el8
libblkid 2.32.1-46.el8
libcap 2.48-6.el8_9
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-5.el8
libcurl 7.61.1-34.el8_10.2
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-20.el8_10
libedit 3.1-23.20170329cvs.el8
libestr 0.1.10-3.el8
libfastjson 0.99.9-2.el8
libfdisk 2.32.1-46.el8
libffi 3.1-24.el8
libgcc 8.5.0-22.el8_10
libgcrypt 1.8.5-7.el8_6
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libjpeg-turbo 1.5.3-12.el8
libksba 1.3.5-9.el8_7
libmodulemd 2.13.0-1.el8
libmount 2.32.1-46.el8
libnet 1.1.6-15.el8
libnghttp2 1.33.0-6.el8_10.1
libnl3 3.7.0-1.el8
libnsl2 1.2.0-2.20180605git4a062cf.el8
libpeas 1.22.0-6.el8
libpq 13.11-1.el8
libpsl 0.20.2-6.el8
libpwquality 1.4.4-6.el8
librepo 1.14.2-5.el8
librhsm 0.0.3-5.el8
libseccomp 2.5.2-1.el8
libsecret 0.18.6-1.el8
libselinux 2.9-8.el8
libselinux-utils 2.9-8.el8
libsemanage 2.9-9.el8_6
libsepol 2.9-3.el8
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-46.el8
libsolv 0.7.20-6.el8
libssh 0.9.6-14.el8
libssh-config 0.9.6-14.el8
libstdc++ 8.5.0-22.el8_10
libtasn1 4.13-4.el8_7
libtirpc 1.1.4-12.el8_10
libunistring 0.9.9-3.el8
libusbx 1.0.23-4.el8
libutempter 1.1.6-14.el8
libuuid 2.32.1-46.el8
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-18.el8_10.1
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
logrotate 3.14.0-6.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-3.el8_4
mailcap 2.1.48-3.el8
microdnf 3.8.0-2.el8
mpdecimal 2.5.1-3.el8
mpfr 3.1.6-1.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
npth 1.5-4.el8
oniguruma 6.9.7.1-2.el8ap
openldap 2.4.46-19.el8_10
openssh 8.0p1-25.el8_10
openssh-clients 8.0p1-25.el8_10
openssl 1.1.1k-12.el8_9
openssl-libs 1.1.1k-12.el8_9
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-34.el8_10
pcre 8.42-6.el8
pcre2 10.32-3.el8_6
pinentry 1.1.0-2.el8
platform-python 3.6.8-67.el8_10
platform-python-setuptools 39.2.0-8.el8_10
policycoreutils 2.9-26.el8_10
popt 1.18-1.el8
protobuf-c 1.3.0-8.el8
publicsuffix-list-dafsa 20180723-1.el8
pulpcore-selinux 2.0.1-1.el8ap
python3-cffi 1.11.5-6.el8
python3-chardet 3.0.4-7.el8
python3-cryptography 3.2.1-7.el8_9
python3-idna 2.5-7.el8_10
python3-libs 3.6.8-67.el8_10
python3-pip-wheel 9.0.3-24.el8
python3-ply 3.9-9.el8
python3-pycparser 2.14-14.el8
python3-pysocks 1.6.8-3.el8
python3-requests 2.20.0-3.el8_8
python3-setuptools 39.2.0-8.el8_10
python3-setuptools-wheel 39.2.0-8.el8_10
python3-six 1.11.0-8.el8
python3-urllib3 1.24.2-8.el8_10
python3.11 3.11.9-7.el8_10
python3.11-aiodns 3.1.1-1.el8ap
python3.11-aiofiles 23.2.1-1.el8ap
python3.11-aiohttp 3.9.5-1.el8ap
python3.11-aiosignal 1.3.1-1.el8ap
python3.11-ansible-compat 24.9.0-1.el8ap
python3.11-asgiref 3.7.2-1.el8ap
python3.11-async-lru 2.0.4-1.el8ap
python3.11-async-timeout 4.0.3-2.el8ap
python3.11-asyncio-throttle 1.0.2-4.el8ap
python3.11-attrs 22.2.0-1.el8ap
python3.11-azure-core 1.29.7-1.el8ap
python3.11-azure-storage-blob 12.19.0-1.el8ap
python3.11-backoff 2.2.1-1.el8ap
python3.11-black 24.4.2-2.el8ap
python3.11-boto3 1.34.30-1.el8ap
python3.11-botocore 1.34.30-1.el8ap
python3.11-bracex 2.4-1.el8ap
python3.11-brotli 1.1.0-1.el8ap
python3.11-certifi 2023.5.7-1.el8ap
python3.11-cffi 1.15.1-1.el8
python3.11-charset-normalizer 2.1.0-1.el8
python3.11-click 8.1.7-1.el8ap
python3.11-commonmark 0.9.1-6.el8ap
python3.11-cryptography 42.0.5-1.el8ap
python3.11-dateutil 2.8.2-2.el8ap
python3.11-defusedxml 0.7.1-4.el8ap
python3.11-deprecated 1.2.14-1.el8ap
python3.11-diff-match-patch 20230430-1.el8ap
python3.11-distro 1.9.0-1.el8ap
python3.11-django 4.2.16-1.el8ap
python3.11-django-ansible-base 2.5.1-1.el8ap
python3.11-django-ansible-base+jwt_consumer 2.5.1-1.el8ap
python3.11-django-auth-ldap 4.0.0-2.el8ap
python3.11-django-crum 0.7.9-2.el8ap
python3.11-django-filter 23.5-1.el8ap
python3.11-django-guid 3.4.0-1.el8ap
python3.11-django-import-export 3.3.6-2.el8ap
python3.11-django-ipware 3.0.7-3.el8ap
python3.11-django-lifecycle 1.1.2-1.el8ap
python3.11-django-picklefield 3.1-1.el8ap
python3.11-django-prometheus 2.3.1-2.el8ap
python3.11-django-split-settings 1.2.0-2.el8ap
python3.11-django-storages 1.14.2-2.el8ap
python3.11-django-storages+azure 1.14.2-2.el8ap
python3.11-django-storages+s3 1.14.2-2.el8ap
python3.11-djangorestframework 3.15.1-1.el8ap
python3.11-djangorestframework-queryfields 1.1.0-1.el8ap
python3.11-drf-access-policy 1.5.0-1.el8ap
python3.11-drf-nested-routers 0.93.5-1.el8ap
python3.11-drf-spectacular 0.26.5-2.el8ap
python3.11-dynaconf 3.2.6-1.el8ap
python3.11-et-xmlfile 1.1.0-3.el8ap
python3.11-filelock 3.13.1-1.el8ap
python3.11-flake8 6.1.0-2.el8ap
python3.11-frozenlist 1.4.0-1.el8ap
python3.11-galaxy-importer 0.4.25-1.el8ap
python3.11-galaxy-ng 4.10.0-1.el8ap
python3.11-gitdb 4.0.11-1.el8ap
python3.11-gitpython 3.1.41-1.el8ap
python3.11-gnupg 0.5.2-1.el8ap
python3.11-googleapis-common-protos 1.59.1-2.el8ap
python3.11-grpcio 1.58.3-1.el8ap
python3.11-gunicorn 22.0.0-1.el8ap
python3.11-idna 3.4-1.el8
python3.11-importlib-metadata 6.0.1-2.el8ap
python3.11-inflection 0.5.1-4.el8ap
python3.11-insights-analytics-collector 0.3.2-2.el8ap
python3.11-isodate 0.6.1-2.el8ap
python3.11-jinja2 3.1.4-1.el8ap
python3.11-jmespath 1.0.1-2.el8ap
python3.11-jq 1.6.0-1.el8ap
python3.11-json-stream 2.3.2-1.el8ap
python3.11-json-stream-rs-tokenizer 0.4.26-1.el8ap
python3.11-jsonschema 4.21.1-1.el8ap
python3.11-jsonschema-specifications 2023.12.1-1.el8ap
python3.11-ldap 3.4.4-1.el8ap
python3.11-libs 3.11.9-7.el8_10
python3.11-markdown 3.5.2-1.el8ap
python3.11-markuppy 1.14-4.el8ap
python3.11-markupsafe 2.1.5-1.el8ap
python3.11-marshmallow 3.20.2-1.el8ap
python3.11-mccabe 0.7.0-2.el8ap
python3.11-multidict 6.0.4-1.el8ap
python3.11-mypy-extensions 1.0.0-1.el8ap
python3.11-nh3 0.2.18-1.el8ap
python3.11-oauthlib 3.2.2-1.el8ap
python3.11-odfpy 1.4.1-8.el8ap
python3.11-openpyxl 3.1.2-1.el8ap
python3.11-opentelemetry-api 1.18.0-2.el8ap
python3.11-opentelemetry-distro 0.39b0-6.el8ap
python3.11-opentelemetry-distro+otlp 0.39b0-6.el8ap
python3.11-opentelemetry-exporter-otlp 1.18.0-2.el8ap
python3.11-opentelemetry-exporter-otlp-proto-common 1.18.0-2.el8ap
python3.11-opentelemetry-exporter-otlp-proto-grpc 1.18.0-2.el8ap
python3.11-opentelemetry-exporter-otlp-proto-http 1.18.0-2.el8ap
python3.11-opentelemetry-instrumentation 0.39b0-6.el8ap
python3.11-opentelemetry-instrumentation-django 0.39b0-6.el8ap
python3.11-opentelemetry-instrumentation-wsgi 0.39b0-6.el8ap
python3.11-opentelemetry-proto 1.18.0-2.el8ap
python3.11-opentelemetry-sdk 1.18.0-2.el8ap
python3.11-opentelemetry-semantic-conventions 0.39b0-2.el8ap
python3.11-opentelemetry-util-http 0.39b0-6.el8ap
python3.11-packaging 23.2-1.el8ap
python3.11-parsley 1.3-3.el8ap
python3.11-pathspec 0.12.1-1.el8ap
python3.11-pbr 6.0.0-2.el8ap
python3.11-pillow 10.3.0-1.el8ap
python3.11-pip-wheel 22.3.1-5.el8
python3.11-platformdirs 4.2.0-1.el8ap
python3.11-ply 3.11-1.el8
python3.11-prometheus-client 0.19.0-1.el8ap
python3.11-protobuf 4.21.12-2.el8ap
python3.11-psycopg 3.1.17-3.el8ap
python3.11-pulp-ansible 0.21.7-1.el8ap
python3.11-pulp-container 2.19.3-1.el8ap
python3.11-pulp-glue 0.23.2-1.el8ap
python3.11-pulpcore 3.49.19-1.el8ap
python3.11-pyOpenSSL 24.1.0-1.el8ap
python3.11-pyasn1 0.5.1-1.el8ap
python3.11-pyasn1-modules 0.3.0-1.el8ap
python3.11-pycares 4.4.0-2.el8ap
python3.11-pycodestyle 2.11.1-1.el8ap
python3.11-pycparser 2.20-1.el8
python3.11-pyflakes 3.1.0-1.el8ap
python3.11-pygments 2.17.2-2.el8ap
python3.11-pygtrie 2.5.0-2.el8ap
python3.11-pyjwt 2.7.0-2.el8ap
python3.11-pyparsing 3.1.1-1.el8ap
python3.11-python3-openid 3.2.0-3.el8ap
python3.11-pyyaml 6.0-1.el8
python3.11-redis 4.6.0-2.el8ap
python3.11-referencing 0.35.1-1.el8ap
python3.11-requests 2.31.0-2.el8ap
python3.11-requests-oauthlib 1.3.1-1.el8ap
python3.11-resolvelib 1.0.1-1.el8ap
python3.11-rich 13.1.0-1.el8ap
python3.11-rpds-py 0.18.1-1.el8ap
python3.11-ruamel-yaml 0.18.6-1.el8ap
python3.11-ruamel-yaml-clib 0.2.8-1.el8ap
python3.11-s3transfer 0.10.0-1.el8ap
python3.11-semantic-version 2.10.0-2.el8ap
python3.11-setuptools 65.5.1-3.el8_10
python3.11-setuptools-wheel 65.5.1-3.el8_10
python3.11-six 1.16.0-1.el8
python3.11-smmap 5.0.1-1.el8ap
python3.11-social-auth-app-django 5.4.1-1.el8ap
python3.11-social-auth-core 4.5.4-1.el8ap
python3.11-sqlparse 0.5.0-1.el8ap
python3.11-subprocess-tee 0.4.1-2.el8ap
python3.11-tablib 3.5.0-1.el8ap
python3.11-tablib+html 3.5.0-1.el8ap
python3.11-tablib+ods 3.5.0-1.el8ap
python3.11-tablib+xls 3.5.0-1.el8ap
python3.11-tablib+xlsx 3.5.0-1.el8ap
python3.11-tablib+yaml 3.5.0-1.el8ap
python3.11-typing-extensions 4.9.0-1.el8ap
python3.11-uritemplate 4.1.1-3.el8ap
python3.11-url-normalize 1.4.3-5.el8ap
python3.11-urllib3 1.26.20-1.el8ap
python3.11-uuid6 2024.1.12-1.el8ap
python3.11-wcmatch 8.5-1.el8ap
python3.11-whitenoise 6.6.0-1.el8ap
python3.11-wrapt 1.16.0-1.el8ap
python3.11-xlrd 2.0.1-6.el8ap
python3.11-xlwt 1.3.0-4.el8ap
python3.11-yarl 1.9.2-1.el8ap
python3.11-zipp 3.19.2-1.el8ap
readline 7.0-10.el8
redhat-release 8.10-0.3.el8
rootfiles 8.1-22.el8
rpm 4.14.3-31.el8
rpm-libs 4.14.3-31.el8
rpm-plugin-selinux 4.14.3-31.el8
rsyslog 8.2102.0-15.el8
runc 1.1.12-4.module+el8.10.0+22283+6d6d094a
sed 4.5-5.el8
selinux-policy 3.14.3-139.el8_10
selinux-policy-targeted 3.14.3-139.el8_10
setup 2.12.2-9.el8
shadow-utils 4.6-22.el8
skopeo 1.14.5-3.module+el8.10.0+22283+6d6d094a
sos 4.7.2-2.el8_10
sqlite-libs 3.26.0-19.el8_9
sshpass 1.09-5.el8ap
systemd 239-82.el8_10.2
systemd-libs 239-82.el8_10.2
systemd-pam 239-82.el8_10.2
tar 1.30-9.el8
tzdata 2024a-1.el8
util-linux 2.32.1-46.el8
xz-libs 5.2.4-4.el8_6
yamllint 1.35.1-1.el8ap
zlib 1.2.11-25.el8
```

</details>

<details><summary>Python packages: /usr (python3.11) (160)</summary>

```text
aiodns 3.1.1
aiofiles 23.2.1
aiohttp 3.9.5
aiosignal 1.3.1
ansible-builder 3.1.0
ansible-compat 24.9.0
ansible-core 2.16.11
ansible-lint 24.9.0
asgiref 3.7.2
async-lru 2.0.4
async-timeout 4.0.3
asyncio-throttle 1.0.2
attrs 22.2.0
azure-core 1.29.7
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
commonmark 0.9.1
cryptography 42.0.5
defusedxml 0.7.1
Deprecated 1.2.14
diff-match-patch 20230430
distro 1.9.0
Django 4.2.16
django-ansible-base 2.5.1
django-auth-ldap 4.0.0
django-crum 0.7.9
django-filter 23.5
django-guid 3.4.0
django-import-export 3.3.6
django-ipware 3.0.7
django-lifecycle 1.1.2
django-picklefield 3.1
django-prometheus 2.3.1
django-split-settings 1.2.0
django-storages 1.14.2
djangorestframework 3.15.1
djangorestframework-queryfields 1.1.0
drf-access-policy 1.5.0
drf-nested-routers 0.93.5
drf-spectacular 0.26.5
dynaconf 3.2.6
et-xmlfile 1.1.0
filelock 3.13.1
flake8 6.1.0
frozenlist 1.4.0
galaxy-importer 0.4.25
galaxy-ng 4.10.0
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
Jinja2 3.1.4
jmespath 1.0.1
jq 1.6.0
json-stream 2.3.2
json-stream-rs-tokenizer 0.4.26
jsonschema 4.21.1
jsonschema-specifications 2023.12.1
Markdown 3.5.2
MarkupPy 1.14
MarkupSafe 2.1.5
marshmallow 3.20.2
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
psycopg 3.1.17
pulp-ansible 0.21.7
pulp-container 2.19.3
pulp-glue 0.23.2
pulpcore 3.49.19
pyasn1 0.5.1
pyasn1-modules 0.3.0
pycares 4.4.0
pycodestyle 2.11.1
pycparser 2.20
pyflakes 3.1.0
Pygments 2.17.2
pygtrie 2.5.0
PyJWT 2.7.0
pyOpenSSL 24.1.0
pyparsing 3.1.1
python-dateutil 2.8.2
python-gnupg 0.5.2
python-ldap 3.4.4
python3-openid 3.2.0
PyYAML 6.0
redis 4.6.0
referencing 0.35.1
requests 2.31.0
requests-oauthlib 1.3.1
resolvelib 1.0.1
rich 13.1.0
rpds-py 0.18.1
ruamel.yaml 0.18.6
ruamel.yaml.clib 0.2.8
s3transfer 0.10.0
semantic-version 2.10.0
setuptools 65.5.1
six 1.16.0
smmap 5.0.1
social-auth-app-django 5.4.1
social-auth-core 4.5.4
sqlparse 0.5.0
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
yarl 1.9.2
zipp 3.19.2
```

</details>

<details><summary>Python packages: /usr (python3.6) (12)</summary>

```text
cffi 1.11.5
chardet 3.0.4
cryptography 3.2.1
idna 2.5
ply 3.9
pycparser 2.14
PySocks 1.6.8
requests 2.20.0
setuptools 39.2.0
six 1.11.0
sos 4.7.2
urllib3 1.24.2
```

</details>

[Back to top](#contents)

### hub-web-rhel8

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/hub-web-rhel8.tar.gz` |
| Labels `version` / `release` | `4.10.0` / `196` |
| Image ID | `sha256:741a253ea19e791c3e3e2b3fa0ebf5c39302f304bf711d1b8c53f501e3f14558` |
| Build date | 2024-10-02T01:15:28 |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | N/A |
| Ansible Core | N/A |

<details><summary>RPM packages (277)</summary>

```text
acl 2.2.53-3.el8
audit-libs 3.1.2-1.el8
basesystem 11-5.el8
bash 4.4.20-5.el8
bind-libs 9.11.36-16.el8_10.2
bind-libs-lite 9.11.36-16.el8_10.2
bind-license 9.11.36-16.el8_10.2
bind-utils 9.11.36-16.el8_10.2
brotli 1.0.6-3.el8
bsdtar 3.3.3-5.el8
bzip2-libs 1.0.6-26.el8
ca-certificates 2024.2.69_v8.0.303-80.0.el8_10
chkconfig 1.19.2-1.el8
cmake 3.26.5-2.el8
cmake-data 3.26.5-2.el8
cmake-filesystem 3.26.5-2.el8
cmake-rpm-macros 3.26.5-2.el8
coreutils-single 8.30-15.el8
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crypto-policies 20230731-1.git3177e06.el8
crypto-policies-scripts 20230731-1.git3177e06.el8
cryptsetup-libs 2.3.7-7.el8
curl 7.61.1-34.el8_10.2
cyrus-sasl-lib 2.1.27-6.el8_5
dbus 1.12.8-26.el8
dbus-common 1.12.8-26.el8
dbus-daemon 1.12.8-26.el8
dbus-glib 0.110-2.el8
dbus-libs 1.12.8-26.el8
dbus-tools 1.12.8-26.el8
device-mapper 1.02.181-14.el8
device-mapper-libs 1.02.181-14.el8
dmidecode 3.5-1.el8
dnf 4.7.0-20.el8
dnf-data 4.7.0-20.el8
dnf-plugin-subscription-manager 1.28.42-1.el8
elfutils-default-yama-scope 0.190-2.el8
elfutils-libelf 0.190-2.el8
elfutils-libs 0.190-2.el8
emacs-filesystem 26.1-12.el8_10
environment-modules 4.5.2-4.el8
expat 2.2.5-15.el8_10
file-libs 5.33-26.el8
filesystem 3.8-6.el8
findutils 4.6.0-23.el8_10
fstrm 0.6.1-3.el8
gawk 4.2.1-4.el8
gdb-gdbserver 8.2-20.el8
gdbm 1.18-2.el8
gdbm-libs 1.18-2.el8
geolite2-city 20180605-1.el8
geolite2-country 20180605-1.el8
gettext 0.19.8.1-17.el8
gettext-libs 0.19.8.1-17.el8
glib2 2.56.4-162.el8
glibc 2.28-251.el8_10.5
glibc-common 2.28-251.el8_10.5
glibc-langpack-en 2.28-251.el8_10.5
glibc-locale-source 2.28-251.el8_10.5
glibc-minimal-langpack 2.28-251.el8_10.5
gmp 6.1.2-11.el8
gnupg2 2.2.20-3.el8_6
gnutls 3.6.16-8.el8_9.3
gobject-introspection 1.56.1-1.el8
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
groff-base 1.22.3-18.el8
gzip 1.9-13.el8_5
hostname 3.20-6.el8
ima-evm-utils 1.3.2-12.el8
info 6.5-7.el8
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
kmod-libs 25-20.el8
krb5-libs 1.18.2-29.el8_10
langpacks-en 1.0-12.el8
less 530-3.el8_10
libacl 2.2.53-3.el8
libarchive 3.3.3-5.el8
libassuan 2.5.1-3.el8
libattr 2.4.48-3.el8
libblkid 2.32.1-46.el8
libcap 2.48-6.el8_9
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-5.el8
libcomps 0.1.18-1.el8
libcroco 0.6.12-4.el8_2.1
libcurl 7.61.1-34.el8_10.2
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-20.el8_10
libfdisk 2.32.1-46.el8
libffi 3.1-24.el8
libgcc 8.5.0-22.el8_10
libgcrypt 1.8.5-7.el8_6
libgomp 8.5.0-22.el8_10
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libksba 1.3.5-9.el8_7
libmaxminddb 1.2.0-10.el8_9.1
libmodulemd 2.13.0-1.el8
libmount 2.32.1-46.el8
libnghttp2 1.33.0-6.el8_10.1
libnl3 3.7.0-1.el8
libnsl2 1.2.0-2.20180605git4a062cf.el8
libpipeline 1.5.0-2.el8
libpkgconf 1.4.2-1.el8
libpsl 0.20.2-6.el8
libpwquality 1.4.4-6.el8
librepo 1.14.2-5.el8
libreport-filesystem 2.9.5-15.el8
librhsm 0.0.3-5.el8
libseccomp 2.5.2-1.el8
libselinux 2.9-8.el8
libsemanage 2.9-9.el8_6
libsepol 2.9-3.el8
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-46.el8
libsolv 0.7.20-6.el8
libssh 0.9.6-14.el8
libssh-config 0.9.6-14.el8
libstdc++ 8.5.0-22.el8_10
libtasn1 4.13-4.el8_7
libtirpc 1.1.4-12.el8_10
libunistring 0.9.9-3.el8
libusbx 1.0.23-4.el8
libuser 0.62-26.el8_10
libutempter 1.1.6-14.el8
libuuid 2.32.1-46.el8
libuv 1.41.1-2.el8_10
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-18.el8_10.1
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-3.el8_4
make 4.2.1-11.el8
man-db 2.7.6.1-18.el8
mpfr 3.1.6-1.el8
ncurses 6.1-10.20180224.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
nginx 1.22.1-1.module+el8.8.0+20355+6d9c8a63.1
nginx-filesystem 1.22.1-1.module+el8.8.0+20355+6d9c8a63.1
nginx-mod-http-perl 1.22.1-1.module+el8.8.0+20355+6d9c8a63.1
nginx-mod-stream 1.22.1-1.module+el8.8.0+20355+6d9c8a63.1
npth 1.5-4.el8
nss_wrapper 1.1.13-1.el8
nss_wrapper-libs 1.1.13-1.el8
openldap 2.4.46-19.el8_10
openssl 1.1.1k-12.el8_9
openssl-libs 1.1.1k-12.el8_9
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-34.el8_10
passwd 0.80-4.el8
pcre 8.42-6.el8
pcre2 10.32-3.el8_6
perl-Carp 1.42-396.el8
perl-Data-Dumper 2.167-399.el8
perl-Digest 1.17-395.el8
perl-Digest-MD5 2.55-396.el8
perl-Encode 2.97-3.el8
perl-Errno 1.28-422.el8
perl-Exporter 5.72-396.el8
perl-File-Path 2.15-2.el8
perl-File-Temp 0.230.600-1.el8
perl-Getopt-Long 2.50-4.el8
perl-HTTP-Tiny 0.074-3.el8
perl-IO 1.38-422.el8
perl-IO-Socket-IP 0.39-5.el8
perl-IO-Socket-SSL 2.066-4.module+el8.3.0+6446+594cad75
perl-MIME-Base64 3.15-396.el8
perl-Mozilla-CA 20160104-7.module+el8.3.0+6498+9eecfe51
perl-Net-SSLeay 1.88-2.module+el8.6.0+13392+f0897f98
perl-PathTools 3.74-1.el8
perl-Pod-Escapes 1.07-395.el8
perl-Pod-Perldoc 3.28-396.el8
perl-Pod-Simple 3.35-395.el8
perl-Pod-Usage 1.69-395.el8
perl-Scalar-List-Utils 1.49-2.el8
perl-Socket 2.027-3.el8
perl-Storable 3.11-3.el8
perl-Term-ANSIColor 4.06-396.el8
perl-Term-Cap 1.17-395.el8
perl-Text-ParseWords 3.30-395.el8
perl-Text-Tabs+Wrap 2013.0523-395.el8
perl-Time-Local 1.280-1.el8
perl-URI 1.73-3.el8
perl-Unicode-Normalize 1.25-396.el8
perl-constant 1.33-396.el8
perl-interpreter 5.26.3-422.el8
perl-libnet 3.11-3.el8
perl-libs 5.26.3-422.el8
perl-macros 5.26.3-422.el8
perl-parent 0.237-1.el8
perl-podlators 4.11-1.el8
perl-threads 2.21-2.el8
perl-threads-shared 1.58-2.el8
pkgconf 1.4.2-1.el8
pkgconf-m4 1.4.2-1.el8
pkgconf-pkg-config 1.4.2-1.el8
platform-python 3.6.8-67.el8_10
platform-python-setuptools 39.2.0-8.el8_10
popt 1.18-1.el8
procps-ng 3.3.15-14.el8
protobuf-c 1.3.0-8.el8
publicsuffix-list-dafsa 20180723-1.el8
python3-bind 9.11.36-16.el8_10.2
python3-chardet 3.0.4-7.el8
python3-cloud-what 1.28.42-1.el8
python3-dateutil 2.6.1-6.el8
python3-dbus 1.2.4-15.el8
python3-decorator 4.2.1-2.el8
python3-dnf 4.7.0-20.el8
python3-dnf-plugins-core 4.0.21-25.el8
python3-ethtool 0.14-5.el8
python3-gobject-base 3.28.3-2.el8
python3-gpg 1.13.1-12.el8
python3-hawkey 0.63.0-20.el8_10
python3-idna 2.5-7.el8_10
python3-iniparse 0.4-31.el8
python3-inotify 0.9.6-13.el8
python3-libcomps 0.1.18-1.el8
python3-libdnf 0.63.0-20.el8_10
python3-librepo 1.14.2-5.el8
python3-libs 3.6.8-67.el8_10
python3-pip-wheel 9.0.3-24.el8
python3-ply 3.9-9.el8
python3-pysocks 1.6.8-3.el8
python3-requests 2.20.0-3.el8_8
python3-rpm 4.14.3-31.el8
python3-setuptools-wheel 39.2.0-8.el8_10
python3-six 1.11.0-8.el8
python3-subscription-manager-rhsm 1.28.42-1.el8
python3-syspurpose 1.28.42-1.el8
python3-systemd 234-8.el8
python3-urllib3 1.24.2-8.el8_10
readline 7.0-10.el8
redhat-logos-httpd 84.5-2.el8
redhat-release 8.10-0.3.el8
rootfiles 8.1-22.el8
rpm 4.14.3-31.el8
rpm-build-libs 4.14.3-31.el8
rpm-libs 4.14.3-31.el8
rsync 3.1.3-19.el8_7.1
scl-utils 2.0.2-16.el8
sed 4.5-5.el8
setup 2.12.2-9.el8
shadow-utils 4.6-22.el8
sqlite-libs 3.26.0-19.el8_9
subscription-manager 1.28.42-1.el8
subscription-manager-rhsm-certificates 20220623-1.el8
systemd 239-82.el8_10.2
systemd-libs 239-82.el8_10.2
systemd-pam 239-82.el8_10.2
tar 1.30-9.el8
tcl 8.6.8-2.el8
tpm2-tss 2.3.2-6.el8
tzdata 2024a-1.el8
unzip 6.0-46.el8
usermode 1.113-2.el8
util-linux 2.32.1-46.el8
vim-filesystem 8.0.1763-19.el8_6.4
vim-minimal 8.0.1763-19.el8_6.4
virt-what 1.25-4.el8
which 2.21-20.el8
xz 5.2.4-4.el8_6
xz-libs 5.2.4-4.el8_6
yum 4.7.0-20.el8
zlib 1.2.11-25.el8
```

</details>

<details><summary>Python packages: /usr (python3.6) (22)</summary>

```text
chardet 3.0.4
dbus-python 1.2.4
decorator 4.2.1
ethtool 0.14
gpg 1.13.1
idna 2.5
iniparse 0.4
isc 2.0
libcomps 0.1.18
ply 3.9
PyGObject 3.28.3
pyinotify 0.9.6
PySocks 1.6.8
python-dateutil 2.6.1
requests 2.20.0
rpm 4.14.3
setuptools 39.2.0
six 1.11.0
subscription-manager 1.28.42
syspurpose 1.28.42
systemd-python 234
urllib3 1.24.2
```

</details>

[Back to top](#contents)

### receptor-rhel8

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-25/receptor-rhel8` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/receptor-rhel8.tar.gz` |
| Labels `version` / `release` | `1.4.8` / `34` |
| Image ID | `sha256:ae9c0820d61d8df29bb0a6bbae57ebd247954ab2bd8b3e4de434e0926c4e0fff` |
| Build date | 2024-10-02T00:33:02 |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | 3.11 |
| Ansible Core | N/A |

<details><summary>RPM packages (172)</summary>

```text
acl 2.2.53-3.el8
ansible-runner 2.4.0-1.el8ap
audit-libs 3.1.2-1.el8
basesystem 11-5.el8
bash 4.4.20-5.el8
brotli 1.0.6-3.el8
bzip2-libs 1.0.6-26.el8
ca-certificates 2024.2.69_v8.0.303-80.0.el8_10
chkconfig 1.19.2-1.el8
coreutils-single 8.30-15.el8
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crypto-policies 20230731-1.git3177e06.el8
cryptsetup-libs 2.3.7-7.el8
curl 7.61.1-34.el8_10.2
cyrus-sasl-lib 2.1.27-6.el8_5
dbus 1.12.8-26.el8
dbus-common 1.12.8-26.el8
dbus-daemon 1.12.8-26.el8
dbus-libs 1.12.8-26.el8
dbus-tools 1.12.8-26.el8
device-mapper 1.02.181-14.el8
device-mapper-libs 1.02.181-14.el8
diffutils 3.6-6.el8
dumb-init 1.2.5-3.el8ap
elfutils-default-yama-scope 0.190-2.el8
elfutils-libelf 0.190-2.el8
elfutils-libs 0.190-2.el8
expat 2.2.5-15.el8_10
file-libs 5.33-26.el8
filesystem 3.8-6.el8
gawk 4.2.1-4.el8
gdbm 1.18-2.el8
gdbm-libs 1.18-2.el8
glib2 2.56.4-162.el8
glibc 2.28-251.el8_10.5
glibc-common 2.28-251.el8_10.5
glibc-minimal-langpack 2.28-251.el8_10.5
gmp 6.1.2-11.el8
gnupg2 2.2.20-3.el8_6
gnutls 3.6.16-8.el8_9.3
gobject-introspection 1.56.1-1.el8
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
gzip 1.9-13.el8_5
info 6.5-7.el8
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
kmod-libs 25-20.el8
krb5-libs 1.18.2-29.el8_10
langpacks-en 1.0-12.el8
libacl 2.2.53-3.el8
libarchive 3.3.3-5.el8
libassuan 2.5.1-3.el8
libattr 2.4.48-3.el8
libblkid 2.32.1-46.el8
libcap 2.48-6.el8_9
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-5.el8
libcurl 7.61.1-34.el8_10.2
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-20.el8_10
libfdisk 2.32.1-46.el8
libffi 3.1-24.el8
libgcc 8.5.0-22.el8_10
libgcrypt 1.8.5-7.el8_6
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libksba 1.3.5-9.el8_7
libmodulemd 2.13.0-1.el8
libmount 2.32.1-46.el8
libnghttp2 1.33.0-6.el8_10.1
libnsl2 1.2.0-2.20180605git4a062cf.el8
libpeas 1.22.0-6.el8
libpsl 0.20.2-6.el8
libpwquality 1.4.4-6.el8
librepo 1.14.2-5.el8
librhsm 0.0.3-5.el8
libseccomp 2.5.2-1.el8
libselinux 2.9-8.el8
libselinux-utils 2.9-8.el8
libsemanage 2.9-9.el8_6
libsepol 2.9-3.el8
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-46.el8
libsolv 0.7.20-6.el8
libssh 0.9.6-14.el8
libssh-config 0.9.6-14.el8
libstdc++ 8.5.0-22.el8_10
libtasn1 4.13-4.el8_7
libtirpc 1.1.4-12.el8_10
libunistring 0.9.9-3.el8
libusbx 1.0.23-4.el8
libutempter 1.1.6-14.el8
libuuid 2.32.1-46.el8
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-18.el8_10.1
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
logrotate 3.14.0-6.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-3.el8_4
microdnf 3.8.0-2.el8
mpdecimal 2.5.1-3.el8
mpfr 3.1.6-1.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
npth 1.5-4.el8
openldap 2.4.46-19.el8_10
openssl-libs 1.1.1k-12.el8_9
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-34.el8_10
pcre 8.42-6.el8
pcre2 10.32-3.el8_6
platform-python 3.6.8-67.el8_10
platform-python-setuptools 39.2.0-8.el8_10
podman-remote 4.9.4-13.module+el8.10.0+22283+6d6d094a
policycoreutils 2.9-26.el8_10
popt 1.18-1.el8
publicsuffix-list-dafsa 20180723-1.el8
python3-chardet 3.0.4-7.el8
python3-idna 2.5-7.el8_10
python3-libs 3.6.8-67.el8_10
python3-pip-wheel 9.0.3-24.el8
python3-pysocks 1.6.8-3.el8
python3-requests 2.20.0-3.el8_8
python3-setuptools 39.2.0-8.el8_10
python3-setuptools-wheel 39.2.0-8.el8_10
python3-six 1.11.0-8.el8
python3-urllib3 1.24.2-8.el8_10
python3.11 3.11.9-7.el8_10
python3.11-ansible-runner 2.4.0-1.el8ap
python3.11-click 8.1.7-1.el8ap
python3.11-daemon 2.3.2-1.el8ap
python3.11-dateutil 2.8.2-2.el8ap
python3.11-docutils 0.20.1-2.el8ap
python3.11-libs 3.11.9-7.el8_10
python3.11-lockfile 0.12.2-2.el8ap
python3.11-packaging 23.2-1.el8ap
python3.11-pexpect 4.9.0-1.el8ap
python3.11-pip-wheel 22.3.1-5.el8
python3.11-ptyprocess 0.7.0-1.el8ap
python3.11-pyyaml 6.0-1.el8
python3.11-setuptools-wheel 65.5.1-3.el8_10
python3.11-six 1.16.0-1.el8
readline 7.0-10.el8
receptor 1.4.8-3.el8ap
receptorctl 1.4.8-3.el8ap
redhat-release 8.10-0.3.el8
rootfiles 8.1-22.el8
rpm 4.14.3-31.el8
rpm-libs 4.14.3-31.el8
sed 4.5-5.el8
setup 2.12.2-9.el8
shadow-utils 4.6-22.el8
shadow-utils-subid 4.6-22.el8
sos 4.7.2-2.el8_10
sqlite-libs 3.26.0-19.el8_9
systemd 239-82.el8_10.2
systemd-libs 239-82.el8_10.2
systemd-pam 239-82.el8_10.2
tzdata 2024a-1.el8
util-linux 2.32.1-46.el8
xz-libs 5.2.4-4.el8_6
zlib 1.2.11-25.el8
```

</details>

<details><summary>Python packages: /usr (python3.11) (12)</summary>

```text
ansible-runner 2.4.0
click 8.1.7
docutils 0.20.1
lockfile 0.12.2
packaging 23.2
pexpect 4.9.0
ptyprocess 0.7.0
python-daemon 2.3.2
python-dateutil 2.8.2
PyYAML 6.0
receptorctl 1.4.8
six 1.16.0
```

</details>

<details><summary>Python packages: /usr (python3.6) (8)</summary>

```text
chardet 3.0.4
idna 2.5
PySocks 1.6.8
requests 2.20.0
setuptools 39.2.0
six 1.11.0
sos 4.7.2
urllib3 1.24.2
```

</details>

[Back to top](#contents)

### pcp

| Field | Value |
|---|---|
| Image | `registry.redhat.io/rhel8/pcp` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/pcp.tar.gz` |
| Labels `version` / `release` | `5` / `233.1727149332` |
| Image ID | `sha256:3d7083e695274cb15de2ddcfc7cf2a5bd3a37258920efdb45459b5a5c3d0b079` |
| Build date | 2024-09-24T04:26:11 |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | 3.6 |
| Ansible Core | N/A |

<details><summary>RPM packages (215)</summary>

```text
acl 2.2.53-3.el8
audit-libs 3.1.2-1.el8
avahi-libs 0.7-27.el8_10.1
basesystem 11-5.el8
bash 4.4.20-5.el8
brotli 1.0.6-3.el8
bzip2-libs 1.0.6-26.el8
ca-certificates 2024.2.69_v8.0.303-80.0.el8_10
chkconfig 1.19.2-1.el8
coreutils-single 8.30-15.el8
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crypto-policies 20230731-1.git3177e06.el8
crypto-policies-scripts 20230731-1.git3177e06.el8
cryptsetup-libs 2.3.7-7.el8
curl 7.61.1-34.el8_10.2
cyrus-sasl-lib 2.1.27-6.el8_5
dbus 1.12.8-26.el8
dbus-common 1.12.8-26.el8
dbus-daemon 1.12.8-26.el8
dbus-glib 0.110-2.el8
dbus-libs 1.12.8-26.el8
dbus-tools 1.12.8-26.el8
device-mapper 1.02.181-14.el8
device-mapper-libs 1.02.181-14.el8
diffutils 3.6-6.el8
dmidecode 3.5-1.el8
dnf 4.7.0-20.el8
dnf-data 4.7.0-20.el8
dnf-plugin-subscription-manager 1.28.42-1.el8
elfutils-default-yama-scope 0.190-2.el8
elfutils-libelf 0.190-2.el8
elfutils-libs 0.190-2.el8
expat 2.2.5-15.el8_10
file-libs 5.33-26.el8
filesystem 3.8-6.el8
findutils 4.6.0-23.el8_10
gawk 4.2.1-4.el8
gdb-gdbserver 8.2-20.el8
gdbm 1.18-2.el8
gdbm-libs 1.18-2.el8
gettext 0.19.8.1-17.el8
gettext-libs 0.19.8.1-17.el8
glib2 2.56.4-162.el8
glibc 2.28-251.el8_10.5
glibc-common 2.28-251.el8_10.5
glibc-minimal-langpack 2.28-251.el8_10.5
gmp 6.1.2-11.el8
gnupg2 2.2.20-3.el8_6
gnutls 3.6.16-8.el8_9.3
gobject-introspection 1.56.1-1.el8
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
gzip 1.9-13.el8_5
hostname 3.20-6.el8
ima-evm-utils 1.3.2-12.el8
info 6.5-7.el8
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
kmod-libs 25-20.el8
krb5-libs 1.18.2-29.el8_10
langpacks-en 1.0-12.el8
libacl 2.2.53-3.el8
libarchive 3.3.3-5.el8
libassuan 2.5.1-3.el8
libattr 2.4.48-3.el8
libblkid 2.32.1-46.el8
libcap 2.48-6.el8_9
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-5.el8
libcomps 0.1.18-1.el8
libcroco 0.6.12-4.el8_2.1
libcurl 7.61.1-34.el8_10.2
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-20.el8_10
libfdisk 2.32.1-46.el8
libffi 3.1-24.el8
libgcc 8.5.0-22.el8_10
libgcrypt 1.8.5-7.el8_6
libgomp 8.5.0-22.el8_10
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libksba 1.3.5-9.el8_7
libmodulemd 2.13.0-1.el8
libmount 2.32.1-46.el8
libnghttp2 1.33.0-6.el8_10.1
libnl3 3.7.0-1.el8
libnsl2 1.2.0-2.20180605git4a062cf.el8
libpsl 0.20.2-6.el8
libpwquality 1.4.4-6.el8
librepo 1.14.2-5.el8
libreport-filesystem 2.9.5-15.el8
librhsm 0.0.3-5.el8
libseccomp 2.5.2-1.el8
libselinux 2.9-8.el8
libsemanage 2.9-9.el8_6
libsepol 2.9-3.el8
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-46.el8
libsolv 0.7.20-6.el8
libssh 0.9.6-14.el8
libssh-config 0.9.6-14.el8
libstdc++ 8.5.0-22.el8_10
libtasn1 4.13-4.el8_7
libtirpc 1.1.4-12.el8_10
libunistring 0.9.9-3.el8
libusbx 1.0.23-4.el8
libuser 0.62-26.el8_10
libutempter 1.1.6-14.el8
libuuid 2.32.1-46.el8
libuv 1.41.1-2.el8_10
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-18.el8_10.1
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-3.el8_4
mpfr 3.1.6-1.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
npth 1.5-4.el8
nspr 4.35.0-1.el8_8
nss 3.101.0-7.el8_8
nss-softokn 3.101.0-7.el8_8
nss-softokn-freebl 3.101.0-7.el8_8
nss-sysinit 3.101.0-7.el8_8
nss-util 3.101.0-7.el8_8
openldap 2.4.46-19.el8_10
openssl-libs 1.1.1k-12.el8_9
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-34.el8_10
passwd 0.80-4.el8
pcp 5.3.7-22.el8_10
pcp-conf 5.3.7-22.el8_10
pcp-doc 5.3.7-22.el8_10
pcp-libs 5.3.7-22.el8_10
pcp-pmda-dm 5.3.7-22.el8_10
pcp-pmda-nfsclient 5.3.7-22.el8_10
pcp-pmda-openmetrics 5.3.7-22.el8_10
pcp-system-tools 5.3.7-22.el8_10
pcp-zeroconf 5.3.7-22.el8_10
pcre 8.42-6.el8
pcre2 10.32-3.el8_6
platform-python 3.6.8-67.el8_10
platform-python-pip 9.0.3-24.el8
platform-python-setuptools 39.2.0-8.el8_10
popt 1.18-1.el8
procps-ng 3.3.15-14.el8
publicsuffix-list-dafsa 20180723-1.el8
python3-chardet 3.0.4-7.el8
python3-cloud-what 1.28.42-1.el8
python3-dateutil 2.6.1-6.el8
python3-dbus 1.2.4-15.el8
python3-decorator 4.2.1-2.el8
python3-dnf 4.7.0-20.el8
python3-dnf-plugins-core 4.0.21-25.el8
python3-ethtool 0.14-5.el8
python3-gobject-base 3.28.3-2.el8
python3-gpg 1.13.1-12.el8
python3-hawkey 0.63.0-20.el8_10
python3-idna 2.5-7.el8_10
python3-iniparse 0.4-31.el8
python3-inotify 0.9.6-13.el8
python3-libcomps 0.1.18-1.el8
python3-libdnf 0.63.0-20.el8_10
python3-librepo 1.14.2-5.el8
python3-libs 3.6.8-67.el8_10
python3-pcp 5.3.7-22.el8_10
python3-pip 9.0.3-24.el8
python3-pip-wheel 9.0.3-24.el8
python3-pysocks 1.6.8-3.el8
python3-requests 2.20.0-3.el8_8
python3-rpm 4.14.3-31.el8
python3-setuptools 39.2.0-8.el8_10
python3-setuptools-wheel 39.2.0-8.el8_10
python3-six 1.11.0-8.el8
python3-subscription-manager-rhsm 1.28.42-1.el8
python3-syspurpose 1.28.42-1.el8
python3-systemd 234-8.el8
python3-urllib3 1.24.2-8.el8_10
python36 3.6.8-39.module+el8.10.0+20784+edafcd43
readline 7.0-10.el8
redhat-release 8.10-0.3.el8
rootfiles 8.1-22.el8
rpm 4.14.3-31.el8
rpm-build-libs 4.14.3-31.el8
rpm-libs 4.14.3-31.el8
sed 4.5-5.el8
setup 2.12.2-9.el8
shadow-utils 4.6-22.el8
sqlite-libs 3.26.0-19.el8_9
subscription-manager 1.28.42-1.el8
subscription-manager-rhsm-certificates 20220623-1.el8
systemd 239-82.el8_10.2
systemd-libs 239-82.el8_10.2
systemd-pam 239-82.el8_10.2
tar 1.30-9.el8
tpm2-tss 2.3.2-6.el8
tzdata 2024a-1.el8
usermode 1.113-2.el8
util-linux 2.32.1-46.el8
vim-minimal 8.0.1763-19.el8_6.4
virt-what 1.25-4.el8
which 2.21-20.el8
xz 5.2.4-4.el8_6
xz-libs 5.2.4-4.el8_6
yum 4.7.0-20.el8
zlib 1.2.11-25.el8
```

</details>

<details><summary>Python packages: /usr (python3.6) (22)</summary>

```text
chardet 3.0.4
dbus-python 1.2.4
decorator 4.2.1
ethtool 0.14
gpg 1.13.1
idna 2.5
iniparse 0.4
libcomps 0.1.18
pcp 5.0
pip 9.0.3
PyGObject 3.28.3
pyinotify 0.9.6
PySocks 1.6.8
python-dateutil 2.6.1
requests 2.20.0
rpm 4.14.3
setuptools 39.2.0
six 1.11.0
subscription-manager 1.28.42
syspurpose 1.28.42
systemd-python 234
urllib3 1.24.2
```

</details>

[Back to top](#contents)

### postgresql-15

| Field | Value |
|---|---|
| Image | `registry.redhat.io/rhel8/postgresql-15` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/postgresql-15.tar.gz` |
| Labels `version` / `release` | `1` / `82` |
| Image ID | `sha256:2392b56e6b5e126bf6f934318b681de64cb02addff2a124b4c2ef3a031582e6d` |
| Build date | 2024-10-04T08:25:37 |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | N/A |
| Ansible Core | N/A |

<details><summary>RPM packages (280)</summary>

```text
acl 2.2.53-3.el8
audit-libs 3.1.2-1.el8
basesystem 11-5.el8
bash 4.4.20-5.el8
bind-libs 9.11.36-16.el8_10.2
bind-libs-lite 9.11.36-16.el8_10.2
bind-license 9.11.36-16.el8_10.2
bind-utils 9.11.36-16.el8_10.2
brotli 1.0.6-3.el8
bsdtar 3.3.3-5.el8
bzip2-libs 1.0.6-26.el8
ca-certificates 2024.2.69_v8.0.303-80.0.el8_10
chkconfig 1.19.2-1.el8
cmake 3.26.5-2.el8
cmake-data 3.26.5-2.el8
cmake-filesystem 3.26.5-2.el8
cmake-rpm-macros 3.26.5-2.el8
coreutils-single 8.30-15.el8
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crypto-policies 20230731-1.git3177e06.el8
crypto-policies-scripts 20230731-1.git3177e06.el8
cryptsetup-libs 2.3.7-7.el8
curl 7.61.1-34.el8_10.2
cyrus-sasl-lib 2.1.27-6.el8_5
dbus 1.12.8-26.el8
dbus-common 1.12.8-26.el8
dbus-daemon 1.12.8-26.el8
dbus-glib 0.110-2.el8
dbus-libs 1.12.8-26.el8
dbus-tools 1.12.8-26.el8
device-mapper 1.02.181-14.el8
device-mapper-libs 1.02.181-14.el8
dmidecode 3.5-1.el8
dnf 4.7.0-20.el8
dnf-data 4.7.0-20.el8
dnf-plugin-subscription-manager 1.28.42-1.el8
elfutils-default-yama-scope 0.190-2.el8
elfutils-libelf 0.190-2.el8
elfutils-libs 0.190-2.el8
emacs-filesystem 26.1-12.el8_10
environment-modules 4.5.2-4.el8
expat 2.2.5-15.el8_10
file-libs 5.33-26.el8
filesystem 3.8-6.el8
findutils 4.6.0-23.el8_10
fstrm 0.6.1-3.el8
gawk 4.2.1-4.el8
gdb-gdbserver 8.2-20.el8
gdbm 1.18-2.el8
gdbm-libs 1.18-2.el8
geolite2-city 20180605-1.el8
geolite2-country 20180605-1.el8
gettext 0.19.8.1-17.el8
gettext-libs 0.19.8.1-17.el8
glib2 2.56.4-162.el8
glibc 2.28-251.el8_10.5
glibc-common 2.28-251.el8_10.5
glibc-langpack-en 2.28-251.el8_10.5
glibc-locale-source 2.28-251.el8_10.5
glibc-minimal-langpack 2.28-251.el8_10.5
gmp 6.1.2-11.el8
gnupg2 2.2.20-3.el8_6
gnutls 3.6.16-8.el8_9.3
gobject-introspection 1.56.1-1.el8
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
groff-base 1.22.3-18.el8
gzip 1.9-13.el8_5
ima-evm-utils 1.3.2-12.el8
info 6.5-7.el8
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
kmod-libs 25-20.el8
krb5-libs 1.18.2-29.el8_10
langpacks-en 1.0-12.el8
less 530-3.el8_10
libacl 2.2.53-3.el8
libarchive 3.3.3-5.el8
libassuan 2.5.1-3.el8
libattr 2.4.48-3.el8
libblkid 2.32.1-46.el8
libcap 2.48-6.el8_9
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-5.el8
libcomps 0.1.18-1.el8
libcroco 0.6.12-4.el8_2.1
libcurl 7.61.1-34.el8_10.2
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-20.el8_10
libfdisk 2.32.1-46.el8
libffi 3.1-24.el8
libgcc 8.5.0-22.el8_10
libgcrypt 1.8.5-7.el8_6
libgomp 8.5.0-22.el8_10
libgpg-error 1.31-1.el8
libicu 60.3-2.el8_1
libidn2 2.2.0-1.el8
libksba 1.3.5-9.el8_7
libmaxminddb 1.2.0-10.el8_9.1
libmodulemd 2.13.0-1.el8
libmount 2.32.1-46.el8
libnghttp2 1.33.0-6.el8_10.1
libnl3 3.7.0-1.el8
libnsl2 1.2.0-2.20180605git4a062cf.el8
libpipeline 1.5.0-2.el8
libpkgconf 1.4.2-1.el8
libpsl 0.20.2-6.el8
libpwquality 1.4.4-6.el8
librepo 1.14.2-5.el8
libreport-filesystem 2.9.5-15.el8
librhsm 0.0.3-5.el8
libseccomp 2.5.2-1.el8
libselinux 2.9-8.el8
libsemanage 2.9-9.el8
libsepol 2.9-3.el8
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-46.el8
libsolv 0.7.20-6.el8
libssh 0.9.6-14.el8
libssh-config 0.9.6-14.el8
libstdc++ 8.5.0-22.el8_10
libtasn1 4.13-4.el8_7
libtirpc 1.1.4-12.el8_10
libunistring 0.9.9-3.el8
libusbx 1.0.23-4.el8
libuser 0.62-26.el8_10
libutempter 1.1.6-14.el8
libuuid 2.32.1-46.el8
libuv 1.41.1-2.el8_10
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-18.el8_10.1
libxslt 1.1.32-6.el8
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-3.el8_4
make 4.2.1-11.el8
man-db 2.7.6.1-18.el8
mpfr 3.1.6-1.el8
ncurses 6.1-10.20180224.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
npth 1.5-4.el8
nss_wrapper 1.1.13-1.el8
nss_wrapper-libs 1.1.13-1.el8
openldap 2.4.46-19.el8_10
openssl 1.1.1k-12.el8_9
openssl-libs 1.1.1k-12.el8_9
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-34.el8_10
passwd 0.80-4.el8
pcre 8.42-6.el8
pcre2 10.32-3.el8_6
perl-Carp 1.42-396.el8
perl-Data-Dumper 2.167-399.el8
perl-Digest 1.17-395.el8
perl-Digest-MD5 2.55-396.el8
perl-Encode 2.97-3.el8
perl-Errno 1.28-422.el8
perl-Exporter 5.72-396.el8
perl-File-Path 2.15-2.el8
perl-File-Temp 0.230.600-1.el8
perl-Getopt-Long 2.50-4.el8
perl-HTTP-Tiny 0.074-3.el8
perl-IO 1.38-422.el8
perl-IO-Socket-IP 0.39-5.el8
perl-IO-Socket-SSL 2.066-4.module+el8.3.0+6446+594cad75
perl-MIME-Base64 3.15-396.el8
perl-Mozilla-CA 20160104-7.module+el8.3.0+6498+9eecfe51
perl-Net-SSLeay 1.88-2.module+el8.6.0+13392+f0897f98
perl-PathTools 3.74-1.el8
perl-Pod-Escapes 1.07-395.el8
perl-Pod-Perldoc 3.28-396.el8
perl-Pod-Simple 3.35-395.el8
perl-Pod-Usage 1.69-395.el8
perl-Scalar-List-Utils 1.49-2.el8
perl-Socket 2.027-3.el8
perl-Storable 3.11-3.el8
perl-Term-ANSIColor 4.06-396.el8
perl-Term-Cap 1.17-395.el8
perl-Text-ParseWords 3.30-395.el8
perl-Text-Tabs+Wrap 2013.0523-395.el8
perl-Time-Local 1.280-1.el8
perl-URI 1.73-3.el8
perl-Unicode-Normalize 1.25-396.el8
perl-constant 1.33-396.el8
perl-interpreter 5.26.3-422.el8
perl-libnet 3.11-3.el8
perl-libs 5.26.3-422.el8
perl-macros 5.26.3-422.el8
perl-parent 0.237-1.el8
perl-podlators 4.11-1.el8
perl-threads 2.21-2.el8
perl-threads-shared 1.58-2.el8
pgaudit 1.7.0-1.module+el8.9.0+19797+c4ce5969
pkgconf 1.4.2-1.el8
pkgconf-m4 1.4.2-1.el8
pkgconf-pkg-config 1.4.2-1.el8
platform-python 3.6.8-67.el8_10
platform-python-setuptools 39.2.0-8.el8_10
popt 1.18-1.el8
postgresql 15.8-1.module+el8.10.0+22212+a51fe170
postgresql-contrib 15.8-1.module+el8.10.0+22212+a51fe170
postgresql-private-libs 15.8-1.module+el8.10.0+22212+a51fe170
postgresql-server 15.8-1.module+el8.10.0+22212+a51fe170
postgresql-upgrade 15.8-1.module+el8.10.0+22212+a51fe170
procps-ng 3.3.15-14.el8
protobuf-c 1.3.0-8.el8
publicsuffix-list-dafsa 20180723-1.el8
python3-bind 9.11.36-16.el8_10.2
python3-chardet 3.0.4-7.el8
python3-cloud-what 1.28.42-1.el8
python3-dateutil 2.6.1-6.el8
python3-dbus 1.2.4-15.el8
python3-decorator 4.2.1-2.el8
python3-dnf 4.7.0-20.el8
python3-dnf-plugins-core 4.0.21-25.el8
python3-ethtool 0.14-5.el8
python3-gobject-base 3.28.3-2.el8
python3-gpg 1.13.1-12.el8
python3-hawkey 0.63.0-20.el8_10
python3-idna 2.5-7.el8_10
python3-iniparse 0.4-31.el8
python3-inotify 0.9.6-13.el8
python3-libcomps 0.1.18-1.el8
python3-libdnf 0.63.0-20.el8_10
python3-librepo 1.14.2-5.el8
python3-libs 3.6.8-67.el8_10
python3-pip-wheel 9.0.3-24.el8
python3-ply 3.9-9.el8
python3-pysocks 1.6.8-3.el8
python3-requests 2.20.0-3.el8_8
python3-rpm 4.14.3-31.el8
python3-setuptools-wheel 39.2.0-8.el8_10
python3-six 1.11.0-8.el8
python3-subscription-manager-rhsm 1.28.42-1.el8
python3-syspurpose 1.28.42-1.el8
python3-systemd 234-8.el8
python3-urllib3 1.24.2-8.el8_10
readline 7.0-10.el8
redhat-release 8.10-0.3.el8
rootfiles 8.1-22.el8
rpm 4.14.3-31.el8
rpm-build-libs 4.14.3-31.el8
rpm-libs 4.14.3-31.el8
rsync 3.1.3-19.el8_7.1
scl-utils 2.0.2-16.el8
sed 4.5-5.el8
setup 2.12.2-9.el8
shadow-utils 4.6-22.el8
sqlite-libs 3.26.0-19.el8_9
subscription-manager 1.28.42-1.el8
subscription-manager-rhsm-certificates 20220623-1.el8
systemd 239-82.el8_10.2
systemd-libs 239-82.el8_10.2
systemd-pam 239-82.el8_10.2
tar 1.30-9.el8
tcl 8.6.8-2.el8
tpm2-tss 2.3.2-6.el8
tzdata 2024a-1.el8
unzip 6.0-46.el8
usermode 1.113-2.el8
util-linux 2.32.1-46.el8
uuid 1.6.2-43.el8
vim-filesystem 8.0.1763-19.el8_6.4
vim-minimal 8.0.1763-19.el8_6.4
virt-what 1.25-4.el8
which 2.21-20.el8
xz 5.2.4-4.el8_6
xz-libs 5.2.4-4.el8_6
yum 4.7.0-20.el8
zlib 1.2.11-25.el8
```

</details>

<details><summary>Python packages: /usr (python3.6) (22)</summary>

```text
chardet 3.0.4
dbus-python 1.2.4
decorator 4.2.1
ethtool 0.14
gpg 1.13.1
idna 2.5
iniparse 0.4
isc 2.0
libcomps 0.1.18
ply 3.9
PyGObject 3.28.3
pyinotify 0.9.6
PySocks 1.6.8
python-dateutil 2.6.1
requests 2.20.0
rpm 4.14.3
setuptools 39.2.0
six 1.11.0
subscription-manager 1.28.42
syspurpose 1.28.42
systemd-python 234
urllib3 1.24.2
```

</details>

[Back to top](#contents)

### redis-6

| Field | Value |
|---|---|
| Image | `registry.redhat.io/rhel8/redis-6` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/redis-6.tar.gz` |
| Labels `version` / `release` | `1` / `204` |
| Image ID | `sha256:c99cedb5e4c13e127c398f6e5507543b9bee4d96f292c72ba980afd15bf9fccd` |
| Build date | 2024-10-04T08:25:42 |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | N/A |
| Ansible Core | N/A |

<details><summary>RPM packages (208)</summary>

```text
acl 2.2.53-3.el8
audit-libs 3.1.2-1.el8
basesystem 11-5.el8
bash 4.4.20-5.el8
brotli 1.0.6-3.el8
bsdtar 3.3.3-5.el8
bzip2-libs 1.0.6-26.el8
ca-certificates 2024.2.69_v8.0.303-80.0.el8_10
chkconfig 1.19.2-1.el8
coreutils-single 8.30-15.el8
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crypto-policies 20230731-1.git3177e06.el8
crypto-policies-scripts 20230731-1.git3177e06.el8
cryptsetup-libs 2.3.7-7.el8
curl 7.61.1-34.el8_10.2
cyrus-sasl-lib 2.1.27-6.el8_5
dbus 1.12.8-26.el8
dbus-common 1.12.8-26.el8
dbus-daemon 1.12.8-26.el8
dbus-glib 0.110-2.el8
dbus-libs 1.12.8-26.el8
dbus-tools 1.12.8-26.el8
device-mapper 1.02.181-14.el8
device-mapper-libs 1.02.181-14.el8
diffutils 3.6-6.el8
dmidecode 3.5-1.el8
dnf 4.7.0-20.el8
dnf-data 4.7.0-20.el8
dnf-plugin-subscription-manager 1.28.42-1.el8
elfutils-default-yama-scope 0.190-2.el8
elfutils-libelf 0.190-2.el8
elfutils-libs 0.190-2.el8
environment-modules 4.5.2-4.el8
expat 2.2.5-15.el8_10
file-libs 5.33-26.el8
filesystem 3.8-6.el8
findutils 4.6.0-23.el8_10
gawk 4.2.1-4.el8
gdb-gdbserver 8.2-20.el8
gdbm 1.18-2.el8
gdbm-libs 1.18-2.el8
gettext 0.19.8.1-17.el8
gettext-libs 0.19.8.1-17.el8
glib2 2.56.4-162.el8
glibc 2.28-251.el8_10.5
glibc-common 2.28-251.el8_10.5
glibc-langpack-en 2.28-251.el8_10.5
glibc-locale-source 2.28-251.el8_10.5
glibc-minimal-langpack 2.28-251.el8_10.5
gmp 6.1.2-11.el8
gnupg2 2.2.20-3.el8_6
gnutls 3.6.16-8.el8_9.3
gobject-introspection 1.56.1-1.el8
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
groff-base 1.22.3-18.el8
gzip 1.9-13.el8_5
ima-evm-utils 1.3.2-12.el8
info 6.5-7.el8
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
kmod-libs 25-20.el8
krb5-libs 1.18.2-29.el8_10
langpacks-en 1.0-12.el8
less 530-3.el8_10
libacl 2.2.53-3.el8
libarchive 3.3.3-5.el8
libassuan 2.5.1-3.el8
libattr 2.4.48-3.el8
libblkid 2.32.1-46.el8
libcap 2.48-6.el8_9
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-5.el8
libcomps 0.1.18-1.el8
libcroco 0.6.12-4.el8_2.1
libcurl 7.61.1-34.el8_10.2
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-20.el8_10
libfdisk 2.32.1-46.el8
libffi 3.1-24.el8
libgcc 8.5.0-22.el8_10
libgcrypt 1.8.5-7.el8_6
libgomp 8.5.0-22.el8_10
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libksba 1.3.5-9.el8_7
libmodulemd 2.13.0-1.el8
libmount 2.32.1-46.el8
libnghttp2 1.33.0-6.el8_10.1
libnl3 3.7.0-1.el8
libnsl2 1.2.0-2.20180605git4a062cf.el8
libpipeline 1.5.0-2.el8
libpsl 0.20.2-6.el8
libpwquality 1.4.4-6.el8
librepo 1.14.2-5.el8
libreport-filesystem 2.9.5-15.el8
librhsm 0.0.3-5.el8
libseccomp 2.5.2-1.el8
libselinux 2.9-8.el8
libselinux-utils 2.9-8.el8
libsemanage 2.9-9.el8
libsepol 2.9-3.el8
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-46.el8
libsolv 0.7.20-6.el8
libssh 0.9.6-14.el8
libssh-config 0.9.6-14.el8
libstdc++ 8.5.0-22.el8_10
libtasn1 4.13-4.el8_7
libtirpc 1.1.4-12.el8_10
libunistring 0.9.9-3.el8
libusbx 1.0.23-4.el8
libuser 0.62-26.el8_10
libutempter 1.1.6-14.el8
libuuid 2.32.1-46.el8
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-18.el8_10.1
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
logrotate 3.14.0-6.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-3.el8_4
man-db 2.7.6.1-18.el8
mpfr 3.1.6-1.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
npth 1.5-4.el8
openldap 2.4.46-19.el8_10
openssl-libs 1.1.1k-12.el8_9
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-34.el8_10
passwd 0.80-4.el8
pcre 8.42-6.el8
pcre2 10.32-3.el8_6
platform-python 3.6.8-67.el8_10
platform-python-setuptools 39.2.0-8.el8_10
policycoreutils 2.9-26.el8_10
popt 1.18-1.el8
procps-ng 3.3.15-14.el8
publicsuffix-list-dafsa 20180723-1.el8
python3-chardet 3.0.4-7.el8
python3-cloud-what 1.28.42-1.el8
python3-dateutil 2.6.1-6.el8
python3-dbus 1.2.4-15.el8
python3-decorator 4.2.1-2.el8
python3-dnf 4.7.0-20.el8
python3-dnf-plugins-core 4.0.21-25.el8
python3-ethtool 0.14-5.el8
python3-gobject-base 3.28.3-2.el8
python3-gpg 1.13.1-12.el8
python3-hawkey 0.63.0-20.el8_10
python3-idna 2.5-7.el8_10
python3-iniparse 0.4-31.el8
python3-inotify 0.9.6-13.el8
python3-libcomps 0.1.18-1.el8
python3-libdnf 0.63.0-20.el8_10
python3-librepo 1.14.2-5.el8
python3-libs 3.6.8-67.el8_10
python3-pip-wheel 9.0.3-24.el8
python3-pysocks 1.6.8-3.el8
python3-requests 2.20.0-3.el8_8
python3-rpm 4.14.3-31.el8
python3-setuptools-wheel 39.2.0-8.el8_10
python3-six 1.11.0-8.el8
python3-subscription-manager-rhsm 1.28.42-1.el8
python3-syspurpose 1.28.42-1.el8
python3-systemd 234-8.el8
python3-urllib3 1.24.2-8.el8_10
readline 7.0-10.el8
redhat-release 8.10-0.3.el8
redis 6.2.7-1.module+el8.7.0+15197+cc495aeb
rootfiles 8.1-22.el8
rpm 4.14.3-31.el8
rpm-build-libs 4.14.3-31.el8
rpm-libs 4.14.3-31.el8
rsync 3.1.3-19.el8_7.1
scl-utils 2.0.2-16.el8
sed 4.5-5.el8
setup 2.12.2-9.el8
shadow-utils 4.6-22.el8
sqlite-libs 3.26.0-19.el8_9
subscription-manager 1.28.42-1.el8
subscription-manager-rhsm-certificates 20220623-1.el8
systemd 239-82.el8_10.2
systemd-libs 239-82.el8_10.2
systemd-pam 239-82.el8_10.2
tar 1.30-9.el8
tcl 8.6.8-2.el8
tpm2-tss 2.3.2-6.el8
tzdata 2024a-1.el8
unzip 6.0-46.el8
usermode 1.113-2.el8
util-linux 2.32.1-46.el8
vim-minimal 8.0.1763-19.el8_6.4
virt-what 1.25-4.el8
which 2.21-20.el8
xz 5.2.4-4.el8_6
xz-libs 5.2.4-4.el8_6
yum 4.7.0-20.el8
zlib 1.2.11-25.el8
```

</details>

<details><summary>Python packages: /usr (python3.6) (20)</summary>

```text
chardet 3.0.4
dbus-python 1.2.4
decorator 4.2.1
ethtool 0.14
gpg 1.13.1
idna 2.5
iniparse 0.4
libcomps 0.1.18
PyGObject 3.28.3
pyinotify 0.9.6
PySocks 1.6.8
python-dateutil 2.6.1
requests 2.20.0
rpm 4.14.3
setuptools 39.2.0
six 1.11.0
subscription-manager 1.28.42
syspurpose 1.28.42
systemd-python 234
urllib3 1.24.2
```

</details>

[Back to top](#contents)

## Installer Collections

Collections shipped with the installer itself (`collections/ansible_collections`).

- `ansible.posix 1.5.4`
- `community.crypto 2.22.0`
- `community.postgresql 3.4.0`
- `containers.podman 1.15.4`
- `infra.ah_configuration 2.0.6`
- `infra.controller_configuration 2.9.0`

## Bundled Collections

Collection tarballs under `bundle/collections/` (uploaded to Automation Hub during install).

<details><summary>Bundled collections (0)</summary>

```text
```

</details>
