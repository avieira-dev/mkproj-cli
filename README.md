# mkproj-cli

> A fast and flexible CLI tool to scaffold structured projects in multiple programming languages.

![status](https://img.shields.io/badge/status-in%20development-orange)
![language](https://img.shields.io/badge/language-Python-yellow)
![license](https://img.shields.io/badge/license-MIT-blue)

> [!IMPORTANT]  
> **mkproj** is a work in progress. We are currently refining the core logic   
> and adding support for new languages (C, Java, etc.). As such, breaking  
> changes and bugs are expected;

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Developer](#developer)
- [License](#license)

## Overview

**mkproj-cli** automates the tedious process of creating directory trees and boilerplate files. Whether you are starting a microservice in Python, a system tool in C/C++, or a corporate app in Java, **mkproj** ensures every project starts with a professional, clean, and consistent structure.

### Preview

<p align="center">
    <em>Interactive language selection menu</em><br>
    <img src="./assets/screenshots/screenshot-001.png" alt="mkproj-cli interface demo 1" width="600">
    <br>
    <em>Automatic directory and file generation</em><br>
    <img src="./assets/screenshots/screenshot-002.png" alt="mkproj-cli interface demo 2" width="600">
</p>

## Features

- Multi-language support
- Modular architecture
- **Smart scaffolding** (automatically generates):
  - Directories
  - Build files
  - Documentation
- Auto-creates `.gitignore` based on the selected language.
- Prevents accidental overwrites of existing projects

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/avieira-dev/mkproj-cli.git
```

### 2. Global Setup (Linux/MacOS)

1. Ensure `main.py` starts with the shebang: `#!/usr/bin/env python3`.
2. Make it executable and create the symbolic link:

```bash
chmod +x main.py
sudo ln -s "$(pwd)/main.py" /usr/local/bin/mkproj
```

> [!NOTE]  
> To remove the global command, run the following in the terminal:  
> ```bash  
> sudo rm /usr/local/bin/mkproj  
> ```

## Usage

Run the command and follow the interactive menu:

```bash
mkproj new <project_name>
```

## Project Structure

```text
mkproj-cli/
├── commands/
├── languages/
├── templates/
├── tests/
├── utils/
├── venv/
├── .gitignore
├── LICENSE
├── main.py
└── README.md
```

## Developer
**Alexandre Vieira**  
GitHub: [@avieira-dev](https://github.com/avieira-dev)

## License
Distributed under the license [MIT License](LICENSE). See the **LICENSE** file for more details.