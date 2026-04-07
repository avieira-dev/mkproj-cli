#!/usr/bin/env python3

import sys
import os
from pathlib import Path

# --- IMPORTANT: Fix for symbolic links ---
script_dir = Path(__file__).resolve().parent
sys.path.append(str(script_dir))

# Import colors and commands
from utils.colors import Colors
from commands.new_project import command_new

def print_banner():
    banner = fr"""{Colors.CYAN}{Colors.BOLD}
           _
 _ __ ___ | | ___ __  _ __ ___ (_)
| '_ ` _ \| |/ / '_ \| '__/ _ \| |
| | | | | |   <| |_) | | | (_) | |
|_| |_| |_|_|\_\ .__/|_|  \___// |
               |_|            |__/ 

{Colors.END}{Colors.BLUE}» Version 1.0.0 | Developer Tool{Colors.END}
"""
    print(banner)

def main():
    # Enable ANSI colors on Windows terminals
    if os.name == 'nt':
        os.system('')

    # Show the logo as soon as the tool is called
    print_banner()
    
    if len(sys.argv) < 2:
        print(f"{Colors.YELLOW}Usage: mkproj <command> [args]{Colors.END}")
        return

    command = sys.argv[1]

    try:
        if command == "new":
            command_new()
        else:
            print(f"{Colors.RED}Unknown command: {command}{Colors.END}")
    except KeyboardInterrupt:
        # If the user presses Ctrl + C (end the process)
        print(f"\n\n{Colors.YELLOW}Operation cancelled by user. Goodbye!{Colors.END}")
        sys.exit(0)

if __name__ == "__main__":
    main()