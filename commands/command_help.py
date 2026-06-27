"""
FILE: commands/command_help.py
DESCRIPTION: Documentation and usage manual for the mkproj-cli.
RESPONSIBILITIES:
  - Display syntax instructions for the command-line interface
  - List all available commands with brief descriptions
  - Provide real-world usage examples for the user
  - Show project authorship and social links
"""

from utils.colors import Colors

def command_help():
    print(f"{Colors.YELLOW}Usage: {Colors.END}mkproj <command> [arguments]\n")

    # Available commands
    print(f"{Colors.BOLD}Available Commands:{Colors.END}")
    print(f" {Colors.GREEN}new <name>{Colors.END}            Starts the interactive project generator")
    print(f" {Colors.GREEN}list{Colors.END}                  Shows history of created projects")
    print(f" {Colors.GREEN}config show{Colors.END}           Shows current global configuration")
    print(f" {Colors.GREEN}config set <key> <value>{Colors.END} Sets a global configuration value")
    print(f" {Colors.GREEN}help, -h, --help{Colors.END}      Shows this help message\n")

    # Examples
    print(f"{Colors.BOLD}Examples:{Colors.END}")
    print(f" $ mkproj new my-awesome-app")
    print(f" $ mkproj list")
    print(f" $ mkproj config show")
    print(f" $ mkproj config set author \"Your Name\"")
    print(f" $ mkproj config set email \"you@example.com\"")
    print(f" $ mkproj --help\n")

    print(f"{Colors.BLUE}Created by Alexandre Vieira (https://github.com/avieira-dev){Colors.END}\n")