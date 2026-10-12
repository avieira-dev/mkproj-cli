"""
FILE: commands/command_config.py
DESCRIPTION: Manages global configuration via CLI.
"""

import sys
from utils import (
    Colors,
    read_config,
    write_config,
)

def command_config():
    args = sys.argv[2:]

    if not args or args[0] == 'show':
        _show_config()
    elif args[0] == 'set' and len(args) == 3:
        _set_config(args[1], args[2])
    else:
        print(f'{Colors.BOLD}Usage:{Colors.END}')
        print('  mkproj config show')
        print('  mkproj config set author "Your Name"')
        print('  mkproj config set email "you@example.com"\n')

def _show_config():
    config = read_config()

    print(f'\n{Colors.BOLD}Global Configuration{Colors.END}\n')

    for key, value in config.items():
        display = value if value else f'{Colors.DIM}(not set){Colors.END}'
        print(f'{Colors.CYAN}{key.capitalize()}{Colors.END}: {display}')

    print()

def _set_config(key, value):
    config = read_config()

    if key not in config:
        print(f'{Colors.RED}✖ Error: Unknown key \'{key}\'.{Colors.END}\n')
        return
    
    config[key] = value
    write_config(config)

    print(f'{Colors.GREEN}✔{Colors.END} {key.capitalize()} set to "{value}"')