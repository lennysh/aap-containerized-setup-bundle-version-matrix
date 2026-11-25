[All AAP versions](../../../README.md) / [AAP 2.5](../README.md) / 2.5-25.5

# AAP Containerized Setup Bundle 2.5-25.5 (x86_64)

- **Bundle file:** `ansible-automation-platform-containerized-setup-bundle-2.5-25.5-x86_64.tar.gz`
- **AAP version:** 2.5
- **Bundle created:** 2026-10-19 18:00:02 UTC
- **Container images:** 14
- **Distinct RPM package versions:** 668
- **Distinct Python package versions:** 553

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
| [registry.redhat.io/ansible-automation-platform-25/controller-rhel8](#controller-rhel8) | `latest` | 4.6.34 | 1791896186 | `63355bc0beb8` | Red Hat Enterprise Linux 8.10 (Ootpa) | 3.12 | N/A | 257 | 224 | 1 |
| [registry.redhat.io/ansible-automation-platform-25/de-supported-rhel8](#de-supported-rhel8) | `latest` | 1.1.7 | 1791896186 | `8f33bb79cf4b` | Red Hat Enterprise Linux 8.10 (Ootpa) | 3.12 | 2.16.19 | 214 | 64 | 2 |
| [registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8](#eda-controller-rhel8) | `latest` | 1.1.23 | 1791896186 | `6f871fb405bb` | Red Hat Enterprise Linux 8.10 (Ootpa) | 3.12 | 2.16.19 | 269 | 95 | 0 |
| [registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8](#eda-controller-ui-rhel8) | `latest` | 1.1.23 | 1791836066 | `be5f2eb5317f` | Red Hat Enterprise Linux 8.10 (Ootpa) | N/A | N/A | 277 | 22 | 0 |
| [registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8](#ee-minimal-rhel8) | `latest` | 2.0.0 | 1791896186 | `453b732edf66` | Red Hat Enterprise Linux 8.10 (Ootpa) | 3.12 | 2.16.19 | 238 | 63 | 0 |
| [registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8](#ee-supported-rhel8) | `latest` | 2.0.0 | 1791765785 | `9a8c53500f7d` | Red Hat Enterprise Linux 8.10 (Ootpa) | 3.12 | 2.16.19 | 337 | 260 | 57 |
| [registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8](#gateway-proxy-rhel8) | `latest` | 2.5.10 | 1791896186 | `6b56b4e12bcc` | Red Hat Enterprise Linux 8.10 (Ootpa) | N/A | N/A | 107 | 0 | 0 |
| [registry.redhat.io/ansible-automation-platform-25/gateway-rhel8](#gateway-rhel8) | `latest` | 2.5.20260923 | 1791896186 | `fbd243f8491e` | Red Hat Enterprise Linux 8.10 (Ootpa) | 3.12 | N/A | 251 | 76 | 0 |
| [registry.redhat.io/ansible-automation-platform-25/hub-rhel8](#hub-rhel8) | `latest` | 4.10.19 | 1791896186 | `9e3128df630e` | Red Hat Enterprise Linux 8.10 (Ootpa) | 3.12 | 2.16.19 | 358 | 171 | 0 |
| [registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8](#hub-web-rhel8) | `latest` | 4.10.19 | 1791940460 | `45142072ef32` | Red Hat Enterprise Linux 8.10 (Ootpa) | N/A | N/A | 277 | 22 | 0 |
| [registry.redhat.io/ansible-automation-platform-25/receptor-rhel8](#receptor-rhel8) | `latest` | 1.6.8 | 1791896186 | `c3bf16344f1d` | Red Hat Enterprise Linux 8.10 (Ootpa) | 3.12 | N/A | 170 | 19 | 0 |
| [registry.redhat.io/rhel8/pcp](#pcp) | `latest` | 5 | 1791892845 | `82b3d5ca8cee` | Red Hat Enterprise Linux 8.10 (Ootpa) | 3.6 | N/A | 215 | 22 | 0 |
| [registry.redhat.io/rhel8/postgresql-15](#postgresql-15) | `latest` | 1 | 1792399398 | `d71c59480312` | Red Hat Enterprise Linux 8.10 (Ootpa) | N/A | N/A | 280 | 22 | 0 |
| [registry.redhat.io/rhel8/redis-6](#redis-6) | `latest` | 1 | 1791943921 | `702ccfad8b3b` | Red Hat Enterprise Linux 8.10 (Ootpa) | N/A | N/A | 208 | 20 | 0 |

## RPM Packages (all images)

Every RPM installed in any image of this bundle (`name version-release`). Search this table for a
package named in a CVE to see which containers ship which version.

| Package | Version-Release | Images |
|---|---|---|
| `aap-metrics-utility` | `0.6.3-2.el8ap` | controller-rhel8 |
| `acl` | `2.4.0-1.el8_10` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `alsa-lib` | `1.2.10-2.el8` | de-supported-rhel8 |
| `ansible-automation-platform-common` | `2.5-2.el8ap` | controller-rhel8, eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `ansible-automation-platform-selinux` | `0.2-3.el8ap` | controller-rhel8, eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `ansible-builder` | `3.1.1-1.2.el8ap` | hub-rhel8 |
| `ansible-core` | `2.16.19-1.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `ansible-lint` | `26.1.1-1.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `ansible-rulebook` | `1.1.7-2.el8ap` | de-supported-rhel8 |
| `ansible-runner` | `2.4.2-3.el8ap` | de-supported-rhel8, ee-minimal-rhel8, ee-supported-rhel8, receptor-rhel8 |
| `ansible-sign` | `0.1.4-2.el8ap` | ee-supported-rhel8 |
| `ansible-test` | `2.16.19-1.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `apr` | `1.6.3-12.el8` | controller-rhel8, ee-supported-rhel8 |
| `apr-util` | `1.6.1-9.el8_10.1` | controller-rhel8, ee-supported-rhel8 |
| `audit-libs` | `3.1.2-1.el8_10.1` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `automation-controller` | `4.6.34-1.el8ap` | controller-rhel8 |
| `automation-controller-cli` | `4.6.34-1.el8ap` | ee-supported-rhel8 |
| `automation-controller-server` | `4.6.34-1.el8ap` | controller-rhel8 |
| `automation-controller-ui` | `4.6.34-1.el8ap` | controller-rhel8 |
| `automation-controller-venv-tower` | `4.6.34-1.el8ap` | controller-rhel8 |
| `automation-eda-controller` | `1.1.23-1.el8ap` | eda-controller-rhel8 |
| `automation-gateway-config` | `2.5.20260923-1.el8ap` | gateway-proxy-rhel8 |
| `automation-gateway-proxy-server` | `2.5.10-8.el8ap` | gateway-proxy-rhel8 |
| `automation-gateway-server` | `2.5.20260923-1.el8ap` | gateway-rhel8 |
| `automation-hub` | `4.10.19-1.el8ap` | hub-rhel8 |
| `avahi-libs` | `0.7-27.el8_10.1` | de-supported-rhel8, pcp |
| `basesystem` | `11-5.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `bash` | `4.4.20-6.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `bash-completion` | `2.7-5.el8` | ee-supported-rhel8 |
| `bind-libs` | `9.11.36-16.el8_10.16` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `bind-libs-lite` | `9.11.36-16.el8_10.16` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `bind-license` | `9.11.36-16.el8_10.16` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `bind-utils` | `9.11.36-16.el8_10.16` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `bindep` | `2.13.0-2.el8ap` | hub-rhel8 |
| `brotli` | `1.0.6-4.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `bsdtar` | `3.3.3-7.el8_10` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15, redis-6 |
| `bzip2` | `1.0.6-28.el8_10` | ee-minimal-rhel8, ee-supported-rhel8 |
| `bzip2-libs` | `1.0.6-28.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `ca-certificates` | `2025.2.80_v9.0.304-80.2.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `checkpolicy` | `2.9-1.el8` | controller-rhel8, eda-controller-rhel8, gateway-rhel8 |
| `chkconfig` | `1.19.2-1.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `cmake` | `3.26.5-2.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `cmake-data` | `3.26.5-2.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `cmake-filesystem` | `3.26.5-2.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `cmake-rpm-macros` | `3.26.5-2.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `container-selinux` | `2.229.0-3.module+el8.10.0+24790+ef71b018` | hub-rhel8 |
| `containers-common` | `1-82.module+el8.10.0+24790+ef71b018` | hub-rhel8 |
| `copy-jdk-configs` | `4.0-2.el8` | de-supported-rhel8 |
| `coreutils-single` | `8.30-21.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `cracklib` | `2.9.6-15.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `cracklib-dicts` | `2.9.6-15.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `crontabs` | `1.11-17.20190603git.el8` | controller-rhel8 |
| `crun` | `1.14.3-4.module+el8.10.0+24790+ef71b018` | controller-rhel8 |
| `crypto-policies` | `20230731-1.git3177e06.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `crypto-policies-scripts` | `20230731-1.git3177e06.el8` | de-supported-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `cryptsetup-libs` | `2.3.7-7.el8` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `cups-libs` | `2.2.6-68.el8_10` | de-supported-rhel8 |
| `curl` | `7.61.1-34.el8_10.13` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `cyrus-sasl-lib` | `2.1.27-6.el8_5` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `dbus` | `1.12.8-28.el8_10` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `dbus-common` | `1.12.8-28.el8_10` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `dbus-daemon` | `1.12.8-28.el8_10` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `dbus-glib` | `0.110-2.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `dbus-libs` | `1.12.8-28.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `dbus-tools` | `1.12.8-28.el8_10` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `device-mapper` | `1.02.181-15.el8_10.3` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `device-mapper-libs` | `1.02.181-15.el8_10.3` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `diffutils` | `3.6-6.el8` | controller-rhel8, eda-controller-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, receptor-rhel8, pcp, redis-6 |
| `dmidecode` | `3.5-1.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `dnf` | `4.7.0-21.el8_10` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `dnf-data` | `4.7.0-21.el8_10` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `dnf-plugin-subscription-manager` | `1.28.44-1.el8_10` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `dumb-init` | `1.2.5-3.el8ap` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, receptor-rhel8 |
| `elfutils-default-yama-scope` | `0.190-2.el8` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `elfutils-libelf` | `0.190-2.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `elfutils-libs` | `0.190-2.el8` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `emacs-filesystem` | `26.1-15.el8_10.2` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `environment-modules` | `4.5.2-4.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15, redis-6 |
| `expat` | `2.5.0-4.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `file` | `5.33-27.el8_10` | ee-minimal-rhel8, ee-supported-rhel8 |
| `file-libs` | `5.33-27.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `filesystem` | `3.8-6.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `findutils` | `4.6.0-24.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `fstrm` | `0.6.1-3.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `gawk` | `4.2.1-5.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `gdb-gdbserver` | `8.2-20.1.el8_10` | eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `gdbm` | `1.18-2.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `gdbm-libs` | `1.18-2.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `geolite2-city` | `20180605-1.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `geolite2-country` | `20180605-1.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `gettext` | `0.19.8.1-17.el8` | eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `gettext-libs` | `0.19.8.1-17.el8` | eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `git-core` | `2.43.7-1.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `git-lfs` | `3.4.1-13.el8_10` | controller-rhel8, ee-supported-rhel8 |
| `glib2` | `2.56.4-178.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `glibc` | `2.28-251.el8_10.43` | eda-controller-ui-rhel8 |
| `glibc` | `2.28-251.el8_10.48` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `glibc-common` | `2.28-251.el8_10.43` | eda-controller-ui-rhel8 |
| `glibc-common` | `2.28-251.el8_10.48` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `glibc-langpack-en` | `2.28-251.el8_10.43` | eda-controller-ui-rhel8 |
| `glibc-langpack-en` | `2.28-251.el8_10.48` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-web-rhel8, postgresql-15, redis-6 |
| `glibc-locale-source` | `2.28-251.el8_10.43` | eda-controller-ui-rhel8 |
| `glibc-locale-source` | `2.28-251.el8_10.48` | hub-web-rhel8, postgresql-15, redis-6 |
| `glibc-minimal-langpack` | `2.28-251.el8_10.43` | eda-controller-ui-rhel8 |
| `glibc-minimal-langpack` | `2.28-251.el8_10.48` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `gmp` | `6.1.2-11.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `gnupg2` | `2.2.20-4.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `gnutls` | `3.6.16-8.el8_10.6` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `gobject-introspection` | `1.56.1-2.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `gpg-pubkey` | `d4082792-5b32db75` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `gpg-pubkey` | `fd431d51-4ae0493b` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `gpgme` | `1.13.1-12.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `grep` | `3.1-6.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `groff-base` | `1.22.3-18.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15, redis-6 |
| `gzip` | `1.9-15.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `hostname` | `3.20-6.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp |
| `ima-evm-utils` | `1.3.2-12.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `info` | `6.5-7.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `java-17-openjdk-headless` | `17.0.20.1.1-1.1.el8` | de-supported-rhel8 |
| `javapackages-filesystem` | `5.3.0-2.module+el8+2598+06babf2e` | de-supported-rhel8 |
| `jq` | `1.6-12.el8_10` | hub-rhel8 |
| `json-c` | `0.13.1-3.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `json-glib` | `1.4.4-1.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `keyutils-libs` | `1.5.10-9.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `kmod-libs` | `25-20.el8` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `krb5-libs` | `1.18.2-34.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `krb5-workstation` | `1.18.2-34.el8_10` | controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8 |
| `langpacks-en` | `1.0-12.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `less` | `530-3.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8, hub-web-rhel8, postgresql-15, redis-6 |
| `libacl` | `2.4.0-1.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libaio` | `0.3.112-1.el8` | ee-supported-rhel8 |
| `libarchive` | `3.3.3-7.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libassuan` | `2.5.1-3.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libattr` | `2.6.0-1.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libblkid` | `2.32.1-48.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libcap` | `2.48-6.el8_10.1` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libcap-ng` | `0.7.11-1.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libcom_err` | `1.45.6-7.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libcomps` | `0.1.18-1.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `libcroco` | `0.6.12-4.el8_2.1` | eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `libcurl` | `7.61.1-34.el8_10.13` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libdb` | `5.3.28-42.el8_4` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libdb-utils` | `5.3.28-42.el8_4` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libdnf` | `0.63.0-21.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libedit` | `3.1-23.20170329cvs.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `libestr` | `0.1.10-3.el8` | controller-rhel8, hub-rhel8 |
| `libfastjson` | `0.99.9-2.el8` | controller-rhel8, hub-rhel8 |
| `libfdisk` | `2.32.1-48.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libffi` | `3.1-24.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libgcc` | `8.5.0-29.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libgcrypt` | `1.8.5-8.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libgfortran` | `8.5.0-29.el8_10` | controller-rhel8 |
| `libgomp` | `8.5.0-29.el8_10` | eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `libgpg-error` | `1.31-1.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libicu` | `60.3-2.el8_1` | postgresql-15 |
| `libidn2` | `2.2.0-1.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libjpeg-turbo` | `1.5.3-14.el8_10` | hub-rhel8 |
| `libkadm5` | `1.18.2-34.el8_10` | controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8 |
| `libksba` | `1.3.5-9.el8_7` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libmaxminddb` | `1.2.0-10.el8_9.1` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `libmodulemd` | `2.13.0-1.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libmount` | `2.32.1-48.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libnghttp2` | `1.33.0-6.el8_10.3` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libnl3` | `3.7.0-1.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `libnsl2` | `1.2.0-2.20180605git4a062cf.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libpeas` | `1.22.0-6.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, receptor-rhel8 |
| `libpipeline` | `1.5.0-2.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15, redis-6 |
| `libpkgconf` | `1.4.2-1.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `libpq` | `13.23-2.el8_10` | de-supported-rhel8, eda-controller-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `libpsl` | `0.20.2-6.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libpwquality` | `1.4.4-6.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libquadmath` | `8.5.0-29.el8_10` | controller-rhel8 |
| `librepo` | `1.14.2-5.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libreport-filesystem` | `2.9.5-15.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `librhsm` | `0.0.3-5.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libseccomp` | `2.5.2-1.el8` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libsecret` | `0.18.6-1.el8` | hub-rhel8 |
| `libselinux` | `2.9-11.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libselinux-utils` | `2.9-11.el8_10` | controller-rhel8, eda-controller-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, receptor-rhel8, redis-6 |
| `libsemanage` | `2.9-12.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libsepol` | `2.9-3.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libserf` | `1.3.9-9.module+el8.3.0+6671+2675c974` | controller-rhel8, ee-supported-rhel8 |
| `libsigsegv` | `2.11-5.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libsmartcols` | `2.32.1-48.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libsolv` | `0.7.20-7.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libss` | `1.45.6-7.el8_10` | controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8 |
| `libssh` | `0.9.6-17.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libssh-config` | `0.9.6-17.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libstdc++` | `8.5.0-29.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libtasn1` | `4.13-6.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libtirpc` | `1.1.4-12.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libtool-ltdl` | `2.4.6-25.el8` | controller-rhel8, gateway-rhel8 |
| `libunistring` | `0.9.9-3.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libusbx` | `1.0.30-1.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libuser` | `0.62-26.el8_10` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `libutempter` | `1.1.6-14.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libuuid` | `2.32.1-48.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libuv` | `1.41.1-2.el8_10` | eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15 |
| `libverto` | `0.3.2-2.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libxcrypt` | `4.1.1-6.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libxml2` | `2.9.7-21.el8_10.10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libxml2` | `2.9.7-21.el8_10.9` | eda-controller-ui-rhel8 |
| `libxslt` | `1.1.32-6.4.el8_10` | controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, postgresql-15 |
| `libyaml` | `0.1.7-5.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `libzstd` | `1.4.4-1.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `lksctp-tools` | `1.0.18-3.el8` | de-supported-rhel8 |
| `logrotate` | `3.14.0-6.el8` | controller-rhel8, ee-supported-rhel8, hub-rhel8, receptor-rhel8, redis-6 |
| `lua` | `5.3.4-12.el8` | de-supported-rhel8 |
| `lua-libs` | `5.3.4-12.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `lz4-libs` | `1.8.3-5.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `mailcap` | `2.1.48-3.el8` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `make` | `4.2.1-11.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `man-db` | `2.7.6.1-18.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15, redis-6 |
| `microdnf` | `3.8.0-2.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, receptor-rhel8 |
| `mpdecimal` | `2.5.1-3.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, receptor-rhel8 |
| `mpfr` | `3.1.6-1.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `ncurses` | `6.1-10.20180224.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `ncurses-base` | `6.1-10.20180224.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `ncurses-libs` | `6.1-10.20180224.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `nettle` | `3.4.1-7.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `nginx` | `1.24.0-3.module+el8.10.0+24848+0300f002.5` | controller-rhel8, eda-controller-ui-rhel8, gateway-rhel8, hub-web-rhel8 |
| `nginx-filesystem` | `1.24.0-3.module+el8.10.0+24848+0300f002.5` | controller-rhel8, eda-controller-ui-rhel8, gateway-rhel8, hub-web-rhel8 |
| `nginx-mod-http-perl` | `1.24.0-3.module+el8.10.0+24848+0300f002.5` | eda-controller-ui-rhel8, hub-web-rhel8 |
| `nginx-mod-stream` | `1.24.0-3.module+el8.10.0+24848+0300f002.5` | eda-controller-ui-rhel8, hub-web-rhel8 |
| `npth` | `1.5-4.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `nspr` | `4.39.0-3.el8_10` | de-supported-rhel8, pcp |
| `nss` | `3.124.0-5.el8_10` | de-supported-rhel8, pcp |
| `nss-softokn` | `3.124.0-5.el8_10` | de-supported-rhel8, pcp |
| `nss-softokn-freebl` | `3.124.0-5.el8_10` | de-supported-rhel8, pcp |
| `nss-sysinit` | `3.124.0-5.el8_10` | de-supported-rhel8, pcp |
| `nss-util` | `3.124.0-5.el8_10` | de-supported-rhel8, pcp |
| `nss_wrapper` | `1.1.13-1.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `nss_wrapper-libs` | `1.1.13-1.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `oniguruma` | `6.9.7.1-2.el8ap` | hub-rhel8 |
| `openblas` | `0.3.15-6.el8` | controller-rhel8 |
| `openldap` | `2.4.46-21.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `openshift-clients` | `4.14.0-202609111720.p2.g44b3ac2.assembly.stream.el8` | ee-supported-rhel8 |
| `openssh` | `8.0p1-33.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `openssh-clients` | `8.0p1-33.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `openssl` | `1.1.1k-17.el8_6` | controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, postgresql-15 |
| `openssl-libs` | `1.1.1k-17.el8_6` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `p11-kit` | `0.23.22-2.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `p11-kit-trust` | `0.23.22-2.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `pam` | `1.3.1-40.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `passwd` | `0.80-4.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `pcp` | `5.3.7-22.el8_10.5` | pcp |
| `pcp-conf` | `5.3.7-22.el8_10.5` | pcp |
| `pcp-doc` | `5.3.7-22.el8_10.5` | pcp |
| `pcp-libs` | `5.3.7-22.el8_10.5` | pcp |
| `pcp-pmda-dm` | `5.3.7-22.el8_10.5` | pcp |
| `pcp-pmda-nfsclient` | `5.3.7-22.el8_10.5` | pcp |
| `pcp-pmda-openmetrics` | `5.3.7-22.el8_10.5` | pcp |
| `pcp-system-tools` | `5.3.7-22.el8_10.5` | pcp |
| `pcp-zeroconf` | `5.3.7-22.el8_10.5` | pcp |
| `pcre` | `8.42-6.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `pcre2` | `10.32-3.el8_6` | eda-controller-ui-rhel8, ee-supported-rhel8, pcp |
| `pcre2` | `10.32-4.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, postgresql-15, redis-6 |
| `perl-Carp` | `1.42-396.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-constant` | `1.33-396.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Data-Dumper` | `2.167-399.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Digest` | `1.17-395.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Digest-MD5` | `2.55-396.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Encode` | `2.97-3.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Errno` | `1.28-423.el8_10.1` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Exporter` | `5.72-396.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-File-Path` | `2.15-2.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-File-Temp` | `0.230.600-1.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Getopt-Long` | `2.50-4.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-HTTP-Tiny` | `0.074-3.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-interpreter` | `5.26.3-423.el8_10.1` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-IO` | `1.38-423.el8_10.1` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-IO-Socket-IP` | `0.39-5.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-IO-Socket-SSL` | `2.066-4.module+el8.3.0+6446+594cad75` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-libnet` | `3.11-3.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-libs` | `5.26.3-423.el8_10.1` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-macros` | `5.26.3-423.el8_10.1` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-MIME-Base64` | `3.15-396.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Mozilla-CA` | `20160104-7.module+el8.3.0+6498+9eecfe51` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Net-SSLeay` | `1.88-2.module+el8.6.0+13392+f0897f98` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-parent` | `0.237-1.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-PathTools` | `3.74-1.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Pod-Escapes` | `1.07-395.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Pod-Perldoc` | `3.28-396.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Pod-Simple` | `3.35-395.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Pod-Usage` | `1.69-395.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-podlators` | `4.11-1.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Scalar-List-Utils` | `1.49-2.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Socket` | `2.027-3.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Storable` | `3.11-3.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Term-ANSIColor` | `4.06-396.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Term-Cap` | `1.17-395.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Text-ParseWords` | `3.30-395.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Text-Tabs+Wrap` | `2013.0523-395.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-threads` | `2.21-2.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-threads-shared` | `1.58-2.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Time-Local` | `1.280-1.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-Unicode-Normalize` | `1.25-396.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `perl-URI` | `1.73-3.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8 |
| `perl-URI` | `1.73-4.el8_10` | postgresql-15 |
| `pgaudit` | `1.7.0-1.module+el8.9.0+19797+c4ce5969` | postgresql-15 |
| `pinentry` | `1.1.0-2.el8` | hub-rhel8 |
| `pkgconf` | `1.4.2-1.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `pkgconf-m4` | `1.4.2-1.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `pkgconf-pkg-config` | `1.4.2-1.el8` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15 |
| `platform-python` | `3.6.8-78.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `platform-python-pip` | `9.0.3-24.el8` | pcp |
| `platform-python-setuptools` | `39.2.0-9.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `podman-remote` | `4.9.4-37.module+el8.10.0+24790+ef71b018` | controller-rhel8, eda-controller-rhel8, ee-supported-rhel8, receptor-rhel8 |
| `policycoreutils` | `2.9-26.el8_10` | controller-rhel8, eda-controller-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, receptor-rhel8, redis-6 |
| `policycoreutils-python-utils` | `2.9-26.el8_10` | controller-rhel8, eda-controller-rhel8, gateway-rhel8 |
| `popt` | `1.18-1.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `postgresql` | `15.19-1.module+el8.10.0+24831+9c841e4e` | controller-rhel8, gateway-rhel8, postgresql-15 |
| `postgresql-contrib` | `15.19-1.module+el8.10.0+24831+9c841e4e` | postgresql-15 |
| `postgresql-private-libs` | `15.19-1.module+el8.10.0+24831+9c841e4e` | controller-rhel8, gateway-rhel8, postgresql-15 |
| `postgresql-server` | `15.19-1.module+el8.10.0+24831+9c841e4e` | postgresql-15 |
| `postgresql-upgrade` | `15.19-1.module+el8.10.0+24831+9c841e4e` | postgresql-15 |
| `procps-ng` | `3.3.15-14.el8` | eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `protobuf-c` | `1.3.0-8.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `publicsuffix-list-dafsa` | `20180723-1.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `pulpcore-selinux` | `2.0.1-2.el8ap` | hub-rhel8 |
| `python3-audit` | `3.1.2-1.el8_10.1` | controller-rhel8, eda-controller-rhel8, gateway-rhel8 |
| `python3-bind` | `9.11.36-16.el8_10.16` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `python3-cffi` | `1.11.5-6.el8` | controller-rhel8, eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3-chardet` | `3.0.4-7.el8` | controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `python3-cloud-what` | `1.28.44-1.el8_10` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-cryptography` | `3.2.1-8.el8_10` | controller-rhel8, eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3-dateutil` | `2.6.1-6.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-dbus` | `1.2.4-15.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-decorator` | `4.2.1-2.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-dnf` | `4.7.0-21.el8_10` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-dnf-plugins-core` | `4.0.21-25.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-ethtool` | `0.14-5.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-gobject-base` | `3.28.3-2.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-gpg` | `1.13.1-12.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-hawkey` | `0.63.0-21.el8_10` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-idna` | `2.5-8.el8_10` | controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `python3-iniparse` | `0.4-31.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-inotify` | `0.9.6-13.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-libcomps` | `0.1.18-1.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-libdnf` | `0.63.0-21.el8_10` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-librepo` | `1.14.2-5.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-libs` | `3.6.8-78.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `python3-libselinux` | `2.9-11.el8_10` | controller-rhel8, eda-controller-rhel8, gateway-rhel8 |
| `python3-libsemanage` | `2.9-12.el8_10` | controller-rhel8, eda-controller-rhel8, gateway-rhel8 |
| `python3-pcp` | `5.3.7-22.el8_10.5` | pcp |
| `python3-pip` | `9.0.3-24.el8` | pcp |
| `python3-pip-wheel` | `9.0.3-24.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `python3-ply` | `3.9-9.el8` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, postgresql-15 |
| `python3-policycoreutils` | `2.9-26.el8_10` | controller-rhel8, eda-controller-rhel8, gateway-rhel8 |
| `python3-pycparser` | `2.14-14.el8` | controller-rhel8, eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3-pysocks` | `1.6.8-3.el8` | controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `python3-requests` | `2.20.0-6.el8_10` | controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `python3-rpm` | `4.14.3-32.el8_10` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-setools` | `4.3.0-5.el8` | controller-rhel8, eda-controller-rhel8, gateway-rhel8 |
| `python3-setuptools` | `39.2.0-9.el8_10` | controller-rhel8, ee-supported-rhel8, hub-rhel8, receptor-rhel8, pcp |
| `python3-setuptools-wheel` | `39.2.0-9.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `python3-six` | `1.11.0-8.el8` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `python3-subscription-manager-rhsm` | `1.28.44-1.el8_10` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-syspurpose` | `1.28.44-1.el8_10` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-systemd` | `234-8.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `python3-urllib3` | `1.24.2-10.el8_10` | controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `python3.12` | `3.12.15-2.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, receptor-rhel8 |
| `python3.12-aiodns` | `3.2.0-2.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-aiofiles` | `23.2.1-2.el8ap` | hub-rhel8 |
| `python3.12-aiohappyeyeballs` | `2.6.1-1.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-aiohttp` | `3.14.3-1.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-aiosignal` | `1.4.0-1.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-ansible-compat` | `25.12.0-3.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-ansible-pylibssh` | `1.2.2-2.el8ap` | ee-supported-rhel8 |
| `python3.12-ansible-runner` | `2.4.2-3.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, receptor-rhel8 |
| `python3.12-argon2-cffi` | `23.1.0-2.el8ap` | gateway-rhel8 |
| `python3.12-argon2-cffi-bindings` | `21.2.0-2.el8ap` | gateway-rhel8 |
| `python3.12-asgiref` | `3.11.1-1.el8ap` | eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-asyncio-throttle` | `1.0.2-5.el8ap` | hub-rhel8 |
| `python3.12-attrs` | `22.2.0-2.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-autobahn` | `24.4.2-2.el8ap` | eda-controller-rhel8 |
| `python3.12-Automat` | `22.10.0-4.el8ap` | eda-controller-rhel8 |
| `python3.12-azure-core` | `1.34.0-2.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-azure-storage-blob` | `12.19.0-2.el8ap` | hub-rhel8 |
| `python3.12-backoff` | `2.2.1-2.el8ap` | hub-rhel8 |
| `python3.12-black` | `26.3.1-1.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-boto3` | `1.34.30-2.el8ap` | ee-supported-rhel8, hub-rhel8 |
| `python3.12-botocore` | `1.34.162-2.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-bracex` | `2.4-2.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-brotli` | `1.2.0-1.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-cachetools` | `5.3.2-2.el8ap` | eda-controller-rhel8, ee-supported-rhel8 |
| `python3.12-certifi` | `2023.5.7-2.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-cffi` | `2.0.0-1.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-channels` | `4.3.2-1.el8ap` | eda-controller-rhel8 |
| `python3.12-channels+daphne` | `4.3.2-1.el8ap` | eda-controller-rhel8 |
| `python3.12-chardet` | `5.2.0-3.el8ap` | ee-supported-rhel8 |
| `python3.12-charset-normalizer` | `3.3.0-2.el8` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-click` | `8.3.3-1.el8ap` | eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8, receptor-rhel8 |
| `python3.12-constantly` | `23.10.4-1.el8ap` | eda-controller-rhel8 |
| `python3.12-croniter` | `2.0.1-2.el8ap` | eda-controller-rhel8 |
| `python3.12-crontab` | `1.0.5-1.el8ap` | eda-controller-rhel8 |
| `python3.12-cryptography` | `46.0.7-1.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-daemon` | `3.1.2-3.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, receptor-rhel8 |
| `python3.12-daphne` | `4.2.2-1.el8ap` | eda-controller-rhel8 |
| `python3.12-dateutil` | `2.8.2-3.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-supported-rhel8, hub-rhel8, receptor-rhel8 |
| `python3.12-defusedxml` | `0.7.1-5.el8ap` | gateway-rhel8, hub-rhel8 |
| `python3.12-deprecated` | `1.2.14-2.el8ap` | ee-supported-rhel8, hub-rhel8 |
| `python3.12-diff-match-patch` | `20230430-2.el8ap` | hub-rhel8 |
| `python3.12-dispatcherd` | `2025.5.19-3.el8ap` | eda-controller-rhel8 |
| `python3.12-dispatcherd+pg_notify` | `2025.5.19-3.el8ap` | eda-controller-rhel8 |
| `python3.12-distlib` | `0.4.0-2.el8ap` | ee-supported-rhel8 |
| `python3.12-distro` | `1.9.0-2.el8ap` | eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-django` | `5.2.17-1.el8ap` | eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-django-ansible-base` | `2.5.20260422-2.el8ap` | eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-django-ansible-base+activitystream` | `2.5.20260422-2.el8ap` | gateway-rhel8 |
| `python3.12-django-ansible-base+api_documentation` | `2.5.20260422-2.el8ap` | gateway-rhel8 |
| `python3.12-django-ansible-base+authentication` | `2.5.20260422-2.el8ap` | gateway-rhel8 |
| `python3.12-django-ansible-base+channel_auth` | `2.5.20260422-2.el8ap` | eda-controller-rhel8 |
| `python3.12-django-ansible-base+feature_flags` | `2.5.20260422-2.el8ap` | eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-django-ansible-base+jwt_consumer` | `2.5.20260422-2.el8ap` | eda-controller-rhel8, hub-rhel8 |
| `python3.12-django-ansible-base+oauth2_provider` | `2.5.20260422-2.el8ap` | gateway-rhel8 |
| `python3.12-django-ansible-base+rbac` | `2.5.20260422-2.el8ap` | eda-controller-rhel8, gateway-rhel8 |
| `python3.12-django-ansible-base+redis_client` | `2.5.20260422-2.el8ap` | eda-controller-rhel8, gateway-rhel8 |
| `python3.12-django-ansible-base+rest_filters` | `2.5.20260422-2.el8ap` | eda-controller-rhel8, gateway-rhel8 |
| `python3.12-django-auth-ldap` | `4.0.0-3.el8ap` | gateway-rhel8, hub-rhel8 |
| `python3.12-django-crum` | `0.7.9-3.el8ap` | eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-django-dynamic-preferences` | `1.16.0-2.el8ap` | gateway-rhel8 |
| `python3.12-django-extensions` | `4.1-2.el8ap` | gateway-rhel8 |
| `python3.12-django-filter` | `25.2-1.el8ap` | eda-controller-rhel8, hub-rhel8 |
| `python3.12-django-flags` | `5.0.13-2.el8ap` | eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-django-guid` | `3.4.0-2.el8ap` | hub-rhel8 |
| `python3.12-django-import-export` | `3.3.6-3.el8ap` | hub-rhel8 |
| `python3.12-django-ipware` | `3.0.7-4.el8ap` | hub-rhel8 |
| `python3.12-django-lifecycle` | `1.1.2-2.el8ap` | hub-rhel8 |
| `python3.12-django-oauth-toolkit` | `2.3.0-2.el8ap` | gateway-rhel8 |
| `python3.12-django-picklefield` | `3.1-2.el8ap` | hub-rhel8 |
| `python3.12-django-prometheus` | `2.3.1-3.el8ap` | hub-rhel8 |
| `python3.12-django-redis` | `5.4.0-2.el8ap` | eda-controller-rhel8, gateway-rhel8 |
| `python3.12-django-rq` | `3.2.2-1.el8ap` | eda-controller-rhel8 |
| `python3.12-django-split-settings` | `1.2.0-3.el8ap` | eda-controller-rhel8 |
| `python3.12-django-storages` | `1.14.2-3.el8ap` | hub-rhel8 |
| `python3.12-django-storages+azure` | `1.14.2-3.el8ap` | hub-rhel8 |
| `python3.12-django-storages+s3` | `1.14.2-3.el8ap` | hub-rhel8 |
| `python3.12-djangorestframework` | `3.15.1-2.el8ap` | eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-djangorestframework-queryfields` | `1.1.0-2.el8ap` | hub-rhel8 |
| `python3.12-dpath` | `2.1.6-2.el8ap` | de-supported-rhel8, ee-supported-rhel8 |
| `python3.12-drf-access-policy` | `1.5.0-2.el8ap` | hub-rhel8 |
| `python3.12-drf-nested-routers` | `0.93.5-2.el8ap` | hub-rhel8 |
| `python3.12-drf-spectacular` | `0.29.0-1.el8ap` | eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-drools-jpy` | `0.3.10-2.el8ap` | de-supported-rhel8 |
| `python3.12-drools-jpy-jar` | `1.0.7-2.Final_redhat_00001.1.el8ap` | de-supported-rhel8 |
| `python3.12-dynaconf` | `3.2.11-2.el8ap` | eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-ecdsa` | `0.18.0-2.el8ap` | eda-controller-rhel8 |
| `python3.12-et-xmlfile` | `1.1.0-4.el8ap` | hub-rhel8 |
| `python3.12-filelock` | `3.13.1-2.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-flake8` | `6.1.0-3.el8ap` | hub-rhel8 |
| `python3.12-freezegun` | `1.5.5-1.el8ap` | eda-controller-rhel8 |
| `python3.12-frozenlist` | `1.4.0-2.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-galaxy-importer` | `0.4.38-1.el8ap` | hub-rhel8 |
| `python3.12-galaxy-ng` | `4.10.19-1.el8ap` | hub-rhel8 |
| `python3.12-gitdb` | `4.0.11-2.el8ap` | hub-rhel8 |
| `python3.12-gitpython` | `3.1.60-1.el8ap` | hub-rhel8 |
| `python3.12-gnupg` | `0.5.2-2.el8ap` | eda-controller-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-google-auth` | `2.27.0-2.el8ap` | eda-controller-rhel8, ee-supported-rhel8 |
| `python3.12-googleapis-common-protos` | `1.72.0-1.el8ap` | gateway-rhel8, hub-rhel8 |
| `python3.12-grpcio` | `1.71.2-1.el8ap` | ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-grpcio-tools` | `1.71.2-1.el8ap` | gateway-rhel8 |
| `python3.12-gunicorn` | `23.0.0-2.el8ap` | eda-controller-rhel8, hub-rhel8 |
| `python3.12-hyperlink` | `21.0.0-3.el8ap` | eda-controller-rhel8 |
| `python3.12-idna` | `3.4-2.el8` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-importlib-metadata` | `6.0.1-3.el8ap` | ee-supported-rhel8, hub-rhel8 |
| `python3.12-incremental` | `24.7.2-2.el8ap` | eda-controller-rhel8 |
| `python3.12-inflection` | `0.5.1-5.el8ap` | eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-insights-analytics-collector` | `0.3.2-3.el8ap` | eda-controller-rhel8, hub-rhel8 |
| `python3.12-isodate` | `0.6.1-3.el8ap` | de-supported-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-janus` | `1.0.0-3.el8ap` | de-supported-rhel8 |
| `python3.12-jinja2` | `3.1.6-2.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-jmespath` | `1.0.1-3.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-jpy` | `0.15.0-2.el8ap` | de-supported-rhel8 |
| `python3.12-jq` | `1.6.0-2.el8ap` | hub-rhel8 |
| `python3.12-json-stream` | `2.3.2-2.el8ap` | hub-rhel8 |
| `python3.12-json-stream-rs-tokenizer` | `0.4.26-2.el8ap` | hub-rhel8 |
| `python3.12-jsonschema` | `4.21.1-2.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-jsonschema-specifications` | `2023.12.1-2.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-jwcrypto` | `1.5.7-1.el8ap` | gateway-rhel8 |
| `python3.12-kubernetes` | `26.1.0-3.el8ap` | eda-controller-rhel8 |
| `python3.12-ldap` | `3.4.5-1.el8ap` | gateway-rhel8, hub-rhel8 |
| `python3.12-ldap-filter` | `1.0.1-2.el8ap` | gateway-rhel8 |
| `python3.12-libs` | `3.12.15-2.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, receptor-rhel8 |
| `python3.12-lockfile` | `0.12.2-3.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, receptor-rhel8 |
| `python3.12-lxml` | `5.3.0-2.el8ap` | gateway-rhel8 |
| `python3.12-markdown` | `3.10.2-1.el8ap` | hub-rhel8 |
| `python3.12-markuppy` | `1.14-5.el8ap` | hub-rhel8 |
| `python3.12-markupsafe` | `2.1.5-2.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-marshmallow` | `3.26.2-1.el8ap` | hub-rhel8 |
| `python3.12-mccabe` | `0.7.0-3.el8ap` | hub-rhel8 |
| `python3.12-multidict` | `6.0.4-2.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-mypy-extensions` | `1.0.0-2.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-netaddr` | `1.2.1-2.el8ap` | ee-supported-rhel8, gateway-rhel8 |
| `python3.12-nh3` | `0.2.18-2.el8ap` | hub-rhel8 |
| `python3.12-oauthlib` | `3.2.2-2.el8ap` | eda-controller-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-odfpy` | `1.4.1-9.el8ap` | hub-rhel8 |
| `python3.12-openpyxl` | `3.1.2-2.el8ap` | hub-rhel8 |
| `python3.12-opentelemetry-api` | `1.28.0-1.el8ap` | hub-rhel8 |
| `python3.12-opentelemetry-distro` | `0.49b0-1.el8ap` | hub-rhel8 |
| `python3.12-opentelemetry-distro+otlp` | `0.49b0-1.el8ap` | hub-rhel8 |
| `python3.12-opentelemetry-exporter-otlp` | `1.28.0-1.el8ap` | hub-rhel8 |
| `python3.12-opentelemetry-exporter-otlp-proto-common` | `1.28.0-1.el8ap` | hub-rhel8 |
| `python3.12-opentelemetry-exporter-otlp-proto-grpc` | `1.28.0-1.el8ap` | hub-rhel8 |
| `python3.12-opentelemetry-exporter-otlp-proto-http` | `1.28.0-1.el8ap` | hub-rhel8 |
| `python3.12-opentelemetry-instrumentation` | `0.49b0-1.el8ap` | hub-rhel8 |
| `python3.12-opentelemetry-instrumentation-django` | `0.49b0-1.el8ap` | hub-rhel8 |
| `python3.12-opentelemetry-instrumentation-wsgi` | `0.49b0-1.el8ap` | hub-rhel8 |
| `python3.12-opentelemetry-proto` | `1.28.0-1.el8ap` | gateway-rhel8, hub-rhel8 |
| `python3.12-opentelemetry-sdk` | `1.28.0-1.el8ap` | hub-rhel8 |
| `python3.12-opentelemetry-semantic-conventions` | `0.49b0-1.el8ap` | hub-rhel8 |
| `python3.12-opentelemetry-util-http` | `0.49b0-1.el8ap` | hub-rhel8 |
| `python3.12-packaging` | `23.2-2.el8` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8, receptor-rhel8 |
| `python3.12-parsley` | `1.3-4.el8ap` | hub-rhel8 |
| `python3.12-pathspec` | `1.0.4-1.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-pbr` | `6.0.0-3.el8ap` | hub-rhel8 |
| `python3.12-persisting-theory` | `1.0-3.el8ap` | gateway-rhel8 |
| `python3.12-pexpect` | `4.9.0-2.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, receptor-rhel8 |
| `python3.12-pillow` | `12.3.0-1.el8ap` | hub-rhel8 |
| `python3.12-pip` | `23.2.1-4.el8` | de-supported-rhel8, ee-minimal-rhel8, ee-supported-rhel8 |
| `python3.12-pip-wheel` | `23.2.1-4.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, receptor-rhel8 |
| `python3.12-platformdirs` | `4.2.0-2.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-ply` | `3.11-2.el8` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-podman` | `5.4.0.1-2.el8ap` | eda-controller-rhel8 |
| `python3.12-prometheus-client` | `0.19.0-2.el8ap` | hub-rhel8 |
| `python3.12-propcache` | `0.4.1-1.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-protobuf` | `5.29.6-1.el8ap` | ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-psycopg` | `3.2.7-2.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-psycopg+c` | `3.2.7-2.el8ap` | de-supported-rhel8 |
| `python3.12-psycopg-c` | `3.2.7-2.el8ap` | de-supported-rhel8 |
| `python3.12-ptyprocess` | `0.7.0-2.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, receptor-rhel8 |
| `python3.12-pulp-ansible` | `0.25.6-1.el8ap` | hub-rhel8 |
| `python3.12-pulp-container` | `2.19.12-1.el8ap` | hub-rhel8 |
| `python3.12-pulp-glue` | `0.23.2-2.el8ap` | hub-rhel8 |
| `python3.12-pulpcore` | `3.49.66-1.el8ap` | hub-rhel8 |
| `python3.12-pyasn1` | `0.6.4-1.el8ap` | eda-controller-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-pyasn1-modules` | `0.4.2-1.el8ap` | eda-controller-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-pycares` | `4.4.0-3.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-pycodestyle` | `2.11.1-2.el8ap` | hub-rhel8 |
| `python3.12-pycparser` | `2.20-2.el8` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-pydantic` | `1.10.15-2.el8ap` | eda-controller-rhel8 |
| `python3.12-pyflakes` | `3.1.0-2.el8ap` | hub-rhel8 |
| `python3.12-pygments` | `2.17.2-3.el8ap` | ee-supported-rhel8 |
| `python3.12-pygtrie` | `2.5.0-3.el8ap` | hub-rhel8 |
| `python3.12-pyjwt` | `2.13.0-1.el8ap` | eda-controller-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-pyjwt+crypto` | `2.13.0-1.el8ap` | eda-controller-rhel8, hub-rhel8 |
| `python3.12-pyOpenSSL` | `26.0.0-1.el8ap` | eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-pyparsing` | `3.1.1-2.el8ap` | de-supported-rhel8, hub-rhel8 |
| `python3.12-pyrad` | `2.4-3.el8ap` | gateway-rhel8 |
| `python3.12-pysequoia` | `0.1.34-1.el8ap` | hub-rhel8 |
| `python3.12-python3-openid` | `3.2.0-4.el8ap` | gateway-rhel8, hub-rhel8 |
| `python3.12-python3-saml` | `1.16.0-3.el8ap` | gateway-rhel8 |
| `python3.12-pytokens` | `0.4.1-1.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-pytz` | `2024.1-2.el8ap` | eda-controller-rhel8, ee-supported-rhel8 |
| `python3.12-pyyaml` | `6.0.1-2.el8` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, receptor-rhel8 |
| `python3.12-redis` | `4.6.0-3.el8ap` | eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-referencing` | `0.36.2-3.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-requests` | `2.31.0-4.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-requests-oauthlib` | `1.3.1-2.el8ap` | eda-controller-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-resolvelib` | `1.0.1-2.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-rpds-py` | `0.18.1-3.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-rq` | `2.6.1-1.el8ap` | eda-controller-rhel8 |
| `python3.12-rq-scheduler` | `0.14.0-1.el8ap` | eda-controller-rhel8 |
| `python3.12-rsa` | `4.9-3.el8ap` | eda-controller-rhel8, ee-supported-rhel8 |
| `python3.12-ruamel-yaml` | `0.18.15-2.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-ruamel-yaml-clib` | `0.2.15-2.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-s3transfer` | `0.10.0-2.el8ap` | ee-supported-rhel8, hub-rhel8 |
| `python3.12-semantic-version` | `2.10.0-3.el8ap` | hub-rhel8 |
| `python3.12-service-identity` | `21.1.0-3.el8ap` | eda-controller-rhel8 |
| `python3.12-setuptools` | `68.2.2-5.el8_10` | controller-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-six` | `1.17.0-1.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, receptor-rhel8 |
| `python3.12-smmap` | `5.0.1-2.el8ap` | hub-rhel8 |
| `python3.12-social-auth-app-django` | `5.4.1-2.el8ap` | gateway-rhel8, hub-rhel8 |
| `python3.12-social-auth-core` | `4.5.4-2.el8ap` | gateway-rhel8, hub-rhel8 |
| `python3.12-sqlparse` | `0.6.0-1.el8ap` | eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-subprocess-tee` | `0.4.2-2.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-tablib` | `3.5.0-2.el8ap` | hub-rhel8 |
| `python3.12-tablib+html` | `3.5.0-2.el8ap` | hub-rhel8 |
| `python3.12-tablib+ods` | `3.5.0-2.el8ap` | hub-rhel8 |
| `python3.12-tablib+xls` | `3.5.0-2.el8ap` | hub-rhel8 |
| `python3.12-tablib+xlsx` | `3.5.0-2.el8ap` | hub-rhel8 |
| `python3.12-tablib+yaml` | `3.5.0-2.el8ap` | hub-rhel8 |
| `python3.12-tabulate` | `0.9.0-4.el8ap` | ee-supported-rhel8, gateway-rhel8 |
| `python3.12-tacacs-plus` | `2.6-3.el8ap` | gateway-rhel8 |
| `python3.12-twisted` | `24.7.0-2.el8ap` | eda-controller-rhel8 |
| `python3.12-twisted+tls` | `24.7.0-2.el8ap` | eda-controller-rhel8 |
| `python3.12-txaio` | `23.1.1-3.el8ap` | eda-controller-rhel8 |
| `python3.12-typing-extensions` | `4.15.0-2.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-uamqp` | `1.6.8-2.el8ap` | ee-supported-rhel8 |
| `python3.12-uritemplate` | `4.1.1-4.el8ap` | eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-url-normalize` | `1.4.3-6.el8ap` | hub-rhel8 |
| `python3.12-urllib3` | `2.7.0-1.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8 |
| `python3.12-uuid6` | `2024.1.12-2.el8ap` | hub-rhel8 |
| `python3.12-validators` | `0.34.0-2.el8ap` | eda-controller-rhel8 |
| `python3.12-watchdog` | `5.0.2-2.el8ap` | de-supported-rhel8, ee-supported-rhel8 |
| `python3.12-wcmatch` | `8.5-2.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-websocket-client` | `1.7.0-3.el8ap` | eda-controller-rhel8, ee-supported-rhel8 |
| `python3.12-websockets` | `15.0-3.el8ap` | de-supported-rhel8 |
| `python3.12-whitenoise` | `6.6.0-2.el8ap` | hub-rhel8 |
| `python3.12-wrapt` | `1.16.0-2.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-xds-protos` | `1.71.2-1.el8ap` | gateway-rhel8 |
| `python3.12-xlrd` | `2.0.1-7.el8ap` | hub-rhel8 |
| `python3.12-xlwt` | `1.3.0-5.el8ap` | hub-rhel8 |
| `python3.12-xmlsec` | `1.3.13-3.el8ap` | gateway-rhel8 |
| `python3.12-xxhash` | `3.4.1-2.el8ap` | de-supported-rhel8, eda-controller-rhel8, ee-supported-rhel8 |
| `python3.12-yarl` | `1.18.3-1.el8ap` | de-supported-rhel8, ee-supported-rhel8, hub-rhel8 |
| `python3.12-zipp` | `3.19.2-2.el8ap` | ee-supported-rhel8, hub-rhel8 |
| `python3.12-zope-interface` | `6.1-2.el8ap` | eda-controller-rhel8 |
| `python36` | `3.6.8-39.module+el8.10.0+20784+edafcd43` | pcp |
| `qemu-img` | `6.2.0-53.module+el8.10.0+23760+c0926e61.6` | ee-supported-rhel8 |
| `readline` | `7.0-10.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `receptor` | `1.6.8-1.el8ap` | ee-supported-rhel8, receptor-rhel8 |
| `receptorctl` | `1.6.8-1.el8ap` | ee-supported-rhel8, receptor-rhel8 |
| `redhat-logos-httpd` | `810.1-1.el8_10` | controller-rhel8, eda-controller-ui-rhel8, gateway-rhel8, hub-web-rhel8 |
| `redhat-release` | `8.10-0.3.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `redis` | `6.2.24-1.module+el8.10.0+24746+7b800ac5` | controller-rhel8, redis-6 |
| `rootfiles` | `8.1-22.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `rpm` | `4.14.3-32.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `rpm-build-libs` | `4.14.3-32.el8_10` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `rpm-libs` | `4.14.3-32.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `rpm-plugin-selinux` | `4.14.3-32.el8_10` | controller-rhel8, eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `rsync` | `3.1.3-28.el8_10` | controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15, redis-6 |
| `rsyslog` | `8.2102.0-15.el8_10.3` | controller-rhel8, hub-rhel8 |
| `runc` | `1.2.9-6.module+el8.10.0+24790+ef71b018` | hub-rhel8 |
| `scl-utils` | `2.0.2-16.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15, redis-6 |
| `sed` | `4.5-5.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `selinux-policy` | `3.14.3-139.el8_10.2` | controller-rhel8, eda-controller-rhel8, gateway-rhel8, hub-rhel8 |
| `selinux-policy-minimum` | `3.14.3-139.el8_10.2` | controller-rhel8, eda-controller-rhel8, gateway-rhel8 |
| `selinux-policy-targeted` | `3.14.3-139.el8_10.2` | hub-rhel8 |
| `setup` | `2.12.2-9.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `shadow-utils` | `4.6-23.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `shadow-utils-subid` | `4.6-23.el8_10` | controller-rhel8, eda-controller-rhel8, ee-supported-rhel8, receptor-rhel8 |
| `skopeo` | `1.14.6-4.module+el8.10.0+24790+ef71b018` | hub-rhel8 |
| `sos` | `4.11.2-4.el8_10` | controller-rhel8, ee-supported-rhel8, hub-rhel8, receptor-rhel8 |
| `sqlite-libs` | `3.26.0-21.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `sshpass` | `1.09-5.el8ap` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `subscription-manager` | `1.28.44-1.el8_10` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `subscription-manager-rhsm-certificates` | `20220623-1.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `subversion` | `1.10.2-5.module+el8.6.0+15157+188c9801` | controller-rhel8, ee-supported-rhel8 |
| `subversion-libs` | `1.10.2-5.module+el8.6.0+15157+188c9801` | controller-rhel8, ee-supported-rhel8 |
| `supervisor` | `4.2.5-2.el8ap` | controller-rhel8, gateway-rhel8 |
| `systemd` | `239-82.el8_10.19` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `systemd-libs` | `239-82.el8_10.19` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `systemd-pam` | `239-82.el8_10.19` | controller-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `tar` | `1.30-13.el8_10` | de-supported-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `tcl` | `8.6.8-2.el8` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15, redis-6 |
| `tpm2-tss` | `2.3.2-6.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `tzdata` | `2026e-1.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `tzdata-java` | `2026e-1.el8_10` | de-supported-rhel8 |
| `unzip` | `6.0-48.el8_10` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, postgresql-15, redis-6 |
| `usermode` | `1.113-2.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `utf8proc` | `2.6.1-3.module+el8.7.0+15837+7cfc8c53` | controller-rhel8, ee-supported-rhel8 |
| `util-linux` | `2.32.1-48.el8_10` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `uuid` | `1.6.2-43.el8` | postgresql-15 |
| `uwsgi` | `2.0.28-2.el8ap` | gateway-rhel8 |
| `vim-filesystem` | `8.0.1763-32.el8_10` | eda-controller-ui-rhel8, hub-web-rhel8, postgresql-15 |
| `vim-minimal` | `8.0.1763-32.el8_10` | eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `virt-what` | `1.25-4.el8` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `which` | `2.21-21.el8_10` | controller-rhel8, eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `xmlsec1` | `1.2.25-8.el8_10` | controller-rhel8, gateway-rhel8 |
| `xmlsec1-openssl` | `1.2.25-8.el8_10` | controller-rhel8, gateway-rhel8 |
| `xz` | `5.2.4-4.el8_6` | eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `xz-libs` | `5.2.4-4.el8_6` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `yajl` | `2.1.0-12.el8` | controller-rhel8 |
| `yamllint` | `1.38.0-1.el8ap` | ee-minimal-rhel8, ee-supported-rhel8, hub-rhel8 |
| `yum` | `4.7.0-21.el8_10` | eda-controller-ui-rhel8, hub-web-rhel8, pcp, postgresql-15, redis-6 |
| `zlib` | `1.2.11-25.el8` | controller-rhel8, de-supported-rhel8, eda-controller-rhel8, eda-controller-ui-rhel8, ee-minimal-rhel8, ee-supported-rhel8, gateway-proxy-rhel8, gateway-rhel8, hub-rhel8, hub-web-rhel8, receptor-rhel8, pcp, postgresql-15, redis-6 |
| `zstd` | `1.4.4-1.el8` | ee-minimal-rhel8, ee-supported-rhel8 |

## Python Packages (all images)

Every Python distribution found in any image (`image:environment prefix (python)`), from
`*.dist-info`/`*.egg-info` metadata. Names are normalized (PEP 503: lowercase, `-` separators). This covers system Python, `/usr/local` and application venvs.

| Package | Version | Images |
|---|---|---|
| `aap-eda` | `1.1.23` | eda-controller-rhel8:/usr (python3.12) |
| `aap-gateway` | `2.5.20260923` | gateway-rhel8:/usr (python3.12) |
| `adal` | `1.2.7` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `aiobotocore` | `2.13.3` | de-supported-rhel8:/usr/local (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `aiodns` | `3.2.0` | de-supported-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `aiodns` | `3.6.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `aiofiles` | `23.2.1` | hub-rhel8:/usr (python3.12) |
| `aiofiles` | `24.1.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `aiohappyeyeballs` | `2.6.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), de-supported-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `aiohttp` | `3.14.3` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), de-supported-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `aiohttp-retry` | `2.8.3` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `aioitertools` | `0.11.0` | de-supported-rhel8:/usr/local (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `aiokafka` | `0.10.0` | de-supported-rhel8:/usr/local (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `aiosignal` | `1.4.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), de-supported-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `annotated-types` | `0.6.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `ansible-builder` | `3.1.1` | hub-rhel8:/usr (python3.12) |
| `ansible-compat` | `25.12.0` | ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `ansible-core` | `2.16.19` | de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `ansible-lint` | `26.1.1` | ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `ansible-pylibssh` | `1.2.2` | ee-supported-rhel8:/usr (python3.12) |
| `ansible-rulebook` | `1.1.7` | de-supported-rhel8:/usr (python3.12) |
| `ansible-runner` | `2.4.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), receptor-rhel8:/usr (python3.12) |
| `ansible-sign` | `0.1.4` | ee-supported-rhel8:/usr (python3.12) |
| `ansiconv` | `1.0.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `anyio` | `4.4.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `appdirs` | `1.4.4` | ee-supported-rhel8:/usr/local (python3.12) |
| `applicationinsights` | `0.11.10` | ee-supported-rhel8:/usr/local (python3.12) |
| `argcomplete` | `3.5.3` | ee-supported-rhel8:/usr/local (python3.12) |
| `argon2-cffi` | `23.1.0` | gateway-rhel8:/usr (python3.12) |
| `argon2-cffi-bindings` | `21.2.0` | gateway-rhel8:/usr (python3.12) |
| `asciichartpy` | `1.5.25` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `asgiref` | `3.11.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `asgiref` | `3.11.1` | eda-controller-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `asn1` | `2.7.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `async-timeout` | `5.0.1` | de-supported-rhel8:/usr/local (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `asyncio-throttle` | `1.0.2` | hub-rhel8:/usr (python3.12) |
| `attrs` | `22.2.0` | de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `attrs` | `23.2.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `autobahn` | `23.6.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `autobahn` | `24.4.2` | eda-controller-rhel8:/usr (python3.12) |
| `autocommand` | `2.2.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `automat` | `22.10.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel8:/usr (python3.12) |
| `awx` | `4.6.34` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `awxkit` | `4.6.34` | ee-supported-rhel8:/usr (python3.12) |
| `azure-cli-core` | `2.74.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-cli-telemetry` | `1.1.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-common` | `1.1.28` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `azure-containerregistry` | `1.2.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-core` | `1.30.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `azure-core` | `1.31.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-core` | `1.34.0` | de-supported-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `azure-identity` | `1.15.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `azure-identity` | `1.19.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-iot-hub` | `2.6.1` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-keyvault` | `4.2.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `azure-keyvault-certificates` | `4.7.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `azure-keyvault-keys` | `4.8.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `azure-keyvault-secrets` | `4.7.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `azure-keyvault-securitydomain` | `1.0.0b1` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-apimanagement` | `4.0.1` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-authorization` | `4.0.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-automation` | `1.1.0b4` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-batch` | `17.3.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-cdn` | `13.1.1` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-compute` | `33.0.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-containerinstance` | `10.1.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-containerregistry` | `10.3.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-containerservice` | `32.1.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-core` | `1.4.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-cosmosdb` | `10.0.0b3` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-datafactory` | `9.0.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-devtestlabs` | `10.0.0b2` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-dns` | `8.1.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-eventhub` | `11.1.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-hdinsight` | `9.1.0b1` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-iothub` | `3.0.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-keyvault` | `10.3.1` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-loganalytics` | `13.0.0b7` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-managedservices` | `7.0.0b2` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-managementgroups` | `1.1.0b2` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-marketplaceordering` | `1.2.0b2` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-monitor` | `6.0.2` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-mysqlflexibleservers` | `1.0.0b3` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-network` | `28.0.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-notificationhubs` | `8.1.0b1` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-nspkg` | `3.0.2` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-postgresqlflexibleservers` | `1.1.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-privatedns` | `1.2.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-rdbms` | `10.2.0b17` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-recoveryservices` | `3.0.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-recoveryservicesbackup` | `9.1.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-redis` | `14.4.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-resource` | `23.2.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-resourcegraph` | `8.0.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-resourcehealth` | `1.0.0b6` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-search` | `9.2.0b2` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-servicebus` | `8.2.1` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-sql` | `4.0.0b19` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-storage` | `21.2.1` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-trafficmanager` | `1.1.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-mgmt-web` | `7.3.1` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-nspkg` | `3.0.2` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-servicebus` | `7.12.1` | de-supported-rhel8:/usr/local (python3.12) |
| `azure-servicebus` | `7.14.2` | ee-supported-rhel8:/usr/local (python3.12) |
| `azure-storage-blob` | `12.19.0` | hub-rhel8:/usr (python3.12) |
| `azure-storage-blob` | `12.23.0b1` | ee-supported-rhel8:/usr/local (python3.12) |
| `backoff` | `2.2.1` | hub-rhel8:/usr (python3.12) |
| `backports-zstd` | `1.3.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `bcrypt` | `3.2.0` | ee-minimal-rhel8:/usr/local (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `bindep` | `2.13.0` | hub-rhel8:/usr (python3.12) |
| `black` | `26.3.1` | ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `boto3` | `1.34.30` | ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `boto3` | `1.42.26` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `botocore` | `1.34.162` | de-supported-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `botocore` | `1.42.26` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `bracex` | `2.4` | ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `brotli` | `1.2.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), de-supported-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `cachetools` | `5.3.2` | eda-controller-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12) |
| `cachetools` | `5.5.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `certifi` | `2023.5.7` | de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `certifi` | `2038.12.31` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `cffi` | `1.11.5` | controller-rhel8:/usr (python3.6), eda-controller-rhel8:/usr (python3.6), gateway-rhel8:/usr (python3.6), hub-rhel8:/usr (python3.6) |
| `cffi` | `2.0.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `channels` | `4.3.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel8:/usr (python3.12) |
| `channels-redis` | `4.2.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `chardet` | `3.0.4` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), ee-supported-rhel8:/usr (python3.6), hub-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), receptor-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `chardet` | `5.2.0` | ee-supported-rhel8:/usr (python3.12) |
| `charset-normalizer` | `3.3.0` | de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `charset-normalizer` | `3.3.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `click` | `8.3.3` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12), receptor-rhel8:/usr (python3.12) |
| `constantly` | `23.10.4` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel8:/usr (python3.12) |
| `croniter` | `2.0.1` | eda-controller-rhel8:/usr (python3.12) |
| `crontab` | `1.0.5` | eda-controller-rhel8:/usr (python3.12) |
| `cryptography` | `3.2.1` | controller-rhel8:/usr (python3.6), eda-controller-rhel8:/usr (python3.6), gateway-rhel8:/usr (python3.6), hub-rhel8:/usr (python3.6) |
| `cryptography` | `46.0.7` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `cython` | `3.1.3` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `daphne` | `4.2.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `daphne` | `4.2.2` | eda-controller-rhel8:/usr (python3.12) |
| `dbus-python` | `1.2.4` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `decorator` | `4.2.1` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `decorator` | `5.1.1` | ee-minimal-rhel8:/usr/local (python3.12) |
| `decorator` | `5.2.1` | de-supported-rhel8:/usr/local (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `defusedxml` | `0.7.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `deprecated` | `1.2.14` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `diff-match-patch` | `20230430` | hub-rhel8:/usr (python3.12) |
| `dispatcherd` | `2025.5.19` | eda-controller-rhel8:/usr (python3.12) |
| `distlib` | `0.4.0` | ee-supported-rhel8:/usr (python3.12) |
| `distro` | `1.9.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `django` | `5.2.17` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `django-ansible-base` | `2.5.20260422` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `django-auth-ldap` | `4.0.0` | gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `django-auth-ldap` | `5.1.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `django-cors-headers` | `4.3.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `django-crum` | `0.7.9` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `django-dynamic-preferences` | `1.16.0` | gateway-rhel8:/usr (python3.12) |
| `django-extensions` | `3.2.3` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `django-extensions` | `4.1` | gateway-rhel8:/usr (python3.12) |
| `django-filter` | `25.2` | eda-controller-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `django-flags` | `5.0.13` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `django-guid` | `3.4.0` | hub-rhel8:/usr (python3.12) |
| `django-guid` | `3.5.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `django-import-export` | `3.3.6` | hub-rhel8:/usr (python3.12) |
| `django-ipware` | `3.0.7` | hub-rhel8:/usr (python3.12) |
| `django-lifecycle` | `1.1.2` | hub-rhel8:/usr (python3.12) |
| `django-oauth-toolkit` | `1.7.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `django-oauth-toolkit` | `2.3.0` | gateway-rhel8:/usr (python3.12) |
| `django-pglocks` | `1.0.4` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `django-picklefield` | `3.1` | hub-rhel8:/usr (python3.12) |
| `django-polymorphic` | `4.10.5` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `django-prometheus` | `2.3.1` | hub-rhel8:/usr (python3.12) |
| `django-radius` | `1.5.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `django-redis` | `5.4.0` | eda-controller-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12) |
| `django-rq` | `3.2.2` | eda-controller-rhel8:/usr (python3.12) |
| `django-solo` | `2.2.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `django-split-settings` | `1.2.0` | eda-controller-rhel8:/usr (python3.12) |
| `django-storages` | `1.14.2` | hub-rhel8:/usr (python3.12) |
| `djangorestframework` | `3.15.1` | eda-controller-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `djangorestframework` | `3.15.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `djangorestframework-queryfields` | `1.1.0` | hub-rhel8:/usr (python3.12) |
| `djangorestframework-yaml` | `2.0.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `dnspython` | `2.6.1` | ee-supported-rhel8:/usr/local (python3.12) |
| `docutils` | `0.20.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `dogpile-cache` | `1.1.2` | ee-supported-rhel8:/usr/local (python3.12) |
| `dpapi-ng` | `0.2.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `dpath` | `2.1.6` | de-supported-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12) |
| `drf-access-policy` | `1.5.0` | hub-rhel8:/usr (python3.12) |
| `drf-nested-routers` | `0.93.5` | hub-rhel8:/usr (python3.12) |
| `drf-spectacular` | `0.29.0` | eda-controller-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `drools-jpy` | `0.3.10` | de-supported-rhel8:/usr (python3.12) |
| `durationpy` | `0.10` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `dynaconf` | `3.2.11` | eda-controller-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `dynaconf` | `3.2.13` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `ecdsa` | `0.18.0` | eda-controller-rhel8:/usr (python3.12) |
| `enum-compat` | `0.0.3` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `et-xmlfile` | `1.1.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), hub-rhel8:/usr (python3.12) |
| `ethtool` | `0.14` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `filelock` | `3.13.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `flake8` | `6.1.0` | hub-rhel8:/usr (python3.12) |
| `freezegun` | `1.5.5` | eda-controller-rhel8:/usr (python3.12) |
| `frozenlist` | `1.4.0` | de-supported-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `frozenlist` | `1.8.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `galaxy-importer` | `0.4.38` | hub-rhel8:/usr (python3.12) |
| `galaxy-ng` | `4.10.19` | hub-rhel8:/usr (python3.12) |
| `gitdb` | `4.0.11` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), hub-rhel8:/usr (python3.12) |
| `gitpython` | `3.1.60` | hub-rhel8:/usr (python3.12) |
| `gitpython` | `3.1.62` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `google-auth` | `2.27.0` | eda-controller-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12) |
| `google-auth` | `2.28.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `googleapis-common-protos` | `1.63.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `googleapis-common-protos` | `1.72.0` | gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `gpg` | `1.13.1` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `grpcio` | `1.68.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `grpcio` | `1.71.2` | ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `grpcio-tools` | `1.71.2` | gateway-rhel8:/usr (python3.12) |
| `gssapi` | `1.8.2` | ee-minimal-rhel8:/usr/local (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `gssapi` | `1.9.0` | de-supported-rhel8:/usr/local (python3.12) |
| `gunicorn` | `23.0.0` | eda-controller-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `h11` | `0.16.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `h2` | `4.1.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `hiredis` | `3.2.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `hpack` | `4.0.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `httpcore` | `1.0.9` | ee-supported-rhel8:/usr/local (python3.12) |
| `httpx` | `0.27.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `humanfriendly` | `10.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `hyperframe` | `6.0.1` | ee-supported-rhel8:/usr/local (python3.12) |
| `hyperlink` | `21.0.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel8:/usr (python3.12) |
| `idna` | `2.5` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), ee-supported-rhel8:/usr (python3.6), hub-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), receptor-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `idna` | `3.4` | de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `idna` | `3.6` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `importlib-metadata` | `6.0.1` | ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `importlib-metadata` | `6.2.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `incremental` | `24.7.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel8:/usr (python3.12) |
| `inflect` | `7.0.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `inflection` | `0.5.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `iniparse` | `0.4` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `insights-analytics-collector` | `0.3.2` | eda-controller-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `irc` | `20.3.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `isc` | `2.0` | eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), postgresql-15:/usr (python3.6) |
| `iso8601` | `0.1.14` | ee-supported-rhel8:/usr/local (python3.12) |
| `isodate` | `0.6.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), de-supported-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `janus` | `1.0.0` | de-supported-rhel8:/usr (python3.12) |
| `jaraco-collections` | `5.0.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `jaraco-context` | `4.3.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `jaraco-functools` | `4.3.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `jaraco-logging` | `3.3.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `jaraco-stream` | `3.0.3` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `jaraco-text` | `3.12.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `jinja2` | `3.1.6` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `jmespath` | `1.0.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), de-supported-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `jpy` | `0.15.0` | de-supported-rhel8:/usr (python3.12) |
| `jq` | `1.6.0` | hub-rhel8:/usr (python3.12) |
| `jq` | `1.8.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `json-log-formatter` | `0.5.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `json-stream` | `2.3.2` | hub-rhel8:/usr (python3.12) |
| `json-stream-rs-tokenizer` | `0.4.26` | hub-rhel8:/usr (python3.12) |
| `jsonpatch` | `1.32` | ee-supported-rhel8:/usr/local (python3.12) |
| `jsonpointer` | `2.1` | ee-supported-rhel8:/usr/local (python3.12) |
| `jsonschema` | `4.21.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `jsonschema-specifications` | `2023.12.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `jwcrypto` | `1.5.7` | gateway-rhel8:/usr (python3.12) |
| `jwcrypto` | `1.5.8` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `jxmlease` | `1.0.3` | ee-supported-rhel8:/usr/local (python3.12) |
| `kafka-python-ng` | `2.2.3` | de-supported-rhel8:/usr/local (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `keystoneauth1` | `4.3.1` | ee-supported-rhel8:/usr/local (python3.12) |
| `knack` | `0.11.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `krb5` | `0.5.0` | ee-minimal-rhel8:/usr/local (python3.12) |
| `krb5` | `0.9.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `kubernetes` | `26.1.0` | eda-controller-rhel8:/usr (python3.12) |
| `kubernetes` | `29.0.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `kubernetes` | `36.0.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `ldap-filter` | `1.0.1` | gateway-rhel8:/usr (python3.12) |
| `libcomps` | `0.1.18` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `lockfile` | `0.12.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), receptor-rhel8:/usr (python3.12) |
| `lxml` | `4.9.4` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `lxml` | `5.3.0` | gateway-rhel8:/usr (python3.12) |
| `lxml` | `6.1.3` | ee-minimal-rhel8:/usr/local (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `markdown` | `3.10.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), hub-rhel8:/usr (python3.12) |
| `markuppy` | `1.14` | hub-rhel8:/usr (python3.12) |
| `markupsafe` | `2.1.5` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `marshmallow` | `3.26.2` | hub-rhel8:/usr (python3.12) |
| `maturin` | `1.11.5` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `mccabe` | `0.7.0` | hub-rhel8:/usr (python3.12) |
| `metrics-utility` | `0.6.3` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `microsoft-kiota-abstractions` | `1.3.3` | ee-supported-rhel8:/usr/local (python3.12) |
| `microsoft-kiota-authentication-azure` | `1.0.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `microsoft-kiota-http` | `1.3.1` | ee-supported-rhel8:/usr/local (python3.12) |
| `microsoft-kiota-serialization-form` | `0.1.1` | ee-supported-rhel8:/usr/local (python3.12) |
| `microsoft-kiota-serialization-json` | `1.3.3` | ee-supported-rhel8:/usr/local (python3.12) |
| `microsoft-kiota-serialization-multipart` | `0.1.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `microsoft-kiota-serialization-text` | `1.0.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `microsoft-security-utilities-secret-masker` | `1.0.0b4` | ee-supported-rhel8:/usr/local (python3.12) |
| `more-itertools` | `10.2.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `msal` | `1.32.3` | ee-supported-rhel8:/usr/local (python3.12) |
| `msal` | `1.35.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `msal-extensions` | `1.1.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `msal-extensions` | `1.2.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `msgpack` | `1.1.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `msgraph-core` | `1.1.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `msgraph-sdk` | `1.6.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `msrest` | `0.7.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `msrestazure` | `0.6.4` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `multidict` | `6.0.4` | de-supported-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `multidict` | `6.0.5` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `munch` | `2.5.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `mypy-extensions` | `1.0.0` | ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `ncclient` | `0.6.19` | ee-minimal-rhel8:/usr/local (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `netaddr` | `1.2.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12) |
| `netifaces` | `0.10.9` | ee-supported-rhel8:/usr/local (python3.12) |
| `nh3` | `0.2.18` | hub-rhel8:/usr (python3.12) |
| `nsx-policy-python-sdk` | `4.1.2.0.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `nsx-python-sdk` | `4.1.2.0.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `nsx-vmc-aws-integration-python-sdk` | `4.1.2.0.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `nsx-vmc-policy-python-sdk` | `4.1.2.0.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `ntlm-auth` | `1.5.0` | ee-minimal-rhel8:/usr/local (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `numpy` | `1.26.4` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `numpy` | `2.2.6` | ee-supported-rhel8:/usr/local (python3.12) |
| `oauthlib` | `3.2.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `odfpy` | `1.4.1` | hub-rhel8:/usr (python3.12) |
| `opa-python-client` | `2.0.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `openpyxl` | `3.1.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), hub-rhel8:/usr (python3.12) |
| `openshift` | `0.13.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `openstacksdk` | `0.56.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `opentelemetry-api` | `1.24.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `opentelemetry-api` | `1.25.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `opentelemetry-api` | `1.28.0` | hub-rhel8:/usr (python3.12) |
| `opentelemetry-distro` | `0.49b0` | hub-rhel8:/usr (python3.12) |
| `opentelemetry-exporter-otlp` | `1.24.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `opentelemetry-exporter-otlp` | `1.28.0` | hub-rhel8:/usr (python3.12) |
| `opentelemetry-exporter-otlp-proto-common` | `1.24.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `opentelemetry-exporter-otlp-proto-common` | `1.28.0` | hub-rhel8:/usr (python3.12) |
| `opentelemetry-exporter-otlp-proto-grpc` | `1.24.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `opentelemetry-exporter-otlp-proto-grpc` | `1.28.0` | hub-rhel8:/usr (python3.12) |
| `opentelemetry-exporter-otlp-proto-http` | `1.24.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `opentelemetry-exporter-otlp-proto-http` | `1.28.0` | hub-rhel8:/usr (python3.12) |
| `opentelemetry-instrumentation` | `0.45b0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `opentelemetry-instrumentation` | `0.49b0` | hub-rhel8:/usr (python3.12) |
| `opentelemetry-instrumentation-django` | `0.49b0` | hub-rhel8:/usr (python3.12) |
| `opentelemetry-instrumentation-logging` | `0.45b0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `opentelemetry-instrumentation-wsgi` | `0.49b0` | hub-rhel8:/usr (python3.12) |
| `opentelemetry-proto` | `1.24.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `opentelemetry-proto` | `1.28.0` | gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `opentelemetry-sdk` | `1.24.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `opentelemetry-sdk` | `1.25.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `opentelemetry-sdk` | `1.28.0` | hub-rhel8:/usr (python3.12) |
| `opentelemetry-semantic-conventions` | `0.45b0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `opentelemetry-semantic-conventions` | `0.46b0` | ee-supported-rhel8:/usr/local (python3.12) |
| `opentelemetry-semantic-conventions` | `0.49b0` | hub-rhel8:/usr (python3.12) |
| `opentelemetry-util-http` | `0.49b0` | hub-rhel8:/usr (python3.12) |
| `oras` | `0.2.37` | ee-supported-rhel8:/usr/local (python3.12) |
| `os-service-types` | `1.7.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `ovirt-engine-sdk-python` | `4.5.2` | ee-supported-rhel8:/usr/local (python3.12) |
| `ovirt-imageio` | `2.4.6` | ee-supported-rhel8:/usr/local (python3.12) |
| `packaging` | `23.2` | de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12), receptor-rhel8:/usr (python3.12) |
| `packaging` | `26.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `pandas` | `2.2.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `pandas` | `2.3.2` | ee-supported-rhel8:/usr/local (python3.12) |
| `paramiko` | `2.8.1` | ee-minimal-rhel8:/usr/local (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `parsley` | `1.3` | hub-rhel8:/usr (python3.12) |
| `pathspec` | `1.0.4` | ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `pbr` | `6.0.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), hub-rhel8:/usr (python3.12) |
| `pbr` | `7.0.1` | ee-supported-rhel8:/usr/local (python3.12) |
| `pcp` | `5.0` | pcp:/usr (python3.6) |
| `pendulum` | `3.0.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `persisting-theory` | `1.0` | gateway-rhel8:/usr (python3.12) |
| `pexpect` | `4.7.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `pexpect` | `4.9.0` | de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), receptor-rhel8:/usr (python3.12) |
| `pillow` | `12.3.0` | hub-rhel8:/usr (python3.12) |
| `pip` | `23.2.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), de-supported-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12) |
| `pip` | `25.3` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `pip` | `9.0.3` | pcp:/usr (python3.6) |
| `pkgconfig` | `1.5.5` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `pkginfo` | `1.7.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `platformdirs` | `4.2.0` | ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `ply` | `3.11` | de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `ply` | `3.9` | controller-rhel8:/usr (python3.6), eda-controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), gateway-rhel8:/usr (python3.6), hub-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), postgresql-15:/usr (python3.6) |
| `podman` | `5.4.0.1` | eda-controller-rhel8:/usr (python3.12) |
| `portalocker` | `1.7.1` | ee-supported-rhel8:/usr/local (python3.12) |
| `portalocker` | `2.8.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `prometheus-client` | `0.19.0` | hub-rhel8:/usr (python3.12) |
| `prometheus-client` | `0.20.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `propcache` | `0.2.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `propcache` | `0.4.1` | de-supported-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `protobuf` | `4.25.3` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `protobuf` | `5.29.6` | ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `psutil` | `5.9.1` | ee-supported-rhel8:/usr/local (python3.12) |
| `psutil` | `5.9.8` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `psycopg` | `3.1.18` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `psycopg` | `3.2.7` | de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `psycopg-c` | `3.2.7` | de-supported-rhel8:/usr (python3.12) |
| `ptyprocess` | `0.7.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), receptor-rhel8:/usr (python3.12) |
| `pulp-ansible` | `0.25.6` | hub-rhel8:/usr (python3.12) |
| `pulp-container` | `2.19.12` | hub-rhel8:/usr (python3.12) |
| `pulp-glue` | `0.23.2` | hub-rhel8:/usr (python3.12) |
| `pulpcore` | `3.49.66` | hub-rhel8:/usr (python3.12) |
| `py-deviceid` | `0.1.1` | ee-supported-rhel8:/usr/local (python3.12) |
| `pyang` | `2.5.3` | ee-supported-rhel8:/usr/local (python3.12) |
| `pyasn1` | `0.6.4` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `pyasn1-modules` | `0.4.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `pycares` | `4.11.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `pycares` | `4.4.0` | de-supported-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `pycodestyle` | `2.11.1` | hub-rhel8:/usr (python3.12) |
| `pycparser` | `2.14` | controller-rhel8:/usr (python3.6), eda-controller-rhel8:/usr (python3.6), gateway-rhel8:/usr (python3.6), hub-rhel8:/usr (python3.6) |
| `pycparser` | `2.20` | de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `pycparser` | `2.21` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `pycurl` | `7.45.3` | ee-supported-rhel8:/usr/local (python3.12) |
| `pydantic` | `1.10.15` | eda-controller-rhel8:/usr (python3.12) |
| `pydantic` | `2.9.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `pydantic-core` | `2.23.4` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `pyflakes` | `3.1.0` | hub-rhel8:/usr (python3.12) |
| `pygerduty` | `0.38.3` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `pygithub` | `2.6.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `pygments` | `2.17.2` | ee-supported-rhel8:/usr (python3.12) |
| `pygobject` | `3.28.3` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `pygtrie` | `2.5.0` | hub-rhel8:/usr (python3.12) |
| `pyinotify` | `0.9.6` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `pyjwt` | `2.13.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `pykerberos` | `1.2.4` | ee-minimal-rhel8:/usr/local (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `pynacl` | `1.4.0` | ee-minimal-rhel8:/usr/local (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `pynacl` | `1.5.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `pyopenssl` | `26.0.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `pyparsing` | `2.4.6` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `pyparsing` | `3.1.1` | de-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `pypsrp` | `0.5.0` | ee-minimal-rhel8:/usr/local (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `pyrad` | `2.4` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), gateway-rhel8:/usr (python3.12) |
| `pysequoia` | `0.1.34` | hub-rhel8:/usr (python3.12) |
| `pysocks` | `1.6.8` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), ee-supported-rhel8:/usr (python3.6), hub-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), receptor-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `pysocks` | `1.7.1` | ee-supported-rhel8:/usr/local (python3.12) |
| `pyspnego` | `0.9.0` | ee-minimal-rhel8:/usr/local (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `python-daemon` | `3.0.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `python-daemon` | `3.1.2` | de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), receptor-rhel8:/usr (python3.12) |
| `python-dateutil` | `2.6.1` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `python-dateutil` | `2.8.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12), receptor-rhel8:/usr (python3.12) |
| `python-dsv-sdk` | `1.0.4` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `python-gnupg` | `0.5.2` | eda-controller-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `python-ldap` | `3.4.4` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `python-ldap` | `3.4.5` | gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `python-string-utils` | `1.0.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `python-tss-sdk` | `1.2.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `python3-openid` | `3.2.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `python3-saml` | `1.14.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `python3-saml` | `1.16.0` | gateway-rhel8:/usr (python3.12) |
| `pytokens` | `0.4.1` | ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `pytz` | `2024.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12) |
| `pyvmomi` | `8.0.3.0.1` | ee-supported-rhel8:/usr/local (python3.12) |
| `pywinrm` | `0.4.3` | ee-minimal-rhel8:/usr/local (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `pyyaml` | `6.0.1` | de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12), receptor-rhel8:/usr (python3.12) |
| `pyyaml` | `6.0.3` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `pyzstd` | `0.15.10` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `receptorctl` | `1.6.8` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), ee-supported-rhel8:/usr (python3.12), receptor-rhel8:/usr (python3.12) |
| `redis` | `4.6.0` | eda-controller-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `redis` | `7.0.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `referencing` | `0.33.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `referencing` | `0.36.2` | de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `requests` | `2.20.0` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), ee-supported-rhel8:/usr (python3.6), hub-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), receptor-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `requests` | `2.31.0` | de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `requests` | `2.32.3` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `requests-credssp` | `2.0.0` | ee-minimal-rhel8:/usr/local (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `requests-ntlm` | `1.1.0` | ee-minimal-rhel8:/usr/local (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `requests-oauthlib` | `1.3.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `requestsexceptions` | `1.4.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `resolvelib` | `1.0.1` | de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `rpds-py` | `0.18.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `rpds-py` | `0.18.1` | de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `rpm` | `4.14.3` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `rq` | `2.6.1` | eda-controller-rhel8:/usr (python3.12) |
| `rq-scheduler` | `0.14.0` | eda-controller-rhel8:/usr (python3.12) |
| `rsa` | `4.9` | eda-controller-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12) |
| `ruamel-yaml` | `0.18.15` | ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `ruamel-yaml-clib` | `0.2.15` | ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `s3transfer` | `0.10.0` | ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `s3transfer` | `0.16.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `sansldap` | `0.1.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `scp` | `0.13.3` | ee-supported-rhel8:/usr/local (python3.12) |
| `selinux` | `2.9` | controller-rhel8:/usr (python3.6), eda-controller-rhel8:/usr (python3.6), gateway-rhel8:/usr (python3.6) |
| `semantic-version` | `2.10.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), hub-rhel8:/usr (python3.12) |
| `sepolicy` | `1.1` | controller-rhel8:/usr (python3.6), eda-controller-rhel8:/usr (python3.6), gateway-rhel8:/usr (python3.6) |
| `service-identity` | `21.1.0` | eda-controller-rhel8:/usr (python3.12) |
| `service-identity` | `24.1.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `setools` | `4.3.0` | controller-rhel8:/usr (python3.6), eda-controller-rhel8:/usr (python3.6), gateway-rhel8:/usr (python3.6) |
| `setuptools` | `39.2.0` | controller-rhel8:/usr (python3.6), de-supported-rhel8:/usr (python3.6), eda-controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), ee-supported-rhel8:/usr (python3.6), gateway-rhel8:/usr (python3.6), hub-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), receptor-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `setuptools` | `68.2.2` | controller-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `setuptools` | `80.9.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `setuptools-rust` | `1.12.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `setuptools-scm` | `9.2.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `six` | `1.11.0` | controller-rhel8:/usr (python3.6), eda-controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), ee-supported-rhel8:/usr (python3.6), gateway-rhel8:/usr (python3.6), hub-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), receptor-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `six` | `1.16.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `six` | `1.17.0` | de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12), receptor-rhel8:/usr (python3.12) |
| `slack-sdk` | `3.27.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `smmap` | `5.0.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), hub-rhel8:/usr (python3.12) |
| `sniffio` | `1.3.1` | ee-supported-rhel8:/usr/local (python3.12) |
| `social-auth-app-django` | `5.4.1` | gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `social-auth-app-django` | `5.4.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `social-auth-core` | `4.5.4` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `sos` | `4.11.2` | controller-rhel8:/usr (python3.6), ee-supported-rhel8:/usr (python3.6), hub-rhel8:/usr (python3.6), receptor-rhel8:/usr (python3.6) |
| `sqlparse` | `0.6.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `std-uritemplate` | `1.0.2` | ee-supported-rhel8:/usr/local (python3.12) |
| `stevedore` | `3.3.3` | ee-supported-rhel8:/usr/local (python3.12) |
| `subprocess-tee` | `0.4.2` | ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `subscription-manager` | `1.28.44` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `suds` | `1.1.2` | ee-supported-rhel8:/usr/local (python3.12) |
| `supervisor` | `4.2.5` | controller-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12) |
| `syspurpose` | `1.28.44` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `systemd-python` | `234` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `tablib` | `3.5.0` | hub-rhel8:/usr (python3.12) |
| `tabulate` | `0.9.0` | ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12) |
| `tacacs-plus` | `1.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `tacacs-plus` | `2.6` | gateway-rhel8:/usr (python3.12) |
| `tempora` | `5.5.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `textfsm` | `0.4.1` | ee-supported-rhel8:/usr/local (python3.12) |
| `time-machine` | `2.14.2` | ee-supported-rhel8:/usr/local (python3.12) |
| `toml` | `0.10.2` | ee-minimal-rhel8:/usr/local (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `ttp` | `0.6.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `twilio` | `8.13.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `twisted` | `24.7.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel8:/usr (python3.12) |
| `txaio` | `23.1.1` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel8:/usr (python3.12) |
| `typing-extensions` | `4.15.0` | de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `typing-extensions` | `4.9.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `tzdata` | `2024.1` | ee-supported-rhel8:/usr/local (python3.12) |
| `uamqp` | `1.6.8` | ee-supported-rhel8:/usr (python3.12) |
| `uritemplate` | `4.1.1` | eda-controller-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `url-normalize` | `1.4.3` | hub-rhel8:/usr (python3.12) |
| `urllib3` | `1.24.2` | controller-rhel8:/usr (python3.6), eda-controller-ui-rhel8:/usr (python3.6), ee-supported-rhel8:/usr (python3.6), hub-rhel8:/usr (python3.6), hub-web-rhel8:/usr (python3.6), receptor-rhel8:/usr (python3.6), pcp:/usr (python3.6), postgresql-15:/usr (python3.6), redis-6:/usr (python3.6) |
| `urllib3` | `2.7.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), gateway-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `uuid6` | `2024.1.12` | hub-rhel8:/usr (python3.12) |
| `uwsgi` | `2.0.28` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `uwsgitop` | `0.11` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `validators` | `0.34.0` | eda-controller-rhel8:/usr (python3.12) |
| `vapi-common-client` | `2.44.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `vapi-runtime` | `2.44.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `vcenter-bindings` | `4.2.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `vmwarecloud-aws` | `1.64.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `vmwarecloud-draas` | `1.23.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `vsphere-automation-sdk` | `1.86.0` | ee-supported-rhel8:/usr/local (python3.12) |
| `watchdog` | `5.0.2` | de-supported-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12) |
| `wcmatch` | `8.5` | ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `websocket-client` | `1.7.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12) |
| `websockets` | `15.0` | de-supported-rhel8:/usr (python3.12) |
| `wheel` | `0.46.3` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `whitenoise` | `6.6.0` | hub-rhel8:/usr (python3.12) |
| `wrapt` | `1.16.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), de-supported-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `xds-protos` | `1.71.2` | gateway-rhel8:/usr (python3.12) |
| `xlrd` | `2.0.1` | hub-rhel8:/usr (python3.12) |
| `xlwt` | `1.3.0` | hub-rhel8:/usr (python3.12) |
| `xmlsec` | `1.3.13` | controller-rhel8:/var/lib/awx/venv/awx (python3.12), gateway-rhel8:/usr (python3.12) |
| `xmltodict` | `0.12.0` | ee-minimal-rhel8:/usr/local (python3.12), ee-supported-rhel8:/usr/local (python3.12) |
| `xxhash` | `3.4.1` | de-supported-rhel8:/usr (python3.12), eda-controller-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12) |
| `yamllint` | `1.38.0` | ee-minimal-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `yarl` | `1.17.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `yarl` | `1.18.3` | de-supported-rhel8:/usr (python3.12), ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `zipp` | `3.17.0` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |
| `zipp` | `3.19.2` | ee-supported-rhel8:/usr (python3.12), hub-rhel8:/usr (python3.12) |
| `zope-interface` | `6.1` | eda-controller-rhel8:/usr (python3.12) |
| `zope-interface` | `6.2` | controller-rhel8:/var/lib/awx/venv/awx (python3.12) |

