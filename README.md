<p align="center">
  <img src="assets/logo_symbol.png" alt="Halal OS Logo Symbol" width="128" height="128" />
</p>

<div align="center">
  <img src="assets/logo.png" width="140" alt="Halal Os App Icon / Logo" /><br />
  <h1>Halal Os</h1>
  <p><strong>Privacy-focused, ethical desktop environment and Linux distribution operating system concept featuring real-time AI content filtering, system-wide protection, and local AI capabilities.</strong></p>
  <p>
    <img src="https://img.shields.io/badge/Visibility-Public-green?style=for-the-badge" alt="Visibility" />
    <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="License" />
    <img src="https://img.shields.io/badge/Status-Active_Development-brightgreen?style=for-the-badge" alt="Status" />
  </p>
</div>


---

## 📌 Topics & Tags
`#arabic` `#content-filtering` `#cybersecurity` `#desktop-environment` `#linux` `#local-ai` `#open-source` `#operating-system` `#privacy` `#halal-os`

---

## 🚀 Overview & Key Features

`halal-os` is an engineered codebase optimized for modular architecture, maintainability, and enterprise-grade code standards.

### ✨ Key Highlights
- ⚡ **High Performance & Scalability**: Designed with clean separation of concerns and optimized execution logic.
- 🔒 **Security-First Standards**: Enforced input validation, safe dependency management, and structured error handling.
- 🎨 **Unified Visual Identity**: Integrated with physical brand assets, customized logos, and standardized design tokens.
- 🛠️ **DevOps & Automation Ready**: Out-of-the-box support for continuous integration, automated tests, and deployment.

## 🎨 Brand Identity & Visual Assets

| Spec | Value |
| :--- | :--- |
| **Brand Name** | `Halal Os` |
| **Primary Brand Color** | `#0D9488` |
| **Asset Package** | `14 Physical Assets` |
| **App Icon Location** | `assets/logo.png` |
| **Brand Folder** | `BRAND_ASSETS/04_Websites_and_Landing_Pages/Halal_Os` |

> 📌 **Brand Package Included**: App Icon PNG, Vector SVG, High-DPI raster icons, Favicons (16px to 512px), and adaptive tokens.


---

## 🛠️ Technology Stack & Architecture

- **Core Frameworks & Tools**: `Polyglot Stack`, `Clean Architecture`, `GitHub Actions`
- **Architectural Pattern**: Layered Architecture (Domain, Data, Logic & UI Layers)
- **Quality Benchmarks**: Clean Code, SOLID Principles, Strict Typing, Unit & Integration Coverage

---

## 📂 Repository Structure

```text
halal-os/
├── assets/               # Brand Assets, Logos, and Media
│   └── logo.png          # App Icon / Logo Image
├── src/ / lib/           # Core Source Code & Modules
├── tests/                # Automated Test Suites
├── config/               # Environment & System Configurations
├── docs/                 # Technical Specs & Architecture Docs
├── README.md             # Repository Documentation
└── package.json / pubspec / requirements.txt
```

---

## ⚙️ Getting Started & Local Setup

### Prerequisites
- Git
- Node.js / Python

### Installation & Run Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ahmedfawzyjr/halal-os.git
   cd halal-os
   ```

2. **Install Dependencies**:
   ```bash
   npm install
   ```

3. **Configure Environment**:
   ```bash
   cp .env.example .env
   ```

4. **Run Application & Services**:
   ```bash
   npm start      # Web Desktop Shell
   npm run store  # Islamic App Store Microservice (Go)
   npm run cloud  # Sovereign Cloud & P2P Mesh (Go)
   npm run ai     # Amina AI Offline RAG Engine (Python)
   npm test       # Run full 123-test validation suite
   ```

---

## 💿 Download & Install Live ISO (دليل حرق وتثبيت النظام عبر روفوس)

Anyone can download the bootable sovereign **Halal OS ISO** directly from GitHub Releases and install it on any laptop or PC using **Rufus**:

### 📥 1. Download the ISO
- Go to [Halal OS Releases](https://github.com/ahmedfawzyjr/halal-os/releases).
- Download `halal-os-v2.0-amd64.iso` and `SHA256SUMS`.
- (Optional) Verify checksum: `sha256sum -c SHA256SUMS`.

### ⚡ 2. Flash to USB via Rufus
1. Download and run [Rufus](https://rufus.ie/) on Windows.
2. Insert a USB flash drive (8 GB or larger).
3. Under **Device**, select your USB flash drive.
4. Under **Boot selection**, click **SELECT** and choose `halal-os-v2.0-amd64.iso`.
5. Under **Partition scheme**:
   - Choose **GPT** for modern laptops (UEFI boot).
   - Choose **MBR** for older PCs (Legacy BIOS).
6. Click **START**. If prompted, select **Write in ISO Image mode** (or DD mode).
7. Wait until the progress bar shows **READY**.

### 💻 3. Boot & Install on Laptop
1. Insert the USB flash drive into your target laptop/PC.
2. Power on and repeatedly tap your laptop's **Boot Menu key** (commonly `F12` on Dell/Lenovo, `F9` on HP, `F11` on MSI, or `Esc`/`F2` on Asus/Acer).
3. Select your USB drive from the boot menu.
4. In the GRUB menu, select **`☪ Launch Halal OS v2.0 (Bismillah - Sovereign Mode)`**.
5. Once inside the live desktop, you can use Halal OS directly in live mode or click **Install Halal OS** (Calamares) to install it permanently on your hard drive alongside or replacing your existing OS.

---

## 🤝 Contributing

Contributions, bug reports, and feature proposals are welcome! Feel free to open an issue or pull request on [GitHub](https://github.com/ahmedfawzyjr/halal-os/issues).

---

## 👨‍💻 Author & Maintainer

**Ahmed Fawzy**
* GitHub: [@ahmedfawzyjr](https://github.com/ahmedfawzyjr)
* Role: Senior Software Engineer (Mobile Architecture, Backend Systems & Infrastructure)

---

## 📄 License

This repository is licensed under the MIT License - see the `LICENSE` file for details.
