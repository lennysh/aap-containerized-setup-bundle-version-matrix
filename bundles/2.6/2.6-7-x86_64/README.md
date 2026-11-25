[All AAP versions](../../../README.md) / [AAP 2.6](../README.md) / 2.6-7

# AAP Containerized Setup Bundle 2.6-7 (x86_64)

- **Bundle file:** `ansible-automation-platform-containerized-setup-bundle-2.6-7-x86_64.tar.gz`
- **AAP version:** 2.6
- **Bundle created:** 2026-04-01 20:37:00 UTC
- **Container images:** 19
- **Distinct RPM package versions:** 447
- **Distinct Python package versions:** 887

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
  - [lightspeed-chatbot-rhel9](#lightspeed-chatbot-rhel9)
  - [lightspeed-rhel9](#lightspeed-rhel9)
  - [mcp-tools-rhel9](#mcp-tools-rhel9)
  - [receptor-rhel9](#receptor-rhel9)
  - [mcp-server-rhel9](#mcp-server-rhel9)
  - [metrics-service-rhel9](#metrics-service-rhel9)
  - [pcp](#pcp)
  - [postgresql-15](#postgresql-15)
  - [redis-6](#redis-6)
- [Installer Collections](#installer-collections)
- [Bundled Collections](#bundled-collections)

## Container Images

| Image | Tag in Bundle | Version | Release | Image ID | RHEL Version | Python | Ansible Core | RPMs | Python Pkgs | Collections |
|---|---|---|---|---|---|---|---|--:|--:|--:|
| [registry.redhat.io/ansible-automation-platform-26/controller-rhel9](#controller-rhel9) | `latest` | 4.7.10 | 1773939694 | `c1caed7cb747` | Red Hat Enterprise Linux 9.7 (Plow) | 3.9, 3.12 | N/A | 242 | 218 | 1 |
| [registry.redhat.io/ansible-automation-platform-26/de-supported-rhel9](#de-supported-rhel9) | `latest` | 1.2.2 | 1773939694 | `7b161bf90dc4` | Red Hat Enterprise Linux 9.7 (Plow) | 3.9, 3.12 | 2.16.18 | 159 | 62 | 4 |
| [registry.redhat.io/ansible-automation-platform-26/eda-controller-rhel9](#eda-controller-rhel9) | `latest` | 1.2.7 | 1773939694 | `9158edd8a3ed` | Red Hat Enterprise Linux 9.7 (Plow) | 3.12 | 2.16.15 | 137 | 108 | 0 |
| [registry.redhat.io/ansible-automation-platform-26/eda-controller-ui-rhel9](#eda-controller-ui-rhel9) | `latest` | 1.2.7 | 1774456665 | `94116fd7c04b` | Red Hat Enterprise Linux 9.7 (Plow) | 3.9 | N/A | 294 | 18 | 0 |
| [registry.redhat.io/ansible-automation-platform-26/ee-minimal-rhel9](#ee-minimal-rhel9) | `latest` | 2.0.0 | 1773939694 | `cbfbac206cd8` | Red Hat Enterprise Linux 9.7 (Plow) | 3.12 | 2.16.18 | 157 | 78 | 0 |
| [registry.redhat.io/ansible-automation-platform-26/ee-supported-rhel9](#ee-supported-rhel9) | `latest` | 2.0.0 | 1773939694 | `f9dc4651f821` | Red Hat Enterprise Linux 9.7 (Plow) | 3.9, 3.12 | 2.16.18 | 226 | 280 | 56 |
| [registry.redhat.io/ansible-automation-platform-26/gateway-proxy-rhel9](#gateway-proxy-rhel9) | `latest` | 2.6.6 | 1773939694 | `ed508370dd1f` | Red Hat Enterprise Linux 9.7 (Plow) | N/A | N/A | 113 | 0 | 0 |
| [registry.redhat.io/ansible-automation-platform-26/gateway-rhel9](#gateway-rhel9) | `latest` | 2.6.20260325 | 1773939694 | `3ac836ca923d` | Red Hat Enterprise Linux 9.7 (Plow) | 3.12 | N/A | 149 | 74 | 0 |
| [registry.redhat.io/ansible-automation-platform-26/hub-rhel9](#hub-rhel9) | `latest` | 4.11.7 | 1773939694 | `f6f7ac95f8bc` | Red Hat Enterprise Linux 9.7 (Plow) | 3.12 | 2.20.3 | 151 | 161 | 0 |
| [registry.redhat.io/ansible-automation-platform-26/hub-web-rhel9](#hub-web-rhel9) | `latest` | 4.11.7 | 1774456665 | `10966cc5ca43` | Red Hat Enterprise Linux 9.7 (Plow) | 3.9 | N/A | 294 | 18 | 0 |
| [registry.redhat.io/ansible-automation-platform-26/lightspeed-chatbot-rhel9](#lightspeed-chatbot-rhel9) | `latest` | 2.6 | 1773939694 | `cf3249a82b9a` | Red Hat Enterprise Linux 9.7 (Plow) | 3.12 | N/A | 139 | 127 | 0 |
| [registry.redhat.io/ansible-automation-platform-26/lightspeed-rhel9](#lightspeed-rhel9) | `latest` | 2.6.260325 | 1773939694 | `9dda2a029985` | Red Hat Enterprise Linux 9.7 (Plow) | 3.12 | 2.16.16 | 153 | 170 | 0 |
| [registry.redhat.io/ansible-automation-platform-26/mcp-tools-rhel9](#mcp-tools-rhel9) | `latest` | 2.6.250924 | 1773939694 | `891bb66c5e58` | Red Hat Enterprise Linux 9.7 (Plow) | 3.12 | N/A | 120 | 47 | 0 |
| [registry.redhat.io/ansible-automation-platform-26/receptor-rhel9](#receptor-rhel9) | `latest` | 1.6.4 | 1773939694 | `f6f72784e6e0` | Red Hat Enterprise Linux 9.7 (Plow) | 3.12 | N/A | 118 | 9 | 0 |
| [registry.redhat.io/ansible-automation-platform-tech-preview/mcp-server-rhel9](#mcp-server-rhel9) | `latest` | 2.6.20260325 | 1774226014 | `2ecee019a1d1` | Red Hat Enterprise Linux 9.7 (Plow) | N/A | N/A | 144 | 0 | 0 |
| [registry.redhat.io/ansible-automation-platform-tech-preview/metrics-service-rhel9](#metrics-service-rhel9) | `latest` | 0.0.1 | 1773939694 | `5826c35fd8a3` | Red Hat Enterprise Linux 9.7 (Plow) | 3.12 | N/A | 137 | 65 | 0 |
| [registry.redhat.io/rhel9/pcp](#pcp) | `latest` | 6 | 1774442196 | `0f8a38250dcb` | Red Hat Enterprise Linux 9.7 (Plow) | 3.9 | N/A | 212 | 19 | 0 |
| [registry.redhat.io/rhel9/postgresql-15](#postgresql-15) | `latest` | 1 | 1775009263 | `9d16ff88f306` | Red Hat Enterprise Linux 9.7 (Plow) | 3.9 | N/A | 280 | 18 | 0 |
| [registry.redhat.io/rhel9/redis-6](#redis-6) | `latest` | 1 | 1774456931 | `bb35dedffd27` | Red Hat Enterprise Linux 9.7 (Plow) | 3.9 | N/A | 210 | 18 | 0 |

## RPM Packages (all images)

Every RPM installed in any image of this bundle (`name version-release`). Search this table for a
package named in a CVE to see which containers ship which version.

| Package | Version-Release | Images |
|---|---|---|
| `acl` | `2.3.1-4.el9` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, gateway-rhel9, hub-web-rhel9, lightspeed-rhel9, mcp-server-rhel9, pcp, postgresql-15, redis-6 |
| `alsa-lib` | `1.2.14-1.el9` | de-supported-rhel9 |
| `alternatives` | `1.24-2.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `apr` | `1.7.0-12.el9_3` | controller-rhel9, ee-supported-rhel9 |
| `apr-util` | `1.6.1-23.el9` | controller-rhel9, ee-supported-rhel9 |
| `apr-util-bdb` | `1.6.1-23.el9` | controller-rhel9, ee-supported-rhel9 |
| `attr` | `2.5.1-3.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `audit-libs` | `3.1.5-7.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `automation-controller-cli` | `4.7.10-2.el9ap` | ee-supported-rhel9 |
| `automation-gateway-config` | `2.6.20260325-2.el9ap` | gateway-proxy-rhel9 |
| `automation-gateway-proxy-server` | `2.6.14-1.el9` | gateway-proxy-rhel9 |
| `avahi-libs` | `0.8-23.el9` | de-supported-rhel9, pcp |
| `basesystem` | `11-13.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `bash` | `5.1.8-9.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `bash-completion` | `2.11-5.el9` | ee-supported-rhel9 |
| `bind9.18-libs` | `9.18.29-5.el9_7.2` | postgresql-15 |
| `bind9.18-utils` | `9.18.29-5.el9_7.2` | postgresql-15 |
| `bsdtar` | `3.5.3-7.el9_7` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15, redis-6 |
| `bzip2` | `1.0.8-10.el9_5` | ee-minimal-rhel9, ee-supported-rhel9 |
| `bzip2-libs` | `1.0.8-10.el9_5` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `c-ares` | `1.19.1-2.el9_4` | controller-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9 |
| `ca-certificates` | `2024.2.69_v8.0.303-91.4.el9_4` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `containers-common` | `1-135.el9_7` | hub-rhel9 |
| `copy-jdk-configs` | `4.0-3.el9` | de-supported-rhel9 |
| `coreutils-single` | `8.32-39.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `cracklib` | `2.9.6-27.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `cracklib-dicts` | `2.9.6-27.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `crontabs` | `1.11-27.20190603git.el9_0` | controller-rhel9 |
| `crun` | `1.26-1.el9_7` | controller-rhel9, hub-rhel9 |
| `crypto-policies` | `20250905-1.git377cc42.el9_7` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `crypto-policies-scripts` | `20250905-1.git377cc42.el9_7` | de-supported-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `cups-libs` | `2.3.3op2-34.el9_7.2` | de-supported-rhel9 |
| `curl-minimal` | `7.76.1-35.el9_7.3` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `cyrus-sasl-lib` | `2.1.27-22.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `dbus` | `1.12.20-8.el9` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, gateway-rhel9, hub-web-rhel9, lightspeed-rhel9, mcp-server-rhel9, pcp, postgresql-15, redis-6 |
| `dbus-broker` | `28-7.el9` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, gateway-rhel9, hub-web-rhel9, lightspeed-rhel9, mcp-server-rhel9, pcp, postgresql-15, redis-6 |
| `dbus-common` | `1.12.20-8.el9` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, gateway-rhel9, hub-web-rhel9, lightspeed-rhel9, mcp-server-rhel9, pcp, postgresql-15, redis-6 |
| `dbus-libs` | `1.12.20-8.el9` | controller-rhel9, de-supported-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `dejavu-sans-fonts` | `2.37-18.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `device-mapper` | `1.02.206-2.el9_7.2` | pcp |
| `device-mapper-libs` | `1.02.206-2.el9_7.2` | pcp |
| `diffutils` | `3.7-12.el9` | ee-supported-rhel9, lightspeed-chatbot-rhel9, pcp, redis-6 |
| `dmidecode` | `3.6-1.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `dnf` | `4.14.0-31.el9` | eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `dnf-data` | `4.14.0-31.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `dumb-init` | `1.2.5-3.el9ap` | gateway-proxy-rhel9 |
| `elfutils-default-yama-scope` | `0.193-1.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `elfutils-libelf` | `0.193-1.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `elfutils-libs` | `0.193-1.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `environment-modules` | `5.3.0-2.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15, redis-6 |
| `expat` | `2.5.0-5.el9_7.1` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `file` | `5.39-16.el9` | ee-supported-rhel9 |
| `file-libs` | `5.39-16.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `filesystem` | `3.16-5.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `findutils` | `4.8.0-7.el9` | controller-rhel9, de-supported-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, hub-web-rhel9, mcp-server-rhel9, pcp, postgresql-15, redis-6 |
| `flexiblas` | `3.0.4-8.el9` | ee-supported-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9 |
| `flexiblas-netlib` | `3.0.4-8.el9` | ee-supported-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9 |
| `flexiblas-openblas-openmp` | `3.0.4-8.el9` | ee-supported-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9 |
| `fontconfig` | `2.14.0-2.el9_1` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `fonts-filesystem` | `2.0.5-7.el9.1` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `freetype` | `2.10.4-10.el9_5` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `fstrm` | `0.6.1-3.el9` | postgresql-15 |
| `gawk` | `5.1.0-6.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `gd` | `2.3.2-3.el9` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `gdb-gdbserver` | `16.3-2.el9` | eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `gdbm-libs` | `1.23-1.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `gettext` | `0.21-8.el9` | eda-controller-ui-rhel9, hub-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `gettext-libs` | `0.21-8.el9` | eda-controller-ui-rhel9, hub-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `git-core` | `2.47.3-1.el9_6` | controller-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9, metrics-service-rhel9 |
| `git-lfs` | `3.6.1-7.el9_7` | controller-rhel9, ee-supported-rhel9 |
| `glib2` | `2.68.4-18.el9_7.1` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `glibc` | `2.34-231.el9_7.10` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `glibc-common` | `2.34-231.el9_7.10` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `glibc-langpack-en` | `2.34-231.el9_7.10` | controller-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-rhel9, mcp-server-rhel9, metrics-service-rhel9, postgresql-15, redis-6 |
| `glibc-locale-source` | `2.34-231.el9_7.10` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15, redis-6 |
| `glibc-minimal-langpack` | `2.34-231.el9_7.10` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `gmp` | `6.2.0-13.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `gnupg2` | `2.3.3-5.el9_7` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `gnutls` | `3.8.3-10.el9_7` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `gobject-introspection` | `1.68.0-11.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `gpg-pubkey` | `5a6340b3-6229229e` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `gpg-pubkey` | `fd431d51-4ae0493b` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `gpgme` | `1.15.1-6.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `graphite2` | `1.3.14-9.el9` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `grep` | `3.6-5.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `groff-base` | `1.22.4-10.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15, redis-6 |
| `gzip` | `1.12-1.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `harfbuzz` | `2.7.4-10.el9` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `hostname` | `3.23-6.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp |
| `ima-evm-utils` | `1.6.2-2.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `iproute` | `6.14.0-2.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `java-17-openjdk-headless` | `17.0.18.0.8-1.el9` | de-supported-rhel9 |
| `javapackages-filesystem` | `6.4.0-1.el9` | de-supported-rhel9 |
| `jbigkit-libs` | `2.1-23.el9` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `jq` | `1.6-19.el9` | lightspeed-chatbot-rhel9 |
| `json-c` | `0.14-11.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `json-glib` | `1.6.6-1.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `keyutils` | `1.6.3-1.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `keyutils-libs` | `1.6.3-1.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `kmod-libs` | `28-11.el9` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, gateway-rhel9, hub-web-rhel9, lightspeed-rhel9, mcp-server-rhel9, pcp, postgresql-15, redis-6 |
| `krb5-libs` | `1.21.1-8.el9_6` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `krb5-pkinit` | `1.21.1-8.el9_6` | controller-rhel9, de-supported-rhel9, ee-minimal-rhel9, ee-supported-rhel9 |
| `krb5-workstation` | `1.21.1-8.el9_6` | controller-rhel9, de-supported-rhel9, ee-minimal-rhel9, ee-supported-rhel9 |
| `langpacks-core-en` | `3.0-16.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `langpacks-core-font-en` | `3.0-16.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `langpacks-en` | `3.0-16.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `less` | `590-6.el9` | controller-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9, hub-web-rhel9, metrics-service-rhel9, postgresql-15, redis-6 |
| `libacl` | `2.3.1-4.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libaio` | `0.3.111-13.el9` | ee-supported-rhel9 |
| `libarchive` | `3.5.3-7.el9_7` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libassuan` | `2.5.5-3.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libattr` | `2.5.1-3.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libblkid` | `2.37.4-21.el9_7` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libbpf` | `1.5.0-2.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `libbrotli` | `1.0.9-9.el9_7` | eda-controller-ui-rhel9, hub-web-rhel9, mcp-server-rhel9 |
| `libcap` | `2.48-10.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libcap-ng` | `0.8.2-7.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libcbor` | `0.7.0-5.el9` | controller-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9, metrics-service-rhel9 |
| `libcom_err` | `1.46.5-8.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libcomps` | `0.1.18-1.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `libcurl-minimal` | `7.76.1-35.el9_7.3` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libdb` | `5.3.28-57.el9_6` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libdnf` | `0.69.0-17.el9_7` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libdnf-plugin-subscription-manager` | `1.29.47.1-1.el9_7` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `libeconf` | `0.4.1-4.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libedit` | `3.1-38.20210216cvs.el9` | controller-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9, metrics-service-rhel9 |
| `libestr` | `0.1.11-4.el9` | controller-rhel9 |
| `libevent` | `2.1.12-8.el9_4` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libfastjson` | `0.99.9-5.el9` | controller-rhel9 |
| `libfdisk` | `2.37.4-21.el9_7` | controller-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libffi` | `3.4.2-8.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libfido2` | `1.13.0-2.el9` | controller-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9, metrics-service-rhel9 |
| `libgcc` | `11.5.0-11.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libgcrypt` | `1.10.0-11.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libgfortran` | `11.5.0-11.el9` | ee-supported-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9 |
| `libgomp` | `11.5.0-11.el9` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, pcp, postgresql-15, redis-6 |
| `libgpg-error` | `1.42-5.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libicu` | `67.1-10.el9_6` | postgresql-15 |
| `libidn2` | `2.3.0-7.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libjpeg-turbo` | `2.0.90-7.el9` | eda-controller-ui-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9 |
| `libkadm5` | `1.21.1-8.el9_6` | controller-rhel9, de-supported-rhel9, ee-minimal-rhel9, ee-supported-rhel9 |
| `libksba` | `1.5.1-7.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libmaxminddb` | `1.5.2-4.el9` | postgresql-15 |
| `libmnl` | `1.0.4-16.el9_4` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `libmodulemd` | `2.13.0-2.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libmount` | `2.37.4-21.el9_7` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libnghttp2` | `1.43.0-6.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libnsl2` | `2.0.0-1.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, metrics-service-rhel9 |
| `libpeas` | `1.30.0-4.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9 |
| `libpipeline` | `1.5.3-4.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15, redis-6 |
| `libpkgconf` | `1.7.3-10.el9` | ee-supported-rhel9, pcp |
| `libpng` | `1.6.37-12.el9_7.2` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `libpq` | `13.23-1.el9_7` | de-supported-rhel9, eda-controller-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, metrics-service-rhel9 |
| `libpwquality` | `1.4.4-8.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libquadmath` | `11.5.0-11.el9` | ee-supported-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9 |
| `librepo` | `1.14.5-3.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libreport-filesystem` | `2.15.2-6.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `librhsm` | `0.0.3-9.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libseccomp` | `2.5.2-2.el9` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-rhel9, mcp-server-rhel9, pcp, postgresql-15, redis-6 |
| `libsecret` | `0.20.4-4.el9` | hub-rhel9 |
| `libselinux` | `3.6-3.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libselinux-utils` | `3.6-3.el9` | ee-supported-rhel9, redis-6 |
| `libsemanage` | `3.6-5.el9_6` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libsepol` | `3.6-3.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libserf` | `1.3.9-27.el9` | controller-rhel9, ee-supported-rhel9 |
| `libsigsegv` | `2.13-4.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libsmartcols` | `2.37.4-21.el9_7` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libsolv` | `0.7.24-3.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libss` | `1.46.5-8.el9` | controller-rhel9, de-supported-rhel9, ee-minimal-rhel9, ee-supported-rhel9 |
| `libssh` | `0.10.4-17.el9_7` | ee-supported-rhel9 |
| `libssh-config` | `0.10.4-17.el9_7` | ee-supported-rhel9 |
| `libstdc++` | `11.5.0-11.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libtasn1` | `4.16.0-9.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libtiff` | `4.4.0-15.el9_7.2` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `libtirpc` | `1.3.3-9.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, metrics-service-rhel9 |
| `libtool-ltdl` | `2.4.6-46.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libunistring` | `0.9.10-15.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `liburing` | `2.5-1.el9` | ee-supported-rhel9 |
| `libusbx` | `1.0.26-1.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9 |
| `libuser` | `0.63-17.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `libutempter` | `1.2.1-6.el9` | controller-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libuuid` | `2.37.4-21.el9_7` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libuv` | `1.42.0-2.el9_4` | pcp, postgresql-15 |
| `libverto` | `0.3.2-3.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libwebp` | `1.2.0-8.el9_3` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `libX11` | `1.7.0-11.el9` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `libX11-common` | `1.7.0-11.el9` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `libXau` | `1.0.9-8.el9` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `libxcb` | `1.13.1-9.el9` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `libxcrypt` | `4.4.18-3.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libxml2` | `2.9.13-14.el9_7` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libXpm` | `3.5.13-10.el9` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `libxslt` | `1.1.34-13.el9_6` | controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9 |
| `libxslt` | `1.1.34-14.el9_7.1` | postgresql-15 |
| `libyaml` | `0.2.5-7.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `libzstd` | `1.5.5-1.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `lksctp-tools` | `1.0.19-3.el9_4` | de-supported-rhel9 |
| `lmdb-libs` | `0.9.29-3.el9` | postgresql-15 |
| `logrotate` | `3.18.0-12.el9` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, hub-web-rhel9, redis-6 |
| `lua` | `5.4.4-4.el9` | de-supported-rhel9 |
| `lua-libs` | `5.4.4-4.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `lua-posix` | `35.0-8.el9` | de-supported-rhel9 |
| `lz4-libs` | `1.9.3-5.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `man-db` | `2.9.3-9.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15, redis-6 |
| `microdnf` | `3.9.1-3.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9 |
| `mpdecimal` | `2.5.1-3.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, metrics-service-rhel9 |
| `mpfr` | `4.1.0-7.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `ncurses` | `6.2-12.20210508.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `ncurses-base` | `6.2-12.20210508.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `ncurses-libs` | `6.2-12.20210508.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `nettle` | `3.10.1-1.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `nginx` | `1.24.0-5.module+el9.7.0+24009+e763bdd7.1` | controller-rhel9, eda-controller-ui-rhel9, gateway-rhel9, hub-web-rhel9, lightspeed-rhel9, mcp-server-rhel9 |
| `nginx-all-modules` | `1.24.0-5.module+el9.7.0+24009+e763bdd7.1` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `nginx-core` | `1.24.0-5.module+el9.7.0+24009+e763bdd7.1` | controller-rhel9, eda-controller-ui-rhel9, gateway-rhel9, hub-web-rhel9, lightspeed-rhel9, mcp-server-rhel9 |
| `nginx-filesystem` | `1.24.0-5.module+el9.7.0+24009+e763bdd7.1` | controller-rhel9, eda-controller-ui-rhel9, gateway-rhel9, hub-web-rhel9, lightspeed-rhel9, mcp-server-rhel9 |
| `nginx-mod-http-image-filter` | `1.24.0-5.module+el9.7.0+24009+e763bdd7.1` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `nginx-mod-http-perl` | `1.24.0-5.module+el9.7.0+24009+e763bdd7.1` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `nginx-mod-http-xslt-filter` | `1.24.0-5.module+el9.7.0+24009+e763bdd7.1` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `nginx-mod-mail` | `1.24.0-5.module+el9.7.0+24009+e763bdd7.1` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `nginx-mod-stream` | `1.24.0-5.module+el9.7.0+24009+e763bdd7.1` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `nodejs` | `22.22.0-1.module+el9.7.0+23896+b5802de9` | mcp-server-rhel9 |
| `nodejs-full-i18n` | `22.22.0-1.module+el9.7.0+23896+b5802de9` | mcp-server-rhel9 |
| `nodejs-libs` | `22.22.0-1.module+el9.7.0+23896+b5802de9` | mcp-server-rhel9 |
| `nodejs-nodemon` | `3.0.1-1.module+el9.7.0+23896+b5802de9` | mcp-server-rhel9 |
| `npm` | `10.9.4-1.22.22.0.1.module+el9.7.0+23896+b5802de9` | mcp-server-rhel9 |
| `npth` | `1.6-8.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `nspr` | `4.36.0-8.el9_4` | de-supported-rhel9 |
| `nss` | `3.112.0-8.el9_4` | de-supported-rhel9 |
| `nss-softokn` | `3.112.0-8.el9_4` | de-supported-rhel9 |
| `nss-softokn-freebl` | `3.112.0-8.el9_4` | de-supported-rhel9 |
| `nss-sysinit` | `3.112.0-8.el9_4` | de-supported-rhel9 |
| `nss-util` | `3.112.0-8.el9_4` | de-supported-rhel9 |
| `nss_wrapper-libs` | `1.1.13-1.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
| `numactl-libs` | `2.0.19-3.el9` | ee-supported-rhel9 |
| `oniguruma` | `6.9.6-1.el9.6` | lightspeed-chatbot-rhel9 |
| `openblas` | `0.3.29-1.el9` | ee-supported-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9 |
| `openblas-openmp` | `0.3.29-1.el9` | ee-supported-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9 |
| `openldap` | `2.6.8-4.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `openshift-clients` | `4.19.0-202602241905.p2.g24755b6.assembly.stream.el9` | ee-supported-rhel9 |
| `openssh` | `8.7p1-47.el9_7` | controller-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9, metrics-service-rhel9 |
| `openssh-clients` | `8.7p1-47.el9_7` | controller-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-rhel9, metrics-service-rhel9 |
| `openssl` | `3.5.1-7.el9_7` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `openssl-fips-provider` | `3.0.7-8.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `openssl-fips-provider-so` | `3.0.7-8.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `openssl-libs` | `3.5.1-7.el9_7` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `p11-kit` | `0.25.3-3.el9_5` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `p11-kit-trust` | `0.25.3-3.el9_5` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `pam` | `1.5.1-26.el9_6` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `passwd` | `0.80-12.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `pcp` | `6.3.7-5.el9` | pcp |
| `pcp-conf` | `6.3.7-5.el9` | pcp |
| `pcp-doc` | `6.3.7-5.el9` | pcp |
| `pcp-libs` | `6.3.7-5.el9` | pcp |
| `pcp-pmda-dm` | `6.3.7-5.el9` | pcp |
| `pcp-pmda-nfsclient` | `6.3.7-5.el9` | pcp |
| `pcp-pmda-openmetrics` | `6.3.7-5.el9` | pcp |
| `pcp-system-tools` | `6.3.7-5.el9` | pcp |
| `pcp-zeroconf` | `6.3.7-5.el9` | pcp |
| `pcre` | `8.44-4.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `pcre2` | `10.40-6.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `pcre2-syntax` | `10.40-6.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
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
| `perl-Net-SSLeay` | `1.94-3.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15 |
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
| `podman-remote` | `5.6.0-14.el9_7` | controller-rhel9, ee-supported-rhel9, receptor-rhel9 |
| `policycoreutils` | `3.6-3.el9` | ee-supported-rhel9, redis-6 |
| `popt` | `1.18-8.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `postgresql` | `15.17-1.module+el9.7.0+24029+ef6a2953` | controller-rhel9, gateway-rhel9, postgresql-15 |
| `postgresql-contrib` | `15.17-1.module+el9.7.0+24029+ef6a2953` | postgresql-15 |
| `postgresql-private-libs` | `15.17-1.module+el9.7.0+24029+ef6a2953` | controller-rhel9, gateway-rhel9, postgresql-15 |
| `postgresql-server` | `15.17-1.module+el9.7.0+24029+ef6a2953` | postgresql-15 |
| `postgresql-upgrade` | `15.17-1.module+el9.7.0+24029+ef6a2953` | postgresql-15 |
| `procps-ng` | `3.3.17-14.el9` | eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `protobuf` | `3.14.0-17.el9_7` | lightspeed-chatbot-rhel9 |
| `protobuf-c` | `1.3.3-13.el9` | postgresql-15 |
| `psmisc` | `23.4-3.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3` | `3.9.25-3.el9_7.1` | controller-rhel9, de-supported-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-chardet` | `4.0.0-5.el9` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-cloud-what` | `1.29.47.1-1.el9_7` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-dateutil` | `2.9.0.post0-1.el9_7` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-dbus` | `1.2.18-2.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-decorator` | `4.4.2-6.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-dnf` | `4.14.0-31.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-dnf-plugins-core` | `4.3.0-24.el9_7` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-gobject-base` | `3.40.1-6.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-gobject-base-noarch` | `3.40.1-6.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-gpg` | `1.15.1-6.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-hawkey` | `0.69.0-17.el9_7` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-idna` | `2.10-7.el9_4.1` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-iniparse` | `0.4-45.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-inotify` | `0.9.6-25.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-libcomps` | `0.1.18-1.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-libdnf` | `0.69.0-17.el9_7` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-librepo` | `1.14.5-3.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-libs` | `3.9.25-3.el9_7.1` | controller-rhel9, de-supported-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-libselinux` | `3.6-3.el9` | controller-rhel9 |
| `python3-libsemanage` | `3.6-5.el9_6` | controller-rhel9 |
| `python3-pcp` | `6.3.7-5.el9` | pcp |
| `python3-pexpect` | `4.8.0-7.el9` | controller-rhel9, ee-supported-rhel9 |
| `python3-pip-wheel` | `21.3.1-1.el9` | controller-rhel9, de-supported-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-ptyprocess` | `0.6.0-12.el9` | controller-rhel9, ee-supported-rhel9 |
| `python3-pysocks` | `1.7.1-12.el9` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-pyyaml` | `5.4.1-6.el9` | controller-rhel9, ee-supported-rhel9 |
| `python3-requests` | `2.25.1-10.el9_6` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-rpm` | `4.16.1.3-39.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-setuptools` | `53.0.0-15.el9` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-setuptools-wheel` | `53.0.0-15.el9` | controller-rhel9, de-supported-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-six` | `1.15.0-9.el9` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-subscription-manager-rhsm` | `1.29.47.1-1.el9_7` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-systemd` | `234-19.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3-urllib3` | `1.26.5-6.el9_7.1` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `python3.12` | `3.12.12-4.el9_7.1` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, metrics-service-rhel9 |
| `python3.12-certifi` | `2023.5.7-2.el9ap` | ee-supported-rhel9 |
| `python3.12-cffi` | `1.16.0-2.el9` | de-supported-rhel9, ee-minimal-rhel9, ee-supported-rhel9, lightspeed-chatbot-rhel9, mcp-tools-rhel9 |
| `python3.12-charset-normalizer` | `3.3.0-2.el9` | ee-minimal-rhel9, ee-supported-rhel9, lightspeed-chatbot-rhel9 |
| `python3.12-cryptography` | `41.0.7-3.el9_7` | ee-minimal-rhel9, ee-supported-rhel9, lightspeed-chatbot-rhel9 |
| `python3.12-cryptography` | `42.0.5-2.el9ap` | de-supported-rhel9 |
| `python3.12-drools-jpy` | `0.3.14-2.el9ap` | de-supported-rhel9 |
| `python3.12-drools-jpy-jar` | `1.0.11-2.Final_redhat_00001.1.el9ap` | de-supported-rhel9 |
| `python3.12-idna` | `3.4-2.el9` | ee-minimal-rhel9, ee-supported-rhel9, lightspeed-chatbot-rhel9, mcp-tools-rhel9 |
| `python3.12-jpy` | `0.15.0-2.el9ap` | de-supported-rhel9 |
| `python3.12-libs` | `3.12.12-4.el9_7.1` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, metrics-service-rhel9 |
| `python3.12-lxml` | `4.9.3-2.el9` | ee-minimal-rhel9, ee-supported-rhel9 |
| `python3.12-numpy` | `1.24.4-3.el9` | ee-supported-rhel9, lightspeed-rhel9 |
| `python3.12-pip` | `23.2.1-5.el9` | controller-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, metrics-service-rhel9 |
| `python3.12-pip-wheel` | `23.2.1-5.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, metrics-service-rhel9 |
| `python3.12-ply` | `3.11-2.el9` | de-supported-rhel9, ee-minimal-rhel9, ee-supported-rhel9, lightspeed-chatbot-rhel9, mcp-tools-rhel9 |
| `python3.12-pycparser` | `2.20-2.el9` | de-supported-rhel9, ee-minimal-rhel9, ee-supported-rhel9, lightspeed-chatbot-rhel9, mcp-tools-rhel9 |
| `python3.12-pyyaml` | `6.0.1-2.el9` | controller-rhel9, de-supported-rhel9, ee-minimal-rhel9, ee-supported-rhel9, lightspeed-rhel9 |
| `python3.12-requests` | `2.31.0-4.el9ap` | ee-supported-rhel9 |
| `python3.12-setuptools` | `68.2.2-5.el9_6` | ee-minimal-rhel9, ee-supported-rhel9, lightspeed-chatbot-rhel9 |
| `python3.12-uamqp` | `1.6.8-2.el9ap` | ee-supported-rhel9 |
| `python3.12-urllib3` | `1.26.19-1.el9_7.1` | ee-minimal-rhel9, ee-supported-rhel9 |
| `qemu-img` | `9.1.0-29.el9_7.6` | ee-supported-rhel9 |
| `readline` | `8.1-4.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `receptor` | `1.6.4-1.el9ap` | ee-supported-rhel9 |
| `redhat-logos-httpd` | `90.5-1.el9_6.1` | controller-rhel9, eda-controller-ui-rhel9, gateway-rhel9, hub-web-rhel9, lightspeed-rhel9, mcp-server-rhel9 |
| `redhat-release` | `9.7-0.7.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `redis` | `6.2.20-3.el9_7` | controller-rhel9, redis-6 |
| `rootfiles` | `8.1-35.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `rpm` | `4.16.1.3-39.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `rpm-build-libs` | `4.16.1.3-39.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `rpm-libs` | `4.16.1.3-39.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `rpm-sign-libs` | `4.16.1.3-39.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `rsync` | `3.2.5-3.el9` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, hub-web-rhel9, postgresql-15, redis-6 |
| `rsyslog` | `8.2506.0-2.el9` | controller-rhel9 |
| `scl-utils` | `2.0.3-4.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15, redis-6 |
| `sed` | `4.8-9.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `setup` | `2.13.7-10.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `shadow-utils` | `4.9-15.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `shadow-utils-subid` | `4.9-15.el9` | controller-rhel9, ee-supported-rhel9, hub-rhel9, receptor-rhel9 |
| `skopeo` | `1.20.0-3.el9_7` | hub-rhel9 |
| `sos` | `4.10.2-2.el9_7` | controller-rhel9, ee-supported-rhel9 |
| `sqlite-libs` | `3.34.1-9.el9_7` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `sshpass` | `1.09-4.el9` | controller-rhel9, ee-minimal-rhel9, ee-supported-rhel9 |
| `subscription-manager` | `1.29.47.1-1.el9_7` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `subscription-manager-rhsm-certificates` | `20220623-1.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `subversion` | `1.14.1-7.el9` | controller-rhel9, ee-supported-rhel9 |
| `subversion-libs` | `1.14.1-7.el9` | controller-rhel9, ee-supported-rhel9 |
| `systemd` | `252-55.el9_7.7` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, gateway-rhel9, hub-web-rhel9, lightspeed-rhel9, mcp-server-rhel9, pcp, postgresql-15, redis-6 |
| `systemd-libs` | `252-55.el9_7.7` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `systemd-pam` | `252-55.el9_7.7` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, gateway-rhel9, hub-web-rhel9, lightspeed-rhel9, mcp-server-rhel9, pcp, postgresql-15, redis-6 |
| `systemd-rpm-macros` | `252-55.el9_7.7` | controller-rhel9, eda-controller-ui-rhel9, ee-supported-rhel9, gateway-rhel9, hub-web-rhel9, lightspeed-rhel9, mcp-server-rhel9, pcp, postgresql-15, redis-6 |
| `tar` | `1.34-9.el9_7` | eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, mcp-server-rhel9, pcp, postgresql-15, redis-6 |
| `tcl` | `8.6.10-7.el9` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15, redis-6 |
| `tpm2-tss` | `3.2.3-1.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `tzdata` | `2026a-1.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `tzdata-java` | `2026a-1.el9` | de-supported-rhel9 |
| `unzip` | `6.0-59.el9` | eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-web-rhel9, postgresql-15, redis-6 |
| `usermode` | `1.114-7.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `utf8proc` | `2.6.1-4.el9` | controller-rhel9, ee-supported-rhel9 |
| `util-linux` | `2.37.4-21.el9_7` | controller-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `util-linux-core` | `2.37.4-21.el9_7` | controller-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `uuid` | `1.6.2-55.el9` | postgresql-15 |
| `vim-filesystem` | `8.2.2637-23.el9_7.1` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15, redis-6 |
| `vim-minimal` | `8.2.2637-23.el9_7` | eda-controller-ui-rhel9, hub-web-rhel9, postgresql-15, redis-6 |
| `vim-minimal` | `8.2.2637-23.el9_7.1` | pcp |
| `virt-what` | `1.27-2.el9` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `which` | `2.21-30.el9_6` | controller-rhel9, eda-controller-ui-rhel9, hub-web-rhel9, mcp-server-rhel9, pcp, postgresql-15, redis-6 |
| `xml-common` | `0.6.3-58.el9` | eda-controller-ui-rhel9, hub-web-rhel9 |
| `xmlsec1` | `1.2.29-13.el9` | controller-rhel9, gateway-rhel9 |
| `xmlsec1-openssl` | `1.2.29-13.el9` | controller-rhel9, gateway-rhel9 |
| `xz` | `5.2.5-8.el9_0` | eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `xz-libs` | `5.2.5-8.el9_0` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `yajl` | `2.1.0-25.el9` | controller-rhel9, hub-rhel9 |
| `yum` | `4.14.0-31.el9` | eda-controller-ui-rhel9, hub-web-rhel9, pcp, postgresql-15, redis-6 |
| `zlib` | `1.2.11-40.el9` | controller-rhel9, de-supported-rhel9, eda-controller-rhel9, eda-controller-ui-rhel9, ee-minimal-rhel9, ee-supported-rhel9, gateway-proxy-rhel9, gateway-rhel9, hub-rhel9, hub-web-rhel9, lightspeed-chatbot-rhel9, lightspeed-rhel9, mcp-tools-rhel9, receptor-rhel9, mcp-server-rhel9, metrics-service-rhel9, pcp, postgresql-15, redis-6 |
| `zstd` | `1.5.5-1.el9` | ee-minimal-rhel9, ee-supported-rhel9 |

## Python Packages (all images)

Every Python distribution found in any image (`image:environment prefix (python)`), from
`*.dist-info`/`*.egg-info` metadata. Names are normalized (PEP 503: lowercase, `-` separators). This covers system Python, `/usr/local` and application venvs.

| Package | Version | Images |
|---|---|---|
| `aap-eda` | `1.2.7` | eda-controller-rhel9:/usr (python3.12) |
| `aap-gateway` | `2.6.20260325` | gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `adal` | `1.2.7` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `aiobotocore` | `2.11.2` | ee-supported-rhel9:/usr/local (python3.12) |
| `aiobotocore` | `3.3.0` | de-supported-rhel9:/usr/local (python3.12) |
| `aiodns` | `3.2.0` | ee-supported-rhel9:/usr/local (python3.12), hub-rhel9:/usr (python3.12) |
| `aiodns` | `3.6.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `aiofiles` | `23.2.1` | hub-rhel9:/usr (python3.12) |
| `aiofiles` | `24.1.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `aiohappyeyeballs` | `2.6.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), de-supported-rhel9:/usr/local (python3.12), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `aiohttp` | `3.13.3` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), de-supported-rhel9:/usr/local (python3.12), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `aiohttp-retry` | `2.8.3` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `aioitertools` | `0.11.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `aioitertools` | `0.13.0` | de-supported-rhel9:/usr/local (python3.12) |
| `aiokafka` | `0.10.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `aiokafka` | `0.13.0` | de-supported-rhel9:/usr/local (python3.12) |
| `aiosignal` | `1.4.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), de-supported-rhel9:/usr/local (python3.12), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `aiosqlite` | `0.22.1` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `annotated-doc` | `0.0.4` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `annotated-types` | `0.6.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `annotated-types` | `0.7.0` | ee-supported-rhel9:/usr/local (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), mcp-tools-rhel9:/usr/local (python3.12) |
| `ansible-ai-connect` | `0.1.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `ansible-anonymizer` | `1.5.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `ansible-builder` | `3.1.1` | hub-rhel9:/usr (python3.12) |
| `ansible-chatbot-stack` | `0.1.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `ansible-compat` | `25.12.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `ansible-compat` | `25.12.1` | hub-rhel9:/usr (python3.12) |
| `ansible-compat` | `25.8.1` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `ansible-core` | `2.16.15` | eda-controller-rhel9:/usr (python3.12) |
| `ansible-core` | `2.16.16` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `ansible-core` | `2.16.18` | de-supported-rhel9:/usr/local (python3.12), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `ansible-core` | `2.20.3` | hub-rhel9:/usr (python3.12) |
| `ansible-lint` | `25.5.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `ansible-lint` | `25.8.2` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `ansible-lint` | `26.1.0` | hub-rhel9:/usr (python3.12) |
| `ansible-mcp-tools` | `0.1.0` | mcp-tools-rhel9:/usr/local (python3.12) |
| `ansible-pylibssh` | `1.2.2` | ee-supported-rhel9:/usr/local (python3.12) |
| `ansible-rulebook` | `1.2.2` | de-supported-rhel9:/usr/local (python3.12) |
| `ansible-runner` | `2.4.1` | eda-controller-rhel9:/usr (python3.12) |
| `ansible-runner` | `2.4.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), de-supported-rhel9:/usr/local (python3.12) |
| `ansible-runner` | `2.4.3` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), receptor-rhel9:/usr (python3.12) |
| `ansible-sign` | `0.1.2` | ee-supported-rhel9:/usr/local (python3.12) |
| `ansiconv` | `1.0.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `anyio` | `4.12.1` | lightspeed-chatbot-rhel9:/usr/local (python3.12), mcp-tools-rhel9:/usr/local (python3.12) |
| `anyio` | `4.4.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `anyio` | `4.9.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `appdirs` | `1.4.4` | ee-supported-rhel9:/usr/local (python3.12) |
| `applicationinsights` | `0.11.10` | ee-supported-rhel9:/usr/local (python3.12) |
| `apscheduler` | `3.11.2` | metrics-service-rhel9:/usr (python3.12) |
| `argcomplete` | `3.5.3` | ee-supported-rhel9:/usr/local (python3.12) |
| `argon2-cffi` | `23.1.0` | gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `argon2-cffi-bindings` | `21.2.0` | gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `argparse` | `1.4.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `asciichartpy` | `1.5.7` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `asgiref` | `3.11.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12) |
| `asgiref` | `3.11.1` | hub-rhel9:/usr (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `asgiref` | `3.8.1` | gateway-rhel9:/opt/aap-gateway/venv (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `asn1` | `2.7.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `asttokens` | `3.0.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `async-timeout` | `5.0.1` | de-supported-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), hub-rhel9:/usr (python3.12) |
| `asyncio-throttle` | `1.0.2` | hub-rhel9:/usr (python3.12) |
| `asyncpg` | `0.31.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `attrs` | `22.2.0` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), hub-rhel9:/usr (python3.12) |
| `attrs` | `23.1.0` | eda-controller-rhel9:/usr (python3.12) |
| `attrs` | `23.2.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `attrs` | `25.3.0` | gateway-rhel9:/opt/aap-gateway/venv (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `attrs` | `25.4.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12), mcp-tools-rhel9:/usr/local (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `attrs` | `26.1.0` | de-supported-rhel9:/usr/local (python3.12) |
| `authlib` | `1.6.9` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `autobahn` | `23.6.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `autobahn` | `24.4.2` | eda-controller-rhel9:/usr (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `autocommand` | `2.2.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `automat` | `22.10.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12) |
| `automat` | `25.4.16` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `awx` | `4.7.10` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `awx-plugins-core` | `0.0.1a10` | eda-controller-rhel9:/usr (python3.12) |
| `awx-plugins-interfaces` | `0.0.1a5` | eda-controller-rhel9:/usr (python3.12) |
| `awxkit` | `4.7.10` | ee-supported-rhel9:/usr (python3.12) |
| `azure-cli-core` | `2.74.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-cli-telemetry` | `1.1.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-common` | `1.1.28` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `azure-containerregistry` | `1.2.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-core` | `1.30.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `azure-core` | `1.31.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-core` | `1.34.0` | eda-controller-rhel9:/usr (python3.12) |
| `azure-core` | `1.39.0` | de-supported-rhel9:/usr/local (python3.12), hub-rhel9:/usr (python3.12) |
| `azure-identity` | `1.15.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `azure-identity` | `1.19.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-identity` | `1.23.0` | eda-controller-rhel9:/usr (python3.12) |
| `azure-iot-hub` | `2.6.1` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-keyvault` | `4.2.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `azure-keyvault-certificates` | `4.7.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `azure-keyvault-keys` | `4.11.0` | eda-controller-rhel9:/usr (python3.12) |
| `azure-keyvault-keys` | `4.8.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `azure-keyvault-secrets` | `4.10.0` | eda-controller-rhel9:/usr (python3.12) |
| `azure-keyvault-secrets` | `4.7.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `azure-keyvault-securitydomain` | `1.0.0b1` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-apimanagement` | `4.0.1` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-authorization` | `4.0.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-automation` | `1.1.0b4` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-batch` | `17.3.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-cdn` | `13.1.1` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-compute` | `33.0.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-containerinstance` | `10.1.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-containerregistry` | `10.3.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-containerservice` | `32.1.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-core` | `1.4.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-cosmosdb` | `10.0.0b3` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-datafactory` | `9.0.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-devtestlabs` | `10.0.0b2` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-dns` | `8.1.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-eventhub` | `11.1.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-hdinsight` | `9.1.0b1` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-iothub` | `3.0.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-keyvault` | `10.3.1` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-loganalytics` | `13.0.0b7` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-managedservices` | `7.0.0b2` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-managementgroups` | `1.1.0b2` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-marketplaceordering` | `1.2.0b2` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-monitor` | `6.0.2` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-mysqlflexibleservers` | `1.0.0b3` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-network` | `28.0.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-notificationhubs` | `8.1.0b1` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-nspkg` | `3.0.2` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-postgresqlflexibleservers` | `1.1.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-privatedns` | `1.2.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-rdbms` | `10.2.0b17` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-recoveryservices` | `3.0.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-recoveryservicesbackup` | `9.1.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-redis` | `14.4.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-resource` | `23.2.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-resourcegraph` | `8.0.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-resourcehealth` | `1.0.0b6` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-search` | `9.2.0b2` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-servicebus` | `8.2.1` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-sql` | `4.0.0b19` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-storage` | `21.2.1` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-trafficmanager` | `1.1.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-mgmt-web` | `7.3.1` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-nspkg` | `3.0.2` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-servicebus` | `7.14.2` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-servicebus` | `7.14.3` | de-supported-rhel9:/usr/local (python3.12) |
| `azure-storage-blob` | `12.23.0b1` | ee-supported-rhel9:/usr/local (python3.12) |
| `azure-storage-blob` | `12.28.0` | hub-rhel9:/usr (python3.12) |
| `backcall` | `0.2.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `backoff` | `2.2.1` | hub-rhel9:/usr (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `backports-tarfile` | `1.2.0` | hub-rhel9:/usr (python3.12) |
| `backports-zstd` | `1.3.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `bcrypt` | `3.2.2` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `bindep` | `2.14.0` | hub-rhel9:/usr (python3.12) |
| `black` | `25.1.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `black` | `25.12.0` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), hub-rhel9:/usr (python3.12) |
| `boto3` | `1.34.34` | ee-supported-rhel9:/usr/local (python3.12) |
| `boto3` | `1.35.96` | metrics-service-rhel9:/usr (python3.12) |
| `boto3` | `1.38.38` | eda-controller-rhel9:/usr (python3.12) |
| `boto3` | `1.40.64` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `boto3` | `1.42.26` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `boto3` | `1.42.73` | hub-rhel9:/usr (python3.12) |
| `botocore` | `1.34.34` | ee-supported-rhel9:/usr/local (python3.12) |
| `botocore` | `1.35.96` | metrics-service-rhel9:/usr (python3.12) |
| `botocore` | `1.38.38` | eda-controller-rhel9:/usr (python3.12) |
| `botocore` | `1.40.64` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `botocore` | `1.42.26` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `botocore` | `1.42.70` | de-supported-rhel9:/usr/local (python3.12) |
| `botocore` | `1.42.73` | hub-rhel9:/usr (python3.12) |
| `bracex` | `2.4` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `bracex` | `2.5.post1` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `bracex` | `2.6` | hub-rhel9:/usr (python3.12) |
| `brotli` | `1.2.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `cachecontrol` | `0.14.3` | hub-rhel9:/usr (python3.12) |
| `cachetools` | `3.1.1` | eda-controller-rhel9:/usr (python3.12) |
| `cachetools` | `5.5.2` | ee-supported-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `cachetools` | `6.2.4` | mcp-tools-rhel9:/usr/local (python3.12) |
| `cachetools` | `6.2.6` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `cachetools` | `7.0.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `cbor2` | `5.8.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `certifi` | `2023.5.7` | ee-supported-rhel9:/usr (python3.12) |
| `certifi` | `2026.1.4` | mcp-tools-rhel9:/usr/local (python3.12) |
| `certifi` | `2026.2.25` | de-supported-rhel9:/usr/local (python3.12) |
| `certifi` | `2038.12.31` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12), gateway-rhel9:/usr (python3.12), hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `cffi` | `1.15.1` | eda-controller-rhel9:/usr (python3.12) |
| `cffi` | `1.16.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), de-supported-rhel9:/usr (python3.12), ee-minimal-rhel9:/usr (python3.12), ee-supported-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr (python3.12), mcp-tools-rhel9:/usr (python3.12) |
| `cffi` | `1.17.1` | gateway-rhel9:/opt/aap-gateway/venv (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `cffi` | `2.0.0` | hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), mcp-tools-rhel9:/usr/local (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `channels` | `4.3.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12) |
| `channels-redis` | `4.2.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `chardet` | `4.0.0` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), ee-supported-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `chardet` | `5.2.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `charset-normalizer` | `3.1.0` | eda-controller-rhel9:/usr (python3.12) |
| `charset-normalizer` | `3.3.0` | ee-minimal-rhel9:/usr (python3.12), ee-supported-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr (python3.12) |
| `charset-normalizer` | `3.3.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `charset-normalizer` | `3.4.0` | gateway-rhel9:/opt/aap-gateway/venv (python3.12), gateway-rhel9:/usr (python3.12) |
| `charset-normalizer` | `3.4.2` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `charset-normalizer` | `3.4.4` | metrics-service-rhel9:/usr (python3.12) |
| `charset-normalizer` | `3.4.6` | de-supported-rhel9:/usr/local (python3.12), hub-rhel9:/usr (python3.12) |
| `click` | `8.1.3` | eda-controller-rhel9:/usr (python3.12) |
| `click` | `8.1.7` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), hub-rhel9:/usr (python3.12) |
| `click` | `8.2.1` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `click` | `8.3.1` | lightspeed-chatbot-rhel9:/usr/local (python3.12), mcp-tools-rhel9:/usr/local (python3.12) |
| `constantly` | `23.10.4` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `croniter` | `1.3.14` | eda-controller-rhel9:/usr (python3.12) |
| `croniter` | `6.0.0` | metrics-service-rhel9:/usr (python3.12) |
| `crontab` | `1.0.5` | eda-controller-rhel9:/usr (python3.12) |
| `cryptography` | `41.0.7` | ee-minimal-rhel9:/usr (python3.12), ee-supported-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr (python3.12) |
| `cryptography` | `42.0.5` | de-supported-rhel9:/usr (python3.12) |
| `cryptography` | `42.0.8` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `cryptography` | `44.0.1` | gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `cryptography` | `45.0.3` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `cryptography` | `46.0.5` | hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), mcp-tools-rhel9:/usr/local (python3.12) |
| `cython` | `3.2.4` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `daphne` | `4.0.0` | eda-controller-rhel9:/usr (python3.12) |
| `daphne` | `4.2.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `dbus-python` | `1.2.18` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `decorator` | `4.4.2` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `decorator` | `5.1.1` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `decorator` | `5.2.1` | de-supported-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `defusedxml` | `0.7.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12), hub-rhel9:/usr (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `deprecated` | `1.2.14` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `deprecated` | `1.2.18` | eda-controller-rhel9:/usr (python3.12) |
| `deprecated` | `1.3.1` | hub-rhel9:/usr (python3.12) |
| `diff-match-patch` | `20241021` | hub-rhel9:/usr (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `dispatcherd` | `2025.5.19` | eda-controller-rhel9:/usr (python3.12) |
| `dispatcherd` | `2026.1.27` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `distlib` | `0.4.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `distro` | `1.9.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12), ee-supported-rhel9:/usr/local (python3.12), hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `django` | `5.2.10` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `django` | `5.2.12` | hub-rhel9:/usr (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `django` | `5.2.7` | metrics-service-rhel9:/usr (python3.12) |
| `django` | `5.2.9` | eda-controller-rhel9:/usr (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `django-allow-cidr` | `0.8.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `django-ansible-base` | `2.6.20260325` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12), hub-rhel9:/usr (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `django-ansible-base` | `2.7.0` | gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `django-auth-ldap` | `4.0.0` | hub-rhel9:/usr (python3.12) |
| `django-auth-ldap` | `5.1.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `django-auth-ldap` | `5.2.0` | gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `django-automated-logging` | `6.2.2` | hub-rhel9:/usr (python3.12) |
| `django-cors-headers` | `4.3.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `django-crum` | `0.7.9` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12), hub-rhel9:/usr (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `django-csp` | `3.8` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `django-deprecate-fields` | `0.1.2` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `django-dynamic-preferences` | `1.16.0` | gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `django-extensions` | `3.2.3` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `django-extensions` | `4.1` | gateway-rhel9:/opt/aap-gateway/venv (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `django-filter` | `25.2` | eda-controller-rhel9:/usr (python3.12), hub-rhel9:/usr (python3.12) |
| `django-flags` | `5.0.13` | eda-controller-rhel9:/usr (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `django-flags` | `5.1.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `django-flags` | `5.2.0` | hub-rhel9:/usr (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `django-guid` | `3.4.0` | hub-rhel9:/usr (python3.12) |
| `django-guid` | `3.5.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `django-health-check` | `3.17.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `django-import-export` | `3.2.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `django-import-export` | `4.4.0` | hub-rhel9:/usr (python3.12) |
| `django-ipware` | `6.0.5` | hub-rhel9:/usr (python3.12) |
| `django-lifecycle` | `1.1.2` | hub-rhel9:/usr (python3.12) |
| `django-oauth-toolkit` | `1.7.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `django-oauth-toolkit` | `2.3.0` | gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `django-oauth-toolkit` | `3.0.1` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `django-pglocks` | `1.0.4` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `django-picklefield` | `3.4.0` | hub-rhel9:/usr (python3.12) |
| `django-polymorphic` | `4.11.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `django-prometheus` | `2.2.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `django-prometheus` | `2.4.1` | hub-rhel9:/usr (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `django-radius` | `1.5.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `django-redis` | `5.4.0` | eda-controller-rhel9:/usr (python3.12) |
| `django-redis` | `6.0.0` | gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `django-rq` | `3.2.2` | eda-controller-rhel9:/usr (python3.12) |
| `django-solo` | `2.2.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `django-storages` | `1.14.6` | hub-rhel9:/usr (python3.12) |
| `django-test-migrations` | `1.5.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `djangorestframework` | `3.15.1` | eda-controller-rhel9:/usr (python3.12) |
| `djangorestframework` | `3.15.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12), hub-rhel9:/usr (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `djangorestframework-queryfields` | `1.1.0` | hub-rhel9:/usr (python3.12) |
| `djangorestframework-yaml` | `2.0.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `dnspython` | `2.6.1` | ee-supported-rhel9:/usr/local (python3.12) |
| `dnspython` | `2.8.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `docutils` | `0.22.1` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `dogpile-cache` | `1.1.2` | ee-supported-rhel9:/usr/local (python3.12) |
| `dpapi-ng` | `0.2.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `dpath` | `2.2.0` | de-supported-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `drf-access-policy` | `1.5.0` | hub-rhel9:/usr (python3.12) |
| `drf-nested-routers` | `0.93.5` | hub-rhel9:/usr (python3.12) |
| `drf-spectacular` | `0.26.5` | gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `drf-spectacular` | `0.29.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12), hub-rhel9:/usr (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `drools-jpy` | `0.3.14` | de-supported-rhel9:/usr (python3.12) |
| `dumb-init` | `1.2.5.post1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), de-supported-rhel9:/usr/local (python3.12), eda-controller-rhel9:/usr (python3.12), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), gateway-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), receptor-rhel9:/usr (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `durationpy` | `0.10` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `dynaconf` | `3.2.10` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `dynaconf` | `3.2.11` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `dynaconf` | `3.2.12` | metrics-service-rhel9:/usr (python3.12) |
| `dynaconf` | `3.2.13` | hub-rhel9:/usr (python3.12) |
| `ecdsa` | `0.18.0` | eda-controller-rhel9:/usr (python3.12) |
| `ecdsa` | `0.19.1` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `email-validator` | `2.3.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `enum-compat` | `0.0.3` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `et-xmlfile` | `2.0.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `executing` | `2.2.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `expiringdict` | `1.2.2` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `faiss-cpu` | `1.12.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `fastapi` | `0.128.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `fastuuid` | `0.14.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `filelock` | `3.13.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `filelock` | `3.20.3` | lightspeed-chatbot-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `filelock` | `3.25.2` | hub-rhel9:/usr (python3.12) |
| `fire` | `0.7.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `fire` | `0.7.1` | lightspeed-chatbot-rhel9:/usr/local (python3.12), mcp-tools-rhel9:/usr/local (python3.12) |
| `flake8` | `6.1.0` | hub-rhel9:/usr (python3.12) |
| `freezegun` | `1.5.5` | eda-controller-rhel9:/usr (python3.12) |
| `frozenlist` | `1.4.1` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `frozenlist` | `1.6.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `frozenlist` | `1.8.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), de-supported-rhel9:/usr/local (python3.12), hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `fsspec` | `2026.1.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `galaxy-importer` | `0.4.37` | hub-rhel9:/usr (python3.12) |
| `galaxy-ng` | `4.11.7` | hub-rhel9:/usr (python3.12) |
| `gitdb` | `4.0.11` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `gitdb` | `4.0.12` | hub-rhel9:/usr (python3.12) |
| `gitpython` | `3.1.42` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `gitpython` | `3.1.46` | hub-rhel9:/usr (python3.12) |
| `google-api-core` | `2.24.2` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `google-api-core` | `2.25.1` | ee-supported-rhel9:/usr/local (python3.12) |
| `google-api-python-client` | `2.170.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `google-auth` | `2.17.3` | eda-controller-rhel9:/usr (python3.12) |
| `google-auth` | `2.40.2` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `google-auth` | `2.40.3` | ee-supported-rhel9:/usr/local (python3.12) |
| `google-auth` | `2.47.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `google-auth-httplib2` | `0.2.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `google-cloud-core` | `2.4.3` | ee-supported-rhel9:/usr/local (python3.12) |
| `google-cloud-storage` | `3.3.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `google-crc32c` | `1.7.1` | ee-supported-rhel9:/usr/local (python3.12) |
| `google-resumable-media` | `2.7.2` | ee-supported-rhel9:/usr/local (python3.12) |
| `googleapis-common-protos` | `1.63.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `googleapis-common-protos` | `1.70.0` | ee-supported-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `googleapis-common-protos` | `1.72.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `googleapis-common-protos` | `1.73.0` | hub-rhel9:/usr (python3.12) |
| `gpg` | `1.15.1` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `greenlet` | `3.3.1` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `grpcio` | `1.68.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `grpcio` | `1.75.1` | ee-supported-rhel9:/usr/local (python3.12) |
| `grpcio` | `1.78.0` | hub-rhel9:/usr (python3.12) |
| `grpcio-tools` | `1.68.1` | gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `gssapi` | `1.11.1` | de-supported-rhel9:/usr/local (python3.12) |
| `gssapi` | `1.8.3` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `gunicorn` | `22.0.0` | eda-controller-rhel9:/usr (python3.12) |
| `gunicorn` | `23.0.0` | hub-rhel9:/usr (python3.12), mcp-tools-rhel9:/usr/local (python3.12) |
| `gunicorn` | `25.1.0` | metrics-service-rhel9:/usr (python3.12) |
| `h11` | `0.16.0` | ee-supported-rhel9:/usr/local (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), mcp-tools-rhel9:/usr/local (python3.12) |
| `h2` | `4.1.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `hf-xet` | `1.2.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `hiredis` | `3.2.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `hpack` | `4.0.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `httpcore` | `1.0.9` | ee-supported-rhel9:/usr/local (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), mcp-tools-rhel9:/usr/local (python3.12) |
| `httplib2` | `0.22.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `httpx` | `0.27.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `httpx` | `0.28.1` | lightspeed-chatbot-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), mcp-tools-rhel9:/usr/local (python3.12) |
| `httpx-sse` | `0.4.3` | lightspeed-chatbot-rhel9:/usr/local (python3.12), mcp-tools-rhel9:/usr/local (python3.12) |
| `huggingface-hub` | `0.36.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `humanfriendly` | `10.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `hyperframe` | `6.0.1` | ee-supported-rhel9:/usr/local (python3.12) |
| `hyperlink` | `21.0.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `idna` | `2.10` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), ee-supported-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `idna` | `3.10` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12), gateway-rhel9:/usr (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `idna` | `3.11` | de-supported-rhel9:/usr/local (python3.12), hub-rhel9:/usr (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `idna` | `3.4` | eda-controller-rhel9:/usr (python3.12), ee-minimal-rhel9:/usr (python3.12), ee-supported-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr (python3.12), mcp-tools-rhel9:/usr (python3.12) |
| `importlib-metadata` | `6.0.1` | hub-rhel9:/usr (python3.12) |
| `importlib-metadata` | `6.2.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `importlib-metadata` | `7.1.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `importlib-metadata` | `8.7.1` | ee-minimal-rhel9:/usr/local (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `incremental` | `24.7.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `inflect` | `7.0.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `inflection` | `0.5.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12), hub-rhel9:/usr (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `iniparse` | `0.4` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `insights-analytics-collector` | `0.3.2` | eda-controller-rhel9:/usr (python3.12), hub-rhel9:/usr (python3.12) |
| `ipython` | `8.10.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `irc` | `20.3.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `iso8601` | `0.1.14` | ee-supported-rhel9:/usr/local (python3.12) |
| `isodate` | `0.6.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `isodate` | `0.7.2` | de-supported-rhel9:/usr/local (python3.12), eda-controller-rhel9:/usr (python3.12), ee-supported-rhel9:/usr/local (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12), hub-rhel9:/usr (python3.12) |
| `janus` | `1.2.0` | de-supported-rhel9:/usr/local (python3.12) |
| `jaraco-collections` | `5.0.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `jaraco-context` | `4.3.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `jaraco-functools` | `4.3.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `jaraco-logging` | `3.3.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `jaraco-stream` | `3.0.3` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `jaraco-text` | `3.12.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `jedi` | `0.19.2` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `jinja2` | `3.1.3` | eda-controller-rhel9:/usr (python3.12) |
| `jinja2` | `3.1.6` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), de-supported-rhel9:/usr/local (python3.12), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `jiter` | `0.10.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `jmespath` | `1.0.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12), ee-supported-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `jmespath` | `1.1.0` | de-supported-rhel9:/usr/local (python3.12), hub-rhel9:/usr (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `joblib` | `1.5.3` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `jpy` | `0.15.0` | de-supported-rhel9:/usr (python3.12) |
| `jq` | `1.6.0` | hub-rhel9:/usr (python3.12) |
| `jq` | `1.8.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `json-log-formatter` | `0.5.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `json-stream` | `2.3.4` | hub-rhel9:/usr (python3.12) |
| `json-stream-rs-tokenizer` | `0.4.30` | hub-rhel9:/usr (python3.12) |
| `jsonpatch` | `1.32` | ee-supported-rhel9:/usr/local (python3.12) |
| `jsonpath-ng` | `1.7.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `jsonpointer` | `2.1` | ee-supported-rhel9:/usr/local (python3.12) |
| `jsonschema` | `4.17.3` | eda-controller-rhel9:/usr (python3.12), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `jsonschema` | `4.21.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), hub-rhel9:/usr (python3.12) |
| `jsonschema` | `4.24.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `jsonschema` | `4.25.0` | gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `jsonschema` | `4.25.1` | de-supported-rhel9:/usr/local (python3.12), mcp-tools-rhel9:/usr/local (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `jsonschema` | `4.26.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `jsonschema-specifications` | `2023.12.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `jsonschema-specifications` | `2025.4.1` | gateway-rhel9:/opt/aap-gateway/venv (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `jsonschema-specifications` | `2025.9.1` | de-supported-rhel9:/usr/local (python3.12), hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), mcp-tools-rhel9:/usr/local (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `jwcrypto` | `1.5.4` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `jwcrypto` | `1.5.6` | gateway-rhel9:/opt/aap-gateway/venv (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `jxmlease` | `1.0.3` | ee-supported-rhel9:/usr/local (python3.12) |
| `kafka-python-ng` | `2.2.3` | de-supported-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `keystoneauth1` | `4.3.1` | ee-supported-rhel9:/usr/local (python3.12) |
| `knack` | `0.11.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `krb5` | `0.5.1` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `kubernetes` | `26.1.0` | eda-controller-rhel9:/usr (python3.12) |
| `kubernetes` | `29.0.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `kubernetes` | `35.0.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `launchdarkly-server-sdk` | `8.3.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `ldap-filter` | `1.0.1` | gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `libcomps` | `0.1.18` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `librt` | `0.8.1` | hub-rhel9:/usr (python3.12) |
| `lightspeed-stack` | `0.3.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `lightspeed-stack-providers` | `0.1.18` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `litellm` | `1.81.5` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `llama-stack` | `0.2.22` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `llama-stack-client` | `0.2.22` | lightspeed-chatbot-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `lockfile` | `0.12.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), de-supported-rhel9:/usr/local (python3.12), eda-controller-rhel9:/usr (python3.12), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), receptor-rhel9:/usr (python3.12) |
| `lxml` | `4.9.3` | ee-minimal-rhel9:/usr (python3.12), ee-supported-rhel9:/usr (python3.12) |
| `lxml` | `4.9.4` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `lxml` | `5.3.0` | gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `lxml` | `6.0.2` | hub-rhel9:/usr (python3.12) |
| `markdown` | `3.10.2` | hub-rhel9:/usr (python3.12) |
| `markdown` | `3.5.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `markdown-it-py` | `3.0.0` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `markdown-it-py` | `4.0.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12), mcp-tools-rhel9:/usr/local (python3.12) |
| `markupsafe` | `2.1.3` | eda-controller-rhel9:/usr (python3.12) |
| `markupsafe` | `2.1.5` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `markupsafe` | `3.0.2` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `markupsafe` | `3.0.3` | de-supported-rhel9:/usr/local (python3.12), hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `marshmallow` | `3.26.2` | hub-rhel9:/usr (python3.12) |
| `matplotlib-inline` | `0.1.7` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `mccabe` | `0.7.0` | hub-rhel9:/usr (python3.12) |
| `mcp` | `1.26.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12), mcp-tools-rhel9:/usr/local (python3.12) |
| `mdurl` | `0.1.2` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), mcp-tools-rhel9:/usr/local (python3.12) |
| `metrics-service` | `0.0.1` | metrics-service-rhel9:/usr (python3.12) |
| `metrics-utility` | `0.6.3` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `metrics-utility` | `0.7.0` | metrics-service-rhel9:/usr (python3.12) |
| `microsoft-kiota-abstractions` | `1.3.3` | ee-supported-rhel9:/usr/local (python3.12) |
| `microsoft-kiota-authentication-azure` | `1.0.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `microsoft-kiota-http` | `1.3.1` | ee-supported-rhel9:/usr/local (python3.12) |
| `microsoft-kiota-serialization-form` | `0.1.1` | ee-supported-rhel9:/usr/local (python3.12) |
| `microsoft-kiota-serialization-json` | `1.3.3` | ee-supported-rhel9:/usr/local (python3.12) |
| `microsoft-kiota-serialization-multipart` | `0.1.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `microsoft-kiota-serialization-text` | `1.0.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `microsoft-security-utilities-secret-masker` | `1.0.0b4` | ee-supported-rhel9:/usr/local (python3.12) |
| `monotonic` | `1.6` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `more-itertools` | `10.2.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `mpmath` | `1.3.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `msal` | `1.26.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `msal` | `1.32.3` | eda-controller-rhel9:/usr (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `msal-extensions` | `1.1.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `msal-extensions` | `1.2.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `msal-extensions` | `1.3.1` | eda-controller-rhel9:/usr (python3.12) |
| `msgpack` | `1.1.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `msgpack` | `1.1.2` | hub-rhel9:/usr (python3.12) |
| `msgraph-core` | `1.1.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `msgraph-sdk` | `1.6.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `msrest` | `0.7.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `msrestazure` | `0.6.4` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `msrestazure` | `0.6.4.post1` | eda-controller-rhel9:/usr (python3.12) |
| `multidict` | `6.0.4` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `multidict` | `6.0.5` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `multidict` | `6.4.4` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `multidict` | `6.7.1` | de-supported-rhel9:/usr/local (python3.12), hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `munch` | `2.5.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `mypy` | `1.19.1` | hub-rhel9:/usr (python3.12) |
| `mypy-extensions` | `1.0.0` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `mypy-extensions` | `1.1.0` | hub-rhel9:/usr (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `ncclient` | `0.6.15` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `netaddr` | `0.8.0` | gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `netaddr` | `1.2.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `netaddr` | `1.3.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `netifaces` | `0.10.9` | ee-supported-rhel9:/usr/local (python3.12) |
| `networkx` | `3.6.1` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `nh3` | `0.3.3` | hub-rhel9:/usr (python3.12) |
| `nsx-policy-python-sdk` | `4.1.2.0.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `nsx-python-sdk` | `4.1.2.0.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `nsx-vmc-aws-integration-python-sdk` | `4.1.2.0.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `nsx-vmc-policy-python-sdk` | `4.1.2.0.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `numpy` | `1.24.4` | ee-supported-rhel9:/usr (python3.12), lightspeed-rhel9:/usr (python3.12) |
| `numpy` | `2.2.6` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `numpy` | `2.4.1` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `numpy` | `2.4.2` | ee-supported-rhel9:/usr/local (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `numpy` | `2.4.3` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `oauth2client` | `4.1.3` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `oauthlib` | `3.2.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12) |
| `oauthlib` | `3.3.1` | ee-supported-rhel9:/usr/local (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12), hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `odfpy` | `1.4.1` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `opa-python-client` | `2.0.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `openai` | `2.16.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `openpyxl` | `3.1.2` | metrics-service-rhel9:/usr (python3.12) |
| `openpyxl` | `3.1.5` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `openshift` | `0.13.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `openstacksdk` | `0.56.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `opentelemetry-api` | `1.24.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `opentelemetry-api` | `1.25.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `opentelemetry-api` | `1.28.0` | hub-rhel9:/usr (python3.12) |
| `opentelemetry-api` | `1.39.1` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `opentelemetry-distro` | `0.49b0` | hub-rhel9:/usr (python3.12) |
| `opentelemetry-exporter-otlp` | `1.24.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `opentelemetry-exporter-otlp` | `1.28.0` | hub-rhel9:/usr (python3.12) |
| `opentelemetry-exporter-otlp-proto-common` | `1.24.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `opentelemetry-exporter-otlp-proto-common` | `1.28.0` | hub-rhel9:/usr (python3.12) |
| `opentelemetry-exporter-otlp-proto-common` | `1.39.1` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `opentelemetry-exporter-otlp-proto-grpc` | `1.24.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `opentelemetry-exporter-otlp-proto-grpc` | `1.28.0` | hub-rhel9:/usr (python3.12) |
| `opentelemetry-exporter-otlp-proto-http` | `1.24.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `opentelemetry-exporter-otlp-proto-http` | `1.28.0` | hub-rhel9:/usr (python3.12) |
| `opentelemetry-exporter-otlp-proto-http` | `1.39.1` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `opentelemetry-instrumentation` | `0.45b0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `opentelemetry-instrumentation` | `0.49b0` | hub-rhel9:/usr (python3.12) |
| `opentelemetry-instrumentation-django` | `0.49b0` | hub-rhel9:/usr (python3.12) |
| `opentelemetry-instrumentation-logging` | `0.45b0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `opentelemetry-instrumentation-wsgi` | `0.49b0` | hub-rhel9:/usr (python3.12) |
| `opentelemetry-proto` | `1.24.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `opentelemetry-proto` | `1.28.0` | hub-rhel9:/usr (python3.12) |
| `opentelemetry-proto` | `1.39.1` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `opentelemetry-sdk` | `1.24.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `opentelemetry-sdk` | `1.25.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `opentelemetry-sdk` | `1.28.0` | hub-rhel9:/usr (python3.12) |
| `opentelemetry-sdk` | `1.39.1` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `opentelemetry-semantic-conventions` | `0.45b0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `opentelemetry-semantic-conventions` | `0.46b0` | ee-supported-rhel9:/usr/local (python3.12) |
| `opentelemetry-semantic-conventions` | `0.49b0` | hub-rhel9:/usr (python3.12) |
| `opentelemetry-semantic-conventions` | `0.60b1` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `opentelemetry-util-http` | `0.49b0` | hub-rhel9:/usr (python3.12) |
| `oras` | `0.2.37` | ee-supported-rhel9:/usr/local (python3.12) |
| `os-service-types` | `1.7.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `ovirt-engine-sdk-python` | `4.5.2` | ee-supported-rhel9:/usr/local (python3.12) |
| `ovirt-imageio` | `2.4.6` | ee-supported-rhel9:/usr/local (python3.12) |
| `packaging` | `24.2` | eda-controller-rhel9:/usr (python3.12), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), hub-rhel9:/usr (python3.12) |
| `packaging` | `25.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), mcp-tools-rhel9:/usr/local (python3.12) |
| `packaging` | `26.0` | de-supported-rhel9:/usr/local (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), receptor-rhel9:/usr (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `pandas` | `2.2.3` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `pandas` | `2.3.2` | ee-supported-rhel9:/usr/local (python3.12) |
| `pandas` | `3.0.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `pandas` | `3.0.1` | metrics-service-rhel9:/usr (python3.12) |
| `paramiko` | `3.4.0` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `parsley` | `1.3` | hub-rhel9:/usr (python3.12) |
| `parso` | `0.8.4` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `pathspec` | `0.12.1` | hub-rhel9:/usr (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `pathspec` | `1.0.3` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `pbr` | `6.0.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `pbr` | `7.0.1` | ee-supported-rhel9:/usr/local (python3.12) |
| `pbr` | `7.0.3` | hub-rhel9:/usr (python3.12) |
| `pcp` | `5.0` | pcp:/usr (python3.9) |
| `pendulum` | `3.0.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `persisting-theory` | `1.0` | gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `pexpect` | `4.7.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `pexpect` | `4.8.0` | controller-rhel9:/usr (python3.9), ee-supported-rhel9:/usr (python3.9) |
| `pexpect` | `4.9.0` | de-supported-rhel9:/usr/local (python3.12), eda-controller-rhel9:/usr (python3.12), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), receptor-rhel9:/usr (python3.12) |
| `pickleshare` | `0.7.5` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `pillow` | `12.1.1` | hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `pip` | `23.2.1` | controller-rhel9:/usr (python3.12), eda-controller-rhel9:/usr (python3.12), ee-minimal-rhel9:/usr (python3.12), ee-supported-rhel9:/usr (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12), gateway-rhel9:/usr (python3.12), hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr (python3.12), lightspeed-rhel9:/usr (python3.12), mcp-tools-rhel9:/usr (python3.12), receptor-rhel9:/usr (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `pip` | `25.3` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `pip` | `26.0.1` | de-supported-rhel9:/usr/local (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `pkgconfig` | `1.5.5` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), hub-rhel9:/usr (python3.12) |
| `pkginfo` | `1.7.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `platformdirs` | `4.1.0` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `platformdirs` | `4.3.8` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `platformdirs` | `4.9.4` | hub-rhel9:/usr (python3.12) |
| `ply` | `3.11` | de-supported-rhel9:/usr (python3.12), ee-minimal-rhel9:/usr (python3.12), ee-supported-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr (python3.12), mcp-tools-rhel9:/usr (python3.12) |
| `podman` | `5.4.0.1` | eda-controller-rhel9:/usr (python3.12) |
| `portalocker` | `1.7.1` | ee-supported-rhel9:/usr/local (python3.12) |
| `portalocker` | `2.8.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `prometheus-client` | `0.20.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `prometheus-client` | `0.22.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `prometheus-client` | `0.24.1` | hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `prompt-toolkit` | `3.0.51` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `prompt-toolkit` | `3.0.52` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `propcache` | `0.2.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `propcache` | `0.3.1` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `propcache` | `0.4.1` | de-supported-rhel9:/usr/local (python3.12), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `proto-plus` | `1.26.1` | ee-supported-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `protobuf` | `4.25.8` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `protobuf` | `5.29.5` | gateway-rhel9:/opt/aap-gateway/venv (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `protobuf` | `5.29.6` | hub-rhel9:/usr (python3.12) |
| `protobuf` | `6.32.1` | ee-supported-rhel9:/usr/local (python3.12) |
| `protobuf` | `6.33.5` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `psutil` | `5.9.1` | ee-supported-rhel9:/usr/local (python3.12) |
| `psutil` | `5.9.8` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `psycopg` | `3.2.10` | ee-supported-rhel9:/usr/local (python3.12) |
| `psycopg` | `3.2.13` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `psycopg` | `3.2.3` | gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `psycopg` | `3.2.7` | eda-controller-rhel9:/usr (python3.12) |
| `psycopg` | `3.2.9` | hub-rhel9:/usr (python3.12) |
| `psycopg` | `3.3.0` | metrics-service-rhel9:/usr (python3.12) |
| `psycopg` | `3.3.3` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), de-supported-rhel9:/usr/local (python3.12) |
| `psycopg-c` | `3.2.3` | gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `psycopg-c` | `3.2.7` | eda-controller-rhel9:/usr (python3.12) |
| `psycopg-c` | `3.3.0` | metrics-service-rhel9:/usr (python3.12) |
| `psycopg-c` | `3.3.3` | de-supported-rhel9:/usr/local (python3.12) |
| `psycopg2` | `2.9.11` | metrics-service-rhel9:/usr (python3.12) |
| `psycopg2-binary` | `2.9.11` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `ptyprocess` | `0.6.0` | controller-rhel9:/usr (python3.9), ee-supported-rhel9:/usr (python3.9) |
| `ptyprocess` | `0.7.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), de-supported-rhel9:/usr/local (python3.12), eda-controller-rhel9:/usr (python3.12), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), receptor-rhel9:/usr (python3.12) |
| `pulp-ansible` | `0.25.5` | hub-rhel9:/usr (python3.12) |
| `pulp-container` | `2.19.8` | hub-rhel9:/usr (python3.12) |
| `pulp-glue` | `0.29.4` | hub-rhel9:/usr (python3.12) |
| `pulpcore` | `3.49.56` | hub-rhel9:/usr (python3.12) |
| `pure-eval` | `0.2.3` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `py-deviceid` | `0.1.1` | ee-supported-rhel9:/usr/local (python3.12) |
| `pyaml` | `25.5.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `pyaml` | `25.7.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `pyang` | `2.5.3` | ee-supported-rhel9:/usr/local (python3.12) |
| `pyasn1` | `0.5.0` | eda-controller-rhel9:/usr (python3.12) |
| `pyasn1` | `0.6.1` | ee-supported-rhel9:/usr/local (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `pyasn1` | `0.6.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `pyasn1` | `0.6.3` | hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `pyasn1-modules` | `0.3.0` | eda-controller-rhel9:/usr (python3.12) |
| `pyasn1-modules` | `0.4.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), ee-supported-rhel9:/usr/local (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12), hub-rhel9:/usr (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `pycares` | `4.11.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), hub-rhel9:/usr (python3.12) |
| `pycares` | `4.4.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `pycodestyle` | `2.11.1` | hub-rhel9:/usr (python3.12) |
| `pycparser` | `2.20` | de-supported-rhel9:/usr (python3.12), ee-minimal-rhel9:/usr (python3.12), ee-supported-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr (python3.12), mcp-tools-rhel9:/usr (python3.12) |
| `pycparser` | `2.21` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12) |
| `pycparser` | `2.22` | gateway-rhel9:/opt/aap-gateway/venv (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `pycparser` | `3.0` | hub-rhel9:/usr (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `pycurl` | `7.45.3` | ee-supported-rhel9:/usr/local (python3.12) |
| `pydantic` | `1.10.18` | eda-controller-rhel9:/usr (python3.12) |
| `pydantic` | `2.11.5` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `pydantic` | `2.12.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `pydantic` | `2.12.5` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), mcp-tools-rhel9:/usr/local (python3.12) |
| `pydantic-core` | `2.33.2` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `pydantic-core` | `2.41.1` | ee-supported-rhel9:/usr/local (python3.12) |
| `pydantic-core` | `2.41.5` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), mcp-tools-rhel9:/usr/local (python3.12) |
| `pydantic-settings` | `2.12.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12), mcp-tools-rhel9:/usr/local (python3.12) |
| `pydrive2` | `1.20.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `pyflakes` | `3.1.0` | hub-rhel9:/usr (python3.12) |
| `pygerduty` | `0.38.3` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `pygithub` | `2.6.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `pygithub` | `2.6.1` | eda-controller-rhel9:/usr (python3.12) |
| `pygments` | `2.17.2` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `pygments` | `2.19.1` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `pygments` | `2.19.2` | lightspeed-chatbot-rhel9:/usr/local (python3.12), mcp-tools-rhel9:/usr/local (python3.12) |
| `pygobject` | `3.40.1` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `pygtrie` | `2.5.0` | hub-rhel9:/usr (python3.12) |
| `pyinotify` | `0.9.6` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `pyjwt` | `2.10.1` | ee-supported-rhel9:/usr/local (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12), mcp-tools-rhel9:/usr/local (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `pyjwt` | `2.11.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `pyjwt` | `2.7.0` | eda-controller-rhel9:/usr (python3.12) |
| `pyjwt` | `2.8.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), hub-rhel9:/usr (python3.12) |
| `pykerberos` | `1.2.4` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `pynacl` | `1.5.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `pyopenssl` | `24.0.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `pyopenssl` | `24.2.1` | eda-controller-rhel9:/usr (python3.12) |
| `pyopenssl` | `25.1.0` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `pyopenssl` | `25.3.0` | hub-rhel9:/usr (python3.12) |
| `pyparsing` | `2.4.6` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `pyparsing` | `3.1.1` | hub-rhel9:/usr (python3.12) |
| `pyparsing` | `3.2.3` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `pyparsing` | `3.3.2` | de-supported-rhel9:/usr/local (python3.12) |
| `pypsrp` | `0.8.1` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `pyrad` | `2.4` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `pyrfc3339` | `2.0.1` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `pyrsistent` | `0.19.3` | eda-controller-rhel9:/usr (python3.12) |
| `pyrsistent` | `0.20.0` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `pysocks` | `1.7.1` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr (python3.9), ee-supported-rhel9:/usr/local (python3.12), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `pyspnego` | `0.10.2` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `python-daemon` | `3.1.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), de-supported-rhel9:/usr/local (python3.12), eda-controller-rhel9:/usr (python3.12), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), receptor-rhel9:/usr (python3.12) |
| `python-dateutil` | `2.8.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12) |
| `python-dateutil` | `2.9.0.post0` | controller-rhel9:/usr (python3.9), de-supported-rhel9:/usr/local (python3.12), eda-controller-ui-rhel9:/usr (python3.9), ee-supported-rhel9:/usr/local (python3.12), hub-rhel9:/usr (python3.12), hub-web-rhel9:/usr (python3.9), lightspeed-chatbot-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), metrics-service-rhel9:/usr (python3.12), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `python-dotenv` | `1.2.1` | lightspeed-chatbot-rhel9:/usr/local (python3.12), mcp-tools-rhel9:/usr/local (python3.12) |
| `python-dsv-sdk` | `1.0.4` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12) |
| `python-gnupg` | `0.5.2` | eda-controller-rhel9:/usr (python3.12), hub-rhel9:/usr (python3.12) |
| `python-gnupg` | `0.5.5` | ee-supported-rhel9:/usr/local (python3.12) |
| `python-ipware` | `3.0.0` | hub-rhel9:/usr (python3.12) |
| `python-jose` | `3.5.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `python-ldap` | `3.4.4` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `python-ldap` | `3.4.5` | hub-rhel9:/usr (python3.12) |
| `python-multipart` | `0.0.21` | mcp-tools-rhel9:/usr/local (python3.12) |
| `python-multipart` | `0.0.22` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `python-string-utils` | `1.0.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `python-tss-sdk` | `1.2.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `python-tss-sdk` | `1.2.3` | eda-controller-rhel9:/usr (python3.12) |
| `python3-openid` | `3.2.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12), hub-rhel9:/usr (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `python3-saml` | `1.16.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `pytokens` | `0.3.0` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `pytokens` | `0.4.1` | hub-rhel9:/usr (python3.12) |
| `pytz` | `2024.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `pytz` | `2025.2` | ee-supported-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `pyvmomi` | `8.0.3.0.1` | ee-supported-rhel9:/usr/local (python3.12) |
| `pywinrm` | `0.4.3` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `pyyaml` | `5.4.1` | controller-rhel9:/usr (python3.9), ee-supported-rhel9:/usr (python3.9) |
| `pyyaml` | `6.0.1` | controller-rhel9:/usr (python3.12), de-supported-rhel9:/usr (python3.12), ee-minimal-rhel9:/usr (python3.12), ee-supported-rhel9:/usr (python3.12), hub-rhel9:/usr (python3.12), lightspeed-rhel9:/usr (python3.12) |
| `pyyaml` | `6.0.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `pyyaml` | `6.0.3` | lightspeed-chatbot-rhel9:/usr/local (python3.12), mcp-tools-rhel9:/usr/local (python3.12), receptor-rhel9:/usr (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `pyzstd` | `0.15.10` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `receptorctl` | `1.6.4` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `redis` | `4.5.4` | eda-controller-rhel9:/usr (python3.12) |
| `redis` | `5.0.2` | hub-rhel9:/usr (python3.12) |
| `redis` | `6.2.0` | gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `redis` | `7.0.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `referencing` | `0.33.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `referencing` | `0.36.2` | gateway-rhel9:/opt/aap-gateway/venv (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `referencing` | `0.37.0` | de-supported-rhel9:/usr/local (python3.12), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), mcp-tools-rhel9:/usr/local (python3.12) |
| `regex` | `2026.1.15` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `requests` | `2.25.1` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), ee-supported-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `requests` | `2.31.0` | eda-controller-rhel9:/usr (python3.12), ee-supported-rhel9:/usr (python3.12) |
| `requests` | `2.32.3` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12), gateway-rhel9:/usr (python3.12) |
| `requests` | `2.32.5` | hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `requests` | `2.33.0` | de-supported-rhel9:/usr/local (python3.12) |
| `requests-credssp` | `2.0.0` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `requests-ntlm` | `1.2.0` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `requests-oauthlib` | `1.3.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12) |
| `requests-oauthlib` | `2.0.0` | ee-supported-rhel9:/usr/local (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12), hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `requestsexceptions` | `1.4.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `resolvelib` | `1.0.1` | de-supported-rhel9:/usr/local (python3.12), eda-controller-rhel9:/usr (python3.12), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `resolvelib` | `1.2.1` | hub-rhel9:/usr (python3.12) |
| `rich` | `13.7.0` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `rich` | `14.0.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `rich` | `14.2.0` | mcp-tools-rhel9:/usr/local (python3.12) |
| `rich` | `14.3.1` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `rpds-py` | `0.18.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `rpds-py` | `0.24.0` | de-supported-rhel9:/usr/local (python3.12), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), mcp-tools-rhel9:/usr/local (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `rpds-py` | `0.30.0` | hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `rpm` | `4.16.1.3` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `rq` | `2.6.1` | eda-controller-rhel9:/usr (python3.12) |
| `rq-scheduler` | `0.14.0` | eda-controller-rhel9:/usr (python3.12) |
| `rsa` | `4.9` | eda-controller-rhel9:/usr (python3.12) |
| `rsa` | `4.9.1` | ee-supported-rhel9:/usr/local (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `ruamel-yaml` | `0.18.12` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `ruamel-yaml` | `0.18.15` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `ruamel-yaml` | `0.19.1` | hub-rhel9:/usr (python3.12) |
| `ruamel-yaml-clib` | `0.2.12` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `ruamel-yaml-clib` | `0.2.15` | hub-rhel9:/usr (python3.12) |
| `ruamel-yaml-clib` | `0.2.8` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `s3transfer` | `0.10.4` | ee-supported-rhel9:/usr/local (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `s3transfer` | `0.13.0` | eda-controller-rhel9:/usr (python3.12) |
| `s3transfer` | `0.14.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `s3transfer` | `0.16.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), hub-rhel9:/usr (python3.12) |
| `safetensors` | `0.7.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `sansldap` | `0.1.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `scikit-learn` | `1.8.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `scipy` | `1.17.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `scp` | `0.13.3` | ee-supported-rhel9:/usr/local (python3.12) |
| `segment-analytics-python` | `2.2.3` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `segment-analytics-python` | `2.3.5` | metrics-service-rhel9:/usr (python3.12) |
| `selinux` | `3.6` | controller-rhel9:/usr (python3.9) |
| `semantic-version` | `2.10.0` | hub-rhel9:/usr (python3.12) |
| `semver` | `3.0.4` | lightspeed-chatbot-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `sentence-transformers` | `5.2.2` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `service-identity` | `21.1.0` | eda-controller-rhel9:/usr (python3.12) |
| `service-identity` | `24.1.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `service-identity` | `24.2.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `setuptools` | `53.0.0` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), ee-supported-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `setuptools` | `68.2.2` | ee-minimal-rhel9:/usr (python3.12), ee-supported-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr (python3.12) |
| `setuptools` | `78.1.1` | gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `setuptools` | `80.9.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), hub-rhel9:/usr (python3.12), lightspeed-rhel9:/usr/local (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `setuptools` | `81.0.0` | eda-controller-rhel9:/usr (python3.12) |
| `setuptools` | `82.0.1` | de-supported-rhel9:/usr/local (python3.12) |
| `shellingham` | `1.5.4` | mcp-tools-rhel9:/usr/local (python3.12) |
| `shortuuid` | `1.0.13` | mcp-tools-rhel9:/usr/local (python3.12) |
| `six` | `1.15.0` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), ee-supported-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `six` | `1.16.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12) |
| `six` | `1.17.0` | de-supported-rhel9:/usr/local (python3.12), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12), hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `slack-sdk` | `3.27.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `slack-sdk` | `3.31.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `smmap` | `5.0.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `smmap` | `5.0.3` | hub-rhel9:/usr (python3.12) |
| `sniffio` | `1.3.1` | ee-supported-rhel9:/usr/local (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `social-auth-app-django` | `5.4.1` | gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `social-auth-app-django` | `5.4.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `social-auth-app-django` | `5.4.3` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `social-auth-app-django` | `5.6.0` | hub-rhel9:/usr (python3.12) |
| `social-auth-core` | `4.5.4` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `social-auth-core` | `4.7.0` | hub-rhel9:/usr (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `sos` | `4.10.2` | controller-rhel9:/usr (python3.9), ee-supported-rhel9:/usr (python3.9) |
| `sqlalchemy` | `2.0.46` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `sqlparse` | `0.5.3` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `sqlparse` | `0.5.5` | hub-rhel9:/usr (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `sse-starlette` | `3.1.2` | mcp-tools-rhel9:/usr/local (python3.12) |
| `sse-starlette` | `3.2.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `stack-data` | `0.6.3` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `starlette` | `0.50.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12), mcp-tools-rhel9:/usr/local (python3.12) |
| `std-uritemplate` | `1.0.2` | ee-supported-rhel9:/usr/local (python3.12) |
| `stevedore` | `3.3.3` | ee-supported-rhel9:/usr/local (python3.12) |
| `subprocess-tee` | `0.4.1` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `subprocess-tee` | `0.4.2` | hub-rhel9:/usr (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `subscription-manager` | `1.29.47.1` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `supervisor` | `4.2.5` | lightspeed-rhel9:/usr/local (python3.12) |
| `supervisor` | `4.3.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), gateway-rhel9:/usr (python3.12) |
| `sympy` | `1.14.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `systemd-python` | `234` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `tablib` | `3.8.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `tablib` | `3.9.0` | hub-rhel9:/usr (python3.12) |
| `tabulate` | `0.9.0` | ee-supported-rhel9:/usr/local (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `tacacs-plus` | `1.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `tacacs-plus` | `2.6` | gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `tempora` | `5.5.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `termcolor` | `3.1.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `termcolor` | `3.3.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12), mcp-tools-rhel9:/usr/local (python3.12) |
| `textfsm` | `0.4.1` | ee-supported-rhel9:/usr/local (python3.12) |
| `threadpoolctl` | `3.6.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `tiktoken` | `0.12.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `time-machine` | `2.14.2` | ee-supported-rhel9:/usr/local (python3.12) |
| `tokenizers` | `0.22.2` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `toml` | `0.10.2` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `torch` | `2.9.1` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `tqdm` | `4.67.1` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `tqdm` | `4.67.2` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `traitlets` | `5.14.3` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `transformers` | `4.57.6` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `ttp` | `0.6.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `twilio` | `8.13.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `twisted` | `24.11.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `twisted` | `24.7.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12) |
| `txaio` | `23.1.1` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `typer` | `0.21.1` | mcp-tools-rhel9:/usr/local (python3.12) |
| `typing-extensions` | `4.12.2` | eda-controller-rhel9:/usr (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `typing-extensions` | `4.14.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `typing-extensions` | `4.15.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), de-supported-rhel9:/usr/local (python3.12), ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), mcp-tools-rhel9:/usr/local (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `typing-inspection` | `0.4.1` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `typing-inspection` | `0.4.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), ee-supported-rhel9:/usr/local (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), mcp-tools-rhel9:/usr/local (python3.12) |
| `tzdata` | `2024.1` | ee-supported-rhel9:/usr/local (python3.12) |
| `tzdata` | `2025.2` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `tzdata` | `2025.3` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), eda-controller-rhel9:/usr (python3.12) |
| `tzlocal` | `5.3.1` | metrics-service-rhel9:/usr (python3.12) |
| `uamqp` | `1.6.8` | ee-supported-rhel9:/usr (python3.12) |
| `uritemplate` | `4.1.1` | eda-controller-rhel9:/usr (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `uritemplate` | `4.2.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12), hub-rhel9:/usr (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `url-normalize` | `1.4.3` | hub-rhel9:/usr (python3.12) |
| `urllib3` | `1.26.19` | ee-minimal-rhel9:/usr (python3.12), ee-supported-rhel9:/usr (python3.12) |
| `urllib3` | `1.26.5` | controller-rhel9:/usr (python3.9), eda-controller-ui-rhel9:/usr (python3.9), ee-supported-rhel9:/usr (python3.9), hub-web-rhel9:/usr (python3.9), pcp:/usr (python3.9), postgresql-15:/usr (python3.9), redis-6:/usr (python3.9) |
| `urllib3` | `2.6.3` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), de-supported-rhel9:/usr/local (python3.12), eda-controller-rhel9:/usr (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12), gateway-rhel9:/usr (python3.12), hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `uuid6` | `2024.1.12` | hub-rhel9:/usr (python3.12) |
| `uvicorn` | `0.40.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12), mcp-tools-rhel9:/usr/local (python3.12) |
| `uvicorn-worker` | `0.4.0` | mcp-tools-rhel9:/usr/local (python3.12) |
| `uwsgi` | `2.0.28` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `uwsgi` | `2.0.29` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `uwsgi-readiness-check` | `0.2.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `uwsgitop` | `0.11` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `validators` | `0.34.0` | eda-controller-rhel9:/usr (python3.12) |
| `vapi-common-client` | `2.44.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `vapi-runtime` | `2.44.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `vcenter-bindings` | `4.2.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `vmwarecloud-aws` | `1.64.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `vmwarecloud-draas` | `1.23.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `vsphere-automation-sdk` | `1.86.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `watchdog` | `6.0.0` | de-supported-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `wcmatch` | `10.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `wcmatch` | `10.1` | hub-rhel9:/usr (python3.12) |
| `wcmatch` | `8.5` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `wcwidth` | `0.2.13` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `wcwidth` | `0.5.3` | lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `websocket-client` | `1.5.1` | eda-controller-rhel9:/usr (python3.12) |
| `websocket-client` | `1.7.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `websocket-client` | `1.8.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `websocket-client` | `1.9.0` | lightspeed-chatbot-rhel9:/usr/local (python3.12), metrics-service-rhel9:/usr (python3.12) |
| `websockets` | `15.0.1` | de-supported-rhel9:/usr/local (python3.12) |
| `whitenoise` | `6.12.0` | metrics-service-rhel9:/usr (python3.12) |
| `whitenoise` | `6.6.0` | hub-rhel9:/usr (python3.12) |
| `wrapt` | `1.16.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `wrapt` | `1.17.2` | eda-controller-rhel9:/usr (python3.12) |
| `wrapt` | `1.17.3` | ee-supported-rhel9:/usr/local (python3.12), hub-rhel9:/usr (python3.12) |
| `wrapt` | `2.1.2` | de-supported-rhel9:/usr/local (python3.12) |
| `xds-protos` | `1.68.1` | gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `xlrd` | `2.0.1` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `xlwt` | `1.3.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `xmlsec` | `1.3.13` | controller-rhel9:/var/lib/awx/venv/awx (python3.12), gateway-rhel9:/opt/aap-gateway/venv (python3.12) |
| `xmltodict` | `0.13.0` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `xxhash` | `3.4.1` | eda-controller-rhel9:/usr (python3.12) |
| `xxhash` | `3.5.0` | ee-supported-rhel9:/usr/local (python3.12) |
| `xxhash` | `3.6.0` | de-supported-rhel9:/usr/local (python3.12) |
| `yamllint` | `1.35.1` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12) |
| `yamllint` | `1.37.1` | hub-rhel9:/usr (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `yarl` | `1.17.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `yarl` | `1.18.3` | hub-rhel9:/usr (python3.12) |
| `yarl` | `1.20.0` | lightspeed-rhel9:/var/www/venv (python3.12) |
| `yarl` | `1.22.0` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12) |
| `yarl` | `1.23.0` | de-supported-rhel9:/usr/local (python3.12) |
| `zipp` | `3.17.0` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `zipp` | `3.23.0` | ee-minimal-rhel9:/usr/local (python3.12), ee-supported-rhel9:/usr/local (python3.12), hub-rhel9:/usr (python3.12), lightspeed-chatbot-rhel9:/usr/local (python3.12), lightspeed-rhel9:/var/www/venv (python3.12) |
| `zope-interface` | `6.0` | eda-controller-rhel9:/usr (python3.12) |
| `zope-interface` | `6.2` | controller-rhel9:/var/lib/awx/venv/awx (python3.12) |
| `zope-interface` | `7.2` | lightspeed-rhel9:/var/www/venv (python3.12) |

## Image Details

### controller-rhel9

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-26/controller-rhel9` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/controller-rhel9.tar.gz` |
| Labels `version` / `release` | `4.7.10` / `1773939694` |
| Image ID | `sha256:c1caed7cb74719d58e40213a29ddf746e11c2dc479c2c9fb7846a01e056a1767` |
| Build date | 2026-03-24T16:14:57Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.7 (Plow) |
| Python | 3.9, 3.12 |
| Ansible Core | N/A |

<details><summary>RPM packages (242)</summary>

```text
acl 2.3.1-4.el9
alternatives 1.24-2.el9
apr 1.7.0-12.el9_3
apr-util 1.6.1-23.el9
apr-util-bdb 1.6.1-23.el9
attr 2.5.1-3.el9
audit-libs 3.1.5-7.el9
basesystem 11-13.el9
bash 5.1.8-9.el9
bzip2-libs 1.0.8-10.el9_5
c-ares 1.19.1-2.el9_4
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crontabs 1.11-27.20190603git.el9_0
crun 1.26-1.el9_7
crypto-policies 20250905-1.git377cc42.el9_7
curl-minimal 7.76.1-35.el9_7.3
cyrus-sasl-lib 2.1.27-22.el9
dbus 1.12.20-8.el9
dbus-broker 28-7.el9
dbus-common 1.12.20-8.el9
dbus-libs 1.12.20-8.el9
dejavu-sans-fonts 2.37-18.el9
dmidecode 3.6-1.el9
dnf-data 4.14.0-31.el9
elfutils-default-yama-scope 0.193-1.el9
elfutils-libelf 0.193-1.el9
elfutils-libs 0.193-1.el9
expat 2.5.0-5.el9_7.1
file-libs 5.39-16.el9
filesystem 3.16-5.el9
findutils 4.8.0-7.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdbm-libs 1.23-1.el9
git-core 2.47.3-1.el9_6
git-lfs 3.6.1-7.el9_7
glib2 2.68.4-18.el9_7.1
glibc 2.34-231.el9_7.10
glibc-common 2.34-231.el9_7.10
glibc-langpack-en 2.34-231.el9_7.10
glibc-minimal-langpack 2.34-231.el9_7.10
gmp 6.2.0-13.el9
gnupg2 2.3.3-5.el9_7
gnutls 3.8.3-10.el9_7
gobject-introspection 1.68.0-11.el9
gpg-pubkey 5a6340b3-6229229e
gpg-pubkey fd431d51-4ae0493b
gpgme 1.15.1-6.el9
grep 3.6-5.el9
gzip 1.12-1.el9
hostname 3.23-6.el9
ima-evm-utils 1.6.2-2.el9
iproute 6.14.0-2.el9
json-c 0.14-11.el9
json-glib 1.6.6-1.el9
keyutils 1.6.3-1.el9
keyutils-libs 1.6.3-1.el9
kmod-libs 28-11.el9
krb5-libs 1.21.1-8.el9_6
krb5-pkinit 1.21.1-8.el9_6
krb5-workstation 1.21.1-8.el9_6
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
less 590-6.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-7.el9_7
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9_7
libbpf 1.5.0-2.el9
libcap 2.48-10.el9
libcap-ng 0.8.2-7.el9
libcbor 0.7.0-5.el9
libcom_err 1.46.5-8.el9
libcomps 0.1.18-1.el9
libcurl-minimal 7.76.1-35.el9_7.3
libdb 5.3.28-57.el9_6
libdnf 0.69.0-17.el9_7
libdnf-plugin-subscription-manager 1.29.47.1-1.el9_7
libeconf 0.4.1-4.el9
libedit 3.1-38.20210216cvs.el9
libestr 0.1.11-4.el9
libevent 2.1.12-8.el9_4
libfastjson 0.99.9-5.el9
libfdisk 2.37.4-21.el9_7
libffi 3.4.2-8.el9
libfido2 1.13.0-2.el9
libgcc 11.5.0-11.el9
libgcrypt 1.10.0-11.el9
libgomp 11.5.0-11.el9
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libkadm5 1.21.1-8.el9_6
libksba 1.5.1-7.el9
libmnl 1.0.4-16.el9_4
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9_7
libnghttp2 1.43.0-6.el9
libnsl2 2.0.0-1.el9
libpeas 1.30.0-4.el9
libpwquality 1.4.4-8.el9
librepo 1.14.5-3.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libseccomp 2.5.2-2.el9
libselinux 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-3.el9
libserf 1.3.9-27.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9_7
libsolv 0.7.24-3.el9
libss 1.46.5-8.el9
libstdc++ 11.5.0-11.el9
libtasn1 4.16.0-9.el9
libtirpc 1.3.3-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libusbx 1.0.26-1.el9
libuser 0.63-17.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9_7
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-14.el9_7
libxslt 1.1.34-13.el9_6
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
logrotate 3.18.0-12.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
microdnf 3.9.1-3.el9
mpdecimal 2.5.1-3.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-12.20210508.el9
ncurses-libs 6.2-12.20210508.el9
nettle 3.10.1-1.el9
nginx 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
nginx-core 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
nginx-filesystem 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
npth 1.6-8.el9
openldap 2.6.8-4.el9
openssh 8.7p1-47.el9_7
openssh-clients 8.7p1-47.el9_7
openssl 3.5.1-7.el9_7
openssl-fips-provider 3.0.7-8.el9
openssl-fips-provider-so 3.0.7-8.el9
openssl-libs 3.5.1-7.el9_7
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pam 1.5.1-26.el9_6
passwd 0.80-12.el9
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
podman-remote 5.6.0-14.el9_7
popt 1.18-8.el9
postgresql 15.17-1.module+el9.7.0+24029+ef6a2953
postgresql-private-libs 15.17-1.module+el9.7.0+24029+ef6a2953
psmisc 23.4-3.el9
python3 3.9.25-3.el9_7.1
python3-chardet 4.0.0-5.el9
python3-cloud-what 1.29.47.1-1.el9_7
python3-dateutil 2.9.0.post0-1.el9_7
python3-dbus 1.2.18-2.el9
python3-decorator 4.4.2-6.el9
python3-dnf 4.14.0-31.el9
python3-dnf-plugins-core 4.3.0-24.el9_7
python3-gobject-base 3.40.1-6.el9
python3-gobject-base-noarch 3.40.1-6.el9
python3-gpg 1.15.1-6.el9
python3-hawkey 0.69.0-17.el9_7
python3-idna 2.10-7.el9_4.1
python3-iniparse 0.4-45.el9
python3-inotify 0.9.6-25.el9
python3-libcomps 0.1.18-1.el9
python3-libdnf 0.69.0-17.el9_7
python3-librepo 1.14.5-3.el9
python3-libs 3.9.25-3.el9_7.1
python3-libselinux 3.6-3.el9
python3-libsemanage 3.6-5.el9_6
python3-pexpect 4.8.0-7.el9
python3-pip-wheel 21.3.1-1.el9
python3-ptyprocess 0.6.0-12.el9
python3-pysocks 1.7.1-12.el9
python3-pyyaml 5.4.1-6.el9
python3-requests 2.25.1-10.el9_6
python3-rpm 4.16.1.3-39.el9
python3-setuptools 53.0.0-15.el9
python3-setuptools-wheel 53.0.0-15.el9
python3-six 1.15.0-9.el9
python3-subscription-manager-rhsm 1.29.47.1-1.el9_7
python3-systemd 234-19.el9
python3-urllib3 1.26.5-6.el9_7.1
python3.12 3.12.12-4.el9_7.1
python3.12-libs 3.12.12-4.el9_7.1
python3.12-pip 23.2.1-5.el9
python3.12-pip-wheel 23.2.1-5.el9
python3.12-pyyaml 6.0.1-2.el9
readline 8.1-4.el9
redhat-logos-httpd 90.5-1.el9_6.1
redhat-release 9.7-0.7.el9
redis 6.2.20-3.el9_7
rootfiles 8.1-35.el9
rpm 4.16.1.3-39.el9
rpm-build-libs 4.16.1.3-39.el9
rpm-libs 4.16.1.3-39.el9
rpm-sign-libs 4.16.1.3-39.el9
rsync 3.2.5-3.el9
rsyslog 8.2506.0-2.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-15.el9
shadow-utils-subid 4.9-15.el9
sos 4.10.2-2.el9_7
sqlite-libs 3.34.1-9.el9_7
sshpass 1.09-4.el9
subscription-manager 1.29.47.1-1.el9_7
subscription-manager-rhsm-certificates 20220623-1.el9
subversion 1.14.1-7.el9
subversion-libs 1.14.1-7.el9
systemd 252-55.el9_7.7
systemd-libs 252-55.el9_7.7
systemd-pam 252-55.el9_7.7
systemd-rpm-macros 252-55.el9_7.7
tpm2-tss 3.2.3-1.el9
tzdata 2026a-1.el9
usermode 1.114-7.el9
utf8proc 2.6.1-4.el9
util-linux 2.37.4-21.el9_7
util-linux-core 2.37.4-21.el9_7
virt-what 1.27-2.el9
which 2.21-30.el9_6
xmlsec1 1.2.29-13.el9
xmlsec1-openssl 1.2.29-13.el9
xz-libs 5.2.5-8.el9_0
yajl 2.1.0-25.el9
zlib 1.2.11-40.el9
```

</details>

<details><summary>Python packages: /usr (python3.12) (2)</summary>

```text
pip 23.2.1
PyYAML 6.0.1
```

</details>

<details><summary>Python packages: /usr (python3.9) (23)</summary>

```text
chardet 4.0.0
dbus-python 1.2.18
decorator 4.4.2
gpg 1.15.1
idna 2.10
iniparse 0.4
libcomps 0.1.18
pexpect 4.8.0
ptyprocess 0.6.0
PyGObject 3.40.1
pyinotify 0.9.6
PySocks 1.7.1
python-dateutil 2.9.0.post0
PyYAML 5.4.1
requests 2.25.1
rpm 4.16.1.3
selinux 3.6
setuptools 53.0.0
six 1.15.0
sos 4.10.2
subscription-manager 1.29.47.1
systemd-python 234
urllib3 1.26.5
```

</details>

<details><summary>Python packages: /var/lib/awx/venv/awx (python3.12) (193)</summary>

```text
adal 1.2.7
aiodns 3.6.1
aiofiles 24.1.0
aiohappyeyeballs 2.6.1
aiohttp 3.13.3
aiohttp_retry 2.8.3
aiosignal 1.4.0
annotated-types 0.6.0
ansible-runner 2.4.2
ansiconv 1.0.0
asciichartpy 1.5.7
asgiref 3.11.0
asn1 2.7.0
attrs 23.2.0
autobahn 23.6.2
autocommand 2.2.2
Automat 22.10.0
awx 4.7.10
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
cachetools 7.0.0
certifi 2038.12.31
cffi 1.16.0
channels 4.3.2
channels_redis 4.2.0
charset-normalizer 3.3.2
click 8.1.7
constantly 23.10.4
cryptography 42.0.8
daphne 4.2.1
defusedxml 0.7.1
Deprecated 1.2.14
dispatcherd 2026.1.27
distro 1.9.0
Django 5.2.10
django-ansible-base 2.6.20260325
django-auth-ldap 5.1.0
django-cors-headers 4.3.1
django-crum 0.7.9
django-extensions 3.2.3
django-flags 5.1.0
django-guid 3.5.2
django-oauth-toolkit 1.7.1
django-pglocks 1.0.4
django-polymorphic 4.11.1
django-radius 1.5.1
django-solo 2.2.0
djangorestframework 3.15.2
djangorestframework-yaml 2.0.0
drf-spectacular 0.29.0
dumb-init 1.2.5.post1
durationpy 0.10
dynaconf 3.2.10
enum-compat 0.0.3
et_xmlfile 2.0.0
filelock 3.13.1
frozenlist 1.8.0
gitdb 4.0.11
GitPython 3.1.42
google-auth 2.47.0
googleapis-common-protos 1.63.0
grpcio 1.68.1
hiredis 3.2.1
hyperlink 21.0.0
idna 3.10
importlib_metadata 6.2.1
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
jwcrypto 1.5.4
kubernetes 35.0.0
lockfile 0.12.2
lxml 4.9.4
Markdown 3.5.2
MarkupSafe 2.1.5
metrics_utility 0.6.3
more-itertools 10.2.0
msal 1.26.0
msal-extensions 1.1.0
msgpack 1.1.1
msrest 0.7.1
msrestazure 0.6.4
multidict 6.0.5
netaddr 1.2.1
numpy 2.4.3
oauthlib 3.2.2
opa-python-client 2.0.2
openpyxl 3.1.5
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
pandas 2.2.3
pbr 6.0.0
pexpect 4.7.0
pip 25.3
pkgconfig 1.5.5
portalocker 2.8.2
prometheus_client 0.20.0
propcache 0.2.0
protobuf 4.25.8
psutil 5.9.8
psycopg 3.3.3
ptyprocess 0.7.0
pyasn1 0.6.2
pyasn1_modules 0.4.2
pycares 4.11.0
pycparser 2.21
pydantic 2.12.5
pydantic_core 2.41.5
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
python3-saml 1.16.0
pytz 2024.1
PyYAML 6.0.2
pyzstd 0.15.10
receptorctl 1.6.4
redis 7.0.1
referencing 0.33.0
requests 2.32.3
requests-oauthlib 1.3.1
rpds-py 0.18.0
s3transfer 0.16.0
service-identity 24.1.0
setuptools 80.9.0
six 1.16.0
slack_sdk 3.27.0
smmap 5.0.1
social-auth-app-django 5.4.2
social-auth-core 4.5.4
sqlparse 0.5.3
supervisor 4.3.0
tacacs_plus 1.0
tempora 5.5.1
twilio 8.13.0
Twisted 24.7.0
txaio 23.1.1
typing-inspection 0.4.2
typing_extensions 4.15.0
tzdata 2025.3
uritemplate 4.2.0
urllib3 2.6.3
uWSGI 2.0.28
uwsgitop 0.11
websocket-client 1.7.0
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

### de-supported-rhel9

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-26/de-supported-rhel9` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/de-supported-rhel9.tar.gz` |
| Labels `version` / `release` | `1.2.2` / `1773939694` |
| Image ID | `sha256:7b161bf90dc4209054ca2b8c3f808bb59f1187e11d5a38256a5e569b7cd04de5` |
| Build date | 2026-03-26T01:57:24Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.7 (Plow) |
| Python | 3.9, 3.12 |
| Ansible Core | 2.16.18 |

<details><summary>RPM packages (159)</summary>

```text
alsa-lib 1.2.14-1.el9
alternatives 1.24-2.el9
audit-libs 3.1.5-7.el9
avahi-libs 0.8-23.el9
basesystem 11-13.el9
bash 5.1.8-9.el9
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
copy-jdk-configs 4.0-3.el9
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crypto-policies 20250905-1.git377cc42.el9_7
crypto-policies-scripts 20250905-1.git377cc42.el9_7
cups-libs 2.3.3op2-34.el9_7.2
curl-minimal 7.76.1-35.el9_7.3
cyrus-sasl-lib 2.1.27-22.el9
dbus-libs 1.12.20-8.el9
dejavu-sans-fonts 2.37-18.el9
dnf-data 4.14.0-31.el9
expat 2.5.0-5.el9_7.1
file-libs 5.39-16.el9
filesystem 3.16-5.el9
findutils 4.8.0-7.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdbm-libs 1.23-1.el9
glib2 2.68.4-18.el9_7.1
glibc 2.34-231.el9_7.10
glibc-common 2.34-231.el9_7.10
glibc-minimal-langpack 2.34-231.el9_7.10
gmp 6.2.0-13.el9
gnupg2 2.3.3-5.el9_7
gnutls 3.8.3-10.el9_7
gobject-introspection 1.68.0-11.el9
gpg-pubkey 5a6340b3-6229229e
gpg-pubkey fd431d51-4ae0493b
gpgme 1.15.1-6.el9
grep 3.6-5.el9
gzip 1.12-1.el9
java-17-openjdk-headless 17.0.18.0.8-1.el9
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
libacl 2.3.1-4.el9
libarchive 3.5.3-7.el9_7
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9_7
libcap 2.48-10.el9
libcap-ng 0.8.2-7.el9
libcom_err 1.46.5-8.el9
libcurl-minimal 7.76.1-35.el9_7.3
libdb 5.3.28-57.el9_6
libdnf 0.69.0-17.el9_7
libeconf 0.4.1-4.el9
libevent 2.1.12-8.el9_4
libffi 3.4.2-8.el9
libgcc 11.5.0-11.el9
libgcrypt 1.10.0-11.el9
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libkadm5 1.21.1-8.el9_6
libksba 1.5.1-7.el9
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9_7
libnghttp2 1.43.0-6.el9
libnsl2 2.0.0-1.el9
libpeas 1.30.0-4.el9
libpq 13.23-1.el9_7
libpwquality 1.4.4-8.el9
librepo 1.14.5-3.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libselinux 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-3.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9_7
libsolv 0.7.24-3.el9
libss 1.46.5-8.el9
libstdc++ 11.5.0-11.el9
libtasn1 4.16.0-9.el9
libtirpc 1.3.3-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libusbx 1.0.26-1.el9
libuuid 2.37.4-21.el9_7
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-14.el9_7
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
lksctp-tools 1.0.19-3.el9_4
lua 5.4.4-4.el9
lua-libs 5.4.4-4.el9
lua-posix 35.0-8.el9
lz4-libs 1.9.3-5.el9
microdnf 3.9.1-3.el9
mpdecimal 2.5.1-3.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-12.20210508.el9
ncurses-libs 6.2-12.20210508.el9
nettle 3.10.1-1.el9
npth 1.6-8.el9
nspr 4.36.0-8.el9_4
nss 3.112.0-8.el9_4
nss-softokn 3.112.0-8.el9_4
nss-softokn-freebl 3.112.0-8.el9_4
nss-sysinit 3.112.0-8.el9_4
nss-util 3.112.0-8.el9_4
openldap 2.6.8-4.el9
openssl 3.5.1-7.el9_7
openssl-fips-provider 3.0.7-8.el9
openssl-fips-provider-so 3.0.7-8.el9
openssl-libs 3.5.1-7.el9_7
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pam 1.5.1-26.el9_6
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
popt 1.18-8.el9
python3 3.9.25-3.el9_7.1
python3-libs 3.9.25-3.el9_7.1
python3-pip-wheel 21.3.1-1.el9
python3-setuptools-wheel 53.0.0-15.el9
python3.12 3.12.12-4.el9_7.1
python3.12-cffi 1.16.0-2.el9
python3.12-cryptography 42.0.5-2.el9ap
python3.12-drools-jpy 0.3.14-2.el9ap
python3.12-drools-jpy-jar 1.0.11-2.Final_redhat_00001.1.el9ap
python3.12-jpy 0.15.0-2.el9ap
python3.12-libs 3.12.12-4.el9_7.1
python3.12-pip-wheel 23.2.1-5.el9
python3.12-ply 3.11-2.el9
python3.12-pycparser 2.20-2.el9
python3.12-pyyaml 6.0.1-2.el9
readline 8.1-4.el9
redhat-release 9.7-0.7.el9
rootfiles 8.1-35.el9
rpm 4.16.1.3-39.el9
rpm-libs 4.16.1.3-39.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-15.el9
sqlite-libs 3.34.1-9.el9_7
systemd-libs 252-55.el9_7.7
tzdata 2026a-1.el9
tzdata-java 2026a-1.el9
xz-libs 5.2.5-8.el9_0
zlib 1.2.11-40.el9
```

</details>

<details><summary>Python packages: /usr (python3.12) (7)</summary>

```text
cffi 1.16.0
cryptography 42.0.5
drools-jpy 0.3.14
jpy 0.15.0
ply 3.11
pycparser 2.20
PyYAML 6.0.1
```

</details>

<details><summary>Python packages: /usr/local (python3.12) (55)</summary>

```text
aiobotocore 3.3.0
aiohappyeyeballs 2.6.1
aiohttp 3.13.3
aioitertools 0.13.0
aiokafka 0.13.0
aiosignal 1.4.0
ansible-core 2.16.18
ansible-runner 2.4.2
ansible_rulebook 1.2.2
async-timeout 5.0.1
attrs 26.1.0
azure-core 1.39.0
azure-servicebus 7.14.3
botocore 1.42.70
certifi 2026.2.25
charset-normalizer 3.4.6
decorator 5.2.1
dpath 2.2.0
dumb-init 1.2.5.post1
frozenlist 1.8.0
gssapi 1.11.1
idna 3.11
isodate 0.7.2
janus 1.2.0
Jinja2 3.1.6
jmespath 1.1.0
jsonschema 4.25.1
jsonschema-specifications 2025.9.1
kafka-python-ng 2.2.3
lockfile 0.12.2
MarkupSafe 3.0.3
multidict 6.7.1
packaging 26.0
pexpect 4.9.0
pip 26.0.1
propcache 0.4.1
psycopg 3.3.3
psycopg-c 3.3.3
ptyprocess 0.7.0
pyparsing 3.3.2
python-daemon 3.1.2
python-dateutil 2.9.0.post0
referencing 0.37.0
requests 2.33.0
resolvelib 1.0.1
rpds-py 0.24.0
setuptools 82.0.1
six 1.17.0
typing_extensions 4.15.0
urllib3 2.6.3
watchdog 6.0.0
websockets 15.0.1
wrapt 2.1.2
xxhash 3.6.0
yarl 1.23.0
```

</details>

<details><summary>Ansible collections (4)</summary>

```text
amazon.aws 11.1.0
ansible.eda 2.11.0
azure.azcollection 3.7.0
redhat.insights_eda 1.2.0
```

</details>

[Back to top](#contents)

### eda-controller-rhel9

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-26/eda-controller-rhel9` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/eda-controller-rhel9.tar.gz` |
| Labels `version` / `release` | `1.2.7` / `1773939694` |
| Image ID | `sha256:9158edd8a3edd83161a9e78bcb4e77d59533b11bf2ac0873aae1fdc2b3eb2fd5` |
| Build date | 2026-03-23T09:33:53Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.7 (Plow) |
| Python | 3.12 |
| Ansible Core | 2.16.15 |

<details><summary>RPM packages (137)</summary>

```text
alternatives 1.24-2.el9
audit-libs 3.1.5-7.el9
basesystem 11-13.el9
bash 5.1.8-9.el9
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crypto-policies 20250905-1.git377cc42.el9_7
curl-minimal 7.76.1-35.el9_7.3
cyrus-sasl-lib 2.1.27-22.el9
dejavu-sans-fonts 2.37-18.el9
dnf-data 4.14.0-31.el9
expat 2.5.0-5.el9_7.1
file-libs 5.39-16.el9
filesystem 3.16-5.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdbm-libs 1.23-1.el9
git-core 2.47.3-1.el9_6
glib2 2.68.4-18.el9_7.1
glibc 2.34-231.el9_7.10
glibc-common 2.34-231.el9_7.10
glibc-langpack-en 2.34-231.el9_7.10
glibc-minimal-langpack 2.34-231.el9_7.10
gmp 6.2.0-13.el9
gnupg2 2.3.3-5.el9_7
gnutls 3.8.3-10.el9_7
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
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
less 590-6.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-7.el9_7
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9_7
libcap 2.48-10.el9
libcap-ng 0.8.2-7.el9
libcbor 0.7.0-5.el9
libcom_err 1.46.5-8.el9
libcurl-minimal 7.76.1-35.el9_7.3
libdb 5.3.28-57.el9_6
libdnf 0.69.0-17.el9_7
libeconf 0.4.1-4.el9
libedit 3.1-38.20210216cvs.el9
libevent 2.1.12-8.el9_4
libfdisk 2.37.4-21.el9_7
libffi 3.4.2-8.el9
libfido2 1.13.0-2.el9
libgcc 11.5.0-11.el9
libgcrypt 1.10.0-11.el9
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libksba 1.5.1-7.el9
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9_7
libnghttp2 1.43.0-6.el9
libnsl2 2.0.0-1.el9
libpeas 1.30.0-4.el9
libpq 13.23-1.el9_7
libpwquality 1.4.4-8.el9
librepo 1.14.5-3.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libselinux 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-3.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9_7
libsolv 0.7.24-3.el9
libstdc++ 11.5.0-11.el9
libtasn1 4.16.0-9.el9
libtirpc 1.3.3-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libusbx 1.0.26-1.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9_7
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-14.el9_7
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
microdnf 3.9.1-3.el9
mpdecimal 2.5.1-3.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-12.20210508.el9
ncurses-libs 6.2-12.20210508.el9
nettle 3.10.1-1.el9
npth 1.6-8.el9
openldap 2.6.8-4.el9
openssh 8.7p1-47.el9_7
openssh-clients 8.7p1-47.el9_7
openssl 3.5.1-7.el9_7
openssl-fips-provider 3.0.7-8.el9
openssl-fips-provider-so 3.0.7-8.el9
openssl-libs 3.5.1-7.el9_7
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pam 1.5.1-26.el9_6
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
popt 1.18-8.el9
python3.12 3.12.12-4.el9_7.1
python3.12-libs 3.12.12-4.el9_7.1
python3.12-pip 23.2.1-5.el9
python3.12-pip-wheel 23.2.1-5.el9
readline 8.1-4.el9
redhat-release 9.7-0.7.el9
rootfiles 8.1-35.el9
rpm 4.16.1.3-39.el9
rpm-libs 4.16.1.3-39.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-15.el9
sqlite-libs 3.34.1-9.el9_7
systemd-libs 252-55.el9_7.7
tzdata 2026a-1.el9
util-linux 2.37.4-21.el9_7
util-linux-core 2.37.4-21.el9_7
xz-libs 5.2.5-8.el9_0
zlib 1.2.11-40.el9
```

</details>

<details><summary>Python packages: /usr (python3.12) (108)</summary>

```text
aap-eda 1.2.7
adal 1.2.7
ansible-core 2.16.15
ansible-runner 2.4.1
asgiref 3.11.0
attrs 23.1.0
autobahn 24.4.2
Automat 22.10.0
awx-plugins-core 0.0.1a10
awx_plugins.interfaces 0.0.1a5
azure-core 1.34.0
azure-identity 1.23.0
azure-keyvault 4.2.0
azure-keyvault-keys 4.11.0
azure-keyvault-secrets 4.10.0
boto3 1.38.38
botocore 1.38.38
cachetools 3.1.1
certifi 2038.12.31
cffi 1.15.1
channels 4.3.2
charset-normalizer 3.1.0
click 8.1.3
constantly 23.10.4
croniter 1.3.14
crontab 1.0.5
cryptography 42.0.8
daphne 4.0.0
Deprecated 1.2.18
dispatcherd 2025.5.19
distro 1.9.0
Django 5.2.9
django-ansible-base 2.6.20260325
django-crum 0.7.9
django-filter 25.2
django-flags 5.0.13
django-redis 5.4.0
django-rq 3.2.2
djangorestframework 3.15.1
drf-spectacular 0.29.0
dumb-init 1.2.5.post1
dynaconf 3.2.10
ecdsa 0.18.0
freezegun 1.5.5
google-auth 2.17.3
gunicorn 22.0.0
hyperlink 21.0.0
idna 3.4
incremental 24.7.2
inflection 0.5.1
insights-analytics-collector 0.3.2
isodate 0.7.2
Jinja2 3.1.3
jmespath 1.0.1
jsonschema 4.17.3
kubernetes 26.1.0
lockfile 0.12.2
MarkupSafe 2.1.3
msal 1.32.3
msal-extensions 1.3.1
msrest 0.7.1
msrestazure 0.6.4.post1
oauthlib 3.2.2
packaging 24.2
pexpect 4.9.0
pip 23.2.1
podman 5.4.0.1
psycopg 3.2.7
psycopg-c 3.2.7
ptyprocess 0.7.0
pyasn1 0.5.0
pyasn1_modules 0.3.0
pycparser 2.21
pydantic 1.10.18
PyGithub 2.6.1
PyJWT 2.7.0
PyNaCl 1.5.0
pyOpenSSL 24.2.1
pyrsistent 0.19.3
python-daemon 3.1.2
python-dateutil 2.8.2
python-dsv-sdk 1.0.4
python-gnupg 0.5.2
python-tss-sdk 1.2.3
PyYAML 6.0.2
redis 4.5.4
requests 2.31.0
requests-oauthlib 1.3.1
resolvelib 1.0.1
rq 2.6.1
rq-scheduler 0.14.0
rsa 4.9
s3transfer 0.13.0
service-identity 21.1.0
setuptools 81.0.0
six 1.16.0
sqlparse 0.5.3
Twisted 24.7.0
txaio 23.1.1
typing_extensions 4.12.2
tzdata 2025.3
uritemplate 4.1.1
urllib3 2.6.3
validators 0.34.0
websocket-client 1.5.1
wrapt 1.17.2
xxhash 3.4.1
zope.interface 6.0
```

</details>

[Back to top](#contents)

### eda-controller-ui-rhel9

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-26/eda-controller-ui-rhel9` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/eda-controller-ui-rhel9.tar.gz` |
| Labels `version` / `release` | `1.2.7` / `1774456665` |
| Image ID | `sha256:94116fd7c04b84757adc07fd9f27716d9171881ea640b00523bbfc81ec9305e7` |
| Build date | 2026-03-26T00:15:06Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.7 (Plow) |
| Python | 3.9 |
| Ansible Core | N/A |

<details><summary>RPM packages (294)</summary>

```text
acl 2.3.1-4.el9
alternatives 1.24-2.el9
attr 2.5.1-3.el9
audit-libs 3.1.5-7.el9
basesystem 11-13.el9
bash 5.1.8-9.el9
bsdtar 3.5.3-7.el9_7
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crypto-policies 20250905-1.git377cc42.el9_7
crypto-policies-scripts 20250905-1.git377cc42.el9_7
curl-minimal 7.76.1-35.el9_7.3
cyrus-sasl-lib 2.1.27-22.el9
dbus 1.12.20-8.el9
dbus-broker 28-7.el9
dbus-common 1.12.20-8.el9
dbus-libs 1.12.20-8.el9
dejavu-sans-fonts 2.37-18.el9
dmidecode 3.6-1.el9
dnf 4.14.0-31.el9
dnf-data 4.14.0-31.el9
elfutils-default-yama-scope 0.193-1.el9
elfutils-libelf 0.193-1.el9
elfutils-libs 0.193-1.el9
environment-modules 5.3.0-2.el9
expat 2.5.0-5.el9_7.1
file-libs 5.39-16.el9
filesystem 3.16-5.el9
findutils 4.8.0-7.el9
fontconfig 2.14.0-2.el9_1
fonts-filesystem 2.0.5-7.el9.1
freetype 2.10.4-10.el9_5
gawk 5.1.0-6.el9
gd 2.3.2-3.el9
gdb-gdbserver 16.3-2.el9
gdbm-libs 1.23-1.el9
gettext 0.21-8.el9
gettext-libs 0.21-8.el9
glib2 2.68.4-18.el9_7.1
glibc 2.34-231.el9_7.10
glibc-common 2.34-231.el9_7.10
glibc-langpack-en 2.34-231.el9_7.10
glibc-locale-source 2.34-231.el9_7.10
glibc-minimal-langpack 2.34-231.el9_7.10
gmp 6.2.0-13.el9
gnupg2 2.3.3-5.el9_7
gnutls 3.8.3-10.el9_7
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
ima-evm-utils 1.6.2-2.el9
iproute 6.14.0-2.el9
jbigkit-libs 2.1-23.el9
json-c 0.14-11.el9
json-glib 1.6.6-1.el9
keyutils 1.6.3-1.el9
keyutils-libs 1.6.3-1.el9
kmod-libs 28-11.el9
krb5-libs 1.21.1-8.el9_6
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
less 590-6.el9
libX11 1.7.0-11.el9
libX11-common 1.7.0-11.el9
libXau 1.0.9-8.el9
libXpm 3.5.13-10.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-7.el9_7
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9_7
libbpf 1.5.0-2.el9
libbrotli 1.0.9-9.el9_7
libcap 2.48-10.el9
libcap-ng 0.8.2-7.el9
libcom_err 1.46.5-8.el9
libcomps 0.1.18-1.el9
libcurl-minimal 7.76.1-35.el9_7.3
libdb 5.3.28-57.el9_6
libdnf 0.69.0-17.el9_7
libdnf-plugin-subscription-manager 1.29.47.1-1.el9_7
libeconf 0.4.1-4.el9
libevent 2.1.12-8.el9_4
libfdisk 2.37.4-21.el9_7
libffi 3.4.2-8.el9
libgcc 11.5.0-11.el9
libgcrypt 1.10.0-11.el9
libgomp 11.5.0-11.el9
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libjpeg-turbo 2.0.90-7.el9
libksba 1.5.1-7.el9
libmnl 1.0.4-16.el9_4
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9_7
libnghttp2 1.43.0-6.el9
libpipeline 1.5.3-4.el9
libpng 1.6.37-12.el9_7.2
libpwquality 1.4.4-8.el9
librepo 1.14.5-3.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libseccomp 2.5.2-2.el9
libselinux 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-3.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9_7
libsolv 0.7.24-3.el9
libstdc++ 11.5.0-11.el9
libtasn1 4.16.0-9.el9
libtiff 4.4.0-15.el9_7.2
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libuser 0.63-17.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9_7
libverto 0.3.2-3.el9
libwebp 1.2.0-8.el9_3
libxcb 1.13.1-9.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-14.el9_7
libxslt 1.1.34-13.el9_6
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
logrotate 3.18.0-12.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
man-db 2.9.3-9.el9
mpfr 4.1.0-7.el9
ncurses 6.2-12.20210508.el9
ncurses-base 6.2-12.20210508.el9
ncurses-libs 6.2-12.20210508.el9
nettle 3.10.1-1.el9
nginx 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
nginx-all-modules 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
nginx-core 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
nginx-filesystem 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
nginx-mod-http-image-filter 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
nginx-mod-http-perl 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
nginx-mod-http-xslt-filter 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
nginx-mod-mail 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
nginx-mod-stream 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
npth 1.6-8.el9
nss_wrapper-libs 1.1.13-1.el9
openldap 2.6.8-4.el9
openssl 3.5.1-7.el9_7
openssl-fips-provider 3.0.7-8.el9
openssl-fips-provider-so 3.0.7-8.el9
openssl-libs 3.5.1-7.el9_7
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
perl-Net-SSLeay 1.94-3.el9
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
psmisc 23.4-3.el9
python3 3.9.25-3.el9_7.1
python3-chardet 4.0.0-5.el9
python3-cloud-what 1.29.47.1-1.el9_7
python3-dateutil 2.9.0.post0-1.el9_7
python3-dbus 1.2.18-2.el9
python3-decorator 4.4.2-6.el9
python3-dnf 4.14.0-31.el9
python3-dnf-plugins-core 4.3.0-24.el9_7
python3-gobject-base 3.40.1-6.el9
python3-gobject-base-noarch 3.40.1-6.el9
python3-gpg 1.15.1-6.el9
python3-hawkey 0.69.0-17.el9_7
python3-idna 2.10-7.el9_4.1
python3-iniparse 0.4-45.el9
python3-inotify 0.9.6-25.el9
python3-libcomps 0.1.18-1.el9
python3-libdnf 0.69.0-17.el9_7
python3-librepo 1.14.5-3.el9
python3-libs 3.9.25-3.el9_7.1
python3-pip-wheel 21.3.1-1.el9
python3-pysocks 1.7.1-12.el9
python3-requests 2.25.1-10.el9_6
python3-rpm 4.16.1.3-39.el9
python3-setuptools 53.0.0-15.el9
python3-setuptools-wheel 53.0.0-15.el9
python3-six 1.15.0-9.el9
python3-subscription-manager-rhsm 1.29.47.1-1.el9_7
python3-systemd 234-19.el9
python3-urllib3 1.26.5-6.el9_7.1
readline 8.1-4.el9
redhat-logos-httpd 90.5-1.el9_6.1
redhat-release 9.7-0.7.el9
rootfiles 8.1-35.el9
rpm 4.16.1.3-39.el9
rpm-build-libs 4.16.1.3-39.el9
rpm-libs 4.16.1.3-39.el9
rpm-sign-libs 4.16.1.3-39.el9
rsync 3.2.5-3.el9
scl-utils 2.0.3-4.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-15.el9
sqlite-libs 3.34.1-9.el9_7
subscription-manager 1.29.47.1-1.el9_7
subscription-manager-rhsm-certificates 20220623-1.el9
systemd 252-55.el9_7.7
systemd-libs 252-55.el9_7.7
systemd-pam 252-55.el9_7.7
systemd-rpm-macros 252-55.el9_7.7
tar 1.34-9.el9_7
tcl 8.6.10-7.el9
tpm2-tss 3.2.3-1.el9
tzdata 2026a-1.el9
unzip 6.0-59.el9
usermode 1.114-7.el9
util-linux 2.37.4-21.el9_7
util-linux-core 2.37.4-21.el9_7
vim-filesystem 8.2.2637-23.el9_7.1
vim-minimal 8.2.2637-23.el9_7
virt-what 1.27-2.el9
which 2.21-30.el9_6
xml-common 0.6.3-58.el9
xz 5.2.5-8.el9_0
xz-libs 5.2.5-8.el9_0
yum 4.14.0-31.el9
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
python-dateutil 2.9.0.post0
requests 2.25.1
rpm 4.16.1.3
setuptools 53.0.0
six 1.15.0
subscription-manager 1.29.47.1
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
| Labels `version` / `release` | `2.0.0` / `1773939694` |
| Image ID | `sha256:cbfbac206cd8c7aa4a24d1412875ca0b881c120c9c2efd03e1577da606460aad` |
| Build date | 2026-03-24T00:18:37Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.7 (Plow) |
| Python | 3.12 |
| Ansible Core | 2.16.18 |

<details><summary>RPM packages (157)</summary>

```text
alternatives 1.24-2.el9
audit-libs 3.1.5-7.el9
basesystem 11-13.el9
bash 5.1.8-9.el9
bzip2 1.0.8-10.el9_5
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crypto-policies 20250905-1.git377cc42.el9_7
curl-minimal 7.76.1-35.el9_7.3
cyrus-sasl-lib 2.1.27-22.el9
dejavu-sans-fonts 2.37-18.el9
dnf-data 4.14.0-31.el9
expat 2.5.0-5.el9_7.1
file-libs 5.39-16.el9
filesystem 3.16-5.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdbm-libs 1.23-1.el9
git-core 2.47.3-1.el9_6
glib2 2.68.4-18.el9_7.1
glibc 2.34-231.el9_7.10
glibc-common 2.34-231.el9_7.10
glibc-langpack-en 2.34-231.el9_7.10
glibc-minimal-langpack 2.34-231.el9_7.10
gmp 6.2.0-13.el9
gnupg2 2.3.3-5.el9_7
gnutls 3.8.3-10.el9_7
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
less 590-6.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-7.el9_7
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9_7
libcap 2.48-10.el9
libcap-ng 0.8.2-7.el9
libcbor 0.7.0-5.el9
libcom_err 1.46.5-8.el9
libcurl-minimal 7.76.1-35.el9_7.3
libdb 5.3.28-57.el9_6
libdnf 0.69.0-17.el9_7
libeconf 0.4.1-4.el9
libedit 3.1-38.20210216cvs.el9
libevent 2.1.12-8.el9_4
libfdisk 2.37.4-21.el9_7
libffi 3.4.2-8.el9
libfido2 1.13.0-2.el9
libgcc 11.5.0-11.el9
libgcrypt 1.10.0-11.el9
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libkadm5 1.21.1-8.el9_6
libksba 1.5.1-7.el9
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9_7
libnghttp2 1.43.0-6.el9
libnsl2 2.0.0-1.el9
libpeas 1.30.0-4.el9
libpwquality 1.4.4-8.el9
librepo 1.14.5-3.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libselinux 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-3.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9_7
libsolv 0.7.24-3.el9
libss 1.46.5-8.el9
libstdc++ 11.5.0-11.el9
libtasn1 4.16.0-9.el9
libtirpc 1.3.3-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libusbx 1.0.26-1.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9_7
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-14.el9_7
libxslt 1.1.34-13.el9_6
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
microdnf 3.9.1-3.el9
mpdecimal 2.5.1-3.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-12.20210508.el9
ncurses-libs 6.2-12.20210508.el9
nettle 3.10.1-1.el9
npth 1.6-8.el9
openldap 2.6.8-4.el9
openssh 8.7p1-47.el9_7
openssh-clients 8.7p1-47.el9_7
openssl 3.5.1-7.el9_7
openssl-fips-provider 3.0.7-8.el9
openssl-fips-provider-so 3.0.7-8.el9
openssl-libs 3.5.1-7.el9_7
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pam 1.5.1-26.el9_6
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
popt 1.18-8.el9
python3.12 3.12.12-4.el9_7.1
python3.12-cffi 1.16.0-2.el9
python3.12-charset-normalizer 3.3.0-2.el9
python3.12-cryptography 41.0.7-3.el9_7
python3.12-idna 3.4-2.el9
python3.12-libs 3.12.12-4.el9_7.1
python3.12-lxml 4.9.3-2.el9
python3.12-pip 23.2.1-5.el9
python3.12-pip-wheel 23.2.1-5.el9
python3.12-ply 3.11-2.el9
python3.12-pycparser 2.20-2.el9
python3.12-pyyaml 6.0.1-2.el9
python3.12-setuptools 68.2.2-5.el9_6
python3.12-urllib3 1.26.19-1.el9_7.1
readline 8.1-4.el9
redhat-release 9.7-0.7.el9
rootfiles 8.1-35.el9
rpm 4.16.1.3-39.el9
rpm-libs 4.16.1.3-39.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-15.el9
sqlite-libs 3.34.1-9.el9_7
sshpass 1.09-4.el9
systemd-libs 252-55.el9_7.7
tar 1.34-9.el9_7
tzdata 2026a-1.el9
unzip 6.0-59.el9
util-linux 2.37.4-21.el9_7
util-linux-core 2.37.4-21.el9_7
xz 5.2.5-8.el9_0
xz-libs 5.2.5-8.el9_0
zlib 1.2.11-40.el9
zstd 1.5.5-1.el9
```

</details>

<details><summary>Python packages: /usr (python3.12) (11)</summary>

```text
cffi 1.16.0
charset-normalizer 3.3.0
cryptography 41.0.7
idna 3.4
lxml 4.9.3
pip 23.2.1
ply 3.11
pycparser 2.20
PyYAML 6.0.1
setuptools 68.2.2
urllib3 1.26.19
```

</details>

<details><summary>Python packages: /usr/local (python3.12) (67)</summary>

```text
aiohappyeyeballs 2.6.1
aiohttp 3.13.3
aiosignal 1.4.0
ansible-compat 25.8.1
ansible-core 2.16.18
ansible-lint 25.8.2
ansible-runner 2.4.3
attrs 22.2.0
bcrypt 3.2.2
black 25.12.0
bracex 2.4
certifi 2038.12.31
click 8.1.7
decorator 5.1.1
docutils 0.22.1
dumb-init 1.2.5.post1
filelock 3.13.1
frozenlist 1.4.1
gssapi 1.8.3
importlib_metadata 8.7.1
Jinja2 3.1.6
jsonschema 4.17.3
krb5 0.5.1
lockfile 0.12.2
markdown-it-py 3.0.0
MarkupSafe 2.1.5
mdurl 0.1.2
multidict 6.0.4
mypy_extensions 1.0.0
ncclient 0.6.15
packaging 24.2
paramiko 3.4.0
pathspec 1.0.3
pexpect 4.9.0
platformdirs 4.1.0
propcache 0.4.1
ptyprocess 0.7.0
Pygments 2.17.2
pykerberos 1.2.4
PyNaCl 1.5.0
pyOpenSSL 25.1.0
pypsrp 0.8.1
pyrsistent 0.20.0
PySocks 1.7.1
pyspnego 0.10.2
python-daemon 3.1.2
pytokens 0.3.0
pywinrm 0.4.3
PyYAML 6.0.2
referencing 0.37.0
requests 2.32.3
requests-credssp 2.0.0
requests_ntlm 1.2.0
resolvelib 1.0.1
rich 13.7.0
rpds-py 0.24.0
ruamel.yaml 0.18.15
ruamel.yaml.clib 0.2.8
six 1.17.0
subprocess-tee 0.4.1
toml 0.10.2
typing_extensions 4.15.0
wcmatch 8.5
xmltodict 0.13.0
yamllint 1.35.1
yarl 1.22.0
zipp 3.23.0
```

</details>

[Back to top](#contents)

### ee-supported-rhel9

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-26/ee-supported-rhel9` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/ee-supported-rhel9.tar.gz` |
| Labels `version` / `release` | `2.0.0` / `1773939694` |
| Image ID | `sha256:f9dc4651f82189efe4fa8b53651ae8f73d527ae072e24daa0a2ef75da161415e` |
| Build date | 2026-03-24T03:01:13Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.7 (Plow) |
| Python | 3.9, 3.12 |
| Ansible Core | 2.16.18 |

<details><summary>RPM packages (226)</summary>

```text
acl 2.3.1-4.el9
alternatives 1.24-2.el9
apr 1.7.0-12.el9_3
apr-util 1.6.1-23.el9
apr-util-bdb 1.6.1-23.el9
audit-libs 3.1.5-7.el9
automation-controller-cli 4.7.10-2.el9ap
basesystem 11-13.el9
bash 5.1.8-9.el9
bash-completion 2.11-5.el9
bzip2 1.0.8-10.el9_5
bzip2-libs 1.0.8-10.el9_5
c-ares 1.19.1-2.el9_4
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crypto-policies 20250905-1.git377cc42.el9_7
curl-minimal 7.76.1-35.el9_7.3
cyrus-sasl-lib 2.1.27-22.el9
dbus 1.12.20-8.el9
dbus-broker 28-7.el9
dbus-common 1.12.20-8.el9
dejavu-sans-fonts 2.37-18.el9
diffutils 3.7-12.el9
dnf-data 4.14.0-31.el9
expat 2.5.0-5.el9_7.1
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
git-lfs 3.6.1-7.el9_7
glib2 2.68.4-18.el9_7.1
glibc 2.34-231.el9_7.10
glibc-common 2.34-231.el9_7.10
glibc-langpack-en 2.34-231.el9_7.10
glibc-minimal-langpack 2.34-231.el9_7.10
gmp 6.2.0-13.el9
gnupg2 2.3.3-5.el9_7
gnutls 3.8.3-10.el9_7
gobject-introspection 1.68.0-11.el9
gpg-pubkey 5a6340b3-6229229e
gpg-pubkey fd431d51-4ae0493b
gpgme 1.15.1-6.el9
grep 3.6-5.el9
gzip 1.12-1.el9
json-c 0.14-11.el9
json-glib 1.6.6-1.el9
keyutils-libs 1.6.3-1.el9
kmod-libs 28-11.el9
krb5-libs 1.21.1-8.el9_6
krb5-pkinit 1.21.1-8.el9_6
krb5-workstation 1.21.1-8.el9_6
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
less 590-6.el9
libacl 2.3.1-4.el9
libaio 0.3.111-13.el9
libarchive 3.5.3-7.el9_7
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9_7
libcap 2.48-10.el9
libcap-ng 0.8.2-7.el9
libcbor 0.7.0-5.el9
libcom_err 1.46.5-8.el9
libcurl-minimal 7.76.1-35.el9_7.3
libdb 5.3.28-57.el9_6
libdnf 0.69.0-17.el9_7
libeconf 0.4.1-4.el9
libedit 3.1-38.20210216cvs.el9
libevent 2.1.12-8.el9_4
libfdisk 2.37.4-21.el9_7
libffi 3.4.2-8.el9
libfido2 1.13.0-2.el9
libgcc 11.5.0-11.el9
libgcrypt 1.10.0-11.el9
libgfortran 11.5.0-11.el9
libgomp 11.5.0-11.el9
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libkadm5 1.21.1-8.el9_6
libksba 1.5.1-7.el9
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9_7
libnghttp2 1.43.0-6.el9
libnsl2 2.0.0-1.el9
libpeas 1.30.0-4.el9
libpkgconf 1.7.3-10.el9
libpq 13.23-1.el9_7
libpwquality 1.4.4-8.el9
libquadmath 11.5.0-11.el9
librepo 1.14.5-3.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libseccomp 2.5.2-2.el9
libselinux 3.6-3.el9
libselinux-utils 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-3.el9
libserf 1.3.9-27.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9_7
libsolv 0.7.24-3.el9
libss 1.46.5-8.el9
libssh 0.10.4-17.el9_7
libssh-config 0.10.4-17.el9_7
libstdc++ 11.5.0-11.el9
libtasn1 4.16.0-9.el9
libtirpc 1.3.3-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
liburing 2.5-1.el9
libusbx 1.0.26-1.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9_7
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-14.el9_7
libxslt 1.1.34-13.el9_6
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
logrotate 3.18.0-12.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
microdnf 3.9.1-3.el9
mpdecimal 2.5.1-3.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-12.20210508.el9
ncurses-libs 6.2-12.20210508.el9
nettle 3.10.1-1.el9
npth 1.6-8.el9
numactl-libs 2.0.19-3.el9
openblas 0.3.29-1.el9
openblas-openmp 0.3.29-1.el9
openldap 2.6.8-4.el9
openshift-clients 4.19.0-202602241905.p2.g24755b6.assembly.stream.el9
openssh 8.7p1-47.el9_7
openssh-clients 8.7p1-47.el9_7
openssl 3.5.1-7.el9_7
openssl-fips-provider 3.0.7-8.el9
openssl-fips-provider-so 3.0.7-8.el9
openssl-libs 3.5.1-7.el9_7
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pam 1.5.1-26.el9_6
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
pkgconf 1.7.3-10.el9
pkgconf-m4 1.7.3-10.el9
pkgconf-pkg-config 1.7.3-10.el9
podman-remote 5.6.0-14.el9_7
policycoreutils 3.6-3.el9
popt 1.18-8.el9
python3 3.9.25-3.el9_7.1
python3-chardet 4.0.0-5.el9
python3-idna 2.10-7.el9_4.1
python3-libs 3.9.25-3.el9_7.1
python3-pexpect 4.8.0-7.el9
python3-pip-wheel 21.3.1-1.el9
python3-ptyprocess 0.6.0-12.el9
python3-pysocks 1.7.1-12.el9
python3-pyyaml 5.4.1-6.el9
python3-requests 2.25.1-10.el9_6
python3-setuptools 53.0.0-15.el9
python3-setuptools-wheel 53.0.0-15.el9
python3-six 1.15.0-9.el9
python3-urllib3 1.26.5-6.el9_7.1
python3.12 3.12.12-4.el9_7.1
python3.12-certifi 2023.5.7-2.el9ap
python3.12-cffi 1.16.0-2.el9
python3.12-charset-normalizer 3.3.0-2.el9
python3.12-cryptography 41.0.7-3.el9_7
python3.12-idna 3.4-2.el9
python3.12-libs 3.12.12-4.el9_7.1
python3.12-lxml 4.9.3-2.el9
python3.12-numpy 1.24.4-3.el9
python3.12-pip 23.2.1-5.el9
python3.12-pip-wheel 23.2.1-5.el9
python3.12-ply 3.11-2.el9
python3.12-pycparser 2.20-2.el9
python3.12-pyyaml 6.0.1-2.el9
python3.12-requests 2.31.0-4.el9ap
python3.12-setuptools 68.2.2-5.el9_6
python3.12-uamqp 1.6.8-2.el9ap
python3.12-urllib3 1.26.19-1.el9_7.1
qemu-img 9.1.0-29.el9_7.6
readline 8.1-4.el9
receptor 1.6.4-1.el9ap
redhat-release 9.7-0.7.el9
rootfiles 8.1-35.el9
rpm 4.16.1.3-39.el9
rpm-libs 4.16.1.3-39.el9
rsync 3.2.5-3.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-15.el9
shadow-utils-subid 4.9-15.el9
sos 4.10.2-2.el9_7
sqlite-libs 3.34.1-9.el9_7
sshpass 1.09-4.el9
subversion 1.14.1-7.el9
subversion-libs 1.14.1-7.el9
systemd 252-55.el9_7.7
systemd-libs 252-55.el9_7.7
systemd-pam 252-55.el9_7.7
systemd-rpm-macros 252-55.el9_7.7
tar 1.34-9.el9_7
tzdata 2026a-1.el9
unzip 6.0-59.el9
utf8proc 2.6.1-4.el9
util-linux 2.37.4-21.el9_7
util-linux-core 2.37.4-21.el9_7
xz 5.2.5-8.el9_0
xz-libs 5.2.5-8.el9_0
zlib 1.2.11-40.el9
zstd 1.5.5-1.el9
```

</details>

<details><summary>Python packages: /usr (python3.12) (16)</summary>

```text
awxkit 4.7.10
certifi 2023.5.7
cffi 1.16.0
charset-normalizer 3.3.0
cryptography 41.0.7
idna 3.4
lxml 4.9.3
numpy 1.24.4
pip 23.2.1
ply 3.11
pycparser 2.20
PyYAML 6.0.1
requests 2.31.0
setuptools 68.2.2
uamqp 1.6.8
urllib3 1.26.19
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
sos 4.10.2
urllib3 1.26.5
```

</details>

<details><summary>Python packages: /usr/local (python3.12) (253)</summary>

```text
adal 1.2.7
aiobotocore 2.11.2
aiodns 3.2.0
aiohappyeyeballs 2.6.1
aiohttp 3.13.3
aioitertools 0.11.0
aiokafka 0.10.0
aiosignal 1.4.0
annotated-types 0.7.0
ansible-compat 25.8.1
ansible-core 2.16.18
ansible-lint 25.8.2
ansible-pylibssh 1.2.2
ansible-runner 2.4.3
ansible-sign 0.1.2
anyio 4.4.0
appdirs 1.4.4
applicationinsights 0.11.10
argcomplete 3.5.3
async-timeout 5.0.1
attrs 22.2.0
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
bcrypt 3.2.2
black 25.12.0
boto3 1.34.34
botocore 1.34.34
bracex 2.4
brotli 1.2.0
cachetools 5.5.2
certifi 2038.12.31
chardet 5.2.0
click 8.1.7
decorator 5.1.1
Deprecated 1.2.14
distlib 0.4.0
distro 1.9.0
dnspython 2.6.1
docutils 0.22.1
dogpile.cache 1.1.2
dpapi-ng 0.2.0
dpath 2.2.0
dumb-init 1.2.5.post1
filelock 3.13.1
frozenlist 1.4.1
google-api-core 2.25.1
google-auth 2.40.3
google-cloud-core 2.4.3
google-cloud-storage 3.3.0
google-crc32c 1.7.1
google-resumable-media 2.7.2
googleapis-common-protos 1.70.0
grpcio 1.75.1
gssapi 1.8.3
h11 0.16.0
h2 4.1.0
hpack 4.0.0
httpcore 1.0.9
httpx 0.27.0
humanfriendly 10.0
hyperframe 6.0.1
importlib_metadata 7.1.0
iso8601 0.1.14
isodate 0.7.2
Jinja2 3.1.6
jmespath 1.0.1
jsonpatch 1.32
jsonpointer 2.1
jsonschema 4.17.3
jxmlease 1.0.3
kafka-python-ng 2.2.3
keystoneauth1 4.3.1
knack 0.11.0
krb5 0.5.1
kubernetes 29.0.0
lockfile 0.12.2
markdown-it-py 3.0.0
MarkupSafe 2.1.5
mdurl 0.1.2
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
multidict 6.0.4
munch 2.5.0
mypy_extensions 1.0.0
ncclient 0.6.15
netaddr 1.3.0
netifaces 0.10.9
nsx-policy-python-sdk 4.1.2.0.0
nsx-python-sdk 4.1.2.0.0
nsx-vmc-aws-integration-python-sdk 4.1.2.0.0
nsx-vmc-policy-python-sdk 4.1.2.0.0
numpy 2.4.2
oauthlib 3.3.1
openstacksdk 0.56.0
opentelemetry-api 1.25.0
opentelemetry-sdk 1.25.0
opentelemetry-semantic-conventions 0.46b0
oras 0.2.37
os-service-types 1.7.0
ovirt-engine-sdk-python 4.5.2
ovirt-imageio 2.4.6
packaging 24.2
pandas 2.3.2
paramiko 3.4.0
pathspec 1.0.3
pbr 7.0.1
pendulum 3.0.0
pexpect 4.9.0
pkginfo 1.7.0
platformdirs 4.1.0
portalocker 1.7.1
propcache 0.4.1
proto-plus 1.26.1
protobuf 6.32.1
psutil 5.9.1
psycopg 3.2.10
ptyprocess 0.7.0
py-deviceid 0.1.1
pyang 2.5.3
pyasn1 0.6.1
pyasn1_modules 0.4.2
pycares 4.4.0
pycurl 7.45.3
pydantic 2.12.0
pydantic_core 2.41.1
Pygments 2.17.2
PyJWT 2.10.1
pykerberos 1.2.4
PyNaCl 1.5.0
pyOpenSSL 25.1.0
pypsrp 0.8.1
pyrsistent 0.20.0
PySocks 1.7.1
pyspnego 0.10.2
python-daemon 3.1.2
python-dateutil 2.9.0.post0
python-gnupg 0.5.5
pytokens 0.3.0
pytz 2025.2
pyvmomi 8.0.3.0.1
pywinrm 0.4.3
PyYAML 6.0.2
receptorctl 1.6.4
referencing 0.37.0
requests 2.32.3
requests-credssp 2.0.0
requests-oauthlib 2.0.0
requests_ntlm 1.2.0
requestsexceptions 1.4.0
resolvelib 1.0.1
rich 13.7.0
rpds-py 0.24.0
rsa 4.9.1
ruamel.yaml 0.18.15
ruamel.yaml.clib 0.2.8
s3transfer 0.10.4
sansldap 0.1.0
scp 0.13.3
six 1.17.0
sniffio 1.3.1
std-uritemplate 1.0.2
stevedore 3.3.3
subprocess-tee 0.4.1
tabulate 0.9.0
textfsm 0.4.1
time-machine 2.14.2
toml 0.10.2
ttp 0.6.0
typing-inspection 0.4.2
typing_extensions 4.15.0
tzdata 2024.1
vapi-common-client 2.44.0
vapi-runtime 2.44.0
vcenter-bindings 4.2.0
vmwarecloud-aws 1.64.0
vmwarecloud-draas 1.23.0
vsphere-automation-sdk 1.86.0
watchdog 6.0.0
wcmatch 8.5
websocket-client 1.8.0
wrapt 1.17.3
xmltodict 0.13.0
xxhash 3.5.0
yamllint 1.35.1
yarl 1.22.0
zipp 3.23.0
```

</details>

<details><summary>Ansible collections (56)</summary>

```text
amazon.aws 9.5.1
ansible.controller 4.7.10
ansible.eda 2.11.0
ansible.hub 1.0.1
ansible.netcommon 8.1.0
ansible.network 5.0.0
ansible.platform 2.6.20260306
ansible.posix 2.1.0
ansible.scm 3.0.0
ansible.security 5.0.0
ansible.snmp 3.0.0
ansible.utils 6.0.0
ansible.windows 3.4.0
ansible.yang 3.0.0
arista.eos 12.0.0
azure.azcollection 3.7.0
cisco.intersight 2.2.0
cisco.ios 11.1.1
cisco.iosxr 12.0.0
cisco.nxos 11.0.0
cloud.common 5.0.0
cloud.terraform 4.0.0
community.vmware 1.9.0
google.cloud 1.7.0
hashicorp.terraform 1.1.0
hashicorp.vault 1.0.0
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
| Labels `version` / `release` | `2.6.6` / `1773939694` |
| Image ID | `sha256:ed508370dd1fe224a7d73776cb74c8499d3a663cf3966e5bd84d07e983212bde` |
| Build date | 2026-03-22T00:27:30Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.7 (Plow) |
| Python | N/A |
| Ansible Core | N/A |

<details><summary>RPM packages (113)</summary>

```text
alternatives 1.24-2.el9
audit-libs 3.1.5-7.el9
automation-gateway-config 2.6.20260325-2.el9ap
automation-gateway-proxy-server 2.6.14-1.el9
basesystem 11-13.el9
bash 5.1.8-9.el9
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
crypto-policies 20250905-1.git377cc42.el9_7
curl-minimal 7.76.1-35.el9_7.3
cyrus-sasl-lib 2.1.27-22.el9
dejavu-sans-fonts 2.37-18.el9
dnf-data 4.14.0-31.el9
dumb-init 1.2.5-3.el9ap
file-libs 5.39-16.el9
filesystem 3.16-5.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdbm-libs 1.23-1.el9
glib2 2.68.4-18.el9_7.1
glibc 2.34-231.el9_7.10
glibc-common 2.34-231.el9_7.10
glibc-langpack-en 2.34-231.el9_7.10
glibc-minimal-langpack 2.34-231.el9_7.10
gmp 6.2.0-13.el9
gnupg2 2.3.3-5.el9_7
gnutls 3.8.3-10.el9_7
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
libarchive 3.5.3-7.el9_7
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9_7
libcap 2.48-10.el9
libcap-ng 0.8.2-7.el9
libcom_err 1.46.5-8.el9
libcurl-minimal 7.76.1-35.el9_7.3
libdnf 0.69.0-17.el9_7
libevent 2.1.12-8.el9_4
libffi 3.4.2-8.el9
libgcc 11.5.0-11.el9
libgcrypt 1.10.0-11.el9
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libksba 1.5.1-7.el9
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9_7
libnghttp2 1.43.0-6.el9
libpeas 1.30.0-4.el9
librepo 1.14.5-3.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libselinux 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-3.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9_7
libsolv 0.7.24-3.el9
libstdc++ 11.5.0-11.el9
libtasn1 4.16.0-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libusbx 1.0.26-1.el9
libuuid 2.37.4-21.el9_7
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-14.el9_7
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
microdnf 3.9.1-3.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-12.20210508.el9
ncurses-libs 6.2-12.20210508.el9
nettle 3.10.1-1.el9
npth 1.6-8.el9
openldap 2.6.8-4.el9
openssl 3.5.1-7.el9_7
openssl-fips-provider 3.0.7-8.el9
openssl-fips-provider-so 3.0.7-8.el9
openssl-libs 3.5.1-7.el9_7
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
popt 1.18-8.el9
readline 8.1-4.el9
redhat-release 9.7-0.7.el9
rootfiles 8.1-35.el9
rpm 4.16.1.3-39.el9
rpm-libs 4.16.1.3-39.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-15.el9
sqlite-libs 3.34.1-9.el9_7
systemd-libs 252-55.el9_7.7
tzdata 2026a-1.el9
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
| Labels `version` / `release` | `2.6.20260325` / `1773939694` |
| Image ID | `sha256:3ac836ca923d54b6d71c692d1a317a88023eb97c322430aa808fb2109ee5d9c7` |
| Build date | 2026-03-23T05:31:02Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.7 (Plow) |
| Python | 3.12 |
| Ansible Core | N/A |

<details><summary>RPM packages (149)</summary>

```text
acl 2.3.1-4.el9
alternatives 1.24-2.el9
audit-libs 3.1.5-7.el9
basesystem 11-13.el9
bash 5.1.8-9.el9
bzip2-libs 1.0.8-10.el9_5
c-ares 1.19.1-2.el9_4
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crypto-policies 20250905-1.git377cc42.el9_7
curl-minimal 7.76.1-35.el9_7.3
cyrus-sasl-lib 2.1.27-22.el9
dbus 1.12.20-8.el9
dbus-broker 28-7.el9
dbus-common 1.12.20-8.el9
dejavu-sans-fonts 2.37-18.el9
dnf-data 4.14.0-31.el9
expat 2.5.0-5.el9_7.1
file-libs 5.39-16.el9
filesystem 3.16-5.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdbm-libs 1.23-1.el9
glib2 2.68.4-18.el9_7.1
glibc 2.34-231.el9_7.10
glibc-common 2.34-231.el9_7.10
glibc-langpack-en 2.34-231.el9_7.10
glibc-minimal-langpack 2.34-231.el9_7.10
gmp 6.2.0-13.el9
gnupg2 2.3.3-5.el9_7
gnutls 3.8.3-10.el9_7
gobject-introspection 1.68.0-11.el9
gpg-pubkey 5a6340b3-6229229e
gpg-pubkey fd431d51-4ae0493b
gpgme 1.15.1-6.el9
grep 3.6-5.el9
gzip 1.12-1.el9
json-c 0.14-11.el9
json-glib 1.6.6-1.el9
keyutils-libs 1.6.3-1.el9
kmod-libs 28-11.el9
krb5-libs 1.21.1-8.el9_6
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-7.el9_7
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9_7
libcap 2.48-10.el9
libcap-ng 0.8.2-7.el9
libcom_err 1.46.5-8.el9
libcurl-minimal 7.76.1-35.el9_7.3
libdb 5.3.28-57.el9_6
libdnf 0.69.0-17.el9_7
libeconf 0.4.1-4.el9
libevent 2.1.12-8.el9_4
libfdisk 2.37.4-21.el9_7
libffi 3.4.2-8.el9
libgcc 11.5.0-11.el9
libgcrypt 1.10.0-11.el9
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libksba 1.5.1-7.el9
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9_7
libnghttp2 1.43.0-6.el9
libnsl2 2.0.0-1.el9
libpeas 1.30.0-4.el9
libpq 13.23-1.el9_7
libpwquality 1.4.4-8.el9
librepo 1.14.5-3.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libseccomp 2.5.2-2.el9
libselinux 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-3.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9_7
libsolv 0.7.24-3.el9
libstdc++ 11.5.0-11.el9
libtasn1 4.16.0-9.el9
libtirpc 1.3.3-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libusbx 1.0.26-1.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9_7
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-14.el9_7
libxslt 1.1.34-13.el9_6
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
microdnf 3.9.1-3.el9
mpdecimal 2.5.1-3.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-12.20210508.el9
ncurses-libs 6.2-12.20210508.el9
nettle 3.10.1-1.el9
nginx 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
nginx-core 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
nginx-filesystem 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
npth 1.6-8.el9
openldap 2.6.8-4.el9
openssl 3.5.1-7.el9_7
openssl-fips-provider 3.0.7-8.el9
openssl-fips-provider-so 3.0.7-8.el9
openssl-libs 3.5.1-7.el9_7
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pam 1.5.1-26.el9_6
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
popt 1.18-8.el9
postgresql 15.17-1.module+el9.7.0+24029+ef6a2953
postgresql-private-libs 15.17-1.module+el9.7.0+24029+ef6a2953
python3.12 3.12.12-4.el9_7.1
python3.12-libs 3.12.12-4.el9_7.1
python3.12-pip 23.2.1-5.el9
python3.12-pip-wheel 23.2.1-5.el9
readline 8.1-4.el9
redhat-logos-httpd 90.5-1.el9_6.1
redhat-release 9.7-0.7.el9
rootfiles 8.1-35.el9
rpm 4.16.1.3-39.el9
rpm-libs 4.16.1.3-39.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-15.el9
sqlite-libs 3.34.1-9.el9_7
systemd 252-55.el9_7.7
systemd-libs 252-55.el9_7.7
systemd-pam 252-55.el9_7.7
systemd-rpm-macros 252-55.el9_7.7
tzdata 2026a-1.el9
util-linux 2.37.4-21.el9_7
util-linux-core 2.37.4-21.el9_7
xmlsec1 1.2.29-13.el9
xmlsec1-openssl 1.2.29-13.el9
xz-libs 5.2.5-8.el9_0
zlib 1.2.11-40.el9
```

</details>

<details><summary>Python packages: /opt/aap-gateway/venv (python3.12) (66)</summary>

```text
aap-gateway 2.6.20260325
argon2-cffi 23.1.0
argon2-cffi-bindings 21.2.0
asgiref 3.8.1
attrs 25.3.0
certifi 2038.12.31
cffi 1.17.1
charset-normalizer 3.4.0
cryptography 44.0.1
defusedxml 0.7.1
Django 5.2.9
django-ansible-base 2.7.0
django-auth-ldap 5.2.0
django-crum 0.7.9
django-dynamic-preferences 1.16.0
django-extensions 4.1
django-flags 5.0.13
django-oauth-toolkit 2.3.0
django-redis 6.0.0
djangorestframework 3.15.2
drf-spectacular 0.26.5
dynaconf 3.2.10
grpcio 1.68.1
grpcio-tools 1.68.1
idna 3.10
inflection 0.5.1
isodate 0.7.2
jsonschema 4.25.0
jsonschema-specifications 2025.4.1
jwcrypto 1.5.6
ldap-filter 1.0.1
lxml 5.3.0
netaddr 0.8.0
oauthlib 3.3.1
persisting-theory 1.0
pip 23.2.1
protobuf 5.29.5
psycopg 3.2.3
psycopg-c 3.2.3
pyasn1 0.6.1
pyasn1_modules 0.4.2
pycparser 2.22
PyJWT 2.10.1
pyrad 2.4
python-ldap 3.4.4
python3-openid 3.2.0
python3-saml 1.16.0
PyYAML 6.0.2
redis 6.2.0
referencing 0.36.2
requests 2.32.3
requests-oauthlib 2.0.0
rpds-py 0.24.0
setuptools 78.1.1
six 1.17.0
social-auth-app-django 5.4.1
social-auth-core 4.5.4
sqlparse 0.5.3
tabulate 0.9.0
tacacs_plus 2.6
typing_extensions 4.12.2
uritemplate 4.2.0
urllib3 2.6.3
uWSGI 2.0.28
xds-protos 1.68.1
xmlsec 1.3.13
```

</details>

<details><summary>Python packages: /usr (python3.12) (8)</summary>

```text
certifi 2038.12.31
charset-normalizer 3.4.0
dumb-init 1.2.5.post1
idna 3.10
pip 23.2.1
requests 2.32.3
supervisor 4.3.0
urllib3 2.6.3
```

</details>

[Back to top](#contents)

### hub-rhel9

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-26/hub-rhel9` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/hub-rhel9.tar.gz` |
| Labels `version` / `release` | `4.11.7` / `1773939694` |
| Image ID | `sha256:f6f7ac95f8bc754664a5e49e5730ad960ce03ad13e6d6eb54c185faf7ac7c5c5` |
| Build date | 2026-03-27T20:50:48Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.7 (Plow) |
| Python | 3.12 |
| Ansible Core | 2.20.3 |

<details><summary>RPM packages (151)</summary>

```text
alternatives 1.24-2.el9
audit-libs 3.1.5-7.el9
basesystem 11-13.el9
bash 5.1.8-9.el9
bzip2-libs 1.0.8-10.el9_5
c-ares 1.19.1-2.el9_4
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
containers-common 1-135.el9_7
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crun 1.26-1.el9_7
crypto-policies 20250905-1.git377cc42.el9_7
curl-minimal 7.76.1-35.el9_7.3
cyrus-sasl-lib 2.1.27-22.el9
dejavu-sans-fonts 2.37-18.el9
dnf-data 4.14.0-31.el9
expat 2.5.0-5.el9_7.1
file-libs 5.39-16.el9
filesystem 3.16-5.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdbm-libs 1.23-1.el9
gettext 0.21-8.el9
gettext-libs 0.21-8.el9
git-core 2.47.3-1.el9_6
glib2 2.68.4-18.el9_7.1
glibc 2.34-231.el9_7.10
glibc-common 2.34-231.el9_7.10
glibc-langpack-en 2.34-231.el9_7.10
glibc-minimal-langpack 2.34-231.el9_7.10
gmp 6.2.0-13.el9
gnupg2 2.3.3-5.el9_7
gnutls 3.8.3-10.el9_7
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
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
less 590-6.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-7.el9_7
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9_7
libcap 2.48-10.el9
libcap-ng 0.8.2-7.el9
libcbor 0.7.0-5.el9
libcom_err 1.46.5-8.el9
libcurl-minimal 7.76.1-35.el9_7.3
libdb 5.3.28-57.el9_6
libdnf 0.69.0-17.el9_7
libeconf 0.4.1-4.el9
libedit 3.1-38.20210216cvs.el9
libevent 2.1.12-8.el9_4
libfdisk 2.37.4-21.el9_7
libffi 3.4.2-8.el9
libfido2 1.13.0-2.el9
libgcc 11.5.0-11.el9
libgcrypt 1.10.0-11.el9
libgomp 11.5.0-11.el9
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libjpeg-turbo 2.0.90-7.el9
libksba 1.5.1-7.el9
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9_7
libnghttp2 1.43.0-6.el9
libnsl2 2.0.0-1.el9
libpeas 1.30.0-4.el9
libpq 13.23-1.el9_7
libpwquality 1.4.4-8.el9
librepo 1.14.5-3.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libseccomp 2.5.2-2.el9
libsecret 0.20.4-4.el9
libselinux 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-3.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9_7
libsolv 0.7.24-3.el9
libstdc++ 11.5.0-11.el9
libtasn1 4.16.0-9.el9
libtirpc 1.3.3-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libusbx 1.0.26-1.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9_7
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-14.el9_7
libxslt 1.1.34-13.el9_6
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
microdnf 3.9.1-3.el9
mpdecimal 2.5.1-3.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-12.20210508.el9
ncurses-libs 6.2-12.20210508.el9
nettle 3.10.1-1.el9
npth 1.6-8.el9
openldap 2.6.8-4.el9
openssh 8.7p1-47.el9_7
openssh-clients 8.7p1-47.el9_7
openssl 3.5.1-7.el9_7
openssl-fips-provider 3.0.7-8.el9
openssl-fips-provider-so 3.0.7-8.el9
openssl-libs 3.5.1-7.el9_7
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pam 1.5.1-26.el9_6
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
pinentry 1.1.1-8.el9
popt 1.18-8.el9
python3.12 3.12.12-4.el9_7.1
python3.12-libs 3.12.12-4.el9_7.1
python3.12-pip 23.2.1-5.el9
python3.12-pip-wheel 23.2.1-5.el9
readline 8.1-4.el9
redhat-release 9.7-0.7.el9
rootfiles 8.1-35.el9
rpm 4.16.1.3-39.el9
rpm-libs 4.16.1.3-39.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-15.el9
shadow-utils-subid 4.9-15.el9
skopeo 1.20.0-3.el9_7
sqlite-libs 3.34.1-9.el9_7
systemd-libs 252-55.el9_7.7
tzdata 2026a-1.el9
util-linux 2.37.4-21.el9_7
util-linux-core 2.37.4-21.el9_7
xz-libs 5.2.5-8.el9_0
yajl 2.1.0-25.el9
zlib 1.2.11-40.el9
```

</details>

<details><summary>Python packages: /usr (python3.12) (161)</summary>

```text
aiodns 3.2.0
aiofiles 23.2.1
aiohappyeyeballs 2.6.1
aiohttp 3.13.3
aiosignal 1.4.0
ansible-builder 3.1.1
ansible-compat 25.12.1
ansible-core 2.20.3
ansible-lint 26.1.0
asgiref 3.11.1
async-timeout 5.0.1
asyncio-throttle 1.0.2
attrs 22.2.0
azure-core 1.39.0
azure-storage-blob 12.28.0
backoff 2.2.1
backports.tarfile 1.2.0
bindep 2.14.0
black 25.12.0
boto3 1.42.73
botocore 1.42.73
bracex 2.6
CacheControl 0.14.3
certifi 2038.12.31
cffi 2.0.0
charset-normalizer 3.4.6
click 8.1.7
cryptography 46.0.5
defusedxml 0.7.1
Deprecated 1.3.1
diff-match-patch 20241021
distro 1.9.0
Django 5.2.12
django-ansible-base 2.6.20260325
django-auth-ldap 4.0.0
django-automated-logging 6.2.2
django-crum 0.7.9
django-filter 25.2
django-flags 5.2.0
django-guid 3.4.0
django-import-export 4.4.0
django-ipware 6.0.5
django-lifecycle 1.1.2
django-picklefield 3.4.0
django-prometheus 2.4.1
django-storages 1.14.6
djangorestframework 3.15.2
djangorestframework-queryfields 1.1.0
drf-access-policy 1.5.0
drf-nested-routers 0.93.5
drf-spectacular 0.29.0
dynaconf 3.2.13
filelock 3.25.2
flake8 6.1.0
frozenlist 1.8.0
galaxy-ng 4.11.7
galaxy_importer 0.4.37
gitdb 4.0.12
GitPython 3.1.46
googleapis-common-protos 1.73.0
grpcio 1.78.0
gunicorn 23.0.0
idna 3.11
importlib_metadata 6.0.1
inflection 0.5.1
insights-analytics-collector 0.3.2
isodate 0.7.2
Jinja2 3.1.6
jmespath 1.1.0
jq 1.6.0
json-stream 2.3.4
json-stream-rs-tokenizer 0.4.30
jsonschema 4.21.1
jsonschema-specifications 2025.9.1
librt 0.8.1
lxml 6.0.2
Markdown 3.10.2
MarkupSafe 3.0.3
marshmallow 3.26.2
mccabe 0.7.0
msgpack 1.1.2
multidict 6.7.1
mypy 1.19.1
mypy_extensions 1.1.0
nh3 0.3.3
oauthlib 3.3.1
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
packaging 24.2
Parsley 1.3
pathspec 0.12.1
pbr 7.0.3
pillow 12.1.1
pip 23.2.1
pkgconfig 1.5.5
platformdirs 4.9.4
prometheus_client 0.24.1
propcache 0.4.1
protobuf 5.29.6
psycopg 3.2.9
pulp-ansible 0.25.5
pulp-container 2.19.8
pulp-glue 0.29.4
pulpcore 3.49.56
pyasn1 0.6.3
pyasn1_modules 0.4.2
pycares 4.11.0
pycodestyle 2.11.1
pycparser 3.0
pyflakes 3.1.0
pygtrie 2.5.0
PyJWT 2.8.0
pyOpenSSL 25.3.0
pyparsing 3.1.1
python-dateutil 2.9.0.post0
python-gnupg 0.5.2
python-ipware 3.0.0
python-ldap 3.4.5
python3-openid 3.2.0
pytokens 0.4.1
PyYAML 6.0.1
redis 5.0.2
referencing 0.37.0
requests 2.32.5
requests-oauthlib 2.0.0
resolvelib 1.2.1
rpds-py 0.30.0
ruamel.yaml 0.19.1
ruamel.yaml.clib 0.2.15
s3transfer 0.16.0
semantic_version 2.10.0
setuptools 80.9.0
six 1.17.0
smmap 5.0.3
social-auth-app-django 5.6.0
social-auth-core 4.7.0
sqlparse 0.5.5
subprocess-tee 0.4.2
tablib 3.9.0
typing_extensions 4.15.0
uritemplate 4.2.0
url-normalize 1.4.3
urllib3 2.6.3
uuid6 2024.1.12
wcmatch 10.1
whitenoise 6.6.0
wrapt 1.17.3
yamllint 1.37.1
yarl 1.18.3
zipp 3.23.0
```

</details>

[Back to top](#contents)

### hub-web-rhel9

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-26/hub-web-rhel9` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/hub-web-rhel9.tar.gz` |
| Labels `version` / `release` | `4.11.7` / `1774456665` |
| Image ID | `sha256:10966cc5ca434d212efe290e9d6ea87407a1601efb898ac49f92f461a8d9fd37` |
| Build date | 2026-03-27T21:40:27Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.7 (Plow) |
| Python | 3.9 |
| Ansible Core | N/A |

<details><summary>RPM packages (294)</summary>

```text
acl 2.3.1-4.el9
alternatives 1.24-2.el9
attr 2.5.1-3.el9
audit-libs 3.1.5-7.el9
basesystem 11-13.el9
bash 5.1.8-9.el9
bsdtar 3.5.3-7.el9_7
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crypto-policies 20250905-1.git377cc42.el9_7
crypto-policies-scripts 20250905-1.git377cc42.el9_7
curl-minimal 7.76.1-35.el9_7.3
cyrus-sasl-lib 2.1.27-22.el9
dbus 1.12.20-8.el9
dbus-broker 28-7.el9
dbus-common 1.12.20-8.el9
dbus-libs 1.12.20-8.el9
dejavu-sans-fonts 2.37-18.el9
dmidecode 3.6-1.el9
dnf 4.14.0-31.el9
dnf-data 4.14.0-31.el9
elfutils-default-yama-scope 0.193-1.el9
elfutils-libelf 0.193-1.el9
elfutils-libs 0.193-1.el9
environment-modules 5.3.0-2.el9
expat 2.5.0-5.el9_7.1
file-libs 5.39-16.el9
filesystem 3.16-5.el9
findutils 4.8.0-7.el9
fontconfig 2.14.0-2.el9_1
fonts-filesystem 2.0.5-7.el9.1
freetype 2.10.4-10.el9_5
gawk 5.1.0-6.el9
gd 2.3.2-3.el9
gdb-gdbserver 16.3-2.el9
gdbm-libs 1.23-1.el9
gettext 0.21-8.el9
gettext-libs 0.21-8.el9
glib2 2.68.4-18.el9_7.1
glibc 2.34-231.el9_7.10
glibc-common 2.34-231.el9_7.10
glibc-langpack-en 2.34-231.el9_7.10
glibc-locale-source 2.34-231.el9_7.10
glibc-minimal-langpack 2.34-231.el9_7.10
gmp 6.2.0-13.el9
gnupg2 2.3.3-5.el9_7
gnutls 3.8.3-10.el9_7
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
ima-evm-utils 1.6.2-2.el9
iproute 6.14.0-2.el9
jbigkit-libs 2.1-23.el9
json-c 0.14-11.el9
json-glib 1.6.6-1.el9
keyutils 1.6.3-1.el9
keyutils-libs 1.6.3-1.el9
kmod-libs 28-11.el9
krb5-libs 1.21.1-8.el9_6
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
less 590-6.el9
libX11 1.7.0-11.el9
libX11-common 1.7.0-11.el9
libXau 1.0.9-8.el9
libXpm 3.5.13-10.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-7.el9_7
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9_7
libbpf 1.5.0-2.el9
libbrotli 1.0.9-9.el9_7
libcap 2.48-10.el9
libcap-ng 0.8.2-7.el9
libcom_err 1.46.5-8.el9
libcomps 0.1.18-1.el9
libcurl-minimal 7.76.1-35.el9_7.3
libdb 5.3.28-57.el9_6
libdnf 0.69.0-17.el9_7
libdnf-plugin-subscription-manager 1.29.47.1-1.el9_7
libeconf 0.4.1-4.el9
libevent 2.1.12-8.el9_4
libfdisk 2.37.4-21.el9_7
libffi 3.4.2-8.el9
libgcc 11.5.0-11.el9
libgcrypt 1.10.0-11.el9
libgomp 11.5.0-11.el9
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libjpeg-turbo 2.0.90-7.el9
libksba 1.5.1-7.el9
libmnl 1.0.4-16.el9_4
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9_7
libnghttp2 1.43.0-6.el9
libpipeline 1.5.3-4.el9
libpng 1.6.37-12.el9_7.2
libpwquality 1.4.4-8.el9
librepo 1.14.5-3.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libseccomp 2.5.2-2.el9
libselinux 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-3.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9_7
libsolv 0.7.24-3.el9
libstdc++ 11.5.0-11.el9
libtasn1 4.16.0-9.el9
libtiff 4.4.0-15.el9_7.2
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libuser 0.63-17.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9_7
libverto 0.3.2-3.el9
libwebp 1.2.0-8.el9_3
libxcb 1.13.1-9.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-14.el9_7
libxslt 1.1.34-13.el9_6
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
logrotate 3.18.0-12.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
man-db 2.9.3-9.el9
mpfr 4.1.0-7.el9
ncurses 6.2-12.20210508.el9
ncurses-base 6.2-12.20210508.el9
ncurses-libs 6.2-12.20210508.el9
nettle 3.10.1-1.el9
nginx 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
nginx-all-modules 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
nginx-core 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
nginx-filesystem 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
nginx-mod-http-image-filter 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
nginx-mod-http-perl 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
nginx-mod-http-xslt-filter 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
nginx-mod-mail 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
nginx-mod-stream 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
npth 1.6-8.el9
nss_wrapper-libs 1.1.13-1.el9
openldap 2.6.8-4.el9
openssl 3.5.1-7.el9_7
openssl-fips-provider 3.0.7-8.el9
openssl-fips-provider-so 3.0.7-8.el9
openssl-libs 3.5.1-7.el9_7
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
perl-Net-SSLeay 1.94-3.el9
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
psmisc 23.4-3.el9
python3 3.9.25-3.el9_7.1
python3-chardet 4.0.0-5.el9
python3-cloud-what 1.29.47.1-1.el9_7
python3-dateutil 2.9.0.post0-1.el9_7
python3-dbus 1.2.18-2.el9
python3-decorator 4.4.2-6.el9
python3-dnf 4.14.0-31.el9
python3-dnf-plugins-core 4.3.0-24.el9_7
python3-gobject-base 3.40.1-6.el9
python3-gobject-base-noarch 3.40.1-6.el9
python3-gpg 1.15.1-6.el9
python3-hawkey 0.69.0-17.el9_7
python3-idna 2.10-7.el9_4.1
python3-iniparse 0.4-45.el9
python3-inotify 0.9.6-25.el9
python3-libcomps 0.1.18-1.el9
python3-libdnf 0.69.0-17.el9_7
python3-librepo 1.14.5-3.el9
python3-libs 3.9.25-3.el9_7.1
python3-pip-wheel 21.3.1-1.el9
python3-pysocks 1.7.1-12.el9
python3-requests 2.25.1-10.el9_6
python3-rpm 4.16.1.3-39.el9
python3-setuptools 53.0.0-15.el9
python3-setuptools-wheel 53.0.0-15.el9
python3-six 1.15.0-9.el9
python3-subscription-manager-rhsm 1.29.47.1-1.el9_7
python3-systemd 234-19.el9
python3-urllib3 1.26.5-6.el9_7.1
readline 8.1-4.el9
redhat-logos-httpd 90.5-1.el9_6.1
redhat-release 9.7-0.7.el9
rootfiles 8.1-35.el9
rpm 4.16.1.3-39.el9
rpm-build-libs 4.16.1.3-39.el9
rpm-libs 4.16.1.3-39.el9
rpm-sign-libs 4.16.1.3-39.el9
rsync 3.2.5-3.el9
scl-utils 2.0.3-4.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-15.el9
sqlite-libs 3.34.1-9.el9_7
subscription-manager 1.29.47.1-1.el9_7
subscription-manager-rhsm-certificates 20220623-1.el9
systemd 252-55.el9_7.7
systemd-libs 252-55.el9_7.7
systemd-pam 252-55.el9_7.7
systemd-rpm-macros 252-55.el9_7.7
tar 1.34-9.el9_7
tcl 8.6.10-7.el9
tpm2-tss 3.2.3-1.el9
tzdata 2026a-1.el9
unzip 6.0-59.el9
usermode 1.114-7.el9
util-linux 2.37.4-21.el9_7
util-linux-core 2.37.4-21.el9_7
vim-filesystem 8.2.2637-23.el9_7.1
vim-minimal 8.2.2637-23.el9_7
virt-what 1.27-2.el9
which 2.21-30.el9_6
xml-common 0.6.3-58.el9
xz 5.2.5-8.el9_0
xz-libs 5.2.5-8.el9_0
yum 4.14.0-31.el9
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
python-dateutil 2.9.0.post0
requests 2.25.1
rpm 4.16.1.3
setuptools 53.0.0
six 1.15.0
subscription-manager 1.29.47.1
systemd-python 234
urllib3 1.26.5
```

</details>

[Back to top](#contents)

### lightspeed-chatbot-rhel9

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-26/lightspeed-chatbot-rhel9` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/lightspeed-chatbot-rhel9.tar.gz` |
| Labels `version` / `release` | `2.6` / `1773939694` |
| Image ID | `sha256:cf3249a82b9aa16c46a2cb24571f67860001b2c7448ce79971e5eccdd64d8174` |
| Build date | 2026-03-25T05:34:51Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.7 (Plow) |
| Python | 3.12 |
| Ansible Core | N/A |

<details><summary>RPM packages (139)</summary>

```text
alternatives 1.24-2.el9
audit-libs 3.1.5-7.el9
basesystem 11-13.el9
bash 5.1.8-9.el9
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
crypto-policies 20250905-1.git377cc42.el9_7
curl-minimal 7.76.1-35.el9_7.3
cyrus-sasl-lib 2.1.27-22.el9
dejavu-sans-fonts 2.37-18.el9
diffutils 3.7-12.el9
dnf-data 4.14.0-31.el9
expat 2.5.0-5.el9_7.1
file-libs 5.39-16.el9
filesystem 3.16-5.el9
flexiblas 3.0.4-8.el9
flexiblas-netlib 3.0.4-8.el9
flexiblas-openblas-openmp 3.0.4-8.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdbm-libs 1.23-1.el9
glib2 2.68.4-18.el9_7.1
glibc 2.34-231.el9_7.10
glibc-common 2.34-231.el9_7.10
glibc-minimal-langpack 2.34-231.el9_7.10
gmp 6.2.0-13.el9
gnupg2 2.3.3-5.el9_7
gnutls 3.8.3-10.el9_7
gobject-introspection 1.68.0-11.el9
gpg-pubkey 5a6340b3-6229229e
gpg-pubkey fd431d51-4ae0493b
gpgme 1.15.1-6.el9
grep 3.6-5.el9
gzip 1.12-1.el9
jq 1.6-19.el9
json-c 0.14-11.el9
json-glib 1.6.6-1.el9
keyutils-libs 1.6.3-1.el9
krb5-libs 1.21.1-8.el9_6
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-7.el9_7
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9_7
libcap 2.48-10.el9
libcap-ng 0.8.2-7.el9
libcom_err 1.46.5-8.el9
libcurl-minimal 7.76.1-35.el9_7.3
libdnf 0.69.0-17.el9_7
libevent 2.1.12-8.el9_4
libffi 3.4.2-8.el9
libgcc 11.5.0-11.el9
libgcrypt 1.10.0-11.el9
libgfortran 11.5.0-11.el9
libgomp 11.5.0-11.el9
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libjpeg-turbo 2.0.90-7.el9
libksba 1.5.1-7.el9
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9_7
libnghttp2 1.43.0-6.el9
libnsl2 2.0.0-1.el9
libpeas 1.30.0-4.el9
libpq 13.23-1.el9_7
libquadmath 11.5.0-11.el9
librepo 1.14.5-3.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libselinux 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-3.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9_7
libsolv 0.7.24-3.el9
libstdc++ 11.5.0-11.el9
libtasn1 4.16.0-9.el9
libtirpc 1.3.3-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libusbx 1.0.26-1.el9
libuuid 2.37.4-21.el9_7
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-14.el9_7
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
microdnf 3.9.1-3.el9
mpdecimal 2.5.1-3.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-12.20210508.el9
ncurses-libs 6.2-12.20210508.el9
nettle 3.10.1-1.el9
npth 1.6-8.el9
oniguruma 6.9.6-1.el9.6
openblas 0.3.29-1.el9
openblas-openmp 0.3.29-1.el9
openldap 2.6.8-4.el9
openssl-fips-provider 3.0.7-8.el9
openssl-fips-provider-so 3.0.7-8.el9
openssl-libs 3.5.1-7.el9_7
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
popt 1.18-8.el9
protobuf 3.14.0-17.el9_7
python3.12 3.12.12-4.el9_7.1
python3.12-cffi 1.16.0-2.el9
python3.12-charset-normalizer 3.3.0-2.el9
python3.12-cryptography 41.0.7-3.el9_7
python3.12-idna 3.4-2.el9
python3.12-libs 3.12.12-4.el9_7.1
python3.12-pip 23.2.1-5.el9
python3.12-pip-wheel 23.2.1-5.el9
python3.12-ply 3.11-2.el9
python3.12-pycparser 2.20-2.el9
python3.12-setuptools 68.2.2-5.el9_6
readline 8.1-4.el9
redhat-release 9.7-0.7.el9
rootfiles 8.1-35.el9
rpm 4.16.1.3-39.el9
rpm-libs 4.16.1.3-39.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-15.el9
sqlite-libs 3.34.1-9.el9_7
systemd-libs 252-55.el9_7.7
tar 1.34-9.el9_7
tzdata 2026a-1.el9
xz-libs 5.2.5-8.el9_0
zlib 1.2.11-40.el9
```

</details>

<details><summary>Python packages: /usr (python3.12) (8)</summary>

```text
cffi 1.16.0
charset-normalizer 3.3.0
cryptography 41.0.7
idna 3.4
pip 23.2.1
ply 3.11
pycparser 2.20
setuptools 68.2.2
```

</details>

<details><summary>Python packages: /usr/local (python3.12) (119)</summary>

```text
aiohappyeyeballs 2.6.1
aiohttp 3.13.3
aiosignal 1.4.0
aiosqlite 0.22.1
annotated-doc 0.0.4
annotated-types 0.7.0
ansible-chatbot-stack 0.1.0
anyio 4.12.1
asyncpg 0.31.0
attrs 25.4.0
Authlib 1.6.9
cachetools 6.2.6
certifi 2038.12.31
cffi 2.0.0
click 8.3.1
cryptography 46.0.5
distro 1.9.0
dnspython 2.8.0
dumb-init 1.2.5.post1
durationpy 0.10
ecdsa 0.19.1
email-validator 2.3.0
faiss-cpu 1.12.0
fastapi 0.128.0
fastuuid 0.14.0
filelock 3.20.3
fire 0.7.1
frozenlist 1.8.0
fsspec 2026.1.0
googleapis-common-protos 1.72.0
greenlet 3.3.1
h11 0.16.0
hf-xet 1.2.0
httpcore 1.0.9
httpx 0.28.1
httpx-sse 0.4.3
huggingface_hub 0.36.0
importlib_metadata 8.7.1
Jinja2 3.1.6
jiter 0.10.0
joblib 1.5.3
jsonpath-ng 1.7.0
jsonschema 4.26.0
jsonschema-specifications 2025.9.1
kubernetes 35.0.0
lightspeed-stack 0.3.0
lightspeed_stack_providers 0.1.18
litellm 1.81.5
llama_stack 0.2.22
llama_stack_client 0.2.22
markdown-it-py 4.0.0
MarkupSafe 3.0.3
mcp 1.26.0
mdurl 0.1.2
mpmath 1.3.0
multidict 6.7.1
networkx 3.6.1
numpy 2.4.1
oauthlib 3.3.1
openai 2.16.0
opentelemetry-api 1.39.1
opentelemetry-exporter-otlp-proto-common 1.39.1
opentelemetry-exporter-otlp-proto-http 1.39.1
opentelemetry-proto 1.39.1
opentelemetry-sdk 1.39.1
opentelemetry-semantic-conventions 0.60b1
packaging 26.0
pandas 3.0.0
pillow 12.1.1
prometheus_client 0.24.1
prompt_toolkit 3.0.52
propcache 0.4.1
protobuf 6.33.5
psycopg2-binary 2.9.11
pyaml 25.7.0
pyasn1 0.6.3
pydantic 2.12.5
pydantic-settings 2.12.0
pydantic_core 2.41.5
Pygments 2.19.2
PyJWT 2.11.0
python-dateutil 2.9.0.post0
python-dotenv 1.2.1
python-jose 3.5.0
python-multipart 0.0.22
PyYAML 6.0.3
referencing 0.37.0
regex 2026.1.15
requests 2.32.5
requests-oauthlib 2.0.0
rich 14.3.1
rpds-py 0.30.0
rsa 4.9.1
safetensors 0.7.0
scikit-learn 1.8.0
scipy 1.17.0
semver 3.0.4
sentence-transformers 5.2.2
six 1.17.0
sniffio 1.3.1
SQLAlchemy 2.0.46
sse-starlette 3.2.0
starlette 0.50.0
sympy 1.14.0
termcolor 3.3.0
threadpoolctl 3.6.0
tiktoken 0.12.0
tokenizers 0.22.2
torch 2.9.1
tqdm 4.67.2
transformers 4.57.6
typing-inspection 0.4.2
typing_extensions 4.15.0
urllib3 2.6.3
uvicorn 0.40.0
wcwidth 0.5.3
websocket-client 1.9.0
yarl 1.22.0
zipp 3.23.0
```

</details>

[Back to top](#contents)

### lightspeed-rhel9

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-26/lightspeed-rhel9` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/lightspeed-rhel9.tar.gz` |
| Labels `version` / `release` | `2.6.260325` / `1773939694` |
| Image ID | `sha256:9dda2a0299851c15f5d9f555d0fcfdd90eef385adb0a733902e68b6b701adbf8` |
| Build date | 2026-03-24T14:37:20Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.7 (Plow) |
| Python | 3.12 |
| Ansible Core | 2.16.16 |

<details><summary>RPM packages (153)</summary>

```text
acl 2.3.1-4.el9
alternatives 1.24-2.el9
audit-libs 3.1.5-7.el9
basesystem 11-13.el9
bash 5.1.8-9.el9
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crypto-policies 20250905-1.git377cc42.el9_7
curl-minimal 7.76.1-35.el9_7.3
cyrus-sasl-lib 2.1.27-22.el9
dbus 1.12.20-8.el9
dbus-broker 28-7.el9
dbus-common 1.12.20-8.el9
dejavu-sans-fonts 2.37-18.el9
dnf-data 4.14.0-31.el9
expat 2.5.0-5.el9_7.1
file-libs 5.39-16.el9
filesystem 3.16-5.el9
flexiblas 3.0.4-8.el9
flexiblas-netlib 3.0.4-8.el9
flexiblas-openblas-openmp 3.0.4-8.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdbm-libs 1.23-1.el9
glib2 2.68.4-18.el9_7.1
glibc 2.34-231.el9_7.10
glibc-common 2.34-231.el9_7.10
glibc-langpack-en 2.34-231.el9_7.10
glibc-minimal-langpack 2.34-231.el9_7.10
gmp 6.2.0-13.el9
gnupg2 2.3.3-5.el9_7
gnutls 3.8.3-10.el9_7
gobject-introspection 1.68.0-11.el9
gpg-pubkey 5a6340b3-6229229e
gpg-pubkey fd431d51-4ae0493b
gpgme 1.15.1-6.el9
grep 3.6-5.el9
gzip 1.12-1.el9
json-c 0.14-11.el9
json-glib 1.6.6-1.el9
keyutils-libs 1.6.3-1.el9
kmod-libs 28-11.el9
krb5-libs 1.21.1-8.el9_6
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-7.el9_7
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9_7
libcap 2.48-10.el9
libcap-ng 0.8.2-7.el9
libcom_err 1.46.5-8.el9
libcurl-minimal 7.76.1-35.el9_7.3
libdb 5.3.28-57.el9_6
libdnf 0.69.0-17.el9_7
libeconf 0.4.1-4.el9
libevent 2.1.12-8.el9_4
libfdisk 2.37.4-21.el9_7
libffi 3.4.2-8.el9
libgcc 11.5.0-11.el9
libgcrypt 1.10.0-11.el9
libgfortran 11.5.0-11.el9
libgomp 11.5.0-11.el9
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libksba 1.5.1-7.el9
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9_7
libnghttp2 1.43.0-6.el9
libnsl2 2.0.0-1.el9
libpeas 1.30.0-4.el9
libpq 13.23-1.el9_7
libpwquality 1.4.4-8.el9
libquadmath 11.5.0-11.el9
librepo 1.14.5-3.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libseccomp 2.5.2-2.el9
libselinux 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-3.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9_7
libsolv 0.7.24-3.el9
libstdc++ 11.5.0-11.el9
libtasn1 4.16.0-9.el9
libtirpc 1.3.3-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libusbx 1.0.26-1.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9_7
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-14.el9_7
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
microdnf 3.9.1-3.el9
mpdecimal 2.5.1-3.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-12.20210508.el9
ncurses-libs 6.2-12.20210508.el9
nettle 3.10.1-1.el9
nginx 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
nginx-core 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
nginx-filesystem 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
npth 1.6-8.el9
openblas 0.3.29-1.el9
openblas-openmp 0.3.29-1.el9
openldap 2.6.8-4.el9
openssl 3.5.1-7.el9_7
openssl-fips-provider 3.0.7-8.el9
openssl-fips-provider-so 3.0.7-8.el9
openssl-libs 3.5.1-7.el9_7
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pam 1.5.1-26.el9_6
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
popt 1.18-8.el9
python3.12 3.12.12-4.el9_7.1
python3.12-libs 3.12.12-4.el9_7.1
python3.12-numpy 1.24.4-3.el9
python3.12-pip 23.2.1-5.el9
python3.12-pip-wheel 23.2.1-5.el9
python3.12-pyyaml 6.0.1-2.el9
readline 8.1-4.el9
redhat-logos-httpd 90.5-1.el9_6.1
redhat-release 9.7-0.7.el9
rootfiles 8.1-35.el9
rpm 4.16.1.3-39.el9
rpm-libs 4.16.1.3-39.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-15.el9
sqlite-libs 3.34.1-9.el9_7
systemd 252-55.el9_7.7
systemd-libs 252-55.el9_7.7
systemd-pam 252-55.el9_7.7
systemd-rpm-macros 252-55.el9_7.7
tzdata 2026a-1.el9
util-linux 2.37.4-21.el9_7
util-linux-core 2.37.4-21.el9_7
xz-libs 5.2.5-8.el9_0
zlib 1.2.11-40.el9
```

</details>

<details><summary>Python packages: /usr (python3.12) (3)</summary>

```text
numpy 1.24.4
pip 23.2.1
PyYAML 6.0.1
```

</details>

<details><summary>Python packages: /usr/local (python3.12) (2)</summary>

```text
setuptools 80.9.0
supervisor 4.2.5
```

</details>

<details><summary>Python packages: /var/www/venv (python3.12) (165)</summary>

```text
aiohappyeyeballs 2.6.1
aiohttp 3.13.3
aiosignal 1.4.0
annotated-types 0.7.0
ansible-ai-connect 0.1.0
ansible-anonymizer 1.5.0
ansible-compat 25.12.0
ansible-core 2.16.16
ansible-lint 25.5.0
anyio 4.9.0
argparse 1.4.0
asgiref 3.8.1
asttokens 3.0.0
attrs 25.3.0
autobahn 24.4.2
Automat 25.4.16
backcall 0.2.0
backoff 2.2.1
black 25.1.0
boto3 1.40.64
botocore 1.40.64
bracex 2.5.post1
cachetools 5.5.2
cbor2 5.8.0
certifi 2038.12.31
cffi 1.17.1
charset-normalizer 3.4.2
click 8.2.1
constantly 23.10.4
cryptography 45.0.3
Cython 3.2.4
daphne 4.2.1
decorator 5.2.1
defusedxml 0.7.1
diff-match-patch 20241021
distro 1.9.0
Django 5.2.12
django-allow-cidr 0.8.0
django-ansible-base 2.6.20260325
django-crum 0.7.9
django-deprecate-fields 0.1.2
django-extensions 3.2.3
django-health-check 3.17.0
django-import-export 3.2.0
django-oauth-toolkit 3.0.1
django-prometheus 2.2.0
django-test-migrations 1.5.0
django_csp 3.8
djangorestframework 3.15.2
drf-spectacular 0.29.0
dynaconf 3.2.11
et_xmlfile 2.0.0
executing 2.2.0
expiringdict 1.2.2
filelock 3.20.3
fire 0.7.0
frozenlist 1.6.0
google-api-core 2.24.2
google-api-python-client 2.170.0
google-auth 2.40.2
google-auth-httplib2 0.2.0
googleapis-common-protos 1.70.0
h11 0.16.0
httpcore 1.0.9
httplib2 0.22.0
httpx 0.28.1
hyperlink 21.0.0
idna 3.10
importlib_metadata 8.7.1
incremental 24.7.2
inflection 0.5.1
ipython 8.10.0
jedi 0.19.2
Jinja2 3.1.6
jmespath 1.0.1
jsonschema 4.24.0
jsonschema-specifications 2025.4.1
jwcrypto 1.5.6
launchdarkly-server-sdk 8.3.0
llama_stack_client 0.2.22
markdown-it-py 3.0.0
MarkupSafe 3.0.2
matplotlib-inline 0.1.7
mdurl 0.1.2
monotonic 1.6
multidict 6.4.4
mypy_extensions 1.1.0
numpy 2.2.6
oauth2client 4.1.3
oauthlib 3.3.1
odfpy 1.4.1
openpyxl 3.1.5
packaging 25.0
pandas 2.2.3
parso 0.8.4
pathspec 0.12.1
pexpect 4.9.0
pickleshare 0.7.5
platformdirs 4.3.8
prometheus_client 0.22.0
prompt_toolkit 3.0.51
propcache 0.3.1
proto-plus 1.26.1
protobuf 5.29.5
psycopg 3.2.13
ptyprocess 0.7.0
pure_eval 0.2.3
pyaml 25.5.0
pyasn1 0.6.2
pyasn1_modules 0.4.2
pycparser 2.22
pydantic 2.11.5
pydantic_core 2.33.2
PyDrive2 1.20.0
Pygments 2.19.1
PyJWT 2.11.0
pyOpenSSL 25.1.0
pyparsing 3.2.3
pyRFC3339 2.0.1
python-dateutil 2.9.0.post0
python3-openid 3.2.0
pytz 2025.2
PyYAML 6.0.2
referencing 0.36.2
requests 2.32.5
requests-oauthlib 2.0.0
resolvelib 1.0.1
rich 14.0.0
rpds-py 0.24.0
rsa 4.9.1
ruamel.yaml 0.18.12
ruamel.yaml.clib 0.2.12
s3transfer 0.14.0
segment-analytics-python 2.2.3
semver 3.0.4
service-identity 24.2.0
six 1.17.0
slack_sdk 3.31.0
sniffio 1.3.1
social-auth-app-django 5.4.3
social-auth-core 4.7.0
sqlparse 0.5.3
stack_data 0.6.3
subprocess-tee 0.4.2
tablib 3.8.0
termcolor 3.1.0
tqdm 4.67.1
traitlets 5.14.3
Twisted 24.11.0
txaio 23.1.1
typing-inspection 0.4.1
typing_extensions 4.14.0
tzdata 2025.2
uritemplate 4.1.1
urllib3 2.6.3
uWSGI 2.0.29
uwsgi-readiness-check 0.2.0
wcmatch 10.0
wcwidth 0.2.13
xlrd 2.0.1
xlwt 1.3.0
yamllint 1.37.1
yarl 1.20.0
zipp 3.23.0
zope.interface 7.2
```

</details>

[Back to top](#contents)

### mcp-tools-rhel9

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-26/mcp-tools-rhel9` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/mcp-tools-rhel9.tar.gz` |
| Labels `version` / `release` | `2.6.250924` / `1773939694` |
| Image ID | `sha256:891bb66c5e58507c1a49509a49123f3fe04e3b50af4aaaa89213568f6f675af3` |
| Build date | 2026-03-23T12:16:14Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.7 (Plow) |
| Python | 3.12 |
| Ansible Core | N/A |

<details><summary>RPM packages (120)</summary>

```text
alternatives 1.24-2.el9
audit-libs 3.1.5-7.el9
basesystem 11-13.el9
bash 5.1.8-9.el9
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
crypto-policies 20250905-1.git377cc42.el9_7
curl-minimal 7.76.1-35.el9_7.3
cyrus-sasl-lib 2.1.27-22.el9
dejavu-sans-fonts 2.37-18.el9
dnf-data 4.14.0-31.el9
expat 2.5.0-5.el9_7.1
file-libs 5.39-16.el9
filesystem 3.16-5.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdbm-libs 1.23-1.el9
glib2 2.68.4-18.el9_7.1
glibc 2.34-231.el9_7.10
glibc-common 2.34-231.el9_7.10
glibc-minimal-langpack 2.34-231.el9_7.10
gmp 6.2.0-13.el9
gnupg2 2.3.3-5.el9_7
gnutls 3.8.3-10.el9_7
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
libarchive 3.5.3-7.el9_7
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9_7
libcap 2.48-10.el9
libcap-ng 0.8.2-7.el9
libcom_err 1.46.5-8.el9
libcurl-minimal 7.76.1-35.el9_7.3
libdnf 0.69.0-17.el9_7
libevent 2.1.12-8.el9_4
libffi 3.4.2-8.el9
libgcc 11.5.0-11.el9
libgcrypt 1.10.0-11.el9
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libksba 1.5.1-7.el9
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9_7
libnghttp2 1.43.0-6.el9
libnsl2 2.0.0-1.el9
libpeas 1.30.0-4.el9
librepo 1.14.5-3.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libselinux 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-3.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9_7
libsolv 0.7.24-3.el9
libstdc++ 11.5.0-11.el9
libtasn1 4.16.0-9.el9
libtirpc 1.3.3-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libusbx 1.0.26-1.el9
libuuid 2.37.4-21.el9_7
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-14.el9_7
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
microdnf 3.9.1-3.el9
mpdecimal 2.5.1-3.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-12.20210508.el9
ncurses-libs 6.2-12.20210508.el9
nettle 3.10.1-1.el9
npth 1.6-8.el9
openldap 2.6.8-4.el9
openssl-fips-provider 3.0.7-8.el9
openssl-fips-provider-so 3.0.7-8.el9
openssl-libs 3.5.1-7.el9_7
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
popt 1.18-8.el9
python3.12 3.12.12-4.el9_7.1
python3.12-cffi 1.16.0-2.el9
python3.12-idna 3.4-2.el9
python3.12-libs 3.12.12-4.el9_7.1
python3.12-pip 23.2.1-5.el9
python3.12-pip-wheel 23.2.1-5.el9
python3.12-ply 3.11-2.el9
python3.12-pycparser 2.20-2.el9
readline 8.1-4.el9
redhat-release 9.7-0.7.el9
rootfiles 8.1-35.el9
rpm 4.16.1.3-39.el9
rpm-libs 4.16.1.3-39.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-15.el9
sqlite-libs 3.34.1-9.el9_7
systemd-libs 252-55.el9_7.7
tzdata 2026a-1.el9
xz-libs 5.2.5-8.el9_0
zlib 1.2.11-40.el9
```

</details>

<details><summary>Python packages: /usr (python3.12) (5)</summary>

```text
cffi 1.16.0
idna 3.4
pip 23.2.1
ply 3.11
pycparser 2.20
```

</details>

<details><summary>Python packages: /usr/local (python3.12) (42)</summary>

```text
annotated-types 0.7.0
ansible-mcp-tools 0.1.0
anyio 4.12.1
attrs 25.4.0
cachetools 6.2.4
certifi 2026.1.4
cffi 2.0.0
click 8.3.1
cryptography 46.0.5
fire 0.7.1
gunicorn 23.0.0
h11 0.16.0
httpcore 1.0.9
httpx 0.28.1
httpx-sse 0.4.3
jsonschema 4.25.1
jsonschema-specifications 2025.9.1
markdown-it-py 4.0.0
mcp 1.26.0
mdurl 0.1.2
packaging 25.0
pydantic 2.12.5
pydantic-settings 2.12.0
pydantic_core 2.41.5
Pygments 2.19.2
PyJWT 2.10.1
python-dotenv 1.2.1
python-multipart 0.0.21
PyYAML 6.0.3
referencing 0.37.0
rich 14.2.0
rpds-py 0.24.0
shellingham 1.5.4
shortuuid 1.0.13
sse-starlette 3.1.2
starlette 0.50.0
termcolor 3.3.0
typer 0.21.1
typing-inspection 0.4.2
typing_extensions 4.15.0
uvicorn 0.40.0
uvicorn-worker 0.4.0
```

</details>

[Back to top](#contents)

### receptor-rhel9

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-26/receptor-rhel9` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/receptor-rhel9.tar.gz` |
| Labels `version` / `release` | `1.6.4` / `1773939694` |
| Image ID | `sha256:f6f72784e6e0f9e806b242330a9f44428dc9eed1b3af969c3349e95a1e1fe424` |
| Build date | 2026-03-27T00:57:15Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.7 (Plow) |
| Python | 3.12 |
| Ansible Core | N/A |

<details><summary>RPM packages (118)</summary>

```text
alternatives 1.24-2.el9
audit-libs 3.1.5-7.el9
basesystem 11-13.el9
bash 5.1.8-9.el9
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
crypto-policies 20250905-1.git377cc42.el9_7
curl-minimal 7.76.1-35.el9_7.3
cyrus-sasl-lib 2.1.27-22.el9
dejavu-sans-fonts 2.37-18.el9
dnf-data 4.14.0-31.el9
expat 2.5.0-5.el9_7.1
file-libs 5.39-16.el9
filesystem 3.16-5.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdbm-libs 1.23-1.el9
glib2 2.68.4-18.el9_7.1
glibc 2.34-231.el9_7.10
glibc-common 2.34-231.el9_7.10
glibc-minimal-langpack 2.34-231.el9_7.10
gmp 6.2.0-13.el9
gnupg2 2.3.3-5.el9_7
gnutls 3.8.3-10.el9_7
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
libarchive 3.5.3-7.el9_7
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9_7
libcap 2.48-10.el9
libcap-ng 0.8.2-7.el9
libcom_err 1.46.5-8.el9
libcurl-minimal 7.76.1-35.el9_7.3
libdnf 0.69.0-17.el9_7
libevent 2.1.12-8.el9_4
libffi 3.4.2-8.el9
libgcc 11.5.0-11.el9
libgcrypt 1.10.0-11.el9
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libksba 1.5.1-7.el9
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9_7
libnghttp2 1.43.0-6.el9
libnsl2 2.0.0-1.el9
libpeas 1.30.0-4.el9
librepo 1.14.5-3.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libselinux 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-3.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9_7
libsolv 0.7.24-3.el9
libstdc++ 11.5.0-11.el9
libtasn1 4.16.0-9.el9
libtirpc 1.3.3-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libusbx 1.0.26-1.el9
libuuid 2.37.4-21.el9_7
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-14.el9_7
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
microdnf 3.9.1-3.el9
mpdecimal 2.5.1-3.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-12.20210508.el9
ncurses-libs 6.2-12.20210508.el9
nettle 3.10.1-1.el9
npth 1.6-8.el9
openldap 2.6.8-4.el9
openssl-fips-provider 3.0.7-8.el9
openssl-fips-provider-so 3.0.7-8.el9
openssl-libs 3.5.1-7.el9_7
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
podman-remote 5.6.0-14.el9_7
popt 1.18-8.el9
python3.12 3.12.12-4.el9_7.1
python3.12-libs 3.12.12-4.el9_7.1
python3.12-pip 23.2.1-5.el9
python3.12-pip-wheel 23.2.1-5.el9
readline 8.1-4.el9
redhat-release 9.7-0.7.el9
rootfiles 8.1-35.el9
rpm 4.16.1.3-39.el9
rpm-libs 4.16.1.3-39.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-15.el9
shadow-utils-subid 4.9-15.el9
sqlite-libs 3.34.1-9.el9_7
systemd-libs 252-55.el9_7.7
tzdata 2026a-1.el9
xz-libs 5.2.5-8.el9_0
zlib 1.2.11-40.el9
```

</details>

<details><summary>Python packages: /usr (python3.12) (9)</summary>

```text
ansible-runner 2.4.3
dumb-init 1.2.5.post1
lockfile 0.12.2
packaging 26.0
pexpect 4.9.0
pip 23.2.1
ptyprocess 0.7.0
python-daemon 3.1.2
PyYAML 6.0.3
```

</details>

[Back to top](#contents)

### mcp-server-rhel9

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-tech-preview/mcp-server-rhel9` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/mcp-server-rhel9.tar.gz` |
| Labels `version` / `release` | `2.6.20260325` / `1774226014` |
| Image ID | `sha256:2ecee019a1d1605ed08d452fabd60877a4ab4c454876c7e2798080b53c0355f0` |
| Build date | 2026-03-23T12:14:24Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.7 (Plow) |
| Python | N/A |
| Ansible Core | N/A |

<details><summary>RPM packages (144)</summary>

```text
acl 2.3.1-4.el9
alternatives 1.24-2.el9
audit-libs 3.1.5-7.el9
basesystem 11-13.el9
bash 5.1.8-9.el9
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crypto-policies 20250905-1.git377cc42.el9_7
curl-minimal 7.76.1-35.el9_7.3
cyrus-sasl-lib 2.1.27-22.el9
dbus 1.12.20-8.el9
dbus-broker 28-7.el9
dbus-common 1.12.20-8.el9
dejavu-sans-fonts 2.37-18.el9
dnf-data 4.14.0-31.el9
expat 2.5.0-5.el9_7.1
file-libs 5.39-16.el9
filesystem 3.16-5.el9
findutils 4.8.0-7.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdbm-libs 1.23-1.el9
glib2 2.68.4-18.el9_7.1
glibc 2.34-231.el9_7.10
glibc-common 2.34-231.el9_7.10
glibc-langpack-en 2.34-231.el9_7.10
glibc-minimal-langpack 2.34-231.el9_7.10
gmp 6.2.0-13.el9
gnupg2 2.3.3-5.el9_7
gnutls 3.8.3-10.el9_7
gobject-introspection 1.68.0-11.el9
gpg-pubkey 5a6340b3-6229229e
gpg-pubkey fd431d51-4ae0493b
gpgme 1.15.1-6.el9
grep 3.6-5.el9
gzip 1.12-1.el9
json-c 0.14-11.el9
json-glib 1.6.6-1.el9
keyutils-libs 1.6.3-1.el9
kmod-libs 28-11.el9
krb5-libs 1.21.1-8.el9_6
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-7.el9_7
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9_7
libbrotli 1.0.9-9.el9_7
libcap 2.48-10.el9
libcap-ng 0.8.2-7.el9
libcom_err 1.46.5-8.el9
libcurl-minimal 7.76.1-35.el9_7.3
libdb 5.3.28-57.el9_6
libdnf 0.69.0-17.el9_7
libeconf 0.4.1-4.el9
libevent 2.1.12-8.el9_4
libfdisk 2.37.4-21.el9_7
libffi 3.4.2-8.el9
libgcc 11.5.0-11.el9
libgcrypt 1.10.0-11.el9
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libksba 1.5.1-7.el9
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9_7
libnghttp2 1.43.0-6.el9
libpeas 1.30.0-4.el9
libpwquality 1.4.4-8.el9
librepo 1.14.5-3.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libseccomp 2.5.2-2.el9
libselinux 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-3.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9_7
libsolv 0.7.24-3.el9
libstdc++ 11.5.0-11.el9
libtasn1 4.16.0-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libusbx 1.0.26-1.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9_7
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-14.el9_7
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
microdnf 3.9.1-3.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-12.20210508.el9
ncurses-libs 6.2-12.20210508.el9
nettle 3.10.1-1.el9
nginx 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
nginx-core 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
nginx-filesystem 1.24.0-5.module+el9.7.0+24009+e763bdd7.1
nodejs 22.22.0-1.module+el9.7.0+23896+b5802de9
nodejs-full-i18n 22.22.0-1.module+el9.7.0+23896+b5802de9
nodejs-libs 22.22.0-1.module+el9.7.0+23896+b5802de9
nodejs-nodemon 3.0.1-1.module+el9.7.0+23896+b5802de9
npm 10.9.4-1.22.22.0.1.module+el9.7.0+23896+b5802de9
npth 1.6-8.el9
openldap 2.6.8-4.el9
openssl 3.5.1-7.el9_7
openssl-fips-provider 3.0.7-8.el9
openssl-fips-provider-so 3.0.7-8.el9
openssl-libs 3.5.1-7.el9_7
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pam 1.5.1-26.el9_6
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
popt 1.18-8.el9
readline 8.1-4.el9
redhat-logos-httpd 90.5-1.el9_6.1
redhat-release 9.7-0.7.el9
rootfiles 8.1-35.el9
rpm 4.16.1.3-39.el9
rpm-libs 4.16.1.3-39.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-15.el9
sqlite-libs 3.34.1-9.el9_7
systemd 252-55.el9_7.7
systemd-libs 252-55.el9_7.7
systemd-pam 252-55.el9_7.7
systemd-rpm-macros 252-55.el9_7.7
tar 1.34-9.el9_7
tzdata 2026a-1.el9
util-linux 2.37.4-21.el9_7
util-linux-core 2.37.4-21.el9_7
which 2.21-30.el9_6
xz-libs 5.2.5-8.el9_0
zlib 1.2.11-40.el9
```

</details>

[Back to top](#contents)

### metrics-service-rhel9

| Field | Value |
|---|---|
| Image | `registry.redhat.io/ansible-automation-platform-tech-preview/metrics-service-rhel9` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/metrics-service-rhel9.tar.gz` |
| Labels `version` / `release` | `0.0.1` / `1773939694` |
| Image ID | `sha256:5826c35fd8a34a65a27a962004319cae172cfb4bc2242a065df18fdfa4dd98ee` |
| Build date | 2026-03-26T15:50:48Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.7 (Plow) |
| Python | 3.12 |
| Ansible Core | N/A |

<details><summary>RPM packages (137)</summary>

```text
alternatives 1.24-2.el9
audit-libs 3.1.5-7.el9
basesystem 11-13.el9
bash 5.1.8-9.el9
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crypto-policies 20250905-1.git377cc42.el9_7
curl-minimal 7.76.1-35.el9_7.3
cyrus-sasl-lib 2.1.27-22.el9
dejavu-sans-fonts 2.37-18.el9
dnf-data 4.14.0-31.el9
expat 2.5.0-5.el9_7.1
file-libs 5.39-16.el9
filesystem 3.16-5.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdbm-libs 1.23-1.el9
git-core 2.47.3-1.el9_6
glib2 2.68.4-18.el9_7.1
glibc 2.34-231.el9_7.10
glibc-common 2.34-231.el9_7.10
glibc-langpack-en 2.34-231.el9_7.10
glibc-minimal-langpack 2.34-231.el9_7.10
gmp 6.2.0-13.el9
gnupg2 2.3.3-5.el9_7
gnutls 3.8.3-10.el9_7
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
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
less 590-6.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-7.el9_7
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9_7
libcap 2.48-10.el9
libcap-ng 0.8.2-7.el9
libcbor 0.7.0-5.el9
libcom_err 1.46.5-8.el9
libcurl-minimal 7.76.1-35.el9_7.3
libdb 5.3.28-57.el9_6
libdnf 0.69.0-17.el9_7
libeconf 0.4.1-4.el9
libedit 3.1-38.20210216cvs.el9
libevent 2.1.12-8.el9_4
libfdisk 2.37.4-21.el9_7
libffi 3.4.2-8.el9
libfido2 1.13.0-2.el9
libgcc 11.5.0-11.el9
libgcrypt 1.10.0-11.el9
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libksba 1.5.1-7.el9
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9_7
libnghttp2 1.43.0-6.el9
libnsl2 2.0.0-1.el9
libpeas 1.30.0-4.el9
libpq 13.23-1.el9_7
libpwquality 1.4.4-8.el9
librepo 1.14.5-3.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libselinux 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-3.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9_7
libsolv 0.7.24-3.el9
libstdc++ 11.5.0-11.el9
libtasn1 4.16.0-9.el9
libtirpc 1.3.3-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libusbx 1.0.26-1.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9_7
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-14.el9_7
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
microdnf 3.9.1-3.el9
mpdecimal 2.5.1-3.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-12.20210508.el9
ncurses-libs 6.2-12.20210508.el9
nettle 3.10.1-1.el9
npth 1.6-8.el9
openldap 2.6.8-4.el9
openssh 8.7p1-47.el9_7
openssh-clients 8.7p1-47.el9_7
openssl 3.5.1-7.el9_7
openssl-fips-provider 3.0.7-8.el9
openssl-fips-provider-so 3.0.7-8.el9
openssl-libs 3.5.1-7.el9_7
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pam 1.5.1-26.el9_6
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
popt 1.18-8.el9
python3.12 3.12.12-4.el9_7.1
python3.12-libs 3.12.12-4.el9_7.1
python3.12-pip 23.2.1-5.el9
python3.12-pip-wheel 23.2.1-5.el9
readline 8.1-4.el9
redhat-release 9.7-0.7.el9
rootfiles 8.1-35.el9
rpm 4.16.1.3-39.el9
rpm-libs 4.16.1.3-39.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-15.el9
sqlite-libs 3.34.1-9.el9_7
systemd-libs 252-55.el9_7.7
tzdata 2026a-1.el9
util-linux 2.37.4-21.el9_7
util-linux-core 2.37.4-21.el9_7
xz-libs 5.2.5-8.el9_0
zlib 1.2.11-40.el9
```

</details>

<details><summary>Python packages: /usr (python3.12) (65)</summary>

```text
APScheduler 3.11.2
asgiref 3.11.1
attrs 25.4.0
backoff 2.2.1
boto3 1.35.96
botocore 1.35.96
certifi 2038.12.31
cffi 2.0.0
charset-normalizer 3.4.4
croniter 6.0.0
cryptography 42.0.8
dispatcherd 2026.1.27
distro 1.9.0
Django 5.2.7
django-ansible-base 2.6.20260325
django-crum 0.7.9
django-extensions 4.1
django-flags 5.2.0
django-prometheus 2.4.1
djangorestframework 3.15.2
drf-spectacular 0.29.0
dumb-init 1.2.5.post1
durationpy 0.10
dynaconf 3.2.12
et_xmlfile 2.0.0
gunicorn 25.1.0
idna 3.11
inflection 0.5.1
jmespath 1.1.0
jsonschema 4.25.1
jsonschema-specifications 2025.9.1
kubernetes 35.0.0
metrics-service 0.0.1
metrics-utility 0.7.0
numpy 2.4.2
oauthlib 3.3.1
openpyxl 3.1.2
packaging 26.0
pandas 3.0.1
pip 23.2.1
pip 26.0.1
prometheus_client 0.24.1
psycopg 3.3.0
psycopg-c 3.3.0
psycopg2 2.9.11
pycparser 3.0
PyJWT 2.10.1
python-dateutil 2.9.0.post0
pytz 2025.2
PyYAML 6.0.3
referencing 0.36.2
requests 2.32.5
requests-oauthlib 2.0.0
rpds-py 0.24.0
s3transfer 0.10.4
segment-analytics-python 2.3.5
setuptools 80.9.0
six 1.17.0
sqlparse 0.5.5
typing_extensions 4.15.0
tzlocal 5.3.1
uritemplate 4.2.0
urllib3 2.6.3
websocket-client 1.9.0
whitenoise 6.12.0
```

</details>

[Back to top](#contents)

### pcp

| Field | Value |
|---|---|
| Image | `registry.redhat.io/rhel9/pcp` |
| Tag in bundle | `latest` |
| Archive | `bundle/images/pcp.tar.gz` |
| Labels `version` / `release` | `6` / `1774442196` |
| Image ID | `sha256:0f8a38250dcb12a077d315e26b8ce68db811e5308632c9de9da4aad858ba8b2a` |
| Build date | 2026-03-25T12:37:05Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.7 (Plow) |
| Python | 3.9 |
| Ansible Core | N/A |

<details><summary>RPM packages (212)</summary>

```text
acl 2.3.1-4.el9
alternatives 1.24-2.el9
attr 2.5.1-3.el9
audit-libs 3.1.5-7.el9
avahi-libs 0.8-23.el9
basesystem 11-13.el9
bash 5.1.8-9.el9
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crypto-policies 20250905-1.git377cc42.el9_7
crypto-policies-scripts 20250905-1.git377cc42.el9_7
curl-minimal 7.76.1-35.el9_7.3
cyrus-sasl-lib 2.1.27-22.el9
dbus 1.12.20-8.el9
dbus-broker 28-7.el9
dbus-common 1.12.20-8.el9
dbus-libs 1.12.20-8.el9
dejavu-sans-fonts 2.37-18.el9
device-mapper 1.02.206-2.el9_7.2
device-mapper-libs 1.02.206-2.el9_7.2
diffutils 3.7-12.el9
dmidecode 3.6-1.el9
dnf 4.14.0-31.el9
dnf-data 4.14.0-31.el9
elfutils-default-yama-scope 0.193-1.el9
elfutils-libelf 0.193-1.el9
elfutils-libs 0.193-1.el9
expat 2.5.0-5.el9_7.1
file-libs 5.39-16.el9
filesystem 3.16-5.el9
findutils 4.8.0-7.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdb-gdbserver 16.3-2.el9
gdbm-libs 1.23-1.el9
gettext 0.21-8.el9
gettext-libs 0.21-8.el9
glib2 2.68.4-18.el9_7.1
glibc 2.34-231.el9_7.10
glibc-common 2.34-231.el9_7.10
glibc-minimal-langpack 2.34-231.el9_7.10
gmp 6.2.0-13.el9
gnupg2 2.3.3-5.el9_7
gnutls 3.8.3-10.el9_7
gobject-introspection 1.68.0-11.el9
gpg-pubkey 5a6340b3-6229229e
gpg-pubkey fd431d51-4ae0493b
gpgme 1.15.1-6.el9
grep 3.6-5.el9
gzip 1.12-1.el9
hostname 3.23-6.el9
ima-evm-utils 1.6.2-2.el9
iproute 6.14.0-2.el9
json-c 0.14-11.el9
json-glib 1.6.6-1.el9
keyutils 1.6.3-1.el9
keyutils-libs 1.6.3-1.el9
kmod-libs 28-11.el9
krb5-libs 1.21.1-8.el9_6
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-7.el9_7
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9_7
libbpf 1.5.0-2.el9
libcap 2.48-10.el9
libcap-ng 0.8.2-7.el9
libcom_err 1.46.5-8.el9
libcomps 0.1.18-1.el9
libcurl-minimal 7.76.1-35.el9_7.3
libdb 5.3.28-57.el9_6
libdnf 0.69.0-17.el9_7
libdnf-plugin-subscription-manager 1.29.47.1-1.el9_7
libeconf 0.4.1-4.el9
libevent 2.1.12-8.el9_4
libfdisk 2.37.4-21.el9_7
libffi 3.4.2-8.el9
libgcc 11.5.0-11.el9
libgcrypt 1.10.0-11.el9
libgomp 11.5.0-11.el9
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libksba 1.5.1-7.el9
libmnl 1.0.4-16.el9_4
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9_7
libnghttp2 1.43.0-6.el9
libpkgconf 1.7.3-10.el9
libpwquality 1.4.4-8.el9
librepo 1.14.5-3.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libseccomp 2.5.2-2.el9
libselinux 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-3.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9_7
libsolv 0.7.24-3.el9
libstdc++ 11.5.0-11.el9
libtasn1 4.16.0-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libuser 0.63-17.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9_7
libuv 1.42.0-2.el9_4
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-14.el9_7
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-12.20210508.el9
ncurses-libs 6.2-12.20210508.el9
nettle 3.10.1-1.el9
npth 1.6-8.el9
openldap 2.6.8-4.el9
openssl 3.5.1-7.el9_7
openssl-fips-provider 3.0.7-8.el9
openssl-fips-provider-so 3.0.7-8.el9
openssl-libs 3.5.1-7.el9_7
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pam 1.5.1-26.el9_6
passwd 0.80-12.el9
pcp 6.3.7-5.el9
pcp-conf 6.3.7-5.el9
pcp-doc 6.3.7-5.el9
pcp-libs 6.3.7-5.el9
pcp-pmda-dm 6.3.7-5.el9
pcp-pmda-nfsclient 6.3.7-5.el9
pcp-pmda-openmetrics 6.3.7-5.el9
pcp-system-tools 6.3.7-5.el9
pcp-zeroconf 6.3.7-5.el9
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
pkgconf 1.7.3-10.el9
pkgconf-m4 1.7.3-10.el9
pkgconf-pkg-config 1.7.3-10.el9
popt 1.18-8.el9
procps-ng 3.3.17-14.el9
psmisc 23.4-3.el9
python3 3.9.25-3.el9_7.1
python3-chardet 4.0.0-5.el9
python3-cloud-what 1.29.47.1-1.el9_7
python3-dateutil 2.9.0.post0-1.el9_7
python3-dbus 1.2.18-2.el9
python3-decorator 4.4.2-6.el9
python3-dnf 4.14.0-31.el9
python3-dnf-plugins-core 4.3.0-24.el9_7
python3-gobject-base 3.40.1-6.el9
python3-gobject-base-noarch 3.40.1-6.el9
python3-gpg 1.15.1-6.el9
python3-hawkey 0.69.0-17.el9_7
python3-idna 2.10-7.el9_4.1
python3-iniparse 0.4-45.el9
python3-inotify 0.9.6-25.el9
python3-libcomps 0.1.18-1.el9
python3-libdnf 0.69.0-17.el9_7
python3-librepo 1.14.5-3.el9
python3-libs 3.9.25-3.el9_7.1
python3-pcp 6.3.7-5.el9
python3-pip-wheel 21.3.1-1.el9
python3-pysocks 1.7.1-12.el9
python3-requests 2.25.1-10.el9_6
python3-rpm 4.16.1.3-39.el9
python3-setuptools 53.0.0-15.el9
python3-setuptools-wheel 53.0.0-15.el9
python3-six 1.15.0-9.el9
python3-subscription-manager-rhsm 1.29.47.1-1.el9_7
python3-systemd 234-19.el9
python3-urllib3 1.26.5-6.el9_7.1
readline 8.1-4.el9
redhat-release 9.7-0.7.el9
rootfiles 8.1-35.el9
rpm 4.16.1.3-39.el9
rpm-build-libs 4.16.1.3-39.el9
rpm-libs 4.16.1.3-39.el9
rpm-sign-libs 4.16.1.3-39.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-15.el9
sqlite-libs 3.34.1-9.el9_7
subscription-manager 1.29.47.1-1.el9_7
subscription-manager-rhsm-certificates 20220623-1.el9
systemd 252-55.el9_7.7
systemd-libs 252-55.el9_7.7
systemd-pam 252-55.el9_7.7
systemd-rpm-macros 252-55.el9_7.7
tar 1.34-9.el9_7
tpm2-tss 3.2.3-1.el9
tzdata 2026a-1.el9
usermode 1.114-7.el9
util-linux 2.37.4-21.el9_7
util-linux-core 2.37.4-21.el9_7
vim-minimal 8.2.2637-23.el9_7.1
virt-what 1.27-2.el9
which 2.21-30.el9_6
xz 5.2.5-8.el9_0
xz-libs 5.2.5-8.el9_0
yum 4.14.0-31.el9
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
python-dateutil 2.9.0.post0
requests 2.25.1
rpm 4.16.1.3
setuptools 53.0.0
six 1.15.0
subscription-manager 1.29.47.1
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
| Labels `version` / `release` | `1` / `1775009263` |
| Image ID | `sha256:9d16ff88f306e9d5395f56aa54169347220efac81c37ee1bba51d353ee4895d5` |
| Build date | 2026-04-01T02:09:41Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.7 (Plow) |
| Python | 3.9 |
| Ansible Core | N/A |

<details><summary>RPM packages (280)</summary>

```text
acl 2.3.1-4.el9
alternatives 1.24-2.el9
attr 2.5.1-3.el9
audit-libs 3.1.5-7.el9
basesystem 11-13.el9
bash 5.1.8-9.el9
bind9.18-libs 9.18.29-5.el9_7.2
bind9.18-utils 9.18.29-5.el9_7.2
bsdtar 3.5.3-7.el9_7
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crypto-policies 20250905-1.git377cc42.el9_7
crypto-policies-scripts 20250905-1.git377cc42.el9_7
curl-minimal 7.76.1-35.el9_7.3
cyrus-sasl-lib 2.1.27-22.el9
dbus 1.12.20-8.el9
dbus-broker 28-7.el9
dbus-common 1.12.20-8.el9
dbus-libs 1.12.20-8.el9
dejavu-sans-fonts 2.37-18.el9
dmidecode 3.6-1.el9
dnf 4.14.0-31.el9
dnf-data 4.14.0-31.el9
elfutils-default-yama-scope 0.193-1.el9
elfutils-libelf 0.193-1.el9
elfutils-libs 0.193-1.el9
environment-modules 5.3.0-2.el9
expat 2.5.0-5.el9_7.1
file-libs 5.39-16.el9
filesystem 3.16-5.el9
findutils 4.8.0-7.el9
fonts-filesystem 2.0.5-7.el9.1
fstrm 0.6.1-3.el9
gawk 5.1.0-6.el9
gdb-gdbserver 16.3-2.el9
gdbm-libs 1.23-1.el9
gettext 0.21-8.el9
gettext-libs 0.21-8.el9
glib2 2.68.4-18.el9_7.1
glibc 2.34-231.el9_7.10
glibc-common 2.34-231.el9_7.10
glibc-langpack-en 2.34-231.el9_7.10
glibc-locale-source 2.34-231.el9_7.10
glibc-minimal-langpack 2.34-231.el9_7.10
gmp 6.2.0-13.el9
gnupg2 2.3.3-5.el9_7
gnutls 3.8.3-10.el9_7
gobject-introspection 1.68.0-11.el9
gpg-pubkey 5a6340b3-6229229e
gpg-pubkey fd431d51-4ae0493b
gpgme 1.15.1-6.el9
grep 3.6-5.el9
groff-base 1.22.4-10.el9
gzip 1.12-1.el9
ima-evm-utils 1.6.2-2.el9
iproute 6.14.0-2.el9
json-c 0.14-11.el9
json-glib 1.6.6-1.el9
keyutils 1.6.3-1.el9
keyutils-libs 1.6.3-1.el9
kmod-libs 28-11.el9
krb5-libs 1.21.1-8.el9_6
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
less 590-6.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-7.el9_7
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9_7
libbpf 1.5.0-2.el9
libcap 2.48-10.el9
libcap-ng 0.8.2-7.el9
libcom_err 1.46.5-8.el9
libcomps 0.1.18-1.el9
libcurl-minimal 7.76.1-35.el9_7.3
libdb 5.3.28-57.el9_6
libdnf 0.69.0-17.el9_7
libdnf-plugin-subscription-manager 1.29.47.1-1.el9_7
libeconf 0.4.1-4.el9
libevent 2.1.12-8.el9_4
libfdisk 2.37.4-21.el9_7
libffi 3.4.2-8.el9
libgcc 11.5.0-11.el9
libgcrypt 1.10.0-11.el9
libgomp 11.5.0-11.el9
libgpg-error 1.42-5.el9
libicu 67.1-10.el9_6
libidn2 2.3.0-7.el9
libksba 1.5.1-7.el9
libmaxminddb 1.5.2-4.el9
libmnl 1.0.4-16.el9_4
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9_7
libnghttp2 1.43.0-6.el9
libpipeline 1.5.3-4.el9
libpwquality 1.4.4-8.el9
librepo 1.14.5-3.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libseccomp 2.5.2-2.el9
libselinux 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-3.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9_7
libsolv 0.7.24-3.el9
libstdc++ 11.5.0-11.el9
libtasn1 4.16.0-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libuser 0.63-17.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9_7
libuv 1.42.0-2.el9_4
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-14.el9_7
libxslt 1.1.34-14.el9_7.1
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
lmdb-libs 0.9.29-3.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
man-db 2.9.3-9.el9
mpfr 4.1.0-7.el9
ncurses 6.2-12.20210508.el9
ncurses-base 6.2-12.20210508.el9
ncurses-libs 6.2-12.20210508.el9
nettle 3.10.1-1.el9
npth 1.6-8.el9
nss_wrapper-libs 1.1.13-1.el9
openldap 2.6.8-4.el9
openssl 3.5.1-7.el9_7
openssl-fips-provider 3.0.7-8.el9
openssl-fips-provider-so 3.0.7-8.el9
openssl-libs 3.5.1-7.el9_7
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
perl-Net-SSLeay 1.94-3.el9
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
postgresql 15.17-1.module+el9.7.0+24029+ef6a2953
postgresql-contrib 15.17-1.module+el9.7.0+24029+ef6a2953
postgresql-private-libs 15.17-1.module+el9.7.0+24029+ef6a2953
postgresql-server 15.17-1.module+el9.7.0+24029+ef6a2953
postgresql-upgrade 15.17-1.module+el9.7.0+24029+ef6a2953
procps-ng 3.3.17-14.el9
protobuf-c 1.3.3-13.el9
psmisc 23.4-3.el9
python3 3.9.25-3.el9_7.1
python3-chardet 4.0.0-5.el9
python3-cloud-what 1.29.47.1-1.el9_7
python3-dateutil 2.9.0.post0-1.el9_7
python3-dbus 1.2.18-2.el9
python3-decorator 4.4.2-6.el9
python3-dnf 4.14.0-31.el9
python3-dnf-plugins-core 4.3.0-24.el9_7
python3-gobject-base 3.40.1-6.el9
python3-gobject-base-noarch 3.40.1-6.el9
python3-gpg 1.15.1-6.el9
python3-hawkey 0.69.0-17.el9_7
python3-idna 2.10-7.el9_4.1
python3-iniparse 0.4-45.el9
python3-inotify 0.9.6-25.el9
python3-libcomps 0.1.18-1.el9
python3-libdnf 0.69.0-17.el9_7
python3-librepo 1.14.5-3.el9
python3-libs 3.9.25-3.el9_7.1
python3-pip-wheel 21.3.1-1.el9
python3-pysocks 1.7.1-12.el9
python3-requests 2.25.1-10.el9_6
python3-rpm 4.16.1.3-39.el9
python3-setuptools 53.0.0-15.el9
python3-setuptools-wheel 53.0.0-15.el9
python3-six 1.15.0-9.el9
python3-subscription-manager-rhsm 1.29.47.1-1.el9_7
python3-systemd 234-19.el9
python3-urllib3 1.26.5-6.el9_7.1
readline 8.1-4.el9
redhat-release 9.7-0.7.el9
rootfiles 8.1-35.el9
rpm 4.16.1.3-39.el9
rpm-build-libs 4.16.1.3-39.el9
rpm-libs 4.16.1.3-39.el9
rpm-sign-libs 4.16.1.3-39.el9
rsync 3.2.5-3.el9
scl-utils 2.0.3-4.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-15.el9
sqlite-libs 3.34.1-9.el9_7
subscription-manager 1.29.47.1-1.el9_7
subscription-manager-rhsm-certificates 20220623-1.el9
systemd 252-55.el9_7.7
systemd-libs 252-55.el9_7.7
systemd-pam 252-55.el9_7.7
systemd-rpm-macros 252-55.el9_7.7
tar 1.34-9.el9_7
tcl 8.6.10-7.el9
tpm2-tss 3.2.3-1.el9
tzdata 2026a-1.el9
unzip 6.0-59.el9
usermode 1.114-7.el9
util-linux 2.37.4-21.el9_7
util-linux-core 2.37.4-21.el9_7
uuid 1.6.2-55.el9
vim-filesystem 8.2.2637-23.el9_7.1
vim-minimal 8.2.2637-23.el9_7
virt-what 1.27-2.el9
which 2.21-30.el9_6
xz 5.2.5-8.el9_0
xz-libs 5.2.5-8.el9_0
yum 4.14.0-31.el9
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
python-dateutil 2.9.0.post0
requests 2.25.1
rpm 4.16.1.3
setuptools 53.0.0
six 1.15.0
subscription-manager 1.29.47.1
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
| Labels `version` / `release` | `1` / `1774456931` |
| Image ID | `sha256:bb35dedffd27752f131d3ea9d32e08dc80519460b3d1227a441eb24c6b1fc7f2` |
| Build date | 2026-03-25T16:42:40Z |
| Architecture | amd64 |
| RHEL version | Red Hat Enterprise Linux 9.7 (Plow) |
| Python | 3.9 |
| Ansible Core | N/A |

<details><summary>RPM packages (210)</summary>

```text
acl 2.3.1-4.el9
alternatives 1.24-2.el9
attr 2.5.1-3.el9
audit-libs 3.1.5-7.el9
basesystem 11-13.el9
bash 5.1.8-9.el9
bsdtar 3.5.3-7.el9_7
bzip2-libs 1.0.8-10.el9_5
ca-certificates 2024.2.69_v8.0.303-91.4.el9_4
coreutils-single 8.32-39.el9
cracklib 2.9.6-27.el9
cracklib-dicts 2.9.6-27.el9
crypto-policies 20250905-1.git377cc42.el9_7
crypto-policies-scripts 20250905-1.git377cc42.el9_7
curl-minimal 7.76.1-35.el9_7.3
cyrus-sasl-lib 2.1.27-22.el9
dbus 1.12.20-8.el9
dbus-broker 28-7.el9
dbus-common 1.12.20-8.el9
dbus-libs 1.12.20-8.el9
dejavu-sans-fonts 2.37-18.el9
diffutils 3.7-12.el9
dmidecode 3.6-1.el9
dnf 4.14.0-31.el9
dnf-data 4.14.0-31.el9
elfutils-default-yama-scope 0.193-1.el9
elfutils-libelf 0.193-1.el9
elfutils-libs 0.193-1.el9
environment-modules 5.3.0-2.el9
expat 2.5.0-5.el9_7.1
file-libs 5.39-16.el9
filesystem 3.16-5.el9
findutils 4.8.0-7.el9
fonts-filesystem 2.0.5-7.el9.1
gawk 5.1.0-6.el9
gdb-gdbserver 16.3-2.el9
gdbm-libs 1.23-1.el9
gettext 0.21-8.el9
gettext-libs 0.21-8.el9
glib2 2.68.4-18.el9_7.1
glibc 2.34-231.el9_7.10
glibc-common 2.34-231.el9_7.10
glibc-langpack-en 2.34-231.el9_7.10
glibc-locale-source 2.34-231.el9_7.10
glibc-minimal-langpack 2.34-231.el9_7.10
gmp 6.2.0-13.el9
gnupg2 2.3.3-5.el9_7
gnutls 3.8.3-10.el9_7
gobject-introspection 1.68.0-11.el9
gpg-pubkey 5a6340b3-6229229e
gpg-pubkey fd431d51-4ae0493b
gpgme 1.15.1-6.el9
grep 3.6-5.el9
groff-base 1.22.4-10.el9
gzip 1.12-1.el9
ima-evm-utils 1.6.2-2.el9
iproute 6.14.0-2.el9
json-c 0.14-11.el9
json-glib 1.6.6-1.el9
keyutils 1.6.3-1.el9
keyutils-libs 1.6.3-1.el9
kmod-libs 28-11.el9
krb5-libs 1.21.1-8.el9_6
langpacks-core-en 3.0-16.el9
langpacks-core-font-en 3.0-16.el9
langpacks-en 3.0-16.el9
less 590-6.el9
libacl 2.3.1-4.el9
libarchive 3.5.3-7.el9_7
libassuan 2.5.5-3.el9
libattr 2.5.1-3.el9
libblkid 2.37.4-21.el9_7
libbpf 1.5.0-2.el9
libcap 2.48-10.el9
libcap-ng 0.8.2-7.el9
libcom_err 1.46.5-8.el9
libcomps 0.1.18-1.el9
libcurl-minimal 7.76.1-35.el9_7.3
libdb 5.3.28-57.el9_6
libdnf 0.69.0-17.el9_7
libdnf-plugin-subscription-manager 1.29.47.1-1.el9_7
libeconf 0.4.1-4.el9
libevent 2.1.12-8.el9_4
libfdisk 2.37.4-21.el9_7
libffi 3.4.2-8.el9
libgcc 11.5.0-11.el9
libgcrypt 1.10.0-11.el9
libgomp 11.5.0-11.el9
libgpg-error 1.42-5.el9
libidn2 2.3.0-7.el9
libksba 1.5.1-7.el9
libmnl 1.0.4-16.el9_4
libmodulemd 2.13.0-2.el9
libmount 2.37.4-21.el9_7
libnghttp2 1.43.0-6.el9
libpipeline 1.5.3-4.el9
libpwquality 1.4.4-8.el9
librepo 1.14.5-3.el9
libreport-filesystem 2.15.2-6.el9
librhsm 0.0.3-9.el9
libseccomp 2.5.2-2.el9
libselinux 3.6-3.el9
libselinux-utils 3.6-3.el9
libsemanage 3.6-5.el9_6
libsepol 3.6-3.el9
libsigsegv 2.13-4.el9
libsmartcols 2.37.4-21.el9_7
libsolv 0.7.24-3.el9
libstdc++ 11.5.0-11.el9
libtasn1 4.16.0-9.el9
libtool-ltdl 2.4.6-46.el9
libunistring 0.9.10-15.el9
libuser 0.63-17.el9
libutempter 1.2.1-6.el9
libuuid 2.37.4-21.el9_7
libverto 0.3.2-3.el9
libxcrypt 4.4.18-3.el9
libxml2 2.9.13-14.el9_7
libyaml 0.2.5-7.el9
libzstd 1.5.5-1.el9
logrotate 3.18.0-12.el9
lua-libs 5.4.4-4.el9
lz4-libs 1.9.3-5.el9
man-db 2.9.3-9.el9
mpfr 4.1.0-7.el9
ncurses-base 6.2-12.20210508.el9
ncurses-libs 6.2-12.20210508.el9
nettle 3.10.1-1.el9
npth 1.6-8.el9
openldap 2.6.8-4.el9
openssl 3.5.1-7.el9_7
openssl-fips-provider 3.0.7-8.el9
openssl-fips-provider-so 3.0.7-8.el9
openssl-libs 3.5.1-7.el9_7
p11-kit 0.25.3-3.el9_5
p11-kit-trust 0.25.3-3.el9_5
pam 1.5.1-26.el9_6
passwd 0.80-12.el9
pcre 8.44-4.el9
pcre2 10.40-6.el9
pcre2-syntax 10.40-6.el9
policycoreutils 3.6-3.el9
popt 1.18-8.el9
procps-ng 3.3.17-14.el9
psmisc 23.4-3.el9
python3 3.9.25-3.el9_7.1
python3-chardet 4.0.0-5.el9
python3-cloud-what 1.29.47.1-1.el9_7
python3-dateutil 2.9.0.post0-1.el9_7
python3-dbus 1.2.18-2.el9
python3-decorator 4.4.2-6.el9
python3-dnf 4.14.0-31.el9
python3-dnf-plugins-core 4.3.0-24.el9_7
python3-gobject-base 3.40.1-6.el9
python3-gobject-base-noarch 3.40.1-6.el9
python3-gpg 1.15.1-6.el9
python3-hawkey 0.69.0-17.el9_7
python3-idna 2.10-7.el9_4.1
python3-iniparse 0.4-45.el9
python3-inotify 0.9.6-25.el9
python3-libcomps 0.1.18-1.el9
python3-libdnf 0.69.0-17.el9_7
python3-librepo 1.14.5-3.el9
python3-libs 3.9.25-3.el9_7.1
python3-pip-wheel 21.3.1-1.el9
python3-pysocks 1.7.1-12.el9
python3-requests 2.25.1-10.el9_6
python3-rpm 4.16.1.3-39.el9
python3-setuptools 53.0.0-15.el9
python3-setuptools-wheel 53.0.0-15.el9
python3-six 1.15.0-9.el9
python3-subscription-manager-rhsm 1.29.47.1-1.el9_7
python3-systemd 234-19.el9
python3-urllib3 1.26.5-6.el9_7.1
readline 8.1-4.el9
redhat-release 9.7-0.7.el9
redis 6.2.20-3.el9_7
rootfiles 8.1-35.el9
rpm 4.16.1.3-39.el9
rpm-build-libs 4.16.1.3-39.el9
rpm-libs 4.16.1.3-39.el9
rpm-sign-libs 4.16.1.3-39.el9
rsync 3.2.5-3.el9
scl-utils 2.0.3-4.el9
sed 4.8-9.el9
setup 2.13.7-10.el9
shadow-utils 4.9-15.el9
sqlite-libs 3.34.1-9.el9_7
subscription-manager 1.29.47.1-1.el9_7
subscription-manager-rhsm-certificates 20220623-1.el9
systemd 252-55.el9_7.7
systemd-libs 252-55.el9_7.7
systemd-pam 252-55.el9_7.7
systemd-rpm-macros 252-55.el9_7.7
tar 1.34-9.el9_7
tcl 8.6.10-7.el9
tpm2-tss 3.2.3-1.el9
tzdata 2026a-1.el9
unzip 6.0-59.el9
usermode 1.114-7.el9
util-linux 2.37.4-21.el9_7
util-linux-core 2.37.4-21.el9_7
vim-filesystem 8.2.2637-23.el9_7.1
vim-minimal 8.2.2637-23.el9_7
virt-what 1.27-2.el9
which 2.21-30.el9_6
xz 5.2.5-8.el9_0
xz-libs 5.2.5-8.el9_0
yum 4.14.0-31.el9
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
python-dateutil 2.9.0.post0
requests 2.25.1
rpm 4.16.1.3
setuptools 53.0.0
six 1.15.0
subscription-manager 1.29.47.1
systemd-python 234
urllib3 1.26.5
```

</details>

[Back to top](#contents)

## Installer Collections

Collections shipped with the installer itself (`collections/ansible_collections`).

- `ansible.posix 1.5.4`
- `community.crypto 2.26.7`
- `community.postgresql 3.14.3`
- `containers.podman 1.17.0`
- `infra.ah_configuration 2.0.6`
- `infra.controller_configuration 2.9.0`

## Bundled Collections

Collection tarballs under `bundle/collections/` (uploaded to Automation Hub during install).

<details><summary>Bundled collections (93)</summary>

```text
amazon.aws 9.5.1 (certified)
ansible.controller 4.7.10 (certified)
ansible.eda 2.11.0 (certified)
ansible.hub 1.0.1 (certified)
ansible.netcommon 8.1.0 (certified)
ansible.network 5.0.0 (certified)
ansible.platform 2.6.20260306 (certified)
ansible.posix 2.1.0 (certified)
ansible.scm 3.0.0 (certified)
ansible.security 5.0.0 (certified)
ansible.snmp 3.0.0 (certified)
ansible.utils 6.0.0 (certified)
ansible.windows 3.4.0 (certified)
ansible.yang 3.0.0 (certified)
arista.eos 12.0.0 (certified)
azure.azcollection 3.7.0 (certified)
cisco.cvd_compute 1.1.0 (validated)
cisco.intersight 2.2.0 (certified)
cisco.ios 11.1.1 (certified)
cisco.iosxr 12.0.0 (certified)
cisco.nxos 11.0.0 (certified)
cloud.aws_ops 4.0.0 (validated)
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
hashicorp.terraform 1.1.0 (certified)
hashicorp.vault 1.0.0 (certified)
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
infra.windows_ops 1.0.2 (validated)
junipernetworks.junos 11.0.0 (certified)
kubernetes.core 6.1.0 (certified)
microsoft.ad 1.9.2 (certified)
microsoft.iis 1.0.3 (certified)
network.acls 4.0.0 (validated)
network.backup 5.0.0 (validated)
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
