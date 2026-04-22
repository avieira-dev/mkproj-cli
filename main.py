#!/usr/bin/env python3

import sys
import os
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
    print(f"{Colors.BG_BLUE}{Colors.WHITE}{Colors.BOLD} v1.3.0 {Colors.END} {Colors.DIM}Developer Productivity Tool{Colors.END}\n")

def main():
    # Enable ANSI colors on Windows terminals
    if os.name == 'nt':
        os.system('')

    # Show the logo as soon as the tool is called
    print_banner()
    
    if len(sys.argv) < 2 or sys.argv[1] in ["help", "-h", "--help"]:
        command_help()
        return

    command = sys.argv[1].lower()

    try:
        if command == "new":
            command_new()
        else:
            print(f"{Colors.RED}✖ Unknown command: {command}{Colors.END}")
            print(f"{Colors.DIM}Hint: Type 'mkproj --help' to see available commands.{Colors.END}")
    except KeyboardInterrupt:
        # If the user presses Ctrl + C (end the process)
        print(f"\n\n{Colors.YELLOW}⚠ Operation cancelled. See you later!{Colors.END}")
        sys.exit(0)

if __name__ == "__main__":
    main()