## Image Details

### controller-rhel8

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/controller-rhel8.tar.gz` |
| Labels `version` / `release` | `4.6.34` / `1791896186` |
| Image ID | `sha256:63355bc0beb8a9bba8659f747d0c183fa339fc2bbfb4181412d54ad1728d268e` |
| Build date | 2026-10-14T01:12:22Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | 3.12 |
| Ansible Core | N/A |

<details><summary>RPM packages (257)</summary>

```text
aap-metrics-utility 0.6.3-2.el8ap
acl 2.4.0-1.el8_10
ansible-automation-platform-common 2.5-2.el8ap
ansible-automation-platform-selinux 0.2-3.el8ap
apr 1.6.3-12.el8
apr-util 1.6.1-9.el8_10.1
audit-libs 3.1.2-1.el8_10.1
automation-controller 4.6.34-1.el8ap
automation-controller-server 4.6.34-1.el8ap
automation-controller-ui 4.6.34-1.el8ap
automation-controller-venv-tower 4.6.34-1.el8ap
basesystem 11-5.el8
bash 4.4.20-6.el8_10
brotli 1.0.6-4.el8_10
bzip2-libs 1.0.6-28.el8_10
ca-certificates 2025.2.80_v9.0.304-80.2.el8_10
checkpolicy 2.9-1.el8
chkconfig 1.19.2-1.el8
coreutils-single 8.30-21.el8_10
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crontabs 1.11-17.20190603git.el8
crun 1.14.3-4.module+el8.10.0+24790+ef71b018
crypto-policies 20230731-1.git3177e06.el8
cryptsetup-libs 2.3.7-7.el8
curl 7.61.1-34.el8_10.13
cyrus-sasl-lib 2.1.27-6.el8_5
dbus 1.12.8-28.el8_10
dbus-common 1.12.8-28.el8_10
dbus-daemon 1.12.8-28.el8_10
dbus-glib 0.110-2.el8
dbus-libs 1.12.8-28.el8_10
dbus-tools 1.12.8-28.el8_10
device-mapper 1.02.181-15.el8_10.3
device-mapper-libs 1.02.181-15.el8_10.3
diffutils 3.6-6.el8
dmidecode 3.5-1.el8
dnf 4.7.0-21.el8_10
dnf-data 4.7.0-21.el8_10
dnf-plugin-subscription-manager 1.28.44-1.el8_10
dumb-init 1.2.5-3.el8ap
elfutils-default-yama-scope 0.190-2.el8
elfutils-libelf 0.190-2.el8
elfutils-libs 0.190-2.el8
expat 2.5.0-4.el8_10
file-libs 5.33-27.el8_10
filesystem 3.8-6.el8
findutils 4.6.0-24.el8_10
gawk 4.2.1-5.el8_10
gdbm 1.18-2.el8
gdbm-libs 1.18-2.el8
git-core 2.43.7-1.el8_10
git-lfs 3.4.1-13.el8_10
glib2 2.56.4-178.el8_10
glibc 2.28-251.el8_10.48
glibc-common 2.28-251.el8_10.48
glibc-langpack-en 2.28-251.el8_10.48
glibc-minimal-langpack 2.28-251.el8_10.48
gmp 6.1.2-11.el8
gnupg2 2.2.20-4.el8_10
gnutls 3.6.16-8.el8_10.6
gobject-introspection 1.56.1-2.el8_10
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
gzip 1.9-15.el8_10
hostname 3.20-6.el8
ima-evm-utils 1.3.2-12.el8
info 6.5-7.el8
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
kmod-libs 25-20.el8
krb5-libs 1.18.2-34.el8_10
krb5-workstation 1.18.2-34.el8_10
langpacks-en 1.0-12.el8
less 530-3.el8_10
libacl 2.4.0-1.el8_10
libarchive 3.3.3-7.el8_10
libassuan 2.5.1-3.el8
libattr 2.6.0-1.el8_10
libblkid 2.32.1-48.el8_10
libcap 2.48-6.el8_10.1
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-7.el8_10
libcomps 0.1.18-1.el8
libcurl 7.61.1-34.el8_10.13
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-21.el8_10
libedit 3.1-23.20170329cvs.el8
libestr 0.1.10-3.el8
libfastjson 0.99.9-2.el8
libfdisk 2.32.1-48.el8_10
libffi 3.1-24.el8
libgcc 8.5.0-29.el8_10
libgcrypt 1.8.5-8.el8_10
libgfortran 8.5.0-29.el8_10
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libkadm5 1.18.2-34.el8_10
libksba 1.3.5-9.el8_7
libmodulemd 2.13.0-1.el8
libmount 2.32.1-48.el8_10
libnghttp2 1.33.0-6.el8_10.3
libnl3 3.7.0-1.el8
libnsl2 1.2.0-2.20180605git4a062cf.el8
libpeas 1.22.0-6.el8
libpsl 0.20.2-6.el8
libpwquality 1.4.4-6.el8
libquadmath 8.5.0-29.el8_10
librepo 1.14.2-5.el8
libreport-filesystem 2.9.5-15.el8
librhsm 0.0.3-5.el8
libseccomp 2.5.2-1.el8
libselinux 2.9-11.el8_10
libselinux-utils 2.9-11.el8_10
libsemanage 2.9-12.el8_10
libsepol 2.9-3.el8
libserf 1.3.9-9.module+el8.3.0+6671+2675c974
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-48.el8_10
libsolv 0.7.20-7.el8_10
libss 1.45.6-7.el8_10
libssh 0.9.6-17.el8_10
libssh-config 0.9.6-17.el8_10
libstdc++ 8.5.0-29.el8_10
libtasn1 4.13-6.el8_10
libtirpc 1.1.4-12.el8_10
libtool-ltdl 2.4.6-25.el8
libunistring 0.9.9-3.el8
libusbx 1.0.30-1.el8_10
libuser 0.62-26.el8_10
libutempter 1.1.6-14.el8
libuuid 2.32.1-48.el8_10
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-21.el8_10.10
libxslt 1.1.32-6.4.el8_10
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
logrotate 3.14.0-6.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-5.el8_10
microdnf 3.8.0-2.el8
mpdecimal 2.5.1-3.el8
mpfr 3.1.6-1.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
nginx 1.24.0-3.module+el8.10.0+24848+0300f002.5
nginx-filesystem 1.24.0-3.module+el8.10.0+24848+0300f002.5
npth 1.5-4.el8
openblas 0.3.15-6.el8
openldap 2.4.46-21.el8_10
openssh 8.0p1-33.el8_10
openssh-clients 8.0p1-33.el8_10
openssl 1.1.1k-17.el8_6
openssl-libs 1.1.1k-17.el8_6
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-40.el8_10
passwd 0.80-4.el8
pcre 8.42-6.el8
pcre2 10.32-4.el8_10
platform-python 3.6.8-78.el8_10
platform-python-setuptools 39.2.0-9.el8_10
podman-remote 4.9.4-37.module+el8.10.0+24790+ef71b018
policycoreutils 2.9-26.el8_10
policycoreutils-python-utils 2.9-26.el8_10
popt 1.18-1.el8
postgresql 15.19-1.module+el8.10.0+24831+9c841e4e
postgresql-private-libs 15.19-1.module+el8.10.0+24831+9c841e4e
publicsuffix-list-dafsa 20180723-1.el8
python3-audit 3.1.2-1.el8_10.1
python3-cffi 1.11.5-6.el8
python3-chardet 3.0.4-7.el8
python3-cloud-what 1.28.44-1.el8_10
python3-cryptography 3.2.1-8.el8_10
python3-dateutil 2.6.1-6.el8
python3-dbus 1.2.4-15.el8
python3-decorator 4.2.1-2.el8
python3-dnf 4.7.0-21.el8_10
python3-dnf-plugins-core 4.0.21-25.el8
python3-ethtool 0.14-5.el8
python3-gobject-base 3.28.3-2.el8
python3-gpg 1.13.1-12.el8
python3-hawkey 0.63.0-21.el8_10
python3-idna 2.5-8.el8_10
python3-iniparse 0.4-31.el8
python3-inotify 0.9.6-13.el8
python3-libcomps 0.1.18-1.el8
python3-libdnf 0.63.0-21.el8_10
python3-librepo 1.14.2-5.el8
python3-libs 3.6.8-78.el8_10
python3-libselinux 2.9-11.el8_10
python3-libsemanage 2.9-12.el8_10
python3-pip-wheel 9.0.3-24.el8
python3-ply 3.9-9.el8
python3-policycoreutils 2.9-26.el8_10
python3-pycparser 2.14-14.el8
python3-pysocks 1.6.8-3.el8
python3-requests 2.20.0-6.el8_10
python3-rpm 4.14.3-32.el8_10
python3-setools 4.3.0-5.el8
python3-setuptools 39.2.0-9.el8_10
python3-setuptools-wheel 39.2.0-9.el8_10
python3-six 1.11.0-8.el8
python3-subscription-manager-rhsm 1.28.44-1.el8_10
python3-syspurpose 1.28.44-1.el8_10
python3-systemd 234-8.el8
python3-urllib3 1.24.2-10.el8_10
python3.12 3.12.15-2.el8_10
python3.12-libs 3.12.15-2.el8_10
python3.12-pip-wheel 23.2.1-4.el8
python3.12-setuptools 68.2.2-5.el8_10
readline 7.0-10.el8
redhat-logos-httpd 810.1-1.el8_10
redhat-release 8.10-0.3.el8
redis 6.2.24-1.module+el8.10.0+24746+7b800ac5
rootfiles 8.1-22.el8
rpm 4.14.3-32.el8_10
rpm-build-libs 4.14.3-32.el8_10
rpm-libs 4.14.3-32.el8_10
rpm-plugin-selinux 4.14.3-32.el8_10
rsync 3.1.3-28.el8_10
rsyslog 8.2102.0-15.el8_10.3
sed 4.5-5.el8_10
selinux-policy 3.14.3-139.el8_10.2
selinux-policy-minimum 3.14.3-139.el8_10.2
setup 2.12.2-9.el8
shadow-utils 4.6-23.el8_10
shadow-utils-subid 4.6-23.el8_10
sos 4.11.2-4.el8_10
sqlite-libs 3.26.0-21.el8_10
sshpass 1.09-5.el8ap
subscription-manager 1.28.44-1.el8_10
subscription-manager-rhsm-certificates 20220623-1.el8
subversion 1.10.2-5.module+el8.6.0+15157+188c9801
subversion-libs 1.10.2-5.module+el8.6.0+15157+188c9801
supervisor 4.2.5-2.el8ap
systemd 239-82.el8_10.19
systemd-libs 239-82.el8_10.19
systemd-pam 239-82.el8_10.19
tpm2-tss 2.3.2-6.el8
tzdata 2026e-1.el8_10
usermode 1.113-2.el8
utf8proc 2.6.1-3.module+el8.7.0+15837+7cfc8c53
util-linux 2.32.1-48.el8_10
virt-what 1.25-4.el8
which 2.21-21.el8_10
xmlsec1 1.2.25-8.el8_10
xmlsec1-openssl 1.2.25-8.el8_10
xz-libs 5.2.4-4.el8_6
yajl 2.1.0-12.el8
zlib 1.2.11-25.el8
```

</details>

<details><summary>Python packages: /usr (python3.12) (2)</summary>

```text
setuptools 68.2.2
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
sos 4.11.2
subscription-manager 1.28.44
syspurpose 1.28.44
systemd-python 234
urllib3 1.24.2
```

</details>

<details><summary>Python packages: /var/lib/awx/venv/awx (python3.12) (194)</summary>

```text
adal 1.2.7
aiodns 3.6.1
aiofiles 24.1.0
aiohappyeyeballs 2.6.1
aiohttp 3.14.3
aiohttp-retry 2.8.3
aiosignal 1.4.0
annotated-types 0.6.0
ansible-runner 2.4.2
ansiconv 1.0.0
asciichartpy 1.5.25
asgiref 3.11.0
asn1 2.7.0
attrs 23.2.0
autobahn 23.6.2
autocommand 2.2.2
Automat 22.10.0
awx 4.6.34
azure-common 1.1.28
azure-core 1.30.0
azure-identity 1.15.0
azure-keyvault 4.2.0
azure-keyvault-certificates 4.7.0
azure-keyvault-keys 4.8.0
azure-keyvault-secrets 4.7.0
backports.zstd 1.3.0
boto3 1.42.26
botocore 1.42.26
brotli 1.2.0
cachetools 5.5.2
certifi 2038.12.31
cffi 2.0.0
channels 4.3.2
channels-redis 4.2.0
charset-normalizer 3.3.2
click 8.3.3
constantly 23.10.4
cryptography 46.0.7
Cython 3.1.3
daphne 4.2.1
defusedxml 0.7.1
Deprecated 1.2.14
distro 1.9.0
Django 5.2.17
django-ansible-base 2.5.20260422
django-auth-ldap 5.1.0
django-cors-headers 4.3.1
django-crum 0.7.9
django-extensions 3.2.3
django-flags 5.0.13
django-guid 3.5.2
django-oauth-toolkit 1.7.1
django-pglocks 1.0.4
django-polymorphic 4.10.5
django-radius 1.5.1
django-solo 2.2.0
djangorestframework 3.15.2
djangorestframework-yaml 2.0.0
docutils 0.20.1
durationpy 0.10
dynaconf 3.2.13
enum-compat 0.0.3
et-xmlfile 1.1.0
filelock 3.13.1
frozenlist 1.8.0
gitdb 4.0.11
GitPython 3.1.62
google-auth 2.28.1
googleapis-common-protos 1.63.0
grpcio 1.68.1
hiredis 3.2.1
hyperlink 21.0.0
idna 3.6
importlib-metadata 6.2.1
incremental 24.7.2
inflect 7.0.0
inflection 0.5.1
irc 20.3.1
isodate 0.6.1
jaraco.collections 5.0.0
jaraco.context 4.3.0
jaraco.functools 4.3.0
jaraco.logging 3.3.0
jaraco.stream 3.0.3
jaraco.text 3.12.0
Jinja2 3.1.6
jmespath 1.0.1
jq 1.8.0
JSON-log-formatter 0.5.2
jsonschema 4.21.1
jsonschema-specifications 2023.12.1
jwcrypto 1.5.8
kubernetes 36.0.2
lockfile 0.12.2
lxml 4.9.4
Markdown 3.10.2
MarkupSafe 2.1.5
maturin 1.11.5
metrics-utility 0.6.3
more-itertools 10.2.0
msal 1.35.1
msal-extensions 1.1.0
msgpack 1.1.2
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
packaging 26.0
pandas 2.2.1
pbr 6.0.0
pexpect 4.7.0
pip 23.2.1
pip 25.3
pkgconfig 1.5.5
portalocker 2.8.2
prometheus_client 0.20.0
propcache 0.2.0
protobuf 4.25.3
psutil 5.9.8
psycopg 3.1.18
ptyprocess 0.7.0
pyasn1 0.6.4
pyasn1_modules 0.4.2
pycares 4.11.0
pycparser 2.21
pydantic 2.9.2
pydantic_core 2.23.4
pygerduty 0.38.3
PyGithub 2.6.0
PyJWT 2.13.0
PyNaCl 1.5.0
pyOpenSSL 26.0.0
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
PyYAML 6.0.3
pyzstd 0.15.10
receptorctl 1.6.8
redis 7.0.1
referencing 0.33.0
requests 2.32.3
requests-oauthlib 1.3.1
rpds-py 0.18.0
s3transfer 0.16.0
semantic-version 2.10.0
service-identity 24.1.0
setuptools 80.9.0
setuptools-rust 1.12.0
setuptools-scm 9.2.2
six 1.16.0
slack_sdk 3.27.0
smmap 5.0.1
social-auth-app-django 5.4.2
social-auth-core 4.5.4
sqlparse 0.6.0
tacacs-plus 1.0
tempora 5.5.1
twilio 8.13.0
Twisted 24.7.0
txaio 23.1.1
typing_extensions 4.9.0
urllib3 2.7.0
uWSGI 2.0.28
uwsgitop 0.11
websocket-client 1.7.0
wheel 0.46.3
wrapt 1.16.0
xmlsec 1.3.13
yarl 1.17.2
zipp 3.17.0
zope.interface 6.2
```

</details>

<details><summary>Ansible collections (1)</summary>

```text
redhat.indirect_accounting 1.0.0
```

</details>

[Back to top](#contents)

### de-supported-rhel8

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-25/de-supported-rhel8` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/de-supported-rhel8.tar.gz` |
| Labels `version` / `release` | `1.1.7` / `1791896186` |
| Image ID | `sha256:8f33bb79cf4bd1bbfe7df8ca9dd2fc8b7fd437868aaf06f1d6bd4838af9cd22e` |
| Build date | 2026-10-14T14:34:55Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | 3.12 |
| Ansible Core | 2.16.19 |

<details><summary>RPM packages (214)</summary>

```text
alsa-lib 1.2.10-2.el8
ansible-core 2.16.19-1.el8ap
ansible-rulebook 1.1.7-2.el8ap
ansible-runner 2.4.2-3.el8ap
audit-libs 3.1.2-1.el8_10.1
avahi-libs 0.7-27.el8_10.1
basesystem 11-5.el8
bash 4.4.20-6.el8_10
brotli 1.0.6-4.el8_10
bzip2-libs 1.0.6-28.el8_10
ca-certificates 2025.2.80_v9.0.304-80.2.el8_10
chkconfig 1.19.2-1.el8
copy-jdk-configs 4.0-2.el8
coreutils-single 8.30-21.el8_10
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crypto-policies 20230731-1.git3177e06.el8
crypto-policies-scripts 20230731-1.git3177e06.el8
cups-libs 2.2.6-68.el8_10
curl 7.61.1-34.el8_10.13
cyrus-sasl-lib 2.1.27-6.el8_5
dbus-libs 1.12.8-28.el8_10
dumb-init 1.2.5-3.el8ap
elfutils-libelf 0.190-2.el8
expat 2.5.0-4.el8_10
file-libs 5.33-27.el8_10
filesystem 3.8-6.el8
findutils 4.6.0-24.el8_10
gawk 4.2.1-5.el8_10
gdbm 1.18-2.el8
gdbm-libs 1.18-2.el8
git-core 2.43.7-1.el8_10
glib2 2.56.4-178.el8_10
glibc 2.28-251.el8_10.48
glibc-common 2.28-251.el8_10.48
glibc-langpack-en 2.28-251.el8_10.48
glibc-minimal-langpack 2.28-251.el8_10.48
gmp 6.1.2-11.el8
gnupg2 2.2.20-4.el8_10
gnutls 3.6.16-8.el8_10.6
gobject-introspection 1.56.1-2.el8_10
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
gzip 1.9-15.el8_10
info 6.5-7.el8
java-17-openjdk-headless 17.0.20.1.1-1.1.el8
javapackages-filesystem 5.3.0-2.module+el8+2598+06babf2e
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
krb5-libs 1.18.2-34.el8_10
langpacks-en 1.0-12.el8
less 530-3.el8_10
libacl 2.4.0-1.el8_10
libarchive 3.3.3-7.el8_10
libassuan 2.5.1-3.el8
libattr 2.6.0-1.el8_10
libblkid 2.32.1-48.el8_10
libcap 2.48-6.el8_10.1
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-7.el8_10
libcurl 7.61.1-34.el8_10.13
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-21.el8_10
libedit 3.1-23.20170329cvs.el8
libfdisk 2.32.1-48.el8_10
libffi 3.1-24.el8
libgcc 8.5.0-29.el8_10
libgcrypt 1.8.5-8.el8_10
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libksba 1.3.5-9.el8_7
libmodulemd 2.13.0-1.el8
libmount 2.32.1-48.el8_10
libnghttp2 1.33.0-6.el8_10.3
libnsl2 1.2.0-2.20180605git4a062cf.el8
libpeas 1.22.0-6.el8
libpq 13.23-2.el8_10
libpsl 0.20.2-6.el8
libpwquality 1.4.4-6.el8
librepo 1.14.2-5.el8
librhsm 0.0.3-5.el8
libselinux 2.9-11.el8_10
libsemanage 2.9-12.el8_10
libsepol 2.9-3.el8
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-48.el8_10
libsolv 0.7.20-7.el8_10
libssh 0.9.6-17.el8_10
libssh-config 0.9.6-17.el8_10
libstdc++ 8.5.0-29.el8_10
libtasn1 4.13-6.el8_10
libtirpc 1.1.4-12.el8_10
libunistring 0.9.9-3.el8
libusbx 1.0.30-1.el8_10
libutempter 1.1.6-14.el8
libuuid 2.32.1-48.el8_10
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-21.el8_10.10
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
lksctp-tools 1.0.18-3.el8
lua 5.3.4-12.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-5.el8_10
mailcap 2.1.48-3.el8
microdnf 3.8.0-2.el8
mpdecimal 2.5.1-3.el8
mpfr 3.1.6-1.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
npth 1.5-4.el8
nspr 4.39.0-3.el8_10
nss 3.124.0-5.el8_10
nss-softokn 3.124.0-5.el8_10
nss-softokn-freebl 3.124.0-5.el8_10
nss-sysinit 3.124.0-5.el8_10
nss-util 3.124.0-5.el8_10
openldap 2.4.46-21.el8_10
openssh 8.0p1-33.el8_10
openssh-clients 8.0p1-33.el8_10
openssl-libs 1.1.1k-17.el8_6
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-40.el8_10
pcre 8.42-6.el8
pcre2 10.32-4.el8_10
platform-python 3.6.8-78.el8_10
platform-python-setuptools 39.2.0-9.el8_10
popt 1.18-1.el8
publicsuffix-list-dafsa 20180723-1.el8
python3-libs 3.6.8-78.el8_10
python3-pip-wheel 9.0.3-24.el8
python3-setuptools-wheel 39.2.0-9.el8_10
python3.12 3.12.15-2.el8_10
python3.12-aiodns 3.2.0-2.el8ap
python3.12-aiohappyeyeballs 2.6.1-1.el8ap
python3.12-aiohttp 3.14.3-1.el8ap
python3.12-aiosignal 1.4.0-1.el8ap
python3.12-ansible-runner 2.4.2-3.el8ap
python3.12-attrs 22.2.0-2.el8ap
python3.12-azure-core 1.34.0-2.el8ap
python3.12-botocore 1.34.162-2.el8ap
python3.12-brotli 1.2.0-1.el8ap
python3.12-certifi 2023.5.7-2.el8ap
python3.12-cffi 2.0.0-1.el8ap
python3.12-charset-normalizer 3.3.0-2.el8
python3.12-cryptography 46.0.7-1.el8ap
python3.12-daemon 3.1.2-3.el8ap
python3.12-dateutil 2.8.2-3.el8ap
python3.12-dpath 2.1.6-2.el8ap
python3.12-drools-jpy 0.3.10-2.el8ap
python3.12-drools-jpy-jar 1.0.7-2.Final_redhat_00001.1.el8ap
python3.12-frozenlist 1.4.0-2.el8ap
python3.12-idna 3.4-2.el8
python3.12-isodate 0.6.1-3.el8ap
python3.12-janus 1.0.0-3.el8ap
python3.12-jinja2 3.1.6-2.el8ap
python3.12-jmespath 1.0.1-3.el8ap
python3.12-jpy 0.15.0-2.el8ap
python3.12-jsonschema 4.21.1-2.el8ap
python3.12-jsonschema-specifications 2023.12.1-2.el8ap
python3.12-libs 3.12.15-2.el8_10
python3.12-lockfile 0.12.2-3.el8ap
python3.12-markupsafe 2.1.5-2.el8ap
python3.12-multidict 6.0.4-2.el8ap
python3.12-packaging 23.2-2.el8
python3.12-pexpect 4.9.0-2.el8ap
python3.12-pip 23.2.1-4.el8
python3.12-pip-wheel 23.2.1-4.el8
python3.12-ply 3.11-2.el8
python3.12-propcache 0.4.1-1.el8ap
python3.12-psycopg 3.2.7-2.el8ap
python3.12-psycopg+c 3.2.7-2.el8ap
python3.12-psycopg-c 3.2.7-2.el8ap
python3.12-ptyprocess 0.7.0-2.el8ap
python3.12-pycares 4.4.0-3.el8ap
python3.12-pycparser 2.20-2.el8
python3.12-pyparsing 3.1.1-2.el8ap
python3.12-pyyaml 6.0.1-2.el8
python3.12-referencing 0.36.2-3.el8ap
python3.12-requests 2.31.0-4.el8ap
python3.12-resolvelib 1.0.1-2.el8ap
python3.12-rpds-py 0.18.1-3.el8ap
python3.12-six 1.17.0-1.el8ap
python3.12-typing-extensions 4.15.0-2.el8ap
python3.12-urllib3 2.7.0-1.el8ap
python3.12-watchdog 5.0.2-2.el8ap
python3.12-websockets 15.0-3.el8ap
python3.12-wrapt 1.16.0-2.el8ap
python3.12-xxhash 3.4.1-2.el8ap
python3.12-yarl 1.18.3-1.el8ap
readline 7.0-10.el8
redhat-release 8.10-0.3.el8
rootfiles 8.1-22.el8
rpm 4.14.3-32.el8_10
rpm-libs 4.14.3-32.el8_10
sed 4.5-5.el8_10
setup 2.12.2-9.el8
shadow-utils 4.6-23.el8_10
sqlite-libs 3.26.0-21.el8_10
sshpass 1.09-5.el8ap
systemd-libs 239-82.el8_10.19
tar 1.30-13.el8_10
tzdata 2026e-1.el8_10
tzdata-java 2026e-1.el8_10
util-linux 2.32.1-48.el8_10
xz-libs 5.2.4-4.el8_6
zlib 1.2.11-25.el8
```

</details>

<details><summary>Python packages: /usr (python3.12) (55)</summary>

```text
aiodns 3.2.0
aiohappyeyeballs 2.6.1
aiohttp 3.14.3
aiosignal 1.4.0
ansible-core 2.16.19
ansible-rulebook 1.1.7
ansible-runner 2.4.2
attrs 22.2.0
azure-core 1.34.0
botocore 1.34.162
Brotli 1.2.0
certifi 2023.5.7
cffi 2.0.0
charset-normalizer 3.3.0
cryptography 46.0.7
dpath 2.1.6
drools-jpy 0.3.10
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
pip 23.2.1
ply 3.11
propcache 0.4.1
psycopg 3.2.7
psycopg-c 3.2.7
ptyprocess 0.7.0
pycares 4.4.0
pycparser 2.20
pyparsing 3.1.1
python-daemon 3.1.2
python-dateutil 2.8.2
PyYAML 6.0.1
referencing 0.36.2
requests 2.31.0
resolvelib 1.0.1
rpds-py 0.18.1
six 1.17.0
typing_extensions 4.15.0
urllib3 2.7.0
watchdog 5.0.2
websockets 15.0
wrapt 1.16.0
xxhash 3.4.1
yarl 1.18.3
```

</details>

<details><summary>Python packages: /usr (python3.6) (1)</summary>

```text
setuptools 39.2.0
```

</details>

<details><summary>Python packages: /usr/local (python3.12) (8)</summary>

```text
aiobotocore 2.13.3
aioitertools 0.11.0
aiokafka 0.10.0
async-timeout 5.0.1
azure-servicebus 7.12.1
decorator 5.2.1
gssapi 1.9.0
kafka-python-ng 2.2.3
```

</details>

<details><summary>Ansible collections (2)</summary>

```text
ansible.eda 2.10.0
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
| Labels `version` / `release` | `1.1.23` / `1791896186` |
| Image ID | `sha256:6f871fb405bbf51af7d1dc453f30d2d3782c5b40f065fcf63317ad78a28f298f` |
| Build date | 2026-10-14T12:37:51Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | 3.12 |
| Ansible Core | 2.16.19 |

