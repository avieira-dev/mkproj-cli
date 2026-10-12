"""
FILE: commands/command_list.py
DESCRIPTION: Displays the history of projects created with mkproj-cli.
RESPONSIBILITIES:
  - Load project history from ~/.mkproj/project-history.json
  - Render a clean, minimal list with project metadata
  - Handle the empty-history case gracefully
"""

from utils import (
    Colors,
    load_history    
)

def command_list():
    history = load_history()

    if not history:
        print(f'{Colors.YELLOW}No projects found in history.{Colors.END}')
        print(f'  {Colors.DIM}↳ Use {Colors.BOLD}{Colors.WHITE}\'mkproj new\'{Colors.END}{Colors.DIM} to create your first project.{Colors.END}\n')
        return

    print(f'\n{Colors.BOLD}Project History:{Colors.END}\n')

    header = f"{'#':<4} {'Name':<20} {'Language':<20} {'License':<10} {'Date':<16}"
    print(f'  {Colors.DIM}{header}{Colors.END}\n')

    for i, project in enumerate(reversed(history), start=1):
        name = project.get('name', '?')[:18]
        language = project.get('language', '?')[:18]
        license_ = project.get('license', '?')[:8]
        date = project.get('created_at', '?')[:16]

        print(
            f'  {Colors.DIM}{str(i):<4}{Colors.END} '
            f'{Colors.BOLD}{name:<20}{Colors.END} '
            f'{Colors.CYAN}{language:<20}{Colors.END} '
            f'{Colors.YELLOW}{license_:<10}{Colors.END} '
            f'{Colors.DIM}{date:<16}{Colors.END}'
        )

    print(f'\n  {Colors.DIM}↳ {len(history)} project(s) total — stored in ~/.mkproj/project-history.json{Colors.END}\n')