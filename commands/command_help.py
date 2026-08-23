"""
FILE: commands/command_help.py
DESCRIPTION: Documentation and usage manual for the mkproj-cli.
"""

from utils.colors import Colors

def command_help():
    print(f"{Colors.BOLD}Usage:{Colors.END} mkproj <command>\n")

    print(f"{Colors.BOLD}Available Commands:{Colors.END}")
    print(f"  {Colors.CYAN}new{Colors.END} Starts the interactive project generator")
    print(f"  {Colors.CYAN}list{Colors.END} Shows history of created projects")
    print(f"  {Colors.CYAN}config [show]{Colors.END} Shows current global configuration")
    print(f"  {Colors.CYAN}config set <key> <value>{Colors.END} Sets a global configuration value")
    print(f"  {Colors.CYAN}help, --help{Colors.END} Shows this help message\n")

    print(f"{Colors.BOLD}Examples:{Colors.END}")
    print(f"  $ mkproj new")
    print(f"  $ mkproj list")
    print(f"  $ mkproj config")
    print(f"  $ mkproj config set author \"Your Name\"")
    print(f"  $ mkproj config set email \"you@example.com\"\n")

    print(f"{Colors.DIM}Created by Alexandre Vieira (https://github.com/avieira-dev){Colors.END}\n")