<details><summary>RPM packages (269)</summary>

```text
acl 2.4.0-1.el8_10
ansible-automation-platform-common 2.5-2.el8ap
ansible-automation-platform-selinux 0.2-3.el8ap
ansible-core 2.16.19-1.el8ap
audit-libs 3.1.2-1.el8_10.1
automation-eda-controller 1.1.23-1.el8ap
basesystem 11-5.el8
bash 4.4.20-6.el8_10
brotli 1.0.6-4.el8_10
bzip2-libs 1.0.6-28.el8_10
ca-certificates 2025.2.80_v9.0.304-80.2.el8_10
checkpolicy 2.9-1.el8
chkconfig 1.19.2-1.el8
coreutils-single 8.30-21.el8_10
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crypto-policies 20230731-1.git3177e06.el8
cryptsetup-libs 2.3.7-7.el8
curl 7.61.1-34.el8_10.13
cyrus-sasl-lib 2.1.27-6.el8_5
dbus 1.12.8-28.el8_10
dbus-common 1.12.8-28.el8_10
dbus-daemon 1.12.8-28.el8_10
dbus-libs 1.12.8-28.el8_10
dbus-tools 1.12.8-28.el8_10
device-mapper 1.02.181-15.el8_10.3
device-mapper-libs 1.02.181-15.el8_10.3
diffutils 3.6-6.el8
dumb-init 1.2.5-3.el8ap
elfutils-default-yama-scope 0.190-2.el8
elfutils-libelf 0.190-2.el8
elfutils-libs 0.190-2.el8
expat 2.5.0-4.el8_10
file-libs 5.33-27.el8_10
filesystem 3.8-6.el8
gawk 4.2.1-5.el8_10
gdbm 1.18-2.el8
gdbm-libs 1.18-2.el8
git-core 2.43.7-1.el8_10
glib2 2.56.4-178.el8_10
glibc 2.28-251.el8_10.48
glibc-common 2.28-251.el8_10.48
glibc-langpack-en 2.28-251.el8_10.48
glibc-minimal-langpack 2.28-251.el8_10.48
gmp 6.1.2-11.el8
gnupg2 2.2.20-4.el8_10
gnutls 3.6.16-8.el8_10.6
gobject-introspection 1.56.1-2.el8_10
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
gzip 1.9-15.el8_10
info 6.5-7.el8
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
kmod-libs 25-20.el8
krb5-libs 1.18.2-34.el8_10
langpacks-en 1.0-12.el8
less 530-3.el8_10
libacl 2.4.0-1.el8_10
libarchive 3.3.3-7.el8_10
libassuan 2.5.1-3.el8
libattr 2.6.0-1.el8_10
libblkid 2.32.1-48.el8_10
libcap 2.48-6.el8_10.1
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-7.el8_10
libcurl 7.61.1-34.el8_10.13
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-21.el8_10
libedit 3.1-23.20170329cvs.el8
libfdisk 2.32.1-48.el8_10
libffi 3.1-24.el8
libgcc 8.5.0-29.el8_10
libgcrypt 1.8.5-8.el8_10
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libksba 1.3.5-9.el8_7
libmodulemd 2.13.0-1.el8
libmount 2.32.1-48.el8_10
libnghttp2 1.33.0-6.el8_10.3
libnsl2 1.2.0-2.20180605git4a062cf.el8
libpeas 1.22.0-6.el8
libpq 13.23-2.el8_10
libpsl 0.20.2-6.el8
libpwquality 1.4.4-6.el8
librepo 1.14.2-5.el8
librhsm 0.0.3-5.el8
libseccomp 2.5.2-1.el8
libselinux 2.9-11.el8_10
libselinux-utils 2.9-11.el8_10
libsemanage 2.9-12.el8_10
libsepol 2.9-3.el8
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-48.el8_10
libsolv 0.7.20-7.el8_10
libssh 0.9.6-17.el8_10
libssh-config 0.9.6-17.el8_10
libstdc++ 8.5.0-29.el8_10
libtasn1 4.13-6.el8_10
libtirpc 1.1.4-12.el8_10
libunistring 0.9.9-3.el8
libusbx 1.0.30-1.el8_10
libutempter 1.1.6-14.el8
libuuid 2.32.1-48.el8_10
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-21.el8_10.10
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-5.el8_10
microdnf 3.8.0-2.el8
mpdecimal 2.5.1-3.el8
mpfr 3.1.6-1.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
npth 1.5-4.el8
openldap 2.4.46-21.el8_10
openssh 8.0p1-33.el8_10
openssh-clients 8.0p1-33.el8_10
openssl-libs 1.1.1k-17.el8_6
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-40.el8_10
pcre 8.42-6.el8
pcre2 10.32-4.el8_10
platform-python 3.6.8-78.el8_10
platform-python-setuptools 39.2.0-9.el8_10
podman-remote 4.9.4-37.module+el8.10.0+24790+ef71b018
policycoreutils 2.9-26.el8_10
policycoreutils-python-utils 2.9-26.el8_10
popt 1.18-1.el8
publicsuffix-list-dafsa 20180723-1.el8
python3-audit 3.1.2-1.el8_10.1
python3-cffi 1.11.5-6.el8
python3-cryptography 3.2.1-8.el8_10
python3-libs 3.6.8-78.el8_10
python3-libselinux 2.9-11.el8_10
python3-libsemanage 2.9-12.el8_10
python3-pip-wheel 9.0.3-24.el8
python3-ply 3.9-9.el8
python3-policycoreutils 2.9-26.el8_10
python3-pycparser 2.14-14.el8
python3-setools 4.3.0-5.el8
python3-setuptools-wheel 39.2.0-9.el8_10
python3-six 1.11.0-8.el8
python3.12 3.12.15-2.el8_10
python3.12-Automat 22.10.0-4.el8ap
python3.12-ansible-runner 2.4.2-3.el8ap
python3.12-asgiref 3.11.1-1.el8ap
python3.12-attrs 22.2.0-2.el8ap
python3.12-autobahn 24.4.2-2.el8ap
python3.12-cachetools 5.3.2-2.el8ap
python3.12-certifi 2023.5.7-2.el8ap
python3.12-cffi 2.0.0-1.el8ap
python3.12-channels 4.3.2-1.el8ap
python3.12-channels+daphne 4.3.2-1.el8ap
python3.12-charset-normalizer 3.3.0-2.el8
python3.12-click 8.3.3-1.el8ap
python3.12-constantly 23.10.4-1.el8ap
python3.12-croniter 2.0.1-2.el8ap
python3.12-crontab 1.0.5-1.el8ap
python3.12-cryptography 46.0.7-1.el8ap
python3.12-daemon 3.1.2-3.el8ap
python3.12-daphne 4.2.2-1.el8ap
python3.12-dateutil 2.8.2-3.el8ap
python3.12-dispatcherd 2025.5.19-3.el8ap
python3.12-dispatcherd+pg_notify 2025.5.19-3.el8ap
python3.12-distro 1.9.0-2.el8ap
python3.12-django 5.2.17-1.el8ap
python3.12-django-ansible-base 2.5.20260422-2.el8ap
python3.12-django-ansible-base+channel_auth 2.5.20260422-2.el8ap
python3.12-django-ansible-base+feature_flags 2.5.20260422-2.el8ap
python3.12-django-ansible-base+jwt_consumer 2.5.20260422-2.el8ap
python3.12-django-ansible-base+rbac 2.5.20260422-2.el8ap
python3.12-django-ansible-base+redis_client 2.5.20260422-2.el8ap
python3.12-django-ansible-base+rest_filters 2.5.20260422-2.el8ap
python3.12-django-crum 0.7.9-3.el8ap
python3.12-django-filter 25.2-1.el8ap
python3.12-django-flags 5.0.13-2.el8ap
python3.12-django-redis 5.4.0-2.el8ap
python3.12-django-rq 3.2.2-1.el8ap
python3.12-django-split-settings 1.2.0-3.el8ap
python3.12-djangorestframework 3.15.1-2.el8ap
python3.12-drf-spectacular 0.29.0-1.el8ap
python3.12-dynaconf 3.2.11-2.el8ap
python3.12-ecdsa 0.18.0-2.el8ap
python3.12-freezegun 1.5.5-1.el8ap
python3.12-gnupg 0.5.2-2.el8ap
python3.12-google-auth 2.27.0-2.el8ap
python3.12-gunicorn 23.0.0-2.el8ap
python3.12-hyperlink 21.0.0-3.el8ap
python3.12-idna 3.4-2.el8
python3.12-incremental 24.7.2-2.el8ap
python3.12-inflection 0.5.1-5.el8ap
python3.12-insights-analytics-collector 0.3.2-3.el8ap
python3.12-jinja2 3.1.6-2.el8ap
python3.12-jsonschema 4.21.1-2.el8ap
python3.12-jsonschema-specifications 2023.12.1-2.el8ap
python3.12-kubernetes 26.1.0-3.el8ap
python3.12-libs 3.12.15-2.el8_10
python3.12-lockfile 0.12.2-3.el8ap
python3.12-markupsafe 2.1.5-2.el8ap
python3.12-oauthlib 3.2.2-2.el8ap
python3.12-packaging 23.2-2.el8
python3.12-pexpect 4.9.0-2.el8ap
python3.12-pip-wheel 23.2.1-4.el8
python3.12-ply 3.11-2.el8
python3.12-podman 5.4.0.1-2.el8ap
python3.12-psycopg 3.2.7-2.el8ap
python3.12-ptyprocess 0.7.0-2.el8ap
python3.12-pyOpenSSL 26.0.0-1.el8ap
python3.12-pyasn1 0.6.4-1.el8ap
python3.12-pyasn1-modules 0.4.2-1.el8ap
python3.12-pycparser 2.20-2.el8
python3.12-pydantic 1.10.15-2.el8ap
python3.12-pyjwt 2.13.0-1.el8ap
python3.12-pyjwt+crypto 2.13.0-1.el8ap
python3.12-pytz 2024.1-2.el8ap
python3.12-pyyaml 6.0.1-2.el8
python3.12-redis 4.6.0-3.el8ap
python3.12-referencing 0.36.2-3.el8ap
python3.12-requests 2.31.0-4.el8ap
python3.12-requests-oauthlib 1.3.1-2.el8ap
python3.12-resolvelib 1.0.1-2.el8ap
python3.12-rpds-py 0.18.1-3.el8ap
python3.12-rq 2.6.1-1.el8ap
python3.12-rq-scheduler 0.14.0-1.el8ap
python3.12-rsa 4.9-3.el8ap
python3.12-service-identity 21.1.0-3.el8ap
python3.12-setuptools 68.2.2-5.el8_10
python3.12-six 1.17.0-1.el8ap
python3.12-sqlparse 0.6.0-1.el8ap
python3.12-twisted 24.7.0-2.el8ap
python3.12-twisted+tls 24.7.0-2.el8ap
python3.12-txaio 23.1.1-3.el8ap
python3.12-typing-extensions 4.15.0-2.el8ap
python3.12-uritemplate 4.1.1-4.el8ap
python3.12-urllib3 2.7.0-1.el8ap
python3.12-validators 0.34.0-2.el8ap
python3.12-websocket-client 1.7.0-3.el8ap
python3.12-xxhash 3.4.1-2.el8ap
python3.12-zope-interface 6.1-2.el8ap
readline 7.0-10.el8
redhat-release 8.10-0.3.el8
rootfiles 8.1-22.el8
rpm 4.14.3-32.el8_10
rpm-libs 4.14.3-32.el8_10
rpm-plugin-selinux 4.14.3-32.el8_10
sed 4.5-5.el8_10
selinux-policy 3.14.3-139.el8_10.2
selinux-policy-minimum 3.14.3-139.el8_10.2
setup 2.12.2-9.el8
shadow-utils 4.6-23.el8_10
shadow-utils-subid 4.6-23.el8_10
sqlite-libs 3.26.0-21.el8_10
sshpass 1.09-5.el8ap
systemd 239-82.el8_10.19
systemd-libs 239-82.el8_10.19
systemd-pam 239-82.el8_10.19
tzdata 2026e-1.el8_10
util-linux 2.32.1-48.el8_10
xz-libs 5.2.4-4.el8_6
zlib 1.2.11-25.el8
```

