"""
FILE: commands/command_config.py
DESCRIPTION: Manages global configuration via CLI.
RESPONSIBILITIES:
  - Display current configuration values
  - Allow the user to set individual configuration keys
"""

import sys
from utils.colors import Colors
from utils.config import read_config, write_config

def command_config():
    args = sys.argv[2:]

    if not args or args[0] == "show":
        _show_config()
    elif args[0] == "set" and len(args) == 3:
        _set_config(args[1], args[2])
    else:
        print(f"{Colors.YELLOW}Usage:{Colors.END}")
        print(f"  mkproj config show")
        print(f"  mkproj config set author \"Your Name\"")
        print(f"  mkproj config set email \"you@example.com\"\n")

def _show_config():
    config = read_config()
    print(f"\n{Colors.CYAN}{Colors.BOLD} Global Configuration{Colors.END}\n")
    for key, value in config.items():
        display = value if value else f"{Colors.DIM}(not set){Colors.END}"
        print(f"  {Colors.GREEN}{key}{Colors.END}: {display}")
    print()

def _set_config(key, value):
    config = read_config()
    if key not in config:
        print(f"{Colors.RED}✖ Unknown key: {key}{Colors.END}\n")
        return
    config[key] = value
    write_config(config)
    print(f"{Colors.GREEN}✔{Colors.END} {key} set to \"{value}\"\n")