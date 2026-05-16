"""
FILE: commands/command_list.py
DESCRIPTION: Displays the history of projects created with mkproj-cli.
RESPONSIBILITIES:
  - Load project history from ~/.mkproj/history.json
  - Render a formatted table with project metadata
  - Handle the empty-history case gracefully
"""

from utils.colors import Colors
from utils.history import load_history

def command_list():
    history = load_history()

    if not history:
        print(f"{Colors.YELLOW}⚠ No projects found in history.{Colors.END}")
        print(f"{Colors.DIM}  ↳ Use 'mkproj new <name>' to create your first project.{Colors.END}\n")
        return

    WIDTH = 76 
    print(f"\n{Colors.CYAN}{Colors.BOLD} 📋 Project History{Colors.END}\n")
    print(f"{Colors.BLUE}┌{'─' * (WIDTH - 2)}┐{Colors.END}")

    header = f"{'#':<4} {'Name':<20} {'Language':<18} {'License':<10} {'Date':<16}"
    print(f"{Colors.BLUE}│{Colors.END} {Colors.BOLD}{header.ljust(WIDTH - 4)}{Colors.END} {Colors.BLUE}│{Colors.END}")
    print(f"{Colors.BLUE}├{'─' * (WIDTH - 2)}┤{Colors.END}")

    for i, project in enumerate(reversed(history), start=1):
        name     = project.get("name", "?")[:18]
        language = project.get("language", "?")[:16]
        license  = project.get("license", "?")[:8]
        date     = project.get("created_at", "?")[:16]

        row = f"{str(i):<4} {name:<20} {language:<18} {license:<10} {date:<16}"
        print(f"{Colors.BLUE}│{Colors.END} {row.ljust(WIDTH - 4)} {Colors.BLUE}│{Colors.END}")

    print(f"{Colors.BLUE}└{'─' * (WIDTH - 2)}┘{Colors.END}")
    print(f"\n{Colors.DIM}  ↳ {len(history)} project(s) total — stored in ~/.mkproj/project-history.json{Colors.END}\n")