</details>

<details><summary>Python packages: /usr (python3.12) (86)</summary>

```text
aap-eda 1.1.23
ansible-core 2.16.19
ansible-runner 2.4.2
asgiref 3.11.1
attrs 22.2.0
autobahn 24.4.2
Automat 22.10.0
cachetools 5.3.2
certifi 2023.5.7
cffi 2.0.0
channels 4.3.2
charset-normalizer 3.3.0
click 8.3.3
constantly 23.10.4
croniter 2.0.1
crontab 1.0.5
cryptography 46.0.7
daphne 4.2.2
dispatcherd 2025.5.19
distro 1.9.0
Django 5.2.17
django-ansible-base 2.5.20260422
django-crum 0.7.9
django-filter 25.2
django-flags 5.0.13
django-redis 5.4.0
django-rq 3.2.2
django-split-settings 1.2.0
djangorestframework 3.15.1
drf-spectacular 0.29.0
dynaconf 3.2.11
ecdsa 0.18.0
freezegun 1.5.5
google-auth 2.27.0
gunicorn 23.0.0
hyperlink 21.0.0
idna 3.4
incremental 24.7.2
inflection 0.5.1
insights-analytics-collector 0.3.2
Jinja2 3.1.6
jsonschema 4.21.1
jsonschema-specifications 2023.12.1
kubernetes 26.1.0
lockfile 0.12.2
MarkupSafe 2.1.5
oauthlib 3.2.2
packaging 23.2
pexpect 4.9.0
ply 3.11
podman 5.4.0.1
psycopg 3.2.7
ptyprocess 0.7.0
pyasn1 0.6.4
pyasn1-modules 0.4.2
pycparser 2.20
pydantic 1.10.15
PyJWT 2.13.0
pyOpenSSL 26.0.0
python-daemon 3.1.2
python-dateutil 2.8.2
python-gnupg 0.5.2
pytz 2024.1
PyYAML 6.0.1
redis 4.6.0
referencing 0.36.2
requests 2.31.0
requests-oauthlib 1.3.1
resolvelib 1.0.1
rpds-py 0.18.1
rq 2.6.1
rq-scheduler 0.14.0
rsa 4.9
service-identity 21.1.0
setuptools 68.2.2
six 1.17.0
sqlparse 0.6.0
Twisted 24.7.0
txaio 23.1.1
typing_extensions 4.15.0
uritemplate 4.1.1
urllib3 2.7.0
validators 0.34.0
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
| Labels `version` / `release` | `1.1.23` / `1791836066` |
| Image ID | `sha256:be5f2eb5317fb95dab95ccc14c1214a50a18adb56a4a3c92c93fb7651c1cdcdc` |
| Build date | 2026-10-14T13:32:10Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | N/A |
| Ansible Core | N/A |

<details><summary>RPM packages (277)</summary>

```text
acl 2.4.0-1.el8_10
audit-libs 3.1.2-1.el8_10.1
basesystem 11-5.el8
bash 4.4.20-6.el8_10
bind-libs 9.11.36-16.el8_10.16
bind-libs-lite 9.11.36-16.el8_10.16
bind-license 9.11.36-16.el8_10.16
bind-utils 9.11.36-16.el8_10.16
brotli 1.0.6-4.el8_10
bsdtar 3.3.3-7.el8_10
bzip2-libs 1.0.6-28.el8_10
ca-certificates 2025.2.80_v9.0.304-80.2.el8_10
chkconfig 1.19.2-1.el8
cmake 3.26.5-2.el8
cmake-data 3.26.5-2.el8
cmake-filesystem 3.26.5-2.el8
cmake-rpm-macros 3.26.5-2.el8
coreutils-single 8.30-21.el8_10
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crypto-policies 20230731-1.git3177e06.el8
crypto-policies-scripts 20230731-1.git3177e06.el8
cryptsetup-libs 2.3.7-7.el8
curl 7.61.1-34.el8_10.13
cyrus-sasl-lib 2.1.27-6.el8_5
dbus 1.12.8-28.el8_10
dbus-common 1.12.8-28.el8_10
dbus-daemon 1.12.8-28.el8_10
dbus-glib 0.110-2.el8
dbus-libs 1.12.8-28.el8_10
dbus-tools 1.12.8-28.el8_10
device-mapper 1.02.181-15.el8_10.3
device-mapper-libs 1.02.181-15.el8_10.3
dmidecode 3.5-1.el8
dnf 4.7.0-21.el8_10
dnf-data 4.7.0-21.el8_10
dnf-plugin-subscription-manager 1.28.44-1.el8_10
elfutils-default-yama-scope 0.190-2.el8
elfutils-libelf 0.190-2.el8
elfutils-libs 0.190-2.el8
emacs-filesystem 26.1-15.el8_10.2
environment-modules 4.5.2-4.el8
expat 2.5.0-4.el8_10
file-libs 5.33-27.el8_10
filesystem 3.8-6.el8
findutils 4.6.0-24.el8_10
fstrm 0.6.1-3.el8
gawk 4.2.1-5.el8_10
gdb-gdbserver 8.2-20.1.el8_10
gdbm 1.18-2.el8
gdbm-libs 1.18-2.el8
geolite2-city 20180605-1.el8
geolite2-country 20180605-1.el8
gettext 0.19.8.1-17.el8
gettext-libs 0.19.8.1-17.el8
glib2 2.56.4-178.el8_10
glibc 2.28-251.el8_10.43
glibc-common 2.28-251.el8_10.43
glibc-langpack-en 2.28-251.el8_10.43
glibc-locale-source 2.28-251.el8_10.43
glibc-minimal-langpack 2.28-251.el8_10.43
gmp 6.1.2-11.el8
gnupg2 2.2.20-4.el8_10
gnutls 3.6.16-8.el8_10.6
gobject-introspection 1.56.1-2.el8_10
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
groff-base 1.22.3-18.el8
gzip 1.9-15.el8_10
hostname 3.20-6.el8
ima-evm-utils 1.3.2-12.el8
info 6.5-7.el8
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
kmod-libs 25-20.el8
krb5-libs 1.18.2-34.el8_10
langpacks-en 1.0-12.el8
less 530-3.el8_10
libacl 2.4.0-1.el8_10
libarchive 3.3.3-7.el8_10
libassuan 2.5.1-3.el8
libattr 2.6.0-1.el8_10
libblkid 2.32.1-48.el8_10
libcap 2.48-6.el8_10.1
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-7.el8_10
libcomps 0.1.18-1.el8
libcroco 0.6.12-4.el8_2.1
libcurl 7.61.1-34.el8_10.13
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-21.el8_10
libfdisk 2.32.1-48.el8_10
libffi 3.1-24.el8
libgcc 8.5.0-29.el8_10
libgcrypt 1.8.5-8.el8_10
libgomp 8.5.0-29.el8_10
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libksba 1.3.5-9.el8_7
libmaxminddb 1.2.0-10.el8_9.1
libmodulemd 2.13.0-1.el8
libmount 2.32.1-48.el8_10
libnghttp2 1.33.0-6.el8_10.3
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
libselinux 2.9-11.el8_10
libsemanage 2.9-12.el8_10
libsepol 2.9-3.el8
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-48.el8_10
libsolv 0.7.20-7.el8_10
libssh 0.9.6-17.el8_10
libssh-config 0.9.6-17.el8_10
libstdc++ 8.5.0-29.el8_10
libtasn1 4.13-6.el8_10
libtirpc 1.1.4-12.el8_10
libunistring 0.9.9-3.el8
libusbx 1.0.30-1.el8_10
libuser 0.62-26.el8_10
libutempter 1.1.6-14.el8
libuuid 2.32.1-48.el8_10
libuv 1.41.1-2.el8_10
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-21.el8_10.9
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-5.el8_10
make 4.2.1-11.el8
man-db 2.7.6.1-18.el8
mpfr 3.1.6-1.el8
ncurses 6.1-10.20180224.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
nginx 1.24.0-3.module+el8.10.0+24848+0300f002.5
nginx-filesystem 1.24.0-3.module+el8.10.0+24848+0300f002.5
nginx-mod-http-perl 1.24.0-3.module+el8.10.0+24848+0300f002.5
nginx-mod-stream 1.24.0-3.module+el8.10.0+24848+0300f002.5
npth 1.5-4.el8
nss_wrapper 1.1.13-1.el8
nss_wrapper-libs 1.1.13-1.el8
openldap 2.4.46-21.el8_10
openssl 1.1.1k-17.el8_6
openssl-libs 1.1.1k-17.el8_6
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-40.el8_10
passwd 0.80-4.el8
pcre 8.42-6.el8
pcre2 10.32-3.el8_6
perl-Carp 1.42-396.el8
perl-Data-Dumper 2.167-399.el8
perl-Digest 1.17-395.el8
perl-Digest-MD5 2.55-396.el8
perl-Encode 2.97-3.el8
perl-Errno 1.28-423.el8_10.1
perl-Exporter 5.72-396.el8
perl-File-Path 2.15-2.el8
perl-File-Temp 0.230.600-1.el8
perl-Getopt-Long 2.50-4.el8
perl-HTTP-Tiny 0.074-3.el8
perl-IO 1.38-423.el8_10.1
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
perl-interpreter 5.26.3-423.el8_10.1
perl-libnet 3.11-3.el8
perl-libs 5.26.3-423.el8_10.1
perl-macros 5.26.3-423.el8_10.1
perl-parent 0.237-1.el8
perl-podlators 4.11-1.el8
perl-threads 2.21-2.el8
perl-threads-shared 1.58-2.el8
pkgconf 1.4.2-1.el8
pkgconf-m4 1.4.2-1.el8
pkgconf-pkg-config 1.4.2-1.el8
platform-python 3.6.8-78.el8_10
platform-python-setuptools 39.2.0-9.el8_10
popt 1.18-1.el8
procps-ng 3.3.15-14.el8
protobuf-c 1.3.0-8.el8
publicsuffix-list-dafsa 20180723-1.el8
python3-bind 9.11.36-16.el8_10.16
python3-chardet 3.0.4-7.el8
python3-cloud-what 1.28.44-1.el8_10
python3-dateutil 2.6.1-6.el8
python3-dbus 1.2.4-15.el8
python3-decorator 4.2.1-2.el8
python3-dnf 4.7.0-21.el8_10
python3-dnf-plugins-core 4.0.21-25.el8
python3-ethtool 0.14-5.el8
python3-gobject-base 3.28.3-2.el8
python3-gpg 1.13.1-12.el8
python3-hawkey 0.63.0-21.el8_10
python3-idna 2.5-8.el8_10
python3-iniparse 0.4-31.el8
python3-inotify 0.9.6-13.el8
python3-libcomps 0.1.18-1.el8
python3-libdnf 0.63.0-21.el8_10
python3-librepo 1.14.2-5.el8
python3-libs 3.6.8-78.el8_10
python3-pip-wheel 9.0.3-24.el8
python3-ply 3.9-9.el8
python3-pysocks 1.6.8-3.el8
python3-requests 2.20.0-6.el8_10
python3-rpm 4.14.3-32.el8_10
python3-setuptools-wheel 39.2.0-9.el8_10
python3-six 1.11.0-8.el8
python3-subscription-manager-rhsm 1.28.44-1.el8_10
python3-syspurpose 1.28.44-1.el8_10
python3-systemd 234-8.el8
python3-urllib3 1.24.2-10.el8_10
readline 7.0-10.el8
redhat-logos-httpd 810.1-1.el8_10
redhat-release 8.10-0.3.el8
rootfiles 8.1-22.el8
rpm 4.14.3-32.el8_10
rpm-build-libs 4.14.3-32.el8_10
rpm-libs 4.14.3-32.el8_10
rsync 3.1.3-28.el8_10
scl-utils 2.0.2-16.el8
sed 4.5-5.el8_10
setup 2.12.2-9.el8
shadow-utils 4.6-23.el8_10
sqlite-libs 3.26.0-21.el8_10
subscription-manager 1.28.44-1.el8_10
subscription-manager-rhsm-certificates 20220623-1.el8
systemd 239-82.el8_10.19
systemd-libs 239-82.el8_10.19
systemd-pam 239-82.el8_10.19
tar 1.30-13.el8_10
tcl 8.6.8-2.el8
tpm2-tss 2.3.2-6.el8
tzdata 2026e-1.el8_10
unzip 6.0-48.el8_10
usermode 1.113-2.el8
util-linux 2.32.1-48.el8_10
vim-filesystem 8.0.1763-32.el8_10
vim-minimal 8.0.1763-32.el8_10
virt-what 1.25-4.el8
which 2.21-21.el8_10
xz 5.2.4-4.el8_6
xz-libs 5.2.4-4.el8_6
yum 4.7.0-21.el8_10
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
subscription-manager 1.28.44
syspurpose 1.28.44
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
| Labels `version` / `release` | `2.0.0` / `1791896186` |
| Image ID | `sha256:453b732edf665ee7dbbd8f28b42e28f788414409a5a7029018375de9f8348de9` |
| Build date | 2026-10-14T13:22:41Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | 3.12 |
| Ansible Core | 2.16.19 |

