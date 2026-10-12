"""
FILE: utils/prompter.py
DESCRIPTION: Handle user interaction via terminal prompts and interactive key navigation.
"""

import os
import sys
from utils.colors import Colors
from utils.terminal_commands import run_command

if os.name == 'nt':
    import msvcrt
    def get_key():
        key = msvcrt.getch()
        if key == b'\x03':  
            raise KeyboardInterrupt
        if key in (b'\x00', b'\xe0'):
            key = msvcrt.getch()
            if key == b'H': return 'UP'
            if key == b'P': return 'DOWN'
        elif key in (b'\r', b'\n'):
            return 'ENTER'
        return None
else:
    import tty
    import termios
    def get_key():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            if ch == '\x03':  
                raise KeyboardInterrupt
            if ch == '\x1b':
                ch2 = sys.stdin.read(1)
                ch3 = sys.stdin.read(1)
                if ch3 == 'A': return 'UP'
                if ch3 == 'B': return 'DOWN'
            elif ch in ('\r', '\n'):
                return 'ENTER'
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return None

def select_menu(options):
    selected_index = 0
    num_options = len(options)

    sys.stdout.write('\033[?25l')
    sys.stdout.flush()

    try:
        while True:
            for i, item in enumerate(options):
                if isinstance(item, tuple):
                    name, color = item
                else:
                    name, color = item, Colors.WHITE

                if i == selected_index:
                    sys.stdout.write(f'\r{Colors.CYAN}❯{Colors.END} {Colors.BOLD}{color}{name}{Colors.END}\033[K\n')
                else:
                    sys.stdout.write(f'\r  {color}{name}{Colors.END}\033[K\n')

            sys.stdout.flush()

            key = get_key()
            if key == 'UP':
                selected_index = (selected_index - 1) % num_options
            elif key == 'DOWN':
                selected_index = (selected_index + 1) % num_options
            elif key == 'ENTER':
                break

            sys.stdout.write(f'\033[{num_options}A')

    finally:
        sys.stdout.write('\033[?25h')
        sys.stdout.flush()

    return selected_index

def get_readme_data(default_name):
    print(f'{Colors.CYAN}?{Colors.END} {Colors.BOLD}Customize README?{Colors.END} {Colors.DIM}(y/n){Colors.END}', end=' ')

    if input(Colors.END).lower().strip() == 'y':
        title = input(f'  {Colors.DIM}↳ Title [{default_name}]: {Colors.END}').strip() or default_name
        description = input(f'  {Colors.DIM}↳ Description: {Colors.END}').strip() or 'Project created with mkproj-cli.'
        overview = input(f'  {Colors.DIM}↳ Overview: {Colors.END}').strip() or 'A project created using the mkproj-cli project creation automation tool.'
        return title, description, overview
    
    return default_name, 'Project created with mkproj-cli.', 'A project created using the mkproj-cli project creation automation tool.'

def get_module_go(default_name):
    print(f'{Colors.CYAN}?{Colors.END} {Colors.BOLD}Use GitHub as Go module?{Colors.END} {Colors.DIM}(y/n){Colors.END}', end=' ')

    if input(Colors.END).lower().strip() == 'y':
        return input(f'  {Colors.DIM}↳ Repo path: {Colors.END}').replace('https://', '').strip() or default_name
    
    return default_name

def get_java_data():
    user = 'user'
    print(f'{Colors.CYAN}?{Colors.END} {Colors.BOLD}Developer Domain?{Colors.END} {Colors.DIM}(y/n){Colors.END}', end=' ')

    if input(Colors.END).lower().strip() == 'y':
        user = input(f'  {Colors.DIM}↳ Domain (ex: com.app): {Colors.END}').strip().lower() or 'user'

    print(f'{Colors.CYAN}?{Colors.END} {Colors.BOLD}Select Java template?{Colors.END} {Colors.DIM}(y/n){Colors.END}', end=' ')
    choice = '1'
    
    if input(Colors.END).lower().strip() == 'y':
        print(f'  {Colors.DIM}1) Console  2) GUI (Swing){Colors.END}')
        choice = input(f'  {Colors.DIM}↳ Selection: {Colors.END}').strip() or '1'

    return user, choice

def git_automation(path_name):
    print(f'\n{Colors.CYAN}?{Colors.END} {Colors.BOLD}Initialize Git repository?{Colors.END} {Colors.DIM}(y/n){Colors.END}', end=' ')

    if input(Colors.END).lower().strip() == 'y':
        path = os.path.abspath(path_name)
        if run_command(['git', 'init', '-b', 'main'], path):
            run_command(['git', 'add', '.'], path)
            run_command(['git', 'commit', '-m', 'first commit'], path)
            return True
    return False

def add_license():
    print(f'{Colors.CYAN}?{Colors.END} {Colors.BOLD}Add a license to the project?{Colors.END} {Colors.DIM}(y/n){Colors.END}', end=' ')
    choice = '4'

    if input(Colors.END).lower().strip() == 'y':
        print(f'  {Colors.DIM}1) MIT  2) Apache 2.0  3) GNU GPL v3.0  4) None{Colors.END}')
        choice = input(f'  {Colors.DIM}↳ Selection [1-4]: {Colors.END}').strip() or '1'

    return choice

def get_docker_choice():
    print(f'{Colors.CYAN}?{Colors.END} {Colors.BOLD}Add Docker support?{Colors.END} {Colors.DIM}(y/n){Colors.END}', end=' ')
    return input(Colors.END).lower().strip() == 'y'

def custom_structure():
    print(f'{Colors.CYAN}?{Colors.END} {Colors.BOLD}Would you like to customize the default directory structure for this project?{Colors.END} {Colors.DIM}(y/n){Colors.END}', end=' ')

    if input(Colors.END).lower().strip() == 'y':
        while True:
            dirs = input(f'  {Colors.DIM}↳ Directories (comma separated, e.g. src, src/assets, tests): {Colors.END}').strip()
            files = input(f'  {Colors.DIM}↳ Files (comma separated, e.g. src/main.cpp, README.md): {Colors.END}').strip()

            custom_dirs = [d.strip() for d in dirs.split(',') if d.strip()]
            custom_files = [f.strip() for f in files.split(',') if f.strip()]

            if custom_dirs or custom_files:
                return True, custom_dirs, custom_files
            
            print(f'    {Colors.YELLOW}↳ ⚠ You must specify at least one directory or file. Try again.{Colors.END}')

    return False, [], []

def preview_and_confirm_structure(dirs, files):
    while True:
        print(f'\n{Colors.BOLD}Project Structure Preview:{Colors.END}')

        print(f'{Colors.CYAN}Directories:{Colors.END}')
        for i, dir in enumerate(dirs):
            prefix = '└──' if i == len(dirs) - 1 else '├──'
            print(f' {prefix} {dir}/')

        print(f'{Colors.CYAN}Files:{Colors.END}')
        for i, file in enumerate(files):
            prefix = '└──' if i == len(files) - 1 else '├──'
            print(f' {prefix} {file}')

        print()

        print(f'{Colors.CYAN}?{Colors.END} {Colors.BOLD}Do you want to create this project?{Colors.END} {Colors.DIM}(y/n){Colors.END}', end=' ')
        choice = input(Colors.END).lower().strip()

        if choice == 'y':
            return True

        print(f'{Colors.YELLOW}↳ Project creation cancelled. Restarting structure configuration...{Colors.END}\n')
        
        return False