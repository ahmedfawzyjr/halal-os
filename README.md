# Halal OS

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Security: Hardened](https://img.shields.io/badge/Security-Privacy--Hardened-emerald.svg)]()
[![Platform: Linux](https://img.shields.io/badge/Platform-Linux-orange.svg)]()

> **Halal OS** is an open-source, privacy-first, and ethically engineered Linux operating system distribution. It combines kernel-level security hardening, zero-telemetry defaults, integrated network filtering, and privacy isolation to create a safe, distraction-free digital workspace.

---

## 🏛 Architecture & Core Security Principles

Halal OS is built with a defense-in-depth architecture designed for developers, privacy enthusiasts, and security-conscious users:

```
┌─────────────────────────────────────────────────────────────┐
│                      User Applications                      │
├─────────────────────────────────────────────────────────────┤
│   Sandboxed Environment (AppArmor / Bubblewrap Containers)  │
├─────────────────────────────────────────────────────────────┤
│    Privacy Engine (DNS-over-HTTPS, eBPF Network Guard)     │
├─────────────────────────────────────────────────────────────┤
│         Hardened Linux Kernel (Zero-Telemetry Core)         │
└─────────────────────────────────────────────────────────────┘
```

- **Kernel Hardening**: Configured with strict kernel self-protection parameters, disabled unprivileged user namespaces where unnecessary, and aggressive memory protection.
- **eBPF-Based Network Filtering**: Kernel-level packet inspection blocking tracking endpoints, telemetry nodes, and harmful domains prior to reaching user space.
- **Isolated User Environments**: Default sandboxing for web browsers and untrusted binaries using lightweight containers.
- **Zero-Telemetry Standard**: Stripped of operating-system-level metrics collection, telemetry daemons, and forced third-party cloud sync.

---

## ✨ Key Features

- **Integrated Privacy Firewall**: Out-of-the-box domain and ad filtering at the OS level.
- **Productivity & Focus Tools**: Native ambient focus modes and distraction-blocking utilities.
- **Developer Workstation Setup**: Pre-configured terminal tooling, container runtimes, and immutable package management support.
- **Encrypted Storage Defaults**: Automated full-disk encryption setup (LUKS / dm-crypt) during installation.

---

## 🛠 Building & Installation

### System Requirements
- **CPU**: 64-bit x86_64 or ARM64 architecture (2.0 GHz+ dual-core minimum)
- **RAM**: 4 GB minimum (8 GB recommended)
- **Storage**: 25 GB available storage
- **Graphics**: OpenGL 3.3+ capable GPU

### Building the ISO / Image
```bash
# Clone the repository
git clone https://github.com/ahmedfawzyjr/halal-os.git
cd halal-os

# Build the system image using the build pipeline
./scripts/build-image.sh --target iso --release
```

---

## 🛡 Security & Vulnerability Reporting

Security is central to Halal OS. If you discover a potential vulnerability, please submit an issue or contact the maintainers directly via security disclosures.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
