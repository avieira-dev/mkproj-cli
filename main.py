#!/usr/bin/env python3

"""
FILE: main.py
VERSION: 2.0.0
DESCRIPTION: Main entry point for the mkproj-cli tool.
"""

import sys
import os
import shutil
from pathlib import Path
from commands.command_list import command_list

script_dir = Path(__file__).resolve().parent
sys.path.append(str(script_dir))

from utils.colors import Colors
from utils.config import read_config
from utils.banner import print_banner
from commands.new_project import command_new
from commands.command_help import command_help
from commands.command_config import command_config

VERSION = "2.0.0"

def _is_config_set():
    config = read_config()
    return bool(config.get("author")) and bool(config.get("email"))

def main():
    if os.name == 'nt':
        os.system('')

    if len(sys.argv) < 2 or sys.argv[1] in ["help", "-h", "--help"]:
        print_banner(VERSION) 
        command_help()
        return

    command = sys.argv[1].lower()
    current_project = None 

    try:
        match command:
            case "new":
                if not _is_config_set():
                    print(f"{Colors.YELLOW}⚠ Global config not set.{Colors.END}")
                    print(f"  {Colors.DIM}↳ Run {Colors.BOLD}{Colors.WHITE}mkproj config set author \"Name\"{Colors.END}{Colors.DIM} and {Colors.BOLD}{Colors.WHITE}mkproj config set email \"Email\"{Colors.END}{Colors.DIM} first.{Colors.END}\n")
                    return
                
                current_project = command_new()
                
            case "list":
                command_list()
                
            case "config":
                command_config()
                
            case _:
                print(f"{Colors.RED}✖ Unknown command: {command}{Colors.END}")
                print(f"  {Colors.DIM}↳ Type 'mkproj --help' to see available commands.{Colors.END}\n")
                
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}⚠ Operation cancelled.{Colors.END}")
        if command == "new" and current_project and os.path.exists(current_project):
            try:
                shutil.rmtree(current_project)
                print(f"  {Colors.DIM}↳ Partially created files removed.{Colors.END}")
            except: 
                pass
        print(f"  {Colors.DIM}↳ Bye!{Colors.END}\n")
        sys.exit(0)

if __name__ == "__main__":
    main()