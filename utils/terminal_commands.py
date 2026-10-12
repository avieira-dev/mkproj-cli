"""
FILE: utils/terminal_commands.py
DESCRIPTION: Safe wrapper for executing system subprocesses.
RESPONSIBILITIES:
  - Check if executables exist in system PATH
  - Execute commands in specific directories
"""

import subprocess
import shutil

def run_command(command_list, cwd):
    if not shutil.which(command_list[0]):
        return False

    try:
        subprocess.run(
            command_list,
            check=True,
            cwd=cwd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        
        return True
    except (subprocess.CalledProcessError, Exception):
        return False