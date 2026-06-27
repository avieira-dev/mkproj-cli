#!/usr/bin/env python3

"""
FILE: main.py
VERSION: 1.7.0
DESCRIPTION: Main entry point for the mkproj-cli tool.
RESPONSIBILITIES:
  - Initialize the terminal environment (ANSI support)
  - Parse CLI arguments and route to specific commands (new, help, config)
  - Display the application branding (Banner)
  - Manage global exceptions and clean up resources on cancellation
"""

import sys
import os
import shutil
from pathlib import Path
from commands.command_list import command_list

# IMPORTANT: Fix for symbolic links
script_dir = Path(__file__).resolve().parent
sys.path.append(str(script_dir))

# Import colors and commands
from utils.colors import Colors
from utils.config import read_config
from commands.new_project import command_new
from commands.command_help import command_help
from commands.command_config import command_config

VERSION = "1.7.0"

def print_banner():
    print(fr"{Colors.CYAN}{Colors.BOLD}           _                    _")
    print(fr" _ __ ___ | | ___ __  _ __ ___ (_)")
    print(fr"| '_ ` _ \| |/ / '_ \| '__/ _ \| |")
    print(fr"{Colors.BLUE}| | | | | |   <| |_) | | | (_) | |")
    print(fr"|_| |_| |_|_|\_\ .__/|_|  \___// |")
    print(fr"               |_|            |__/ {Colors.END}")
    print()
    print(f"{Colors.BG_BLUE}{Colors.WHITE}{Colors.BOLD} v{VERSION} {Colors.END} {Colors.DIM}Developer Productivity Tool{Colors.END}\n")

def _is_config_set():
    config = read_config()
    return bool(config.get("author")) and bool(config.get("email"))

def main():
    # Enable ANSI colors on Windows terminals
    if os.name == 'nt':
        os.system('')

    print_banner()

    if len(sys.argv) < 2 or sys.argv[1] in ["help", "-h", "--help"]:
        command_help()
        return

    command = sys.argv[1].lower()
    current_project = sys.argv[2].strip() if len(sys.argv) > 2 else None

    try:
        if command == "new":
            if not _is_config_set():
                print(f"{Colors.YELLOW}⚠ Global config not set.{Colors.END}")
                print(f"{Colors.DIM}  ↳ Run 'mkproj config set author \"Your Name\"' and 'mkproj config set email \"you@example.com\"' before creating projects.{Colors.END}\n")
                return
            current_project = command_new()
        elif command == "list":
            command_list()
        elif command == "config":
            command_config()
        else:
            print(f"{Colors.RED}✖ Unknown command: {command}{Colors.END}")
            print(f"{Colors.DIM}Hint: Type 'mkproj --help' to see available commands.{Colors.END}\n")
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}⚠ Operation cancelled.{Colors.END}")
        if command == "new" and current_project and os.path.exists(current_project):
            try:
                shutil.rmtree(current_project)
                print(f"{Colors.DIM}  ↳ Partially created files removed.{Colors.END}")
            except: pass
        print(f"{Colors.CYAN}Bye!{Colors.END}\n")
        sys.exit(0)

if __name__ == "__main__":
    main()