<details><summary>RPM packages (238)</summary>

```text
ansible-core 2.16.19-1.el8ap
ansible-lint 26.1.1-1.el8ap
ansible-runner 2.4.2-3.el8ap
ansible-test 2.16.19-1.el8ap
audit-libs 3.1.2-1.el8_10.1
basesystem 11-5.el8
bash 4.4.20-6.el8_10
brotli 1.0.6-4.el8_10
bzip2 1.0.6-28.el8_10
bzip2-libs 1.0.6-28.el8_10
ca-certificates 2025.2.80_v9.0.304-80.2.el8_10
chkconfig 1.19.2-1.el8
cmake-filesystem 3.26.5-2.el8
coreutils-single 8.30-21.el8_10
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crypto-policies 20230731-1.git3177e06.el8
curl 7.61.1-34.el8_10.13
cyrus-sasl-lib 2.1.27-6.el8_5
dumb-init 1.2.5-3.el8ap
elfutils-libelf 0.190-2.el8
expat 2.5.0-4.el8_10
file 5.33-27.el8_10
file-libs 5.33-27.el8_10
filesystem 3.8-6.el8
gawk 4.2.1-5.el8_10
gdbm-libs 1.18-2.el8
git-core 2.43.7-1.el8_10
glib2 2.56.4-178.el8_10
glibc 2.28-251.el8_10.48
glibc-common 2.28-251.el8_10.48
glibc-langpack-en 2.28-251.el8_10.48
glibc-minimal-langpack 2.28-251.el8_10.48
gmp 6.1.2-11.el8
gnupg2 2.2.20-4.el8_10
gnutls 3.6.16-8.el8_10.6
gobject-introspection 1.56.1-2.el8_10
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
groff-base 1.22.3-18.el8
gzip 1.9-15.el8_10
info 6.5-7.el8
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
krb5-libs 1.18.2-34.el8_10
krb5-workstation 1.18.2-34.el8_10
langpacks-en 1.0-12.el8
less 530-3.el8_10
libacl 2.4.0-1.el8_10
libarchive 3.3.3-7.el8_10
libassuan 2.5.1-3.el8
libattr 2.6.0-1.el8_10
libblkid 2.32.1-48.el8_10
libcap 2.48-6.el8_10.1
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-7.el8_10
libcurl 7.61.1-34.el8_10.13
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-21.el8_10
libedit 3.1-23.20170329cvs.el8
libfdisk 2.32.1-48.el8_10
libffi 3.1-24.el8
libgcc 8.5.0-29.el8_10
libgcrypt 1.8.5-8.el8_10
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libkadm5 1.18.2-34.el8_10
libksba 1.3.5-9.el8_7
libmodulemd 2.13.0-1.el8
libmount 2.32.1-48.el8_10
libnghttp2 1.33.0-6.el8_10.3
libnsl2 1.2.0-2.20180605git4a062cf.el8
libpeas 1.22.0-6.el8
libpkgconf 1.4.2-1.el8
libpsl 0.20.2-6.el8
libpwquality 1.4.4-6.el8
librepo 1.14.2-5.el8
librhsm 0.0.3-5.el8
libselinux 2.9-11.el8_10
libsemanage 2.9-12.el8_10
libsepol 2.9-3.el8
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-48.el8_10
libsolv 0.7.20-7.el8_10
libss 1.45.6-7.el8_10
libssh 0.9.6-17.el8_10
libssh-config 0.9.6-17.el8_10
libstdc++ 8.5.0-29.el8_10
libtasn1 4.13-6.el8_10
libtirpc 1.1.4-12.el8_10
libunistring 0.9.9-3.el8
libusbx 1.0.30-1.el8_10
libutempter 1.1.6-14.el8
libuuid 2.32.1-48.el8_10
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-21.el8_10.10
libxslt 1.1.32-6.4.el8_10
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-5.el8_10
microdnf 3.8.0-2.el8
mpdecimal 2.5.1-3.el8
mpfr 3.1.6-1.el8
ncurses 6.1-10.20180224.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
npth 1.5-4.el8
nss_wrapper 1.1.13-1.el8
nss_wrapper-libs 1.1.13-1.el8
openldap 2.4.46-21.el8_10
openssh 8.0p1-33.el8_10
openssh-clients 8.0p1-33.el8_10
openssl 1.1.1k-17.el8_6
openssl-libs 1.1.1k-17.el8_6
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-40.el8_10
pcre 8.42-6.el8
pcre2 10.32-4.el8_10
perl-Carp 1.42-396.el8
perl-Data-Dumper 2.167-399.el8
perl-Digest 1.17-395.el8
perl-Digest-MD5 2.55-396.el8
perl-Encode 2.97-3.el8
perl-Errno 1.28-423.el8_10.1
perl-Exporter 5.72-396.el8
perl-File-Path 2.15-2.el8
perl-File-Temp 0.230.600-1.el8
perl-Getopt-Long 2.50-4.el8
perl-HTTP-Tiny 0.074-3.el8
perl-IO 1.38-423.el8_10.1
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
perl-interpreter 5.26.3-423.el8_10.1
perl-libnet 3.11-3.el8
perl-libs 5.26.3-423.el8_10.1
perl-macros 5.26.3-423.el8_10.1
perl-parent 0.237-1.el8
perl-podlators 4.11-1.el8
perl-threads 2.21-2.el8
perl-threads-shared 1.58-2.el8
pkgconf 1.4.2-1.el8
pkgconf-m4 1.4.2-1.el8
pkgconf-pkg-config 1.4.2-1.el8
popt 1.18-1.el8
publicsuffix-list-dafsa 20180723-1.el8
python3.12 3.12.15-2.el8_10
python3.12-ansible-compat 25.12.0-3.el8ap
python3.12-ansible-runner 2.4.2-3.el8ap
python3.12-attrs 22.2.0-2.el8ap
python3.12-black 26.3.1-1.el8ap
python3.12-bracex 2.4-2.el8ap
python3.12-certifi 2023.5.7-2.el8ap
python3.12-cffi 2.0.0-1.el8ap
python3.12-charset-normalizer 3.3.0-2.el8
python3.12-click 8.3.3-1.el8ap
python3.12-cryptography 46.0.7-1.el8ap
python3.12-daemon 3.1.2-3.el8ap
python3.12-distro 1.9.0-2.el8ap
python3.12-filelock 3.13.1-2.el8ap
python3.12-idna 3.4-2.el8
python3.12-jinja2 3.1.6-2.el8ap
python3.12-jsonschema 4.21.1-2.el8ap
python3.12-jsonschema-specifications 2023.12.1-2.el8ap
python3.12-libs 3.12.15-2.el8_10
python3.12-lockfile 0.12.2-3.el8ap
python3.12-markupsafe 2.1.5-2.el8ap
python3.12-mypy-extensions 1.0.0-2.el8ap
python3.12-packaging 23.2-2.el8
python3.12-pathspec 1.0.4-1.el8ap
python3.12-pexpect 4.9.0-2.el8ap
python3.12-pip 23.2.1-4.el8
python3.12-pip-wheel 23.2.1-4.el8
python3.12-platformdirs 4.2.0-2.el8ap
python3.12-ply 3.11-2.el8
python3.12-ptyprocess 0.7.0-2.el8ap
python3.12-pyOpenSSL 26.0.0-1.el8ap
python3.12-pycparser 2.20-2.el8
python3.12-pytokens 0.4.1-1.el8ap
python3.12-pyyaml 6.0.1-2.el8
python3.12-referencing 0.36.2-3.el8ap
python3.12-requests 2.31.0-4.el8ap
python3.12-resolvelib 1.0.1-2.el8ap
python3.12-rpds-py 0.18.1-3.el8ap
python3.12-ruamel-yaml 0.18.15-2.el8ap
python3.12-ruamel-yaml-clib 0.2.15-2.el8ap
python3.12-setuptools 68.2.2-5.el8_10
python3.12-six 1.17.0-1.el8ap
python3.12-subprocess-tee 0.4.2-2.el8ap
python3.12-typing-extensions 4.15.0-2.el8ap
python3.12-urllib3 2.7.0-1.el8ap
python3.12-wcmatch 8.5-2.el8ap
readline 7.0-10.el8
redhat-release 8.10-0.3.el8
rootfiles 8.1-22.el8
rpm 4.14.3-32.el8_10
rpm-libs 4.14.3-32.el8_10
sed 4.5-5.el8_10
setup 2.12.2-9.el8
shadow-utils 4.6-23.el8_10
sqlite-libs 3.26.0-21.el8_10
sshpass 1.09-5.el8ap
systemd-libs 239-82.el8_10.19
tar 1.30-13.el8_10
tzdata 2026e-1.el8_10
unzip 6.0-48.el8_10
util-linux 2.32.1-48.el8_10
xz 5.2.4-4.el8_6
xz-libs 5.2.4-4.el8_6
yamllint 1.38.0-1.el8ap
zlib 1.2.11-25.el8
zstd 1.4.4-1.el8
```

</details>

<details><summary>Python packages: /usr (python3.12) (46)</summary>

```text
ansible-compat 25.12.0
ansible-core 2.16.19
ansible-lint 26.1.1
ansible-runner 2.4.2
attrs 22.2.0
black 26.3.1
bracex 2.4
certifi 2023.5.7
cffi 2.0.0
charset-normalizer 3.3.0
click 8.3.3
cryptography 46.0.7
distro 1.9.0
filelock 3.13.1
idna 3.4
Jinja2 3.1.6
jsonschema 4.21.1
jsonschema-specifications 2023.12.1
lockfile 0.12.2
MarkupSafe 2.1.5
mypy-extensions 1.0.0
packaging 23.2
pathspec 1.0.4
pexpect 4.9.0
pip 23.2.1
platformdirs 4.2.0
ply 3.11
ptyprocess 0.7.0
pycparser 2.20
pyOpenSSL 26.0.0
python-daemon 3.1.2
pytokens 0.4.1
PyYAML 6.0.1
referencing 0.36.2
requests 2.31.0
resolvelib 1.0.1
rpds-py 0.18.1
ruamel.yaml 0.18.15
ruamel.yaml.clib 0.2.15
setuptools 68.2.2
six 1.17.0
subprocess-tee 0.4.2
typing_extensions 4.15.0
urllib3 2.7.0
wcmatch 8.5
yamllint 1.38.0
```

</details>

<details><summary>Python packages: /usr/local (python3.12) (17)</summary>

```text
bcrypt 3.2.0
decorator 5.1.1
gssapi 1.8.2
krb5 0.5.0
lxml 6.1.3
ncclient 0.6.19
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

### ee-supported-rhel8

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/ee-supported-rhel8.tar.gz` |
| Labels `version` / `release` | `2.0.0` / `1791765785` |
| Image ID | `sha256:9a8c53500f7d3b3385acd86250d6ab6d540cbc4fce25b694dd67d10148b60bde` |
| Build date | 2026-10-13T12:45:17Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | 3.12 |
| Ansible Core | 2.16.19 |

<details><summary>RPM packages (337)</summary>

```text
acl 2.4.0-1.el8_10
ansible-core 2.16.19-1.el8ap
ansible-lint 26.1.1-1.el8ap
ansible-runner 2.4.2-3.el8ap
ansible-sign 0.1.4-2.el8ap
ansible-test 2.16.19-1.el8ap
apr 1.6.3-12.el8
apr-util 1.6.1-9.el8_10.1
audit-libs 3.1.2-1.el8_10.1
automation-controller-cli 4.6.34-1.el8ap
basesystem 11-5.el8
bash 4.4.20-6.el8_10
bash-completion 2.7-5.el8
brotli 1.0.6-4.el8_10
bzip2 1.0.6-28.el8_10
bzip2-libs 1.0.6-28.el8_10
ca-certificates 2025.2.80_v9.0.304-80.2.el8_10
chkconfig 1.19.2-1.el8
cmake-filesystem 3.26.5-2.el8
coreutils-single 8.30-21.el8_10
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crypto-policies 20230731-1.git3177e06.el8
cryptsetup-libs 2.3.7-7.el8
curl 7.61.1-34.el8_10.13
cyrus-sasl-lib 2.1.27-6.el8_5
dbus 1.12.8-28.el8_10
dbus-common 1.12.8-28.el8_10
dbus-daemon 1.12.8-28.el8_10
dbus-libs 1.12.8-28.el8_10
dbus-tools 1.12.8-28.el8_10
device-mapper 1.02.181-15.el8_10.3
device-mapper-libs 1.02.181-15.el8_10.3
diffutils 3.6-6.el8
dumb-init 1.2.5-3.el8ap
elfutils-default-yama-scope 0.190-2.el8
elfutils-libelf 0.190-2.el8
elfutils-libs 0.190-2.el8
expat 2.5.0-4.el8_10
file 5.33-27.el8_10
file-libs 5.33-27.el8_10
filesystem 3.8-6.el8
findutils 4.6.0-24.el8_10
gawk 4.2.1-5.el8_10
gdbm 1.18-2.el8
gdbm-libs 1.18-2.el8
git-core 2.43.7-1.el8_10
git-lfs 3.4.1-13.el8_10
glib2 2.56.4-178.el8_10
glibc 2.28-251.el8_10.48
glibc-common 2.28-251.el8_10.48
glibc-langpack-en 2.28-251.el8_10.48
glibc-minimal-langpack 2.28-251.el8_10.48
gmp 6.1.2-11.el8
gnupg2 2.2.20-4.el8_10
gnutls 3.6.16-8.el8_10.6
gobject-introspection 1.56.1-2.el8_10
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
groff-base 1.22.3-18.el8
gzip 1.9-15.el8_10
info 6.5-7.el8
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
kmod-libs 25-20.el8
krb5-libs 1.18.2-34.el8_10
krb5-workstation 1.18.2-34.el8_10
langpacks-en 1.0-12.el8
less 530-3.el8_10
libacl 2.4.0-1.el8_10
libaio 0.3.112-1.el8
libarchive 3.3.3-7.el8_10
libassuan 2.5.1-3.el8
libattr 2.6.0-1.el8_10
libblkid 2.32.1-48.el8_10
libcap 2.48-6.el8_10.1
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-7.el8_10
libcurl 7.61.1-34.el8_10.13
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-21.el8_10
libedit 3.1-23.20170329cvs.el8
libfdisk 2.32.1-48.el8_10
libffi 3.1-24.el8
libgcc 8.5.0-29.el8_10
libgcrypt 1.8.5-8.el8_10
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libkadm5 1.18.2-34.el8_10
libksba 1.3.5-9.el8_7
libmodulemd 2.13.0-1.el8
libmount 2.32.1-48.el8_10
libnghttp2 1.33.0-6.el8_10.3
libnsl2 1.2.0-2.20180605git4a062cf.el8
libpeas 1.22.0-6.el8
libpkgconf 1.4.2-1.el8
libpq 13.23-2.el8_10
libpsl 0.20.2-6.el8
libpwquality 1.4.4-6.el8
librepo 1.14.2-5.el8
librhsm 0.0.3-5.el8
libseccomp 2.5.2-1.el8
libselinux 2.9-11.el8_10
libselinux-utils 2.9-11.el8_10
libsemanage 2.9-12.el8_10
libsepol 2.9-3.el8
libserf 1.3.9-9.module+el8.3.0+6671+2675c974
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-48.el8_10
libsolv 0.7.20-7.el8_10
libss 1.45.6-7.el8_10
libssh 0.9.6-17.el8_10
libssh-config 0.9.6-17.el8_10
libstdc++ 8.5.0-29.el8_10
libtasn1 4.13-6.el8_10
libtirpc 1.1.4-12.el8_10
libunistring 0.9.9-3.el8
libusbx 1.0.30-1.el8_10
libutempter 1.1.6-14.el8
libuuid 2.32.1-48.el8_10
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-21.el8_10.10
libxslt 1.1.32-6.4.el8_10
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
logrotate 3.14.0-6.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-5.el8_10
mailcap 2.1.48-3.el8
microdnf 3.8.0-2.el8
mpdecimal 2.5.1-3.el8
mpfr 3.1.6-1.el8
ncurses 6.1-10.20180224.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
npth 1.5-4.el8
nss_wrapper 1.1.13-1.el8
nss_wrapper-libs 1.1.13-1.el8
openldap 2.4.46-21.el8_10
openshift-clients 4.14.0-202609111720.p2.g44b3ac2.assembly.stream.el8
openssh 8.0p1-33.el8_10
openssh-clients 8.0p1-33.el8_10
openssl 1.1.1k-17.el8_6
openssl-libs 1.1.1k-17.el8_6
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-40.el8_10
pcre 8.42-6.el8
pcre2 10.32-3.el8_6
perl-Carp 1.42-396.el8
perl-Data-Dumper 2.167-399.el8
perl-Digest 1.17-395.el8
perl-Digest-MD5 2.55-396.el8
perl-Encode 2.97-3.el8
perl-Errno 1.28-423.el8_10.1
perl-Exporter 5.72-396.el8
perl-File-Path 2.15-2.el8
perl-File-Temp 0.230.600-1.el8
perl-Getopt-Long 2.50-4.el8
perl-HTTP-Tiny 0.074-3.el8
perl-IO 1.38-423.el8_10.1
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
perl-interpreter 5.26.3-423.el8_10.1
perl-libnet 3.11-3.el8
perl-libs 5.26.3-423.el8_10.1
perl-macros 5.26.3-423.el8_10.1
perl-parent 0.237-1.el8
perl-podlators 4.11-1.el8
perl-threads 2.21-2.el8
perl-threads-shared 1.58-2.el8
pkgconf 1.4.2-1.el8
pkgconf-m4 1.4.2-1.el8
pkgconf-pkg-config 1.4.2-1.el8
platform-python 3.6.8-78.el8_10
platform-python-setuptools 39.2.0-9.el8_10
podman-remote 4.9.4-37.module+el8.10.0+24790+ef71b018
policycoreutils 2.9-26.el8_10
popt 1.18-1.el8
publicsuffix-list-dafsa 20180723-1.el8
python3-chardet 3.0.4-7.el8
python3-idna 2.5-8.el8_10
python3-libs 3.6.8-78.el8_10
python3-pip-wheel 9.0.3-24.el8
python3-pysocks 1.6.8-3.el8
python3-requests 2.20.0-6.el8_10
python3-setuptools 39.2.0-9.el8_10
python3-setuptools-wheel 39.2.0-9.el8_10
python3-six 1.11.0-8.el8
python3-urllib3 1.24.2-10.el8_10
python3.12 3.12.15-2.el8_10
python3.12-aiodns 3.2.0-2.el8ap
python3.12-aiohappyeyeballs 2.6.1-1.el8ap
python3.12-aiohttp 3.14.3-1.el8ap
python3.12-aiosignal 1.4.0-1.el8ap
python3.12-ansible-compat 25.12.0-3.el8ap
python3.12-ansible-pylibssh 1.2.2-2.el8ap
python3.12-ansible-runner 2.4.2-3.el8ap
python3.12-attrs 22.2.0-2.el8ap
python3.12-azure-core 1.34.0-2.el8ap
python3.12-black 26.3.1-1.el8ap
python3.12-boto3 1.34.30-2.el8ap
python3.12-botocore 1.34.162-2.el8ap
python3.12-bracex 2.4-2.el8ap
python3.12-brotli 1.2.0-1.el8ap
python3.12-cachetools 5.3.2-2.el8ap
python3.12-certifi 2023.5.7-2.el8ap
python3.12-cffi 2.0.0-1.el8ap
python3.12-chardet 5.2.0-3.el8ap
python3.12-charset-normalizer 3.3.0-2.el8
python3.12-click 8.3.3-1.el8ap
python3.12-cryptography 46.0.7-1.el8ap
python3.12-daemon 3.1.2-3.el8ap
python3.12-dateutil 2.8.2-3.el8ap
python3.12-deprecated 1.2.14-2.el8ap
python3.12-distlib 0.4.0-2.el8ap
python3.12-distro 1.9.0-2.el8ap
python3.12-dpath 2.1.6-2.el8ap
python3.12-filelock 3.13.1-2.el8ap
python3.12-frozenlist 1.4.0-2.el8ap
python3.12-gnupg 0.5.2-2.el8ap
python3.12-google-auth 2.27.0-2.el8ap
python3.12-grpcio 1.71.2-1.el8ap
python3.12-idna 3.4-2.el8
python3.12-importlib-metadata 6.0.1-3.el8ap
python3.12-isodate 0.6.1-3.el8ap
python3.12-jinja2 3.1.6-2.el8ap
python3.12-jmespath 1.0.1-3.el8ap
python3.12-jsonschema 4.21.1-2.el8ap
python3.12-jsonschema-specifications 2023.12.1-2.el8ap
python3.12-libs 3.12.15-2.el8_10
python3.12-lockfile 0.12.2-3.el8ap
python3.12-markupsafe 2.1.5-2.el8ap
python3.12-multidict 6.0.4-2.el8ap
python3.12-mypy-extensions 1.0.0-2.el8ap
python3.12-netaddr 1.2.1-2.el8ap
python3.12-oauthlib 3.2.2-2.el8ap
python3.12-packaging 23.2-2.el8
python3.12-pathspec 1.0.4-1.el8ap
python3.12-pexpect 4.9.0-2.el8ap
python3.12-pip 23.2.1-4.el8
python3.12-pip-wheel 23.2.1-4.el8
python3.12-platformdirs 4.2.0-2.el8ap
python3.12-ply 3.11-2.el8
python3.12-propcache 0.4.1-1.el8ap
python3.12-protobuf 5.29.6-1.el8ap
python3.12-psycopg 3.2.7-2.el8ap
python3.12-ptyprocess 0.7.0-2.el8ap
python3.12-pyOpenSSL 26.0.0-1.el8ap
python3.12-pyasn1 0.6.4-1.el8ap
python3.12-pyasn1-modules 0.4.2-1.el8ap
python3.12-pycares 4.4.0-3.el8ap
python3.12-pycparser 2.20-2.el8
python3.12-pygments 2.17.2-3.el8ap
python3.12-pyjwt 2.13.0-1.el8ap
python3.12-pytokens 0.4.1-1.el8ap
python3.12-pytz 2024.1-2.el8ap
python3.12-pyyaml 6.0.1-2.el8
python3.12-referencing 0.36.2-3.el8ap
python3.12-requests 2.31.0-4.el8ap
python3.12-requests-oauthlib 1.3.1-2.el8ap
python3.12-resolvelib 1.0.1-2.el8ap
python3.12-rpds-py 0.18.1-3.el8ap
python3.12-rsa 4.9-3.el8ap
python3.12-ruamel-yaml 0.18.15-2.el8ap
python3.12-ruamel-yaml-clib 0.2.15-2.el8ap
python3.12-s3transfer 0.10.0-2.el8ap
python3.12-setuptools 68.2.2-5.el8_10
python3.12-six 1.17.0-1.el8ap
python3.12-subprocess-tee 0.4.2-2.el8ap
python3.12-tabulate 0.9.0-4.el8ap
python3.12-typing-extensions 4.15.0-2.el8ap
python3.12-uamqp 1.6.8-2.el8ap
python3.12-urllib3 2.7.0-1.el8ap
python3.12-watchdog 5.0.2-2.el8ap
python3.12-wcmatch 8.5-2.el8ap
python3.12-websocket-client 1.7.0-3.el8ap
python3.12-wrapt 1.16.0-2.el8ap
python3.12-xxhash 3.4.1-2.el8ap
python3.12-yarl 1.18.3-1.el8ap
python3.12-zipp 3.19.2-2.el8ap
qemu-img 6.2.0-53.module+el8.10.0+23760+c0926e61.6
readline 7.0-10.el8
receptor 1.6.8-1.el8ap
receptorctl 1.6.8-1.el8ap
redhat-release 8.10-0.3.el8
rootfiles 8.1-22.el8
rpm 4.14.3-32.el8_10
rpm-libs 4.14.3-32.el8_10
rsync 3.1.3-28.el8_10
sed 4.5-5.el8_10
setup 2.12.2-9.el8
shadow-utils 4.6-23.el8_10
shadow-utils-subid 4.6-23.el8_10
sos 4.11.2-4.el8_10
sqlite-libs 3.26.0-21.el8_10
sshpass 1.09-5.el8ap
subversion 1.10.2-5.module+el8.6.0+15157+188c9801
subversion-libs 1.10.2-5.module+el8.6.0+15157+188c9801
systemd 239-82.el8_10.19
systemd-libs 239-82.el8_10.19
systemd-pam 239-82.el8_10.19
tar 1.30-13.el8_10
tzdata 2026e-1.el8_10
unzip 6.0-48.el8_10
utf8proc 2.6.1-3.module+el8.7.0+15837+7cfc8c53
util-linux 2.32.1-48.el8_10
xz 5.2.4-4.el8_6
xz-libs 5.2.4-4.el8_6
yamllint 1.38.0-1.el8ap
zlib 1.2.11-25.el8
zstd 1.4.4-1.el8
```

