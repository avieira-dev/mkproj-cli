#!/usr/bin/env python3

"""
FILE: main.py
VERSION: 1.4.0
DESCRIPTION: Main entry point for the mkproj-cli tool.
RESPONSIBILITIES:
  - Initialize the terminal environment (ANSI support)
  - Parse CLI arguments and route to specific commands (new, help)
  - Display the application branding (Banner)
  - Manage global exceptions and clean up resources on cancellation
"""

import sys
import os
import shutil
from pathlib import Path

# IMPORTANT: Fix for symbolic links
script_dir = Path(__file__).resolve().parent
sys.path.append(str(script_dir))

# Import colors and command
from utils.colors import Colors
from commands.new_project import command_new
from commands.command_help import command_help

def print_banner():
    print(fr"{Colors.CYAN}{Colors.BOLD}           _                    _")
    print(fr" _ __ ___ | | ___ __  _ __ ___ (_)")
    print(fr"| '_ ` _ \| |/ / '_ \| '__/ _ \| |")
    print(fr"{Colors.BLUE}| | | | | |   <| |_) | | | (_) | |")
    print(fr"|_| |_| |_|_|\_\ .__/|_|  \___// |")
    print(fr"               |_|            |__/ {Colors.END}")
    print()
    print(f"{Colors.BG_BLUE}{Colors.WHITE}{Colors.BOLD} v1.4.0 {Colors.END} {Colors.DIM}Developer Productivity Tool{Colors.END}\n")

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
            current_project = command_new()
        else:
            print(f"{Colors.RED}✖ Unknown command: {command}{Colors.END}")
            print(f"{Colors.DIM}Hint: Type 'mkproj --help' to see available commands.{Colors.END}")
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}⚠ Operation cancelled.{Colors.END}")
        if command == "new" and current_project and os.path.exists(current_project):
            try:
                shutil.rmtree(current_project)
                print(f"{Colors.DIM}  ↳ Partially created files removed.{Colors.END}")
            except: pass
        print(f"{Colors.CYAN}Bye!{Colors.END}")
        sys.exit(0)

if __name__ == "__main__":
    main()