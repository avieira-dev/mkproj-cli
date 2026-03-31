#!/usr/bin/env python3

import sys
from pathlib import Path

# --- IMPORTANT: Fix for symbolic links ---
# This ensures that internal modules are 
# found when running via /usr/local/bin

script_dir = Path(__file__).resolve().parent
sys.path.append(str(script_dir))

# -----------------------------------------

from commands.new_project import command_new

def main():
    if len(sys.argv) < 2:
        print("Usage: mkproj <command>")
        return

    command = sys.argv[1]

    if command == "new":
        command_new()
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()