</details>

<details><summary>Python packages: /usr (python3.12) (94)</summary>

```text
aiodns 3.2.0
aiohappyeyeballs 2.6.1
aiohttp 3.14.3
aiosignal 1.4.0
ansible-compat 25.12.0
ansible-core 2.16.19
ansible-lint 26.1.1
ansible-pylibssh 1.2.2
ansible-runner 2.4.2
ansible-sign 0.1.4
attrs 22.2.0
awxkit 4.6.34
azure-core 1.34.0
black 26.3.1
boto3 1.34.30
botocore 1.34.162
bracex 2.4
Brotli 1.2.0
cachetools 5.3.2
certifi 2023.5.7
cffi 2.0.0
chardet 5.2.0
charset-normalizer 3.3.0
click 8.3.3
cryptography 46.0.7
Deprecated 1.2.14
distlib 0.4.0
distro 1.9.0
dpath 2.1.6
filelock 3.13.1
frozenlist 1.4.0
google-auth 2.27.0
grpcio 1.71.2
idna 3.4
importlib-metadata 6.0.1
isodate 0.6.1
Jinja2 3.1.6
jmespath 1.0.1
jsonschema 4.21.1
jsonschema-specifications 2023.12.1
lockfile 0.12.2
MarkupSafe 2.1.5
multidict 6.0.4
mypy-extensions 1.0.0
netaddr 1.2.1
oauthlib 3.2.2
packaging 23.2
pathspec 1.0.4
pexpect 4.9.0
pip 23.2.1
platformdirs 4.2.0
ply 3.11
propcache 0.4.1
protobuf 5.29.6
psycopg 3.2.7
ptyprocess 0.7.0
pyasn1 0.6.4
pyasn1-modules 0.4.2
pycares 4.4.0
pycparser 2.20
Pygments 2.17.2
PyJWT 2.13.0
pyOpenSSL 26.0.0
python-daemon 3.1.2
python-dateutil 2.8.2
python-gnupg 0.5.2
pytokens 0.4.1
pytz 2024.1
PyYAML 6.0.1
receptorctl 1.6.8
referencing 0.36.2
requests 2.31.0
requests-oauthlib 1.3.1
resolvelib 1.0.1
rpds-py 0.18.1
rsa 4.9
ruamel.yaml 0.18.15
ruamel.yaml.clib 0.2.15
s3transfer 0.10.0
setuptools 68.2.2
six 1.17.0
subprocess-tee 0.4.2
tabulate 0.9.0
typing_extensions 4.15.0
uamqp 1.6.8
urllib3 2.7.0
watchdog 5.0.2
wcmatch 8.5
websocket-client 1.7.0
wrapt 1.16.0
xxhash 3.4.1
yamllint 1.38.0
yarl 1.18.3
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
sos 4.11.2
urllib3 1.24.2
```

</details>

<details><summary>Python packages: /usr/local (python3.12) (158)</summary>

```text
adal 1.2.7
aiobotocore 2.13.3
aioitertools 0.11.0
aiokafka 0.10.0
anyio 4.4.0
appdirs 1.4.4
applicationinsights 0.11.10
argcomplete 3.5.3
async-timeout 5.0.1
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
gssapi 1.8.2
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
kafka-python-ng 2.2.3
keystoneauth1 4.3.1
knack 0.11.0
krb5 0.9.0
kubernetes 29.0.0
lxml 6.1.3
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
ncclient 0.6.19
netifaces 0.10.9
nsx-policy-python-sdk 4.1.2.0.0
nsx-python-sdk 4.1.2.0.0
nsx-vmc-aws-integration-python-sdk 4.1.2.0.0
nsx-vmc-policy-python-sdk 4.1.2.0.0
ntlm-auth 1.5.0
numpy 2.2.6
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
pbr 7.0.1
pendulum 3.0.0
pkginfo 1.7.0
portalocker 1.7.1
psutil 5.9.1
py-deviceid 0.1.1
pyang 2.5.3
pycurl 7.45.3
pykerberos 1.2.4
PyNaCl 1.4.0
pypsrp 0.5.0
PySocks 1.7.1
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
stevedore 3.3.3
suds 1.1.2
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

<details><summary>Ansible collections (57)</summary>

```text
amazon.aws 9.2.0
ansible.controller 4.6.34
ansible.eda 2.10.0
ansible.hub 1.0.0
ansible.netcommon 7.1.0
ansible.network 4.0.0
ansible.platform 2.5.20260306
ansible.posix 1.5.4
ansible.scm 3.0.0
ansible.security 3.0.0
ansible.snmp 3.0.0
ansible.utils 5.1.2
ansible.windows 3.4.0
ansible.yang 3.0.0
arista.eos 10.0.1
azure.azcollection 3.7.0
cisco.asa 6.0.0
cisco.ios 9.1.1
cisco.iosxr 10.3.0
cisco.nxos 9.3.0
cloud.common 4.0.0
cloud.terraform 3.0.0
community.vmware 1.9.0
frr.frr 2.0.2
google.cloud 1.0.2
ibm.qradar 4.0.0
junipernetworks.junos 9.1.0
kubernetes.core 5.4.0
microsoft.ad 1.8.0
openstack.cloud 1.5.0
openvswitch.openvswitch 2.1.1
redhat.amq_broker 1.3.0
redhat.amq_streams 1.0.0
redhat.data_grid 1.3.1
redhat.eap 1.3.1
redhat.insights 1.3.0
redhat.jbcs 1.0.1
redhat.jws 2.0.0
redhat.openshift 4.0.2
redhat.openshift_virtualization 1.5.0
redhat.redhat_csp_download 1.2.2
redhat.rhbk 2.2.2
redhat.rhel_idm 1.10.0
redhat.rhel_system_roles 1.95.7
redhat.rhv 2.4.2
redhat.runtimes_common 1.1.3
redhat.sap_install 1.2.1
redhat.satellite 3.15.0
redhat.satellite_operations 3.0.0
redhat.sso 1.3.0
sap.sap_operations 1.0.4
servicenow.itsm 2.6.3
splunk.es 4.0.0
trendmicro.deepsec 4.0.0
vmware.vmware 1.10.1
vmware.vmware_rest 4.6.0
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
| Labels `version` / `release` | `2.5.10` / `1791896186` |
| Image ID | `sha256:6b56b4e12bcc4bab31750bc634c379f77591edf7b458e80f0fd55595c2bdd167` |
| Build date | 2026-10-14T01:38:07Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | N/A |
| Ansible Core | N/A |

<details><summary>RPM packages (107)</summary>

```text
audit-libs 3.1.2-1.el8_10.1
automation-gateway-config 2.5.20260923-1.el8ap
automation-gateway-proxy-server 2.5.10-8.el8ap
basesystem 11-5.el8
bash 4.4.20-6.el8_10
brotli 1.0.6-4.el8_10
bzip2-libs 1.0.6-28.el8_10
ca-certificates 2025.2.80_v9.0.304-80.2.el8_10
chkconfig 1.19.2-1.el8
coreutils-single 8.30-21.el8_10
crypto-policies 20230731-1.git3177e06.el8
curl 7.61.1-34.el8_10.13
cyrus-sasl-lib 2.1.27-6.el8_5
dumb-init 1.2.5-3.el8ap
elfutils-libelf 0.190-2.el8
file-libs 5.33-27.el8_10
filesystem 3.8-6.el8
gawk 4.2.1-5.el8_10
glib2 2.56.4-178.el8_10
glibc 2.28-251.el8_10.48
glibc-common 2.28-251.el8_10.48
glibc-langpack-en 2.28-251.el8_10.48
glibc-minimal-langpack 2.28-251.el8_10.48
gmp 6.1.2-11.el8
gnupg2 2.2.20-4.el8_10
gnutls 3.6.16-8.el8_10.6
gobject-introspection 1.56.1-2.el8_10
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
info 6.5-7.el8
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
krb5-libs 1.18.2-34.el8_10
langpacks-en 1.0-12.el8
libacl 2.4.0-1.el8_10
libarchive 3.3.3-7.el8_10
libassuan 2.5.1-3.el8
libattr 2.6.0-1.el8_10
libblkid 2.32.1-48.el8_10
libcap 2.48-6.el8_10.1
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-7.el8_10
libcurl 7.61.1-34.el8_10.13
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-21.el8_10
libffi 3.1-24.el8
libgcc 8.5.0-29.el8_10
libgcrypt 1.8.5-8.el8_10
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libksba 1.3.5-9.el8_7
libmodulemd 2.13.0-1.el8
libmount 2.32.1-48.el8_10
libnghttp2 1.33.0-6.el8_10.3
libpeas 1.22.0-6.el8
libpsl 0.20.2-6.el8
librepo 1.14.2-5.el8
librhsm 0.0.3-5.el8
libselinux 2.9-11.el8_10
libsepol 2.9-3.el8
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-48.el8_10
libsolv 0.7.20-7.el8_10
libssh 0.9.6-17.el8_10
libssh-config 0.9.6-17.el8_10
libstdc++ 8.5.0-29.el8_10
libtasn1 4.13-6.el8_10
libunistring 0.9.9-3.el8
libusbx 1.0.30-1.el8_10
libuuid 2.32.1-48.el8_10
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-21.el8_10.10
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-5.el8_10
microdnf 3.8.0-2.el8
mpfr 3.1.6-1.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
npth 1.5-4.el8
openldap 2.4.46-21.el8_10
openssl-libs 1.1.1k-17.el8_6
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pcre 8.42-6.el8
pcre2 10.32-4.el8_10
popt 1.18-1.el8
publicsuffix-list-dafsa 20180723-1.el8
readline 7.0-10.el8
redhat-release 8.10-0.3.el8
rootfiles 8.1-22.el8
rpm 4.14.3-32.el8_10
rpm-libs 4.14.3-32.el8_10
sed 4.5-5.el8_10
setup 2.12.2-9.el8
sqlite-libs 3.26.0-21.el8_10
systemd-libs 239-82.el8_10.19
tzdata 2026e-1.el8_10
xz-libs 5.2.4-4.el8_6
zlib 1.2.11-25.el8
```

</details>

