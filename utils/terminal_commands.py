import subprocess
import shutil

def run_command(command_list, cwd):
    # Runs a system command within a specific directory
    # Checks whether the command exists before attempting to execute it
    # Verifies that the executable (e.g., "git") is installed on the system
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