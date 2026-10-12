"""
FILE: commands/new_project.py
DESCRIPTION: Orchestrator for the project creation workflow.
"""

from datetime import datetime
import os
import sys
import time
from utils import (
    Colors,
    add_license,
    custom_structure,
    get_docker_choice,
    get_java_data,
    get_module_go,
    get_readme_data,
    git_automation,
    preview_and_confirm_structure,
    print_robot,
    read_config,
    save_project,
    select_menu,
)

from languages import (
    get_c_structure,
    get_cpp_structure,
    get_go_structure,
    get_java_structure,
    get_python_structure,
    get_rust_structure,
    get_typescript_structure,
    get_web_structure,
    setup_c,
    setup_cpp,
    setup_custom,
    setup_go,
    setup_java,
    setup_python,
    setup_rust,
    setup_typescript,
    setup_web,
)

STRATEGIES = [
    ('C', setup_c, Colors.CYAN),
    ('C++', setup_cpp, Colors.BLUE),
    ('Go (Golang)', setup_go, Colors.LIGHT_BLUE),
    ('Java', setup_java, Colors.WHITE),
    ('Python', setup_python, Colors.YELLOW),
    ('Rust', setup_rust, Colors.ORANGE),
    ('TypeScript (Node)', setup_typescript, Colors.BLUE),
    ('Web (HTML/CSS/JS)', setup_web, Colors.PURPLE)
]

def command_new():
    if len(sys.argv) > 2:
        print(f'{Colors.RED}✖ Error: Do not specify the project name in the command.{Colors.END}')
        print(f'  {Colors.DIM}↳ Usage: mkproj new{Colors.END}\n')
        return None

    print_robot()

    config = read_config()
    author = config['author']
    email = config['email']
    year = str(datetime.now().year)

    context = {
        'user':   author,
        'holder': author,
        'email':  email,
        'year':   year
    }

    print(f'{Colors.BOLD}Select Strategy:{Colors.END} {Colors.DIM}(Use ↑/↓ arrows and Enter){Colors.END}\n')

    menu_options = [(lang_name, lang_color) for lang_name, _, lang_color in STRATEGIES]
    selected_idx = select_menu(menu_options)
    
    lang_name, setup_func, lang_color = STRATEGIES[selected_idx]

    print(f'\n{Colors.GREEN}✔{Colors.END} Selected: {lang_color}{Colors.BOLD}{lang_name}{Colors.END}')

    raw_name = input(f'\n{Colors.CYAN}?{Colors.END} {Colors.BOLD}Project name:{Colors.END} ').strip()
    if not raw_name:
        print(f'{Colors.RED}✖ Error: Project name cannot be empty.{Colors.END}\n')
        return None

    if lang_name == 'C' or lang_name == 'C++' or lang_name == 'Python':
        safe_name = raw_name.replace(' ', '_').replace('-', '_').lower()
    else:
        safe_name = raw_name.replace(' ', '-').replace('_', '-').lower()

    if safe_name != raw_name:
        print(f'  {Colors.YELLOW}↳ Adjusted directory name to: {safe_name}{Colors.END}')

    if os.path.exists(safe_name):
        print(f'\n{Colors.RED}✖ Error: Directory \'{safe_name}\' already exists.{Colors.END}\n')
        return None

    try:
        project_dir = safe_name

        while True:
            conf_struct, dirs_custom, files_custom = custom_structure()
            if conf_struct:
                if preview_and_confirm_structure(dirs_custom, files_custom):
                    selected_license = 'None'
                    project_dir = setup_custom(safe_name, dirs_custom, files_custom)
                    break
            else:
                readme_title, readme_description, readme_overview = get_readme_data(raw_name)
                
                if lang_name == 'Go (Golang)':
                    context['module'] = get_module_go(safe_name)
                elif lang_name == 'Java':
                    context['user'], context['gui_choice'] = get_java_data()
                
                option_license = add_license()
                lic_map = {'1': 'MIT', '2': 'Apache', '3': 'GNU GPL', '4': 'None'}
                selected_license = lic_map.get(option_license, 'None')

                use_docker = get_docker_choice()

                if lang_name == 'C':
                    dirs, files = get_c_structure(use_docker)
                elif lang_name == 'C++':
                    dirs, files = get_cpp_structure(use_docker)
                elif lang_name == 'Go (Golang)':
                    dirs, files = get_go_structure(use_docker)
                elif lang_name == 'Java':
                    dirs, files = get_java_structure(safe_name, context['user'], context['gui_choice'],use_docker)
                elif lang_name == 'Python':
                    dirs, files = get_python_structure(safe_name, use_docker)
                elif lang_name == 'Rust':
                    dirs, files = get_rust_structure(use_docker)
                elif lang_name == 'TypeScript (Node)':
                    dirs, files = get_typescript_structure(use_docker)
                elif lang_name == 'Web (HTML/CSS/JS)':
                    dirs, files = get_web_structure(use_docker)

                if preview_and_confirm_structure(dirs, files):
                    if lang_name == "Go (Golang)":
                        project_dir = setup_func(safe_name, readme_title, readme_description, readme_overview, context['module'], author, selected_license, year, use_docker)
                    elif lang_name == "Java":
                        project_dir = setup_func(safe_name, readme_title, readme_description, readme_overview, context['user'], context['gui_choice'], author, selected_license, year, use_docker)
                    else:
                        project_dir = setup_func(safe_name, readme_title, readme_description, readme_overview, author, selected_license, year, use_docker)

                    break

        print(f'\n{Colors.DIM}⚙ Building project...{Colors.END}')
        spinner = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        for i in range(12):
            sys.stdout.write(f'\r{Colors.CYAN}{spinner[i % len(spinner)]}{Colors.END} {Colors.DIM}Applying templates...{Colors.END}')
            sys.stdout.flush()
            time.sleep(0.08)

        sys.stdout.write(f'\r{Colors.GREEN}✔{Colors.END} {Colors.DIM}Project structure generated.{Colors.END}\n')

        git_status = git_automation(project_dir)
        save_project(project_dir, lang_name, selected_license, author, os.path.abspath(project_dir))

        git_label = 'Initialized' if git_status else 'Skipped'
        print(f'\n{Colors.GREEN}✔{Colors.END} {Colors.BOLD}Done! Project \'{project_dir}\' is ready.{Colors.END}')
        print(f'  {Colors.DIM}↳ Author:{Colors.END} {author}')
        print(f'  {Colors.DIM}↳ Language:{Colors.END} {lang_color}{lang_name}{Colors.END}')
        print(f'  {Colors.DIM}↳ License:{Colors.END} {selected_license}')
        print(f'  {Colors.DIM}↳ Git:{Colors.END} {git_label}')
        print(f'  {Colors.DIM}↳ Path:{Colors.END} {os.path.abspath(project_dir)}')

        print(f'\n{Colors.BOLD}Next steps:{Colors.END}')
        print(f'  cd {project_dir}')
        print(f'  code .\n')

        return project_dir

    except Exception as e:
        print(f'\n{Colors.RED}✖ Unexpected error: {e}{Colors.END}\n')
        return None