[Back to top](#contents)

### gateway-rhel8

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/gateway-rhel8.tar.gz` |
| Labels `version` / `release` | `2.5.20260923` / `1791896186` |
| Image ID | `sha256:fbd243f8491e88fbb1d40308f72b4b8825659b7ade2bc81732b5e19a6741629d` |
| Build date | 2026-10-14T01:27:25Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | 3.12 |
| Ansible Core | N/A |

<details><summary>RPM packages (251)</summary>

```text
acl 2.4.0-1.el8_10
ansible-automation-platform-common 2.5-2.el8ap
ansible-automation-platform-selinux 0.2-3.el8ap
audit-libs 3.1.2-1.el8_10.1
automation-gateway-server 2.5.20260923-1.el8ap
basesystem 11-5.el8
bash 4.4.20-6.el8_10
brotli 1.0.6-4.el8_10
bzip2-libs 1.0.6-28.el8_10
ca-certificates 2025.2.80_v9.0.304-80.2.el8_10
checkpolicy 2.9-1.el8
chkconfig 1.19.2-1.el8
coreutils-single 8.30-21.el8_10
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crypto-policies 20230731-1.git3177e06.el8
cryptsetup-libs 2.3.7-7.el8
curl 7.61.1-34.el8_10.13
cyrus-sasl-lib 2.1.27-6.el8_5
dbus 1.12.8-28.el8_10
dbus-common 1.12.8-28.el8_10
dbus-daemon 1.12.8-28.el8_10
dbus-libs 1.12.8-28.el8_10
dbus-tools 1.12.8-28.el8_10
device-mapper 1.02.181-15.el8_10.3
device-mapper-libs 1.02.181-15.el8_10.3
diffutils 3.6-6.el8
dumb-init 1.2.5-3.el8ap
elfutils-default-yama-scope 0.190-2.el8
elfutils-libelf 0.190-2.el8
elfutils-libs 0.190-2.el8
expat 2.5.0-4.el8_10
file-libs 5.33-27.el8_10
filesystem 3.8-6.el8
gawk 4.2.1-5.el8_10
gdbm 1.18-2.el8
gdbm-libs 1.18-2.el8
glib2 2.56.4-178.el8_10
glibc 2.28-251.el8_10.48
glibc-common 2.28-251.el8_10.48
glibc-langpack-en 2.28-251.el8_10.48
glibc-minimal-langpack 2.28-251.el8_10.48
gmp 6.1.2-11.el8
gnupg2 2.2.20-4.el8_10
gnutls 3.6.16-8.el8_10.6
gobject-introspection 1.56.1-2.el8_10
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
gzip 1.9-15.el8_10
info 6.5-7.el8
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
kmod-libs 25-20.el8
krb5-libs 1.18.2-34.el8_10
langpacks-en 1.0-12.el8
libacl 2.4.0-1.el8_10
libarchive 3.3.3-7.el8_10
libassuan 2.5.1-3.el8
libattr 2.6.0-1.el8_10
libblkid 2.32.1-48.el8_10
libcap 2.48-6.el8_10.1
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-7.el8_10
libcurl 7.61.1-34.el8_10.13
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-21.el8_10
libfdisk 2.32.1-48.el8_10
libffi 3.1-24.el8
libgcc 8.5.0-29.el8_10
libgcrypt 1.8.5-8.el8_10
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libksba 1.3.5-9.el8_7
libmodulemd 2.13.0-1.el8
libmount 2.32.1-48.el8_10
libnghttp2 1.33.0-6.el8_10.3
libnsl2 1.2.0-2.20180605git4a062cf.el8
libpeas 1.22.0-6.el8
libpq 13.23-2.el8_10
libpsl 0.20.2-6.el8
libpwquality 1.4.4-6.el8
librepo 1.14.2-5.el8
librhsm 0.0.3-5.el8
libseccomp 2.5.2-1.el8
libselinux 2.9-11.el8_10
libselinux-utils 2.9-11.el8_10
libsemanage 2.9-12.el8_10
libsepol 2.9-3.el8
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-48.el8_10
libsolv 0.7.20-7.el8_10
libssh 0.9.6-17.el8_10
libssh-config 0.9.6-17.el8_10
libstdc++ 8.5.0-29.el8_10
libtasn1 4.13-6.el8_10
libtirpc 1.1.4-12.el8_10
libtool-ltdl 2.4.6-25.el8
libunistring 0.9.9-3.el8
libusbx 1.0.30-1.el8_10
libutempter 1.1.6-14.el8
libuuid 2.32.1-48.el8_10
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-21.el8_10.10
libxslt 1.1.32-6.4.el8_10
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-5.el8_10
microdnf 3.8.0-2.el8
mpdecimal 2.5.1-3.el8
mpfr 3.1.6-1.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
nginx 1.24.0-3.module+el8.10.0+24848+0300f002.5
nginx-filesystem 1.24.0-3.module+el8.10.0+24848+0300f002.5
npth 1.5-4.el8
openldap 2.4.46-21.el8_10
openssl 1.1.1k-17.el8_6
openssl-libs 1.1.1k-17.el8_6
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-40.el8_10
pcre 8.42-6.el8
pcre2 10.32-4.el8_10
platform-python 3.6.8-78.el8_10
platform-python-setuptools 39.2.0-9.el8_10
policycoreutils 2.9-26.el8_10
policycoreutils-python-utils 2.9-26.el8_10
popt 1.18-1.el8
postgresql 15.19-1.module+el8.10.0+24831+9c841e4e
postgresql-private-libs 15.19-1.module+el8.10.0+24831+9c841e4e
publicsuffix-list-dafsa 20180723-1.el8
python3-audit 3.1.2-1.el8_10.1
python3-cffi 1.11.5-6.el8
python3-cryptography 3.2.1-8.el8_10
python3-libs 3.6.8-78.el8_10
python3-libselinux 2.9-11.el8_10
python3-libsemanage 2.9-12.el8_10
python3-pip-wheel 9.0.3-24.el8
python3-ply 3.9-9.el8
python3-policycoreutils 2.9-26.el8_10
python3-pycparser 2.14-14.el8
python3-setools 4.3.0-5.el8
python3-setuptools-wheel 39.2.0-9.el8_10
python3-six 1.11.0-8.el8
python3.12 3.12.15-2.el8_10
python3.12-argon2-cffi 23.1.0-2.el8ap
python3.12-argon2-cffi-bindings 21.2.0-2.el8ap
python3.12-asgiref 3.11.1-1.el8ap
python3.12-attrs 22.2.0-2.el8ap
python3.12-certifi 2023.5.7-2.el8ap
python3.12-cffi 2.0.0-1.el8ap
python3.12-charset-normalizer 3.3.0-2.el8
python3.12-cryptography 46.0.7-1.el8ap
python3.12-defusedxml 0.7.1-5.el8ap
python3.12-django 5.2.17-1.el8ap
python3.12-django-ansible-base 2.5.20260422-2.el8ap
python3.12-django-ansible-base+activitystream 2.5.20260422-2.el8ap
python3.12-django-ansible-base+api_documentation 2.5.20260422-2.el8ap
python3.12-django-ansible-base+authentication 2.5.20260422-2.el8ap
python3.12-django-ansible-base+feature_flags 2.5.20260422-2.el8ap
python3.12-django-ansible-base+oauth2_provider 2.5.20260422-2.el8ap
python3.12-django-ansible-base+rbac 2.5.20260422-2.el8ap
python3.12-django-ansible-base+redis_client 2.5.20260422-2.el8ap
python3.12-django-ansible-base+rest_filters 2.5.20260422-2.el8ap
python3.12-django-auth-ldap 4.0.0-3.el8ap
python3.12-django-crum 0.7.9-3.el8ap
python3.12-django-dynamic-preferences 1.16.0-2.el8ap
python3.12-django-extensions 4.1-2.el8ap
python3.12-django-flags 5.0.13-2.el8ap
python3.12-django-oauth-toolkit 2.3.0-2.el8ap
python3.12-django-redis 5.4.0-2.el8ap
python3.12-djangorestframework 3.15.1-2.el8ap
python3.12-drf-spectacular 0.29.0-1.el8ap
python3.12-dynaconf 3.2.11-2.el8ap
python3.12-googleapis-common-protos 1.72.0-1.el8ap
python3.12-grpcio 1.71.2-1.el8ap
python3.12-grpcio-tools 1.71.2-1.el8ap
python3.12-idna 3.4-2.el8
python3.12-inflection 0.5.1-5.el8ap
python3.12-isodate 0.6.1-3.el8ap
python3.12-jsonschema 4.21.1-2.el8ap
python3.12-jsonschema-specifications 2023.12.1-2.el8ap
python3.12-jwcrypto 1.5.7-1.el8ap
python3.12-ldap 3.4.5-1.el8ap
python3.12-ldap-filter 1.0.1-2.el8ap
python3.12-libs 3.12.15-2.el8_10
python3.12-lxml 5.3.0-2.el8ap
python3.12-netaddr 1.2.1-2.el8ap
python3.12-oauthlib 3.2.2-2.el8ap
python3.12-opentelemetry-proto 1.28.0-1.el8ap
python3.12-persisting-theory 1.0-3.el8ap
python3.12-pip-wheel 23.2.1-4.el8
python3.12-ply 3.11-2.el8
python3.12-protobuf 5.29.6-1.el8ap
python3.12-psycopg 3.2.7-2.el8ap
python3.12-pyasn1 0.6.4-1.el8ap
python3.12-pyasn1-modules 0.4.2-1.el8ap
python3.12-pycparser 2.20-2.el8
python3.12-pyjwt 2.13.0-1.el8ap
python3.12-pyrad 2.4-3.el8ap
python3.12-python3-openid 3.2.0-4.el8ap
python3.12-python3-saml 1.16.0-3.el8ap
python3.12-pyyaml 6.0.1-2.el8
python3.12-redis 4.6.0-3.el8ap
python3.12-referencing 0.36.2-3.el8ap
python3.12-requests 2.31.0-4.el8ap
python3.12-requests-oauthlib 1.3.1-2.el8ap
python3.12-rpds-py 0.18.1-3.el8ap
python3.12-setuptools 68.2.2-5.el8_10
python3.12-six 1.17.0-1.el8ap
python3.12-social-auth-app-django 5.4.1-2.el8ap
python3.12-social-auth-core 4.5.4-2.el8ap
python3.12-sqlparse 0.6.0-1.el8ap
python3.12-tabulate 0.9.0-4.el8ap
python3.12-tacacs-plus 2.6-3.el8ap
python3.12-typing-extensions 4.15.0-2.el8ap
python3.12-uritemplate 4.1.1-4.el8ap
python3.12-urllib3 2.7.0-1.el8ap
python3.12-xds-protos 1.71.2-1.el8ap
python3.12-xmlsec 1.3.13-3.el8ap
readline 7.0-10.el8
redhat-logos-httpd 810.1-1.el8_10
redhat-release 8.10-0.3.el8
rootfiles 8.1-22.el8
rpm 4.14.3-32.el8_10
rpm-libs 4.14.3-32.el8_10
rpm-plugin-selinux 4.14.3-32.el8_10
sed 4.5-5.el8_10
selinux-policy 3.14.3-139.el8_10.2
selinux-policy-minimum 3.14.3-139.el8_10.2
setup 2.12.2-9.el8
shadow-utils 4.6-23.el8_10
sqlite-libs 3.26.0-21.el8_10
supervisor 4.2.5-2.el8ap
systemd 239-82.el8_10.19
systemd-libs 239-82.el8_10.19
systemd-pam 239-82.el8_10.19
tzdata 2026e-1.el8_10
util-linux 2.32.1-48.el8_10
uwsgi 2.0.28-2.el8ap
xmlsec1 1.2.25-8.el8_10
xmlsec1-openssl 1.2.25-8.el8_10
xz-libs 5.2.4-4.el8_6
zlib 1.2.11-25.el8
```

</details>

<details><summary>Python packages: /usr (python3.12) (67)</summary>

```text
aap-gateway 2.5.20260923
argon2-cffi 23.1.0
argon2-cffi-bindings 21.2.0
asgiref 3.11.1
attrs 22.2.0
certifi 2023.5.7
cffi 2.0.0
charset-normalizer 3.3.0
cryptography 46.0.7
defusedxml 0.7.1
Django 5.2.17
django-ansible-base 2.5.20260422
django-auth-ldap 4.0.0
django-crum 0.7.9
django-dynamic-preferences 1.16.0
django-extensions 4.1
django-flags 5.0.13
django-oauth-toolkit 2.3.0
django-redis 5.4.0
djangorestframework 3.15.1
drf-spectacular 0.29.0
dynaconf 3.2.11
googleapis-common-protos 1.72.0
grpcio 1.71.2
grpcio-tools 1.71.2
idna 3.4
inflection 0.5.1
isodate 0.6.1
jsonschema 4.21.1
jsonschema-specifications 2023.12.1
jwcrypto 1.5.7
ldap-filter 1.0.1
lxml 5.3.0
netaddr 1.2.1
oauthlib 3.2.2
opentelemetry-proto 1.28.0
persisting-theory 1.0
ply 3.11
protobuf 5.29.6
psycopg 3.2.7
pyasn1 0.6.4
pyasn1-modules 0.4.2
pycparser 2.20
PyJWT 2.13.0
pyrad 2.4
python-ldap 3.4.5
python3-openid 3.2.0
python3-saml 1.16.0
PyYAML 6.0.1
redis 4.6.0
referencing 0.36.2
requests 2.31.0
requests-oauthlib 1.3.1
rpds-py 0.18.1
setuptools 68.2.2
six 1.17.0
social-auth-app-django 5.4.1
social-auth-core 4.5.4
sqlparse 0.6.0
supervisor 4.2.5
tabulate 0.9.0
tacacs-plus 2.6
typing_extensions 4.15.0
uritemplate 4.1.1
urllib3 2.7.0
xds-protos 1.71.2
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
| Labels `version` / `release` | `4.10.19` / `1791896186` |
| Image ID | `sha256:9e3128df630e3d39e0d2ec610b1ae94808ef67c112137a8a1482dfafdf45beac` |
| Build date | 2026-10-14T01:53:18Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | 3.12 |
| Ansible Core | 2.16.19 |

<details><summary>RPM packages (358)</summary>

```text
acl 2.4.0-1.el8_10
ansible-automation-platform-common 2.5-2.el8ap
ansible-automation-platform-selinux 0.2-3.el8ap
ansible-builder 3.1.1-1.2.el8ap
ansible-core 2.16.19-1.el8ap
ansible-lint 26.1.1-1.el8ap
ansible-test 2.16.19-1.el8ap
audit-libs 3.1.2-1.el8_10.1
automation-hub 4.10.19-1.el8ap
basesystem 11-5.el8
bash 4.4.20-6.el8_10
bindep 2.13.0-2.el8ap
brotli 1.0.6-4.el8_10
bzip2-libs 1.0.6-28.el8_10
ca-certificates 2025.2.80_v9.0.304-80.2.el8_10
chkconfig 1.19.2-1.el8
container-selinux 2.229.0-3.module+el8.10.0+24790+ef71b018
containers-common 1-82.module+el8.10.0+24790+ef71b018
coreutils-single 8.30-21.el8_10
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crypto-policies 20230731-1.git3177e06.el8
cryptsetup-libs 2.3.7-7.el8
curl 7.61.1-34.el8_10.13
cyrus-sasl-lib 2.1.27-6.el8_5
dbus 1.12.8-28.el8_10
dbus-common 1.12.8-28.el8_10
dbus-daemon 1.12.8-28.el8_10
dbus-libs 1.12.8-28.el8_10
dbus-tools 1.12.8-28.el8_10
device-mapper 1.02.181-15.el8_10.3
device-mapper-libs 1.02.181-15.el8_10.3
diffutils 3.6-6.el8
elfutils-default-yama-scope 0.190-2.el8
elfutils-libelf 0.190-2.el8
elfutils-libs 0.190-2.el8
expat 2.5.0-4.el8_10
file-libs 5.33-27.el8_10
filesystem 3.8-6.el8
gawk 4.2.1-5.el8_10
gdbm 1.18-2.el8
gdbm-libs 1.18-2.el8
git-core 2.43.7-1.el8_10
glib2 2.56.4-178.el8_10
glibc 2.28-251.el8_10.48
glibc-common 2.28-251.el8_10.48
glibc-minimal-langpack 2.28-251.el8_10.48
gmp 6.1.2-11.el8
gnupg2 2.2.20-4.el8_10
gnutls 3.6.16-8.el8_10.6
gobject-introspection 1.56.1-2.el8_10
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
gzip 1.9-15.el8_10
info 6.5-7.el8
jq 1.6-12.el8_10
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
kmod-libs 25-20.el8
krb5-libs 1.18.2-34.el8_10
langpacks-en 1.0-12.el8
less 530-3.el8_10
libacl 2.4.0-1.el8_10
libarchive 3.3.3-7.el8_10
libassuan 2.5.1-3.el8
libattr 2.6.0-1.el8_10
libblkid 2.32.1-48.el8_10
libcap 2.48-6.el8_10.1
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-7.el8_10
libcurl 7.61.1-34.el8_10.13
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-21.el8_10
libedit 3.1-23.20170329cvs.el8
libestr 0.1.10-3.el8
libfastjson 0.99.9-2.el8
libfdisk 2.32.1-48.el8_10
libffi 3.1-24.el8
libgcc 8.5.0-29.el8_10
libgcrypt 1.8.5-8.el8_10
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libjpeg-turbo 1.5.3-14.el8_10
libksba 1.3.5-9.el8_7
libmodulemd 2.13.0-1.el8
libmount 2.32.1-48.el8_10
libnghttp2 1.33.0-6.el8_10.3
libnsl2 1.2.0-2.20180605git4a062cf.el8
libpeas 1.22.0-6.el8
libpq 13.23-2.el8_10
libpsl 0.20.2-6.el8
libpwquality 1.4.4-6.el8
librepo 1.14.2-5.el8
librhsm 0.0.3-5.el8
libseccomp 2.5.2-1.el8
libsecret 0.18.6-1.el8
libselinux 2.9-11.el8_10
libselinux-utils 2.9-11.el8_10
libsemanage 2.9-12.el8_10
libsepol 2.9-3.el8
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-48.el8_10
libsolv 0.7.20-7.el8_10
libssh 0.9.6-17.el8_10
libssh-config 0.9.6-17.el8_10
libstdc++ 8.5.0-29.el8_10
libtasn1 4.13-6.el8_10
libtirpc 1.1.4-12.el8_10
libunistring 0.9.9-3.el8
libusbx 1.0.30-1.el8_10
libutempter 1.1.6-14.el8
libuuid 2.32.1-48.el8_10
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-21.el8_10.10
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
logrotate 3.14.0-6.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-5.el8_10
mailcap 2.1.48-3.el8
microdnf 3.8.0-2.el8
mpdecimal 2.5.1-3.el8
mpfr 3.1.6-1.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
npth 1.5-4.el8
oniguruma 6.9.7.1-2.el8ap
openldap 2.4.46-21.el8_10
openssh 8.0p1-33.el8_10
openssh-clients 8.0p1-33.el8_10
openssl 1.1.1k-17.el8_6
openssl-libs 1.1.1k-17.el8_6
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-40.el8_10
pcre 8.42-6.el8
pcre2 10.32-4.el8_10
pinentry 1.1.0-2.el8
platform-python 3.6.8-78.el8_10
platform-python-setuptools 39.2.0-9.el8_10
policycoreutils 2.9-26.el8_10
popt 1.18-1.el8
publicsuffix-list-dafsa 20180723-1.el8
pulpcore-selinux 2.0.1-2.el8ap
python3-cffi 1.11.5-6.el8
python3-chardet 3.0.4-7.el8
python3-cryptography 3.2.1-8.el8_10
python3-idna 2.5-8.el8_10
python3-libs 3.6.8-78.el8_10
python3-pip-wheel 9.0.3-24.el8
python3-ply 3.9-9.el8
python3-pycparser 2.14-14.el8
python3-pysocks 1.6.8-3.el8
python3-requests 2.20.0-6.el8_10
python3-setuptools 39.2.0-9.el8_10
python3-setuptools-wheel 39.2.0-9.el8_10
python3-six 1.11.0-8.el8
python3-urllib3 1.24.2-10.el8_10
python3.12 3.12.15-2.el8_10
python3.12-aiodns 3.2.0-2.el8ap
python3.12-aiofiles 23.2.1-2.el8ap
python3.12-aiohappyeyeballs 2.6.1-1.el8ap
python3.12-aiohttp 3.14.3-1.el8ap
python3.12-aiosignal 1.4.0-1.el8ap
python3.12-ansible-compat 25.12.0-3.el8ap
python3.12-asgiref 3.11.1-1.el8ap
python3.12-asyncio-throttle 1.0.2-5.el8ap
python3.12-attrs 22.2.0-2.el8ap
python3.12-azure-core 1.34.0-2.el8ap
python3.12-azure-storage-blob 12.19.0-2.el8ap
python3.12-backoff 2.2.1-2.el8ap
python3.12-black 26.3.1-1.el8ap
python3.12-boto3 1.34.30-2.el8ap
python3.12-botocore 1.34.162-2.el8ap
python3.12-bracex 2.4-2.el8ap
python3.12-brotli 1.2.0-1.el8ap
python3.12-certifi 2023.5.7-2.el8ap
python3.12-cffi 2.0.0-1.el8ap
python3.12-charset-normalizer 3.3.0-2.el8
python3.12-click 8.3.3-1.el8ap
python3.12-cryptography 46.0.7-1.el8ap
python3.12-dateutil 2.8.2-3.el8ap
python3.12-defusedxml 0.7.1-5.el8ap
python3.12-deprecated 1.2.14-2.el8ap
python3.12-diff-match-patch 20230430-2.el8ap
python3.12-distro 1.9.0-2.el8ap
python3.12-django 5.2.17-1.el8ap
python3.12-django-ansible-base 2.5.20260422-2.el8ap
python3.12-django-ansible-base+feature_flags 2.5.20260422-2.el8ap
python3.12-django-ansible-base+jwt_consumer 2.5.20260422-2.el8ap
python3.12-django-auth-ldap 4.0.0-3.el8ap
python3.12-django-crum 0.7.9-3.el8ap
python3.12-django-filter 25.2-1.el8ap
python3.12-django-flags 5.0.13-2.el8ap
python3.12-django-guid 3.4.0-2.el8ap
python3.12-django-import-export 3.3.6-3.el8ap
python3.12-django-ipware 3.0.7-4.el8ap
python3.12-django-lifecycle 1.1.2-2.el8ap
python3.12-django-picklefield 3.1-2.el8ap
python3.12-django-prometheus 2.3.1-3.el8ap
python3.12-django-storages 1.14.2-3.el8ap
python3.12-django-storages+azure 1.14.2-3.el8ap
python3.12-django-storages+s3 1.14.2-3.el8ap
python3.12-djangorestframework 3.15.1-2.el8ap
python3.12-djangorestframework-queryfields 1.1.0-2.el8ap
python3.12-drf-access-policy 1.5.0-2.el8ap
python3.12-drf-nested-routers 0.93.5-2.el8ap
python3.12-drf-spectacular 0.29.0-1.el8ap
python3.12-dynaconf 3.2.11-2.el8ap
python3.12-et-xmlfile 1.1.0-4.el8ap
python3.12-filelock 3.13.1-2.el8ap
python3.12-flake8 6.1.0-3.el8ap
python3.12-frozenlist 1.4.0-2.el8ap
python3.12-galaxy-importer 0.4.38-1.el8ap
python3.12-galaxy-ng 4.10.19-1.el8ap
python3.12-gitdb 4.0.11-2.el8ap
python3.12-gitpython 3.1.60-1.el8ap
python3.12-gnupg 0.5.2-2.el8ap
python3.12-googleapis-common-protos 1.72.0-1.el8ap
python3.12-grpcio 1.71.2-1.el8ap
python3.12-gunicorn 23.0.0-2.el8ap
python3.12-idna 3.4-2.el8
python3.12-importlib-metadata 6.0.1-3.el8ap
python3.12-inflection 0.5.1-5.el8ap
python3.12-insights-analytics-collector 0.3.2-3.el8ap
python3.12-isodate 0.6.1-3.el8ap
python3.12-jinja2 3.1.6-2.el8ap
python3.12-jmespath 1.0.1-3.el8ap
python3.12-jq 1.6.0-2.el8ap
python3.12-json-stream 2.3.2-2.el8ap
python3.12-json-stream-rs-tokenizer 0.4.26-2.el8ap
python3.12-jsonschema 4.21.1-2.el8ap
python3.12-jsonschema-specifications 2023.12.1-2.el8ap
python3.12-ldap 3.4.5-1.el8ap
python3.12-libs 3.12.15-2.el8_10
python3.12-markdown 3.10.2-1.el8ap
python3.12-markuppy 1.14-5.el8ap
python3.12-markupsafe 2.1.5-2.el8ap
python3.12-marshmallow 3.26.2-1.el8ap
python3.12-mccabe 0.7.0-3.el8ap
python3.12-multidict 6.0.4-2.el8ap
python3.12-mypy-extensions 1.0.0-2.el8ap
python3.12-nh3 0.2.18-2.el8ap
python3.12-oauthlib 3.2.2-2.el8ap
python3.12-odfpy 1.4.1-9.el8ap
python3.12-openpyxl 3.1.2-2.el8ap
python3.12-opentelemetry-api 1.28.0-1.el8ap
python3.12-opentelemetry-distro 0.49b0-1.el8ap
python3.12-opentelemetry-distro+otlp 0.49b0-1.el8ap
python3.12-opentelemetry-exporter-otlp 1.28.0-1.el8ap
python3.12-opentelemetry-exporter-otlp-proto-common 1.28.0-1.el8ap
python3.12-opentelemetry-exporter-otlp-proto-grpc 1.28.0-1.el8ap
python3.12-opentelemetry-exporter-otlp-proto-http 1.28.0-1.el8ap
python3.12-opentelemetry-instrumentation 0.49b0-1.el8ap
python3.12-opentelemetry-instrumentation-django 0.49b0-1.el8ap
python3.12-opentelemetry-instrumentation-wsgi 0.49b0-1.el8ap
python3.12-opentelemetry-proto 1.28.0-1.el8ap
python3.12-opentelemetry-sdk 1.28.0-1.el8ap
python3.12-opentelemetry-semantic-conventions 0.49b0-1.el8ap
python3.12-opentelemetry-util-http 0.49b0-1.el8ap
python3.12-packaging 23.2-2.el8
python3.12-parsley 1.3-4.el8ap
python3.12-pathspec 1.0.4-1.el8ap
python3.12-pbr 6.0.0-3.el8ap
python3.12-pillow 12.3.0-1.el8ap
python3.12-pip-wheel 23.2.1-4.el8
python3.12-platformdirs 4.2.0-2.el8ap
python3.12-ply 3.11-2.el8
python3.12-prometheus-client 0.19.0-2.el8ap
python3.12-propcache 0.4.1-1.el8ap
python3.12-protobuf 5.29.6-1.el8ap
python3.12-psycopg 3.2.7-2.el8ap
python3.12-pulp-ansible 0.25.6-1.el8ap
python3.12-pulp-container 2.19.12-1.el8ap
python3.12-pulp-glue 0.23.2-2.el8ap
python3.12-pulpcore 3.49.66-1.el8ap
python3.12-pyOpenSSL 26.0.0-1.el8ap
python3.12-pyasn1 0.6.4-1.el8ap
python3.12-pyasn1-modules 0.4.2-1.el8ap
python3.12-pycares 4.4.0-3.el8ap
python3.12-pycodestyle 2.11.1-2.el8ap
python3.12-pycparser 2.20-2.el8
python3.12-pyflakes 3.1.0-2.el8ap
python3.12-pygtrie 2.5.0-3.el8ap
python3.12-pyjwt 2.13.0-1.el8ap
python3.12-pyjwt+crypto 2.13.0-1.el8ap
python3.12-pyparsing 3.1.1-2.el8ap
python3.12-pysequoia 0.1.34-1.el8ap
python3.12-python3-openid 3.2.0-4.el8ap
python3.12-pytokens 0.4.1-1.el8ap
python3.12-pyyaml 6.0.1-2.el8
python3.12-redis 4.6.0-3.el8ap
python3.12-referencing 0.36.2-3.el8ap
python3.12-requests 2.31.0-4.el8ap
python3.12-requests-oauthlib 1.3.1-2.el8ap
python3.12-resolvelib 1.0.1-2.el8ap
python3.12-rpds-py 0.18.1-3.el8ap
python3.12-ruamel-yaml 0.18.15-2.el8ap
python3.12-ruamel-yaml-clib 0.2.15-2.el8ap
python3.12-s3transfer 0.10.0-2.el8ap
python3.12-semantic-version 2.10.0-3.el8ap
python3.12-setuptools 68.2.2-5.el8_10
python3.12-six 1.17.0-1.el8ap
python3.12-smmap 5.0.1-2.el8ap
python3.12-social-auth-app-django 5.4.1-2.el8ap
python3.12-social-auth-core 4.5.4-2.el8ap
python3.12-sqlparse 0.6.0-1.el8ap
python3.12-subprocess-tee 0.4.2-2.el8ap
python3.12-tablib 3.5.0-2.el8ap
python3.12-tablib+html 3.5.0-2.el8ap
python3.12-tablib+ods 3.5.0-2.el8ap
python3.12-tablib+xls 3.5.0-2.el8ap
python3.12-tablib+xlsx 3.5.0-2.el8ap
python3.12-tablib+yaml 3.5.0-2.el8ap
python3.12-typing-extensions 4.15.0-2.el8ap
python3.12-uritemplate 4.1.1-4.el8ap
python3.12-url-normalize 1.4.3-6.el8ap
python3.12-urllib3 2.7.0-1.el8ap
python3.12-uuid6 2024.1.12-2.el8ap
python3.12-wcmatch 8.5-2.el8ap
python3.12-whitenoise 6.6.0-2.el8ap
python3.12-wrapt 1.16.0-2.el8ap
python3.12-xlrd 2.0.1-7.el8ap
python3.12-xlwt 1.3.0-5.el8ap
python3.12-yarl 1.18.3-1.el8ap
python3.12-zipp 3.19.2-2.el8ap
readline 7.0-10.el8
redhat-release 8.10-0.3.el8
rootfiles 8.1-22.el8
rpm 4.14.3-32.el8_10
rpm-libs 4.14.3-32.el8_10
rpm-plugin-selinux 4.14.3-32.el8_10
rsyslog 8.2102.0-15.el8_10.3
runc 1.2.9-6.module+el8.10.0+24790+ef71b018
sed 4.5-5.el8_10
selinux-policy 3.14.3-139.el8_10.2
selinux-policy-targeted 3.14.3-139.el8_10.2
setup 2.12.2-9.el8
shadow-utils 4.6-23.el8_10
skopeo 1.14.6-4.module+el8.10.0+24790+ef71b018
sos 4.11.2-4.el8_10
sqlite-libs 3.26.0-21.el8_10
sshpass 1.09-5.el8ap
systemd 239-82.el8_10.19
systemd-libs 239-82.el8_10.19
systemd-pam 239-82.el8_10.19
tar 1.30-13.el8_10
tzdata 2026e-1.el8_10
util-linux 2.32.1-48.el8_10
xz-libs 5.2.4-4.el8_6
yamllint 1.38.0-1.el8ap
zlib 1.2.11-25.el8
```

</details>

<details><summary>Python packages: /usr (python3.12) (159)</summary>

```text
aiodns 3.2.0
aiofiles 23.2.1
aiohappyeyeballs 2.6.1
aiohttp 3.14.3
aiosignal 1.4.0
ansible-builder 3.1.1
ansible-compat 25.12.0
ansible-core 2.16.19
ansible-lint 26.1.1
asgiref 3.11.1
asyncio-throttle 1.0.2
attrs 22.2.0
azure-core 1.34.0
azure-storage-blob 12.19.0
backoff 2.2.1
bindep 2.13.0
black 26.3.1
boto3 1.34.30
botocore 1.34.162
bracex 2.4
Brotli 1.2.0
certifi 2023.5.7
cffi 2.0.0
charset-normalizer 3.3.0
click 8.3.3
cryptography 46.0.7
defusedxml 0.7.1
Deprecated 1.2.14
diff-match-patch 20230430
distro 1.9.0
Django 5.2.17
django-ansible-base 2.5.20260422
django-auth-ldap 4.0.0
django-crum 0.7.9
django-filter 25.2
django-flags 5.0.13
django-guid 3.4.0
django-import-export 3.3.6
django-ipware 3.0.7
django-lifecycle 1.1.2
django-picklefield 3.1
django-prometheus 2.3.1
django-storages 1.14.2
djangorestframework 3.15.1
djangorestframework-queryfields 1.1.0
drf-access-policy 1.5.0
drf-nested-routers 0.93.5
drf-spectacular 0.29.0
dynaconf 3.2.11
et-xmlfile 1.1.0
filelock 3.13.1
flake8 6.1.0
frozenlist 1.4.0
galaxy-importer 0.4.38
galaxy-ng 4.10.19
gitdb 4.0.11
GitPython 3.1.60
googleapis-common-protos 1.72.0
grpcio 1.71.2
gunicorn 23.0.0
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
Markdown 3.10.2
MarkupPy 1.14
MarkupSafe 2.1.5
marshmallow 3.26.2
mccabe 0.7.0
multidict 6.0.4
mypy-extensions 1.0.0
nh3 0.2.18
oauthlib 3.2.2
odfpy 1.4.1
openpyxl 3.1.2
opentelemetry-api 1.28.0
opentelemetry-distro 0.49b0
opentelemetry-exporter-otlp 1.28.0
opentelemetry-exporter-otlp-proto-common 1.28.0
opentelemetry-exporter-otlp-proto-grpc 1.28.0
opentelemetry-exporter-otlp-proto-http 1.28.0
opentelemetry-instrumentation 0.49b0
opentelemetry-instrumentation-django 0.49b0
opentelemetry-instrumentation-wsgi 0.49b0
opentelemetry-proto 1.28.0
opentelemetry-sdk 1.28.0
opentelemetry-semantic-conventions 0.49b0
opentelemetry-util-http 0.49b0
packaging 23.2
Parsley 1.3
pathspec 1.0.4
pbr 6.0.0
pillow 12.3.0
platformdirs 4.2.0
ply 3.11
prometheus-client 0.19.0
propcache 0.4.1
protobuf 5.29.6
psycopg 3.2.7
pulp-ansible 0.25.6
pulp-container 2.19.12
pulp-glue 0.23.2
pulpcore 3.49.66
pyasn1 0.6.4
pyasn1-modules 0.4.2
pycares 4.4.0
pycodestyle 2.11.1
pycparser 2.20
pyflakes 3.1.0
pygtrie 2.5.0
PyJWT 2.13.0
pyOpenSSL 26.0.0
pyparsing 3.1.1
pysequoia 0.1.34
python-dateutil 2.8.2
python-gnupg 0.5.2
python-ldap 3.4.5
python3-openid 3.2.0
pytokens 0.4.1
PyYAML 6.0.1
redis 4.6.0
referencing 0.36.2
requests 2.31.0
requests-oauthlib 1.3.1
resolvelib 1.0.1
rpds-py 0.18.1
ruamel.yaml 0.18.15
ruamel.yaml.clib 0.2.15
s3transfer 0.10.0
semantic-version 2.10.0
setuptools 68.2.2
six 1.17.0
smmap 5.0.1
social-auth-app-django 5.4.1
social-auth-core 4.5.4
sqlparse 0.6.0
subprocess-tee 0.4.2
tablib 3.5.0
typing_extensions 4.15.0
uritemplate 4.1.1
url-normalize 1.4.3
urllib3 2.7.0
uuid6 2024.1.12
wcmatch 8.5
whitenoise 6.6.0
wrapt 1.16.0
xlrd 2.0.1
xlwt 1.3.0
yamllint 1.38.0
yarl 1.18.3
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
sos 4.11.2
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
| Labels `version` / `release` | `4.10.19` / `1791940460` |
| Image ID | `sha256:45142072ef32fde6e24f778e2b19d20288ad844a7931f193aa835630b8cc6945` |
| Build date | 2026-10-14T07:54:27Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | N/A |
| Ansible Core | N/A |

<details><summary>RPM packages (277)</summary>

```text
acl 2.4.0-1.el8_10
audit-libs 3.1.2-1.el8_10.1
basesystem 11-5.el8
bash 4.4.20-6.el8_10
bind-libs 9.11.36-16.el8_10.16
bind-libs-lite 9.11.36-16.el8_10.16
bind-license 9.11.36-16.el8_10.16
bind-utils 9.11.36-16.el8_10.16
brotli 1.0.6-4.el8_10
bsdtar 3.3.3-7.el8_10
bzip2-libs 1.0.6-28.el8_10
ca-certificates 2025.2.80_v9.0.304-80.2.el8_10
chkconfig 1.19.2-1.el8
cmake 3.26.5-2.el8
cmake-data 3.26.5-2.el8
cmake-filesystem 3.26.5-2.el8
cmake-rpm-macros 3.26.5-2.el8
coreutils-single 8.30-21.el8_10
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crypto-policies 20230731-1.git3177e06.el8
crypto-policies-scripts 20230731-1.git3177e06.el8
cryptsetup-libs 2.3.7-7.el8
curl 7.61.1-34.el8_10.13
cyrus-sasl-lib 2.1.27-6.el8_5
dbus 1.12.8-28.el8_10
dbus-common 1.12.8-28.el8_10
dbus-daemon 1.12.8-28.el8_10
dbus-glib 0.110-2.el8
dbus-libs 1.12.8-28.el8_10
dbus-tools 1.12.8-28.el8_10
device-mapper 1.02.181-15.el8_10.3
device-mapper-libs 1.02.181-15.el8_10.3
dmidecode 3.5-1.el8
dnf 4.7.0-21.el8_10
dnf-data 4.7.0-21.el8_10
dnf-plugin-subscription-manager 1.28.44-1.el8_10
elfutils-default-yama-scope 0.190-2.el8
elfutils-libelf 0.190-2.el8
elfutils-libs 0.190-2.el8
emacs-filesystem 26.1-15.el8_10.2
environment-modules 4.5.2-4.el8
expat 2.5.0-4.el8_10
file-libs 5.33-27.el8_10
filesystem 3.8-6.el8
findutils 4.6.0-24.el8_10
fstrm 0.6.1-3.el8
gawk 4.2.1-5.el8_10
gdb-gdbserver 8.2-20.1.el8_10
gdbm 1.18-2.el8
gdbm-libs 1.18-2.el8
geolite2-city 20180605-1.el8
geolite2-country 20180605-1.el8
gettext 0.19.8.1-17.el8
gettext-libs 0.19.8.1-17.el8
glib2 2.56.4-178.el8_10
glibc 2.28-251.el8_10.48
glibc-common 2.28-251.el8_10.48
glibc-langpack-en 2.28-251.el8_10.48
glibc-locale-source 2.28-251.el8_10.48
glibc-minimal-langpack 2.28-251.el8_10.48
gmp 6.1.2-11.el8
gnupg2 2.2.20-4.el8_10
gnutls 3.6.16-8.el8_10.6
gobject-introspection 1.56.1-2.el8_10
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
groff-base 1.22.3-18.el8
gzip 1.9-15.el8_10
hostname 3.20-6.el8
ima-evm-utils 1.3.2-12.el8
info 6.5-7.el8
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
kmod-libs 25-20.el8
krb5-libs 1.18.2-34.el8_10
langpacks-en 1.0-12.el8
less 530-3.el8_10
libacl 2.4.0-1.el8_10
libarchive 3.3.3-7.el8_10
libassuan 2.5.1-3.el8
libattr 2.6.0-1.el8_10
libblkid 2.32.1-48.el8_10
libcap 2.48-6.el8_10.1
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-7.el8_10
libcomps 0.1.18-1.el8
libcroco 0.6.12-4.el8_2.1
libcurl 7.61.1-34.el8_10.13
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-21.el8_10
libfdisk 2.32.1-48.el8_10
libffi 3.1-24.el8
libgcc 8.5.0-29.el8_10
libgcrypt 1.8.5-8.el8_10
libgomp 8.5.0-29.el8_10
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libksba 1.3.5-9.el8_7
libmaxminddb 1.2.0-10.el8_9.1
libmodulemd 2.13.0-1.el8
libmount 2.32.1-48.el8_10
libnghttp2 1.33.0-6.el8_10.3
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
libselinux 2.9-11.el8_10
libsemanage 2.9-12.el8_10
libsepol 2.9-3.el8
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-48.el8_10
libsolv 0.7.20-7.el8_10
libssh 0.9.6-17.el8_10
libssh-config 0.9.6-17.el8_10
libstdc++ 8.5.0-29.el8_10
libtasn1 4.13-6.el8_10
libtirpc 1.1.4-12.el8_10
libunistring 0.9.9-3.el8
libusbx 1.0.30-1.el8_10
libuser 0.62-26.el8_10
libutempter 1.1.6-14.el8
libuuid 2.32.1-48.el8_10
libuv 1.41.1-2.el8_10
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-21.el8_10.10
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-5.el8_10
make 4.2.1-11.el8
man-db 2.7.6.1-18.el8
mpfr 3.1.6-1.el8
ncurses 6.1-10.20180224.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
nginx 1.24.0-3.module+el8.10.0+24848+0300f002.5
nginx-filesystem 1.24.0-3.module+el8.10.0+24848+0300f002.5
nginx-mod-http-perl 1.24.0-3.module+el8.10.0+24848+0300f002.5
nginx-mod-stream 1.24.0-3.module+el8.10.0+24848+0300f002.5
npth 1.5-4.el8
nss_wrapper 1.1.13-1.el8
nss_wrapper-libs 1.1.13-1.el8
openldap 2.4.46-21.el8_10
openssl 1.1.1k-17.el8_6
openssl-libs 1.1.1k-17.el8_6
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-40.el8_10
passwd 0.80-4.el8
pcre 8.42-6.el8
pcre2 10.32-4.el8_10
perl-Carp 1.42-396.el8
perl-Data-Dumper 2.167-399.el8
perl-Digest 1.17-395.el8
perl-Digest-MD5 2.55-396.el8
perl-Encode 2.97-3.el8
perl-Errno 1.28-423.el8_10.1
perl-Exporter 5.72-396.el8
perl-File-Path 2.15-2.el8
perl-File-Temp 0.230.600-1.el8
perl-Getopt-Long 2.50-4.el8
perl-HTTP-Tiny 0.074-3.el8
perl-IO 1.38-423.el8_10.1
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
perl-interpreter 5.26.3-423.el8_10.1
perl-libnet 3.11-3.el8
perl-libs 5.26.3-423.el8_10.1
perl-macros 5.26.3-423.el8_10.1
perl-parent 0.237-1.el8
perl-podlators 4.11-1.el8
perl-threads 2.21-2.el8
perl-threads-shared 1.58-2.el8
pkgconf 1.4.2-1.el8
pkgconf-m4 1.4.2-1.el8
pkgconf-pkg-config 1.4.2-1.el8
platform-python 3.6.8-78.el8_10
platform-python-setuptools 39.2.0-9.el8_10
popt 1.18-1.el8
procps-ng 3.3.15-14.el8
protobuf-c 1.3.0-8.el8
publicsuffix-list-dafsa 20180723-1.el8
python3-bind 9.11.36-16.el8_10.16
python3-chardet 3.0.4-7.el8
python3-cloud-what 1.28.44-1.el8_10
python3-dateutil 2.6.1-6.el8
python3-dbus 1.2.4-15.el8
python3-decorator 4.2.1-2.el8
python3-dnf 4.7.0-21.el8_10
python3-dnf-plugins-core 4.0.21-25.el8
python3-ethtool 0.14-5.el8
python3-gobject-base 3.28.3-2.el8
python3-gpg 1.13.1-12.el8
python3-hawkey 0.63.0-21.el8_10
python3-idna 2.5-8.el8_10
python3-iniparse 0.4-31.el8
python3-inotify 0.9.6-13.el8
python3-libcomps 0.1.18-1.el8
python3-libdnf 0.63.0-21.el8_10
python3-librepo 1.14.2-5.el8
python3-libs 3.6.8-78.el8_10
python3-pip-wheel 9.0.3-24.el8
python3-ply 3.9-9.el8
python3-pysocks 1.6.8-3.el8
python3-requests 2.20.0-6.el8_10
python3-rpm 4.14.3-32.el8_10
python3-setuptools-wheel 39.2.0-9.el8_10
python3-six 1.11.0-8.el8
python3-subscription-manager-rhsm 1.28.44-1.el8_10
python3-syspurpose 1.28.44-1.el8_10
python3-systemd 234-8.el8
python3-urllib3 1.24.2-10.el8_10
readline 7.0-10.el8
redhat-logos-httpd 810.1-1.el8_10
redhat-release 8.10-0.3.el8
rootfiles 8.1-22.el8
rpm 4.14.3-32.el8_10
rpm-build-libs 4.14.3-32.el8_10
rpm-libs 4.14.3-32.el8_10
rsync 3.1.3-28.el8_10
scl-utils 2.0.2-16.el8
sed 4.5-5.el8_10
setup 2.12.2-9.el8
shadow-utils 4.6-23.el8_10
sqlite-libs 3.26.0-21.el8_10
subscription-manager 1.28.44-1.el8_10
subscription-manager-rhsm-certificates 20220623-1.el8
systemd 239-82.el8_10.19
systemd-libs 239-82.el8_10.19
systemd-pam 239-82.el8_10.19
tar 1.30-13.el8_10
tcl 8.6.8-2.el8
tpm2-tss 2.3.2-6.el8
tzdata 2026e-1.el8_10
unzip 6.0-48.el8_10
usermode 1.113-2.el8
util-linux 2.32.1-48.el8_10
vim-filesystem 8.0.1763-32.el8_10
vim-minimal 8.0.1763-32.el8_10
virt-what 1.25-4.el8
which 2.21-21.el8_10
xz 5.2.4-4.el8_6
xz-libs 5.2.4-4.el8_6
yum 4.7.0-21.el8_10
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
subscription-manager 1.28.44
syspurpose 1.28.44
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
| Labels `version` / `release` | `1.6.8` / `1791896186` |
| Image ID | `sha256:c3bf16344f1dcd114aa569868b5a684d0643545f0e26eb32ebd59474486fc4d6` |
| Build date | 2026-10-14T01:13:54Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | 3.12 |
| Ansible Core | N/A |

<details><summary>RPM packages (170)</summary>

```text
acl 2.4.0-1.el8_10
ansible-runner 2.4.2-3.el8ap
audit-libs 3.1.2-1.el8_10.1
basesystem 11-5.el8
bash 4.4.20-6.el8_10
brotli 1.0.6-4.el8_10
bzip2-libs 1.0.6-28.el8_10
ca-certificates 2025.2.80_v9.0.304-80.2.el8_10
chkconfig 1.19.2-1.el8
coreutils-single 8.30-21.el8_10
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crypto-policies 20230731-1.git3177e06.el8
cryptsetup-libs 2.3.7-7.el8
curl 7.61.1-34.el8_10.13
cyrus-sasl-lib 2.1.27-6.el8_5
dbus 1.12.8-28.el8_10
dbus-common 1.12.8-28.el8_10
dbus-daemon 1.12.8-28.el8_10
dbus-libs 1.12.8-28.el8_10
dbus-tools 1.12.8-28.el8_10
device-mapper 1.02.181-15.el8_10.3
device-mapper-libs 1.02.181-15.el8_10.3
diffutils 3.6-6.el8
dumb-init 1.2.5-3.el8ap
elfutils-default-yama-scope 0.190-2.el8
elfutils-libelf 0.190-2.el8
elfutils-libs 0.190-2.el8
expat 2.5.0-4.el8_10
file-libs 5.33-27.el8_10
filesystem 3.8-6.el8
gawk 4.2.1-5.el8_10
gdbm 1.18-2.el8
gdbm-libs 1.18-2.el8
glib2 2.56.4-178.el8_10
glibc 2.28-251.el8_10.48
glibc-common 2.28-251.el8_10.48
glibc-minimal-langpack 2.28-251.el8_10.48
gmp 6.1.2-11.el8
gnupg2 2.2.20-4.el8_10
gnutls 3.6.16-8.el8_10.6
gobject-introspection 1.56.1-2.el8_10
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
gzip 1.9-15.el8_10
info 6.5-7.el8
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
kmod-libs 25-20.el8
krb5-libs 1.18.2-34.el8_10
langpacks-en 1.0-12.el8
libacl 2.4.0-1.el8_10
libarchive 3.3.3-7.el8_10
libassuan 2.5.1-3.el8
libattr 2.6.0-1.el8_10
libblkid 2.32.1-48.el8_10
libcap 2.48-6.el8_10.1
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-7.el8_10
libcurl 7.61.1-34.el8_10.13
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-21.el8_10
libfdisk 2.32.1-48.el8_10
libffi 3.1-24.el8
libgcc 8.5.0-29.el8_10
libgcrypt 1.8.5-8.el8_10
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libksba 1.3.5-9.el8_7
libmodulemd 2.13.0-1.el8
libmount 2.32.1-48.el8_10
libnghttp2 1.33.0-6.el8_10.3
libnsl2 1.2.0-2.20180605git4a062cf.el8
libpeas 1.22.0-6.el8
libpsl 0.20.2-6.el8
libpwquality 1.4.4-6.el8
librepo 1.14.2-5.el8
librhsm 0.0.3-5.el8
libseccomp 2.5.2-1.el8
libselinux 2.9-11.el8_10
libselinux-utils 2.9-11.el8_10
libsemanage 2.9-12.el8_10
libsepol 2.9-3.el8
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-48.el8_10
libsolv 0.7.20-7.el8_10
libssh 0.9.6-17.el8_10
libssh-config 0.9.6-17.el8_10
libstdc++ 8.5.0-29.el8_10
libtasn1 4.13-6.el8_10
libtirpc 1.1.4-12.el8_10
libunistring 0.9.9-3.el8
libusbx 1.0.30-1.el8_10
libutempter 1.1.6-14.el8
libuuid 2.32.1-48.el8_10
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-21.el8_10.10
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
logrotate 3.14.0-6.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-5.el8_10
microdnf 3.8.0-2.el8
mpdecimal 2.5.1-3.el8
mpfr 3.1.6-1.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
npth 1.5-4.el8
openldap 2.4.46-21.el8_10
openssl-libs 1.1.1k-17.el8_6
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-40.el8_10
pcre 8.42-6.el8
pcre2 10.32-4.el8_10
platform-python 3.6.8-78.el8_10
platform-python-setuptools 39.2.0-9.el8_10
podman-remote 4.9.4-37.module+el8.10.0+24790+ef71b018
policycoreutils 2.9-26.el8_10
popt 1.18-1.el8
publicsuffix-list-dafsa 20180723-1.el8
python3-chardet 3.0.4-7.el8
python3-idna 2.5-8.el8_10
python3-libs 3.6.8-78.el8_10
python3-pip-wheel 9.0.3-24.el8
python3-pysocks 1.6.8-3.el8
python3-requests 2.20.0-6.el8_10
python3-setuptools 39.2.0-9.el8_10
python3-setuptools-wheel 39.2.0-9.el8_10
python3-six 1.11.0-8.el8
python3-urllib3 1.24.2-10.el8_10
python3.12 3.12.15-2.el8_10
python3.12-ansible-runner 2.4.2-3.el8ap
python3.12-click 8.3.3-1.el8ap
python3.12-daemon 3.1.2-3.el8ap
python3.12-dateutil 2.8.2-3.el8ap
python3.12-libs 3.12.15-2.el8_10
python3.12-lockfile 0.12.2-3.el8ap
python3.12-packaging 23.2-2.el8
python3.12-pexpect 4.9.0-2.el8ap
python3.12-pip-wheel 23.2.1-4.el8
python3.12-ptyprocess 0.7.0-2.el8ap
python3.12-pyyaml 6.0.1-2.el8
python3.12-six 1.17.0-1.el8ap
readline 7.0-10.el8
receptor 1.6.8-1.el8ap
receptorctl 1.6.8-1.el8ap
redhat-release 8.10-0.3.el8
rootfiles 8.1-22.el8
rpm 4.14.3-32.el8_10
rpm-libs 4.14.3-32.el8_10
sed 4.5-5.el8_10
setup 2.12.2-9.el8
shadow-utils 4.6-23.el8_10
shadow-utils-subid 4.6-23.el8_10
sos 4.11.2-4.el8_10
sqlite-libs 3.26.0-21.el8_10
systemd 239-82.el8_10.19
systemd-libs 239-82.el8_10.19
systemd-pam 239-82.el8_10.19
tzdata 2026e-1.el8_10
util-linux 2.32.1-48.el8_10
xz-libs 5.2.4-4.el8_6
zlib 1.2.11-25.el8
```

</details>

<details><summary>Python packages: /usr (python3.12) (11)</summary>

```text
ansible-runner 2.4.2
click 8.3.3
lockfile 0.12.2
packaging 23.2
pexpect 4.9.0
ptyprocess 0.7.0
python-daemon 3.1.2
python-dateutil 2.8.2
PyYAML 6.0.1
receptorctl 1.6.8
six 1.17.0
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
sos 4.11.2
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
| Labels `version` / `release` | `5` / `1791892845` |
| Image ID | `sha256:82b3d5ca8cee53d378b8c9ddac0a1106ec0ed5d635ae73a0c4a94259bd5da44d` |
| Build date | 2026-10-13T12:01:38Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | 3.6 |
| Ansible Core | N/A |

<details><summary>RPM packages (215)</summary>

```text
acl 2.4.0-1.el8_10
audit-libs 3.1.2-1.el8_10.1
avahi-libs 0.7-27.el8_10.1
basesystem 11-5.el8
bash 4.4.20-6.el8_10
brotli 1.0.6-4.el8_10
bzip2-libs 1.0.6-28.el8_10
ca-certificates 2025.2.80_v9.0.304-80.2.el8_10
chkconfig 1.19.2-1.el8
coreutils-single 8.30-21.el8_10
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crypto-policies 20230731-1.git3177e06.el8
crypto-policies-scripts 20230731-1.git3177e06.el8
cryptsetup-libs 2.3.7-7.el8
curl 7.61.1-34.el8_10.13
cyrus-sasl-lib 2.1.27-6.el8_5
dbus 1.12.8-28.el8_10
dbus-common 1.12.8-28.el8_10
dbus-daemon 1.12.8-28.el8_10
dbus-glib 0.110-2.el8
dbus-libs 1.12.8-28.el8_10
dbus-tools 1.12.8-28.el8_10
device-mapper 1.02.181-15.el8_10.3
device-mapper-libs 1.02.181-15.el8_10.3
diffutils 3.6-6.el8
dmidecode 3.5-1.el8
dnf 4.7.0-21.el8_10
dnf-data 4.7.0-21.el8_10
dnf-plugin-subscription-manager 1.28.44-1.el8_10
elfutils-default-yama-scope 0.190-2.el8
elfutils-libelf 0.190-2.el8
elfutils-libs 0.190-2.el8
expat 2.5.0-4.el8_10
file-libs 5.33-27.el8_10
filesystem 3.8-6.el8
findutils 4.6.0-24.el8_10
gawk 4.2.1-5.el8_10
gdb-gdbserver 8.2-20.1.el8_10
gdbm 1.18-2.el8
gdbm-libs 1.18-2.el8
gettext 0.19.8.1-17.el8
gettext-libs 0.19.8.1-17.el8
glib2 2.56.4-178.el8_10
glibc 2.28-251.el8_10.48
glibc-common 2.28-251.el8_10.48
glibc-minimal-langpack 2.28-251.el8_10.48
gmp 6.1.2-11.el8
gnupg2 2.2.20-4.el8_10
gnutls 3.6.16-8.el8_10.6
gobject-introspection 1.56.1-2.el8_10
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
gzip 1.9-15.el8_10
hostname 3.20-6.el8
ima-evm-utils 1.3.2-12.el8
info 6.5-7.el8
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
kmod-libs 25-20.el8
krb5-libs 1.18.2-34.el8_10
langpacks-en 1.0-12.el8
libacl 2.4.0-1.el8_10
libarchive 3.3.3-7.el8_10
libassuan 2.5.1-3.el8
libattr 2.6.0-1.el8_10
libblkid 2.32.1-48.el8_10
libcap 2.48-6.el8_10.1
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-7.el8_10
libcomps 0.1.18-1.el8
libcroco 0.6.12-4.el8_2.1
libcurl 7.61.1-34.el8_10.13
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-21.el8_10
libfdisk 2.32.1-48.el8_10
libffi 3.1-24.el8
libgcc 8.5.0-29.el8_10
libgcrypt 1.8.5-8.el8_10
libgomp 8.5.0-29.el8_10
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libksba 1.3.5-9.el8_7
libmodulemd 2.13.0-1.el8
libmount 2.32.1-48.el8_10
libnghttp2 1.33.0-6.el8_10.3
libnl3 3.7.0-1.el8
libnsl2 1.2.0-2.20180605git4a062cf.el8
libpsl 0.20.2-6.el8
libpwquality 1.4.4-6.el8
librepo 1.14.2-5.el8
libreport-filesystem 2.9.5-15.el8
librhsm 0.0.3-5.el8
libseccomp 2.5.2-1.el8
libselinux 2.9-11.el8_10
libsemanage 2.9-12.el8_10
libsepol 2.9-3.el8
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-48.el8_10
libsolv 0.7.20-7.el8_10
libssh 0.9.6-17.el8_10
libssh-config 0.9.6-17.el8_10
libstdc++ 8.5.0-29.el8_10
libtasn1 4.13-6.el8_10
libtirpc 1.1.4-12.el8_10
libunistring 0.9.9-3.el8
libusbx 1.0.30-1.el8_10
libuser 0.62-26.el8_10
libutempter 1.1.6-14.el8
libuuid 2.32.1-48.el8_10
libuv 1.41.1-2.el8_10
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-21.el8_10.10
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-5.el8_10
mpfr 3.1.6-1.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
npth 1.5-4.el8
nspr 4.39.0-3.el8_10
nss 3.124.0-5.el8_10
nss-softokn 3.124.0-5.el8_10
nss-softokn-freebl 3.124.0-5.el8_10
nss-sysinit 3.124.0-5.el8_10
nss-util 3.124.0-5.el8_10
openldap 2.4.46-21.el8_10
openssl-libs 1.1.1k-17.el8_6
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-40.el8_10
passwd 0.80-4.el8
pcp 5.3.7-22.el8_10.5
pcp-conf 5.3.7-22.el8_10.5
pcp-doc 5.3.7-22.el8_10.5
pcp-libs 5.3.7-22.el8_10.5
pcp-pmda-dm 5.3.7-22.el8_10.5
pcp-pmda-nfsclient 5.3.7-22.el8_10.5
pcp-pmda-openmetrics 5.3.7-22.el8_10.5
pcp-system-tools 5.3.7-22.el8_10.5
pcp-zeroconf 5.3.7-22.el8_10.5
pcre 8.42-6.el8
pcre2 10.32-3.el8_6
platform-python 3.6.8-78.el8_10
platform-python-pip 9.0.3-24.el8
platform-python-setuptools 39.2.0-9.el8_10
popt 1.18-1.el8
procps-ng 3.3.15-14.el8
publicsuffix-list-dafsa 20180723-1.el8
python3-chardet 3.0.4-7.el8
python3-cloud-what 1.28.44-1.el8_10
python3-dateutil 2.6.1-6.el8
python3-dbus 1.2.4-15.el8
python3-decorator 4.2.1-2.el8
python3-dnf 4.7.0-21.el8_10
python3-dnf-plugins-core 4.0.21-25.el8
python3-ethtool 0.14-5.el8
python3-gobject-base 3.28.3-2.el8
python3-gpg 1.13.1-12.el8
python3-hawkey 0.63.0-21.el8_10
python3-idna 2.5-8.el8_10
python3-iniparse 0.4-31.el8
python3-inotify 0.9.6-13.el8
python3-libcomps 0.1.18-1.el8
python3-libdnf 0.63.0-21.el8_10
python3-librepo 1.14.2-5.el8
python3-libs 3.6.8-78.el8_10
python3-pcp 5.3.7-22.el8_10.5
python3-pip 9.0.3-24.el8
python3-pip-wheel 9.0.3-24.el8
python3-pysocks 1.6.8-3.el8
python3-requests 2.20.0-6.el8_10
python3-rpm 4.14.3-32.el8_10
python3-setuptools 39.2.0-9.el8_10
python3-setuptools-wheel 39.2.0-9.el8_10
python3-six 1.11.0-8.el8
python3-subscription-manager-rhsm 1.28.44-1.el8_10
python3-syspurpose 1.28.44-1.el8_10
python3-systemd 234-8.el8
python3-urllib3 1.24.2-10.el8_10
python36 3.6.8-39.module+el8.10.0+20784+edafcd43
readline 7.0-10.el8
redhat-release 8.10-0.3.el8
rootfiles 8.1-22.el8
rpm 4.14.3-32.el8_10
rpm-build-libs 4.14.3-32.el8_10
rpm-libs 4.14.3-32.el8_10
sed 4.5-5.el8_10
setup 2.12.2-9.el8
shadow-utils 4.6-23.el8_10
sqlite-libs 3.26.0-21.el8_10
subscription-manager 1.28.44-1.el8_10
subscription-manager-rhsm-certificates 20220623-1.el8
systemd 239-82.el8_10.19
systemd-libs 239-82.el8_10.19
systemd-pam 239-82.el8_10.19
tar 1.30-13.el8_10
tpm2-tss 2.3.2-6.el8
tzdata 2026e-1.el8_10
usermode 1.113-2.el8
util-linux 2.32.1-48.el8_10
vim-minimal 8.0.1763-32.el8_10
virt-what 1.25-4.el8
which 2.21-21.el8_10
xz 5.2.4-4.el8_6
xz-libs 5.2.4-4.el8_6
yum 4.7.0-21.el8_10
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
subscription-manager 1.28.44
syspurpose 1.28.44
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
| Labels `version` / `release` | `1` / `1792399398` |
| Image ID | `sha256:d71c594803121971c207b7454d8bfd0b53d8dde92254fa5d2150fc039aa006a4` |
| Build date | 2026-10-19T08:44:16Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | N/A |
| Ansible Core | N/A |

<details><summary>RPM packages (280)</summary>

```text
acl 2.4.0-1.el8_10
audit-libs 3.1.2-1.el8_10.1
basesystem 11-5.el8
bash 4.4.20-6.el8_10
bind-libs 9.11.36-16.el8_10.16
bind-libs-lite 9.11.36-16.el8_10.16
bind-license 9.11.36-16.el8_10.16
bind-utils 9.11.36-16.el8_10.16
brotli 1.0.6-4.el8_10
bsdtar 3.3.3-7.el8_10
bzip2-libs 1.0.6-28.el8_10
ca-certificates 2025.2.80_v9.0.304-80.2.el8_10
chkconfig 1.19.2-1.el8
cmake 3.26.5-2.el8
cmake-data 3.26.5-2.el8
cmake-filesystem 3.26.5-2.el8
cmake-rpm-macros 3.26.5-2.el8
coreutils-single 8.30-21.el8_10
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crypto-policies 20230731-1.git3177e06.el8
crypto-policies-scripts 20230731-1.git3177e06.el8
cryptsetup-libs 2.3.7-7.el8
curl 7.61.1-34.el8_10.13
cyrus-sasl-lib 2.1.27-6.el8_5
dbus 1.12.8-28.el8_10
dbus-common 1.12.8-28.el8_10
dbus-daemon 1.12.8-28.el8_10
dbus-glib 0.110-2.el8
dbus-libs 1.12.8-28.el8_10
dbus-tools 1.12.8-28.el8_10
device-mapper 1.02.181-15.el8_10.3
device-mapper-libs 1.02.181-15.el8_10.3
dmidecode 3.5-1.el8
dnf 4.7.0-21.el8_10
dnf-data 4.7.0-21.el8_10
dnf-plugin-subscription-manager 1.28.44-1.el8_10
elfutils-default-yama-scope 0.190-2.el8
elfutils-libelf 0.190-2.el8
elfutils-libs 0.190-2.el8
emacs-filesystem 26.1-15.el8_10.2
environment-modules 4.5.2-4.el8
expat 2.5.0-4.el8_10
file-libs 5.33-27.el8_10
filesystem 3.8-6.el8
findutils 4.6.0-24.el8_10
fstrm 0.6.1-3.el8
gawk 4.2.1-5.el8_10
gdb-gdbserver 8.2-20.1.el8_10
gdbm 1.18-2.el8
gdbm-libs 1.18-2.el8
geolite2-city 20180605-1.el8
geolite2-country 20180605-1.el8
gettext 0.19.8.1-17.el8
gettext-libs 0.19.8.1-17.el8
glib2 2.56.4-178.el8_10
glibc 2.28-251.el8_10.48
glibc-common 2.28-251.el8_10.48
glibc-langpack-en 2.28-251.el8_10.48
glibc-locale-source 2.28-251.el8_10.48
glibc-minimal-langpack 2.28-251.el8_10.48
gmp 6.1.2-11.el8
gnupg2 2.2.20-4.el8_10
gnutls 3.6.16-8.el8_10.6
gobject-introspection 1.56.1-2.el8_10
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
groff-base 1.22.3-18.el8
gzip 1.9-15.el8_10
ima-evm-utils 1.3.2-12.el8
info 6.5-7.el8
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
kmod-libs 25-20.el8
krb5-libs 1.18.2-34.el8_10
langpacks-en 1.0-12.el8
less 530-3.el8_10
libacl 2.4.0-1.el8_10
libarchive 3.3.3-7.el8_10
libassuan 2.5.1-3.el8
libattr 2.6.0-1.el8_10
libblkid 2.32.1-48.el8_10
libcap 2.48-6.el8_10.1
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-7.el8_10
libcomps 0.1.18-1.el8
libcroco 0.6.12-4.el8_2.1
libcurl 7.61.1-34.el8_10.13
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-21.el8_10
libfdisk 2.32.1-48.el8_10
libffi 3.1-24.el8
libgcc 8.5.0-29.el8_10
libgcrypt 1.8.5-8.el8_10
libgomp 8.5.0-29.el8_10
libgpg-error 1.31-1.el8
libicu 60.3-2.el8_1
libidn2 2.2.0-1.el8
libksba 1.3.5-9.el8_7
libmaxminddb 1.2.0-10.el8_9.1
libmodulemd 2.13.0-1.el8
libmount 2.32.1-48.el8_10
libnghttp2 1.33.0-6.el8_10.3
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
libselinux 2.9-11.el8_10
libsemanage 2.9-12.el8_10
libsepol 2.9-3.el8
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-48.el8_10
libsolv 0.7.20-7.el8_10
libssh 0.9.6-17.el8_10
libssh-config 0.9.6-17.el8_10
libstdc++ 8.5.0-29.el8_10
libtasn1 4.13-6.el8_10
libtirpc 1.1.4-12.el8_10
libunistring 0.9.9-3.el8
libusbx 1.0.30-1.el8_10
libuser 0.62-26.el8_10
libutempter 1.1.6-14.el8
libuuid 2.32.1-48.el8_10
libuv 1.41.1-2.el8_10
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-21.el8_10.10
libxslt 1.1.32-6.4.el8_10
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-5.el8_10
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
openldap 2.4.46-21.el8_10
openssl 1.1.1k-17.el8_6
openssl-libs 1.1.1k-17.el8_6
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-40.el8_10
passwd 0.80-4.el8
pcre 8.42-6.el8
pcre2 10.32-4.el8_10
perl-Carp 1.42-396.el8
perl-Data-Dumper 2.167-399.el8
perl-Digest 1.17-395.el8
perl-Digest-MD5 2.55-396.el8
perl-Encode 2.97-3.el8
perl-Errno 1.28-423.el8_10.1
perl-Exporter 5.72-396.el8
perl-File-Path 2.15-2.el8
perl-File-Temp 0.230.600-1.el8
perl-Getopt-Long 2.50-4.el8
perl-HTTP-Tiny 0.074-3.el8
perl-IO 1.38-423.el8_10.1
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
perl-URI 1.73-4.el8_10
perl-Unicode-Normalize 1.25-396.el8
perl-constant 1.33-396.el8
perl-interpreter 5.26.3-423.el8_10.1
perl-libnet 3.11-3.el8
perl-libs 5.26.3-423.el8_10.1
perl-macros 5.26.3-423.el8_10.1
perl-parent 0.237-1.el8
perl-podlators 4.11-1.el8
perl-threads 2.21-2.el8
perl-threads-shared 1.58-2.el8
pgaudit 1.7.0-1.module+el8.9.0+19797+c4ce5969
pkgconf 1.4.2-1.el8
pkgconf-m4 1.4.2-1.el8
pkgconf-pkg-config 1.4.2-1.el8
platform-python 3.6.8-78.el8_10
platform-python-setuptools 39.2.0-9.el8_10
popt 1.18-1.el8
postgresql 15.19-1.module+el8.10.0+24831+9c841e4e
postgresql-contrib 15.19-1.module+el8.10.0+24831+9c841e4e
postgresql-private-libs 15.19-1.module+el8.10.0+24831+9c841e4e
postgresql-server 15.19-1.module+el8.10.0+24831+9c841e4e
postgresql-upgrade 15.19-1.module+el8.10.0+24831+9c841e4e
procps-ng 3.3.15-14.el8
protobuf-c 1.3.0-8.el8
publicsuffix-list-dafsa 20180723-1.el8
python3-bind 9.11.36-16.el8_10.16
python3-chardet 3.0.4-7.el8
python3-cloud-what 1.28.44-1.el8_10
python3-dateutil 2.6.1-6.el8
python3-dbus 1.2.4-15.el8
python3-decorator 4.2.1-2.el8
python3-dnf 4.7.0-21.el8_10
python3-dnf-plugins-core 4.0.21-25.el8
python3-ethtool 0.14-5.el8
python3-gobject-base 3.28.3-2.el8
python3-gpg 1.13.1-12.el8
python3-hawkey 0.63.0-21.el8_10
python3-idna 2.5-8.el8_10
python3-iniparse 0.4-31.el8
python3-inotify 0.9.6-13.el8
python3-libcomps 0.1.18-1.el8
python3-libdnf 0.63.0-21.el8_10
python3-librepo 1.14.2-5.el8
python3-libs 3.6.8-78.el8_10
python3-pip-wheel 9.0.3-24.el8
python3-ply 3.9-9.el8
python3-pysocks 1.6.8-3.el8
python3-requests 2.20.0-6.el8_10
python3-rpm 4.14.3-32.el8_10
python3-setuptools-wheel 39.2.0-9.el8_10
python3-six 1.11.0-8.el8
python3-subscription-manager-rhsm 1.28.44-1.el8_10
python3-syspurpose 1.28.44-1.el8_10
python3-systemd 234-8.el8
python3-urllib3 1.24.2-10.el8_10
readline 7.0-10.el8
redhat-release 8.10-0.3.el8
rootfiles 8.1-22.el8
rpm 4.14.3-32.el8_10
rpm-build-libs 4.14.3-32.el8_10
rpm-libs 4.14.3-32.el8_10
rsync 3.1.3-28.el8_10
scl-utils 2.0.2-16.el8
sed 4.5-5.el8_10
setup 2.12.2-9.el8
shadow-utils 4.6-23.el8_10
sqlite-libs 3.26.0-21.el8_10
subscription-manager 1.28.44-1.el8_10
subscription-manager-rhsm-certificates 20220623-1.el8
systemd 239-82.el8_10.19
systemd-libs 239-82.el8_10.19
systemd-pam 239-82.el8_10.19
tar 1.30-13.el8_10
tcl 8.6.8-2.el8
tpm2-tss 2.3.2-6.el8
tzdata 2026e-1.el8_10
unzip 6.0-48.el8_10
usermode 1.113-2.el8
util-linux 2.32.1-48.el8_10
uuid 1.6.2-43.el8
vim-filesystem 8.0.1763-32.el8_10
vim-minimal 8.0.1763-32.el8_10
virt-what 1.25-4.el8
which 2.21-21.el8_10
xz 5.2.4-4.el8_6
xz-libs 5.2.4-4.el8_6
yum 4.7.0-21.el8_10
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
subscription-manager 1.28.44
syspurpose 1.28.44
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
| Labels `version` / `release` | `1` / `1791943921` |
| Image ID | `sha256:702ccfad8b3b61bda08f657885ada5dbc58c971e34bab2930347f89390b77381` |
| Build date | 2026-10-14T02:12:44Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 8.10 (Ootpa) |
| Python | N/A |
| Ansible Core | N/A |

<details><summary>RPM packages (208)</summary>

```text
acl 2.4.0-1.el8_10
audit-libs 3.1.2-1.el8_10.1
basesystem 11-5.el8
bash 4.4.20-6.el8_10
brotli 1.0.6-4.el8_10
bsdtar 3.3.3-7.el8_10
bzip2-libs 1.0.6-28.el8_10
ca-certificates 2025.2.80_v9.0.304-80.2.el8_10
chkconfig 1.19.2-1.el8
coreutils-single 8.30-21.el8_10
cracklib 2.9.6-15.el8
cracklib-dicts 2.9.6-15.el8
crypto-policies 20230731-1.git3177e06.el8
crypto-policies-scripts 20230731-1.git3177e06.el8
cryptsetup-libs 2.3.7-7.el8
curl 7.61.1-34.el8_10.13
cyrus-sasl-lib 2.1.27-6.el8_5
dbus 1.12.8-28.el8_10
dbus-common 1.12.8-28.el8_10
dbus-daemon 1.12.8-28.el8_10
dbus-glib 0.110-2.el8
dbus-libs 1.12.8-28.el8_10
dbus-tools 1.12.8-28.el8_10
device-mapper 1.02.181-15.el8_10.3
device-mapper-libs 1.02.181-15.el8_10.3
diffutils 3.6-6.el8
dmidecode 3.5-1.el8
dnf 4.7.0-21.el8_10
dnf-data 4.7.0-21.el8_10
dnf-plugin-subscription-manager 1.28.44-1.el8_10
elfutils-default-yama-scope 0.190-2.el8
elfutils-libelf 0.190-2.el8
elfutils-libs 0.190-2.el8
environment-modules 4.5.2-4.el8
expat 2.5.0-4.el8_10
file-libs 5.33-27.el8_10
filesystem 3.8-6.el8
findutils 4.6.0-24.el8_10
gawk 4.2.1-5.el8_10
gdb-gdbserver 8.2-20.1.el8_10
gdbm 1.18-2.el8
gdbm-libs 1.18-2.el8
gettext 0.19.8.1-17.el8
gettext-libs 0.19.8.1-17.el8
glib2 2.56.4-178.el8_10
glibc 2.28-251.el8_10.48
glibc-common 2.28-251.el8_10.48
glibc-langpack-en 2.28-251.el8_10.48
glibc-locale-source 2.28-251.el8_10.48
glibc-minimal-langpack 2.28-251.el8_10.48
gmp 6.1.2-11.el8
gnupg2 2.2.20-4.el8_10
gnutls 3.6.16-8.el8_10.6
gobject-introspection 1.56.1-2.el8_10
gpg-pubkey d4082792-5b32db75
gpg-pubkey fd431d51-4ae0493b
gpgme 1.13.1-12.el8
grep 3.1-6.el8
groff-base 1.22.3-18.el8
gzip 1.9-15.el8_10
ima-evm-utils 1.3.2-12.el8
info 6.5-7.el8
json-c 0.13.1-3.el8
json-glib 1.4.4-1.el8
keyutils-libs 1.5.10-9.el8
kmod-libs 25-20.el8
krb5-libs 1.18.2-34.el8_10
langpacks-en 1.0-12.el8
less 530-3.el8_10
libacl 2.4.0-1.el8_10
libarchive 3.3.3-7.el8_10
libassuan 2.5.1-3.el8
libattr 2.6.0-1.el8_10
libblkid 2.32.1-48.el8_10
libcap 2.48-6.el8_10.1
libcap-ng 0.7.11-1.el8
libcom_err 1.45.6-7.el8_10
libcomps 0.1.18-1.el8
libcroco 0.6.12-4.el8_2.1
libcurl 7.61.1-34.el8_10.13
libdb 5.3.28-42.el8_4
libdb-utils 5.3.28-42.el8_4
libdnf 0.63.0-21.el8_10
libfdisk 2.32.1-48.el8_10
libffi 3.1-24.el8
libgcc 8.5.0-29.el8_10
libgcrypt 1.8.5-8.el8_10
libgomp 8.5.0-29.el8_10
libgpg-error 1.31-1.el8
libidn2 2.2.0-1.el8
libksba 1.3.5-9.el8_7
libmodulemd 2.13.0-1.el8
libmount 2.32.1-48.el8_10
libnghttp2 1.33.0-6.el8_10.3
libnl3 3.7.0-1.el8
libnsl2 1.2.0-2.20180605git4a062cf.el8
libpipeline 1.5.0-2.el8
libpsl 0.20.2-6.el8
libpwquality 1.4.4-6.el8
librepo 1.14.2-5.el8
libreport-filesystem 2.9.5-15.el8
librhsm 0.0.3-5.el8
libseccomp 2.5.2-1.el8
libselinux 2.9-11.el8_10
libselinux-utils 2.9-11.el8_10
libsemanage 2.9-12.el8_10
libsepol 2.9-3.el8
libsigsegv 2.11-5.el8
libsmartcols 2.32.1-48.el8_10
libsolv 0.7.20-7.el8_10
libssh 0.9.6-17.el8_10
libssh-config 0.9.6-17.el8_10
libstdc++ 8.5.0-29.el8_10
libtasn1 4.13-6.el8_10
libtirpc 1.1.4-12.el8_10
libunistring 0.9.9-3.el8
libusbx 1.0.30-1.el8_10
libuser 0.62-26.el8_10
libutempter 1.1.6-14.el8
libuuid 2.32.1-48.el8_10
libverto 0.3.2-2.el8
libxcrypt 4.1.1-6.el8
libxml2 2.9.7-21.el8_10.10
libyaml 0.1.7-5.el8
libzstd 1.4.4-1.el8
logrotate 3.14.0-6.el8
lua-libs 5.3.4-12.el8
lz4-libs 1.8.3-5.el8_10
man-db 2.7.6.1-18.el8
mpfr 3.1.6-1.el8
ncurses-base 6.1-10.20180224.el8
ncurses-libs 6.1-10.20180224.el8
nettle 3.4.1-7.el8
npth 1.5-4.el8
openldap 2.4.46-21.el8_10
openssl-libs 1.1.1k-17.el8_6
p11-kit 0.23.22-2.el8
p11-kit-trust 0.23.22-2.el8
pam 1.3.1-40.el8_10
passwd 0.80-4.el8
pcre 8.42-6.el8
pcre2 10.32-4.el8_10
platform-python 3.6.8-78.el8_10
platform-python-setuptools 39.2.0-9.el8_10
policycoreutils 2.9-26.el8_10
popt 1.18-1.el8
procps-ng 3.3.15-14.el8
publicsuffix-list-dafsa 20180723-1.el8
python3-chardet 3.0.4-7.el8
python3-cloud-what 1.28.44-1.el8_10
python3-dateutil 2.6.1-6.el8
python3-dbus 1.2.4-15.el8
python3-decorator 4.2.1-2.el8
python3-dnf 4.7.0-21.el8_10
python3-dnf-plugins-core 4.0.21-25.el8
python3-ethtool 0.14-5.el8
python3-gobject-base 3.28.3-2.el8
python3-gpg 1.13.1-12.el8
python3-hawkey 0.63.0-21.el8_10
python3-idna 2.5-8.el8_10
python3-iniparse 0.4-31.el8
python3-inotify 0.9.6-13.el8
python3-libcomps 0.1.18-1.el8
python3-libdnf 0.63.0-21.el8_10
python3-librepo 1.14.2-5.el8
python3-libs 3.6.8-78.el8_10
python3-pip-wheel 9.0.3-24.el8
python3-pysocks 1.6.8-3.el8
python3-requests 2.20.0-6.el8_10
python3-rpm 4.14.3-32.el8_10
python3-setuptools-wheel 39.2.0-9.el8_10
python3-six 1.11.0-8.el8
python3-subscription-manager-rhsm 1.28.44-1.el8_10
python3-syspurpose 1.28.44-1.el8_10
python3-systemd 234-8.el8
python3-urllib3 1.24.2-10.el8_10
readline 7.0-10.el8
redhat-release 8.10-0.3.el8
redis 6.2.24-1.module+el8.10.0+24746+7b800ac5
rootfiles 8.1-22.el8
rpm 4.14.3-32.el8_10
rpm-build-libs 4.14.3-32.el8_10
rpm-libs 4.14.3-32.el8_10
rsync 3.1.3-28.el8_10
scl-utils 2.0.2-16.el8
sed 4.5-5.el8_10
setup 2.12.2-9.el8
shadow-utils 4.6-23.el8_10
sqlite-libs 3.26.0-21.el8_10
subscription-manager 1.28.44-1.el8_10
subscription-manager-rhsm-certificates 20220623-1.el8
systemd 239-82.el8_10.19
systemd-libs 239-82.el8_10.19
systemd-pam 239-82.el8_10.19
tar 1.30-13.el8_10
tcl 8.6.8-2.el8
tpm2-tss 2.3.2-6.el8
tzdata 2026e-1.el8_10
unzip 6.0-48.el8_10
usermode 1.113-2.el8
util-linux 2.32.1-48.el8_10
vim-minimal 8.0.1763-32.el8_10
virt-what 1.25-4.el8
which 2.21-21.el8_10
xz 5.2.4-4.el8_6
xz-libs 5.2.4-4.el8_6
yum 4.7.0-21.el8_10
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
subscription-manager 1.28.44
syspurpose 1.28.44
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

<details><summary>Bundled collections (81)</summary>

```text
amazon.aws 9.2.0 (certified)
ansible.controller 4.6.34 (certified)
ansible.eda 2.10.0 (certified)
ansible.hub 1.0.0 (certified)
ansible.netcommon 7.1.0 (certified)
ansible.network 4.0.0 (certified)
ansible.platform 2.5.20260306 (certified)
ansible.posix 1.5.4 (certified)
ansible.scm 3.0.0 (certified)
ansible.security 3.0.0 (certified)
ansible.snmp 3.0.0 (certified)
ansible.utils 5.1.2 (certified)
ansible.windows 3.4.0 (certified)
ansible.yang 3.0.0 (certified)
arista.eos 10.0.1 (certified)
azure.azcollection 2.5.0 (certified)
cisco.asa 6.0.0 (certified)
cisco.ios 9.1.1 (certified)
cisco.iosxr 10.3.0 (certified)
cisco.nxos 9.3.0 (certified)
cloud.aws_ops 3.0.0 (validated)
cloud.aws_troubleshooting 3.0.0 (validated)
cloud.azure_ops 4.0.1 (validated)
cloud.common 4.0.0 (certified)
cloud.gcp_ops 2.0.0 (validated)
cloud.terraform 3.0.0 (certified)
cloud.terraform_ops 1.0.0 (validated)
cloud.vmware_ops 1.5.1 (validated)
edge.microshift 1.0.3 (validated)
frr.frr 2.0.2 (certified)
ibm.qradar 4.0.0 (certified)
infra.aap_utilities 2.5.1 (validated)
infra.ah_configuration 2.0.6 (validated)
infra.ansible_rekey_variables 1.1.4 (validated)
infra.controller_configuration 2.9.0 (validated)
infra.convert2rhel 1.2.1 (validated)
infra.eda_configuration 1.1.0 (validated)
infra.ee_utilities 3.2.0 (validated)
infra.leapp 1.4.0 (validated)
infra.lvm_snapshots 2.1.0 (validated)
infra.middleware_ocpv 1.0.0 (validated)
infra.osbuild 2.3.0 (validated)
junipernetworks.junos 9.1.0 (certified)
kubernetes.core 5.4.0 (certified)
microsoft.ad 1.8.0 (certified)
network.acls 3.0.0 (validated)
network.backup 3.0.0 (validated)
network.base 6.0.0 (validated)
network.bgp 6.0.1 (validated)
network.interfaces 5.0.0 (validated)
network.ospf 5.0.0 (validated)
network.telemetry 3.0.0 (validated)
network.vpn 4.0.0 (validated)
openvswitch.openvswitch 2.1.1 (certified)
redhat.amq_broker 1.3.0 (certified)
redhat.amq_streams 1.0.0 (certified)
redhat.data_grid 1.3.1 (certified)
redhat.eap 1.3.1 (certified)
redhat.insights 1.3.0 (certified)
redhat.insights_eda 1.2.0 (certified)
redhat.jbcs 1.0.1 (certified)
redhat.jws 2.0.0 (certified)
redhat.openshift 4.0.2 (certified)
redhat.openshift_virtualization 1.5.0 (certified)
redhat.redhat_csp_download 1.2.2 (certified)
redhat.rhbk 2.2.2 (certified)
redhat.rhel_idm 1.10.0 (certified)
redhat.rhel_system_roles 1.95.7 (certified)
redhat.rhv 2.4.2 (certified)
redhat.runtimes_common 1.1.3 (certified)
redhat.sap_install 1.2.1 (certified)
redhat.satellite 3.15.0 (certified)
redhat.satellite_operations 3.0.0 (certified)
redhat.sso 1.3.0 (certified)
sap.sap_operations 1.0.4 (certified)
servicenow.itsm 2.6.3 (certified)
splunk.es 4.0.0 (certified)
trendmicro.deepsec 4.0.0 (certified)
vmware.vmware 1.10.1 (certified)
vmware.vmware_rest 4.6.0 (certified)
vyos.vyos 4.0.2 (certified)
```

</details>
