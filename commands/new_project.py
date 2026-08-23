"""
FILE: commands/new_project.py
DESCRIPTION: Orchestrator for the project creation workflow.
"""

import os
import sys
import time
from datetime import datetime
from utils.colors import Colors
from utils.config import read_config
from utils.history import save_project
from utils.robot import print_robot
from utils.prompter import (select_menu, get_readme_data, get_module_go, get_java_data, git_automation, add_license, get_docker_choice)
from languages import (setup_python, setup_cpp, setup_c, setup_web, setup_java, setup_go, setup_rust, setup_typescript)

STRATEGIES = [
    ("C", setup_c, Colors.CYAN),
    ("C++", setup_cpp, Colors.BLUE),
    ("Go (Golang)", setup_go, Colors.LIGHT_BLUE),
    ("Java", setup_java, Colors.WHITE),
    ("Python", setup_python, Colors.YELLOW),
    ("Rust", setup_rust, Colors.ORANGE),
    ("TypeScript (Node)", setup_typescript, Colors.BLUE),
    ("Web (HTML/CSS/JS)", setup_web, Colors.PURPLE)
]

def command_new():
    if len(sys.argv) > 2:
        print(f"{Colors.RED}✖ Error: Do not specify the project name in the command.{Colors.END}")
        print(f"  {Colors.DIM}↳ Usage: mkproj new{Colors.END}\n")
        return None

    print_robot()

    config = read_config()
    author = config["author"]
    email = config["email"]
    year = str(datetime.now().year)

    context = {
        "user":   author,
        "holder": author,
        "email":  email,
        "year":   year
    }

    print(f"{Colors.BOLD}Select Strategy:{Colors.END} {Colors.DIM}(Use ↑/↓ arrows and Enter){Colors.END}\n")

    menu_options = [(lang_name, lang_color) for lang_name, _, lang_color in STRATEGIES]
    selected_idx = select_menu(menu_options)
    
    lang_name, setup_func, lang_color = STRATEGIES[selected_idx]

    print(f"\n{Colors.GREEN}✔{Colors.END} Selected: {lang_color}{Colors.BOLD}{lang_name}{Colors.END}")

    raw_name = input(f"\n{Colors.CYAN}?{Colors.END} {Colors.BOLD}Project name:{Colors.END} ").strip()
    if not raw_name:
        print(f"{Colors.RED}✖ Error: Project name cannot be empty.{Colors.END}\n")
        return None

    if lang_name == "C":
        safe_name = raw_name.replace(" ", "_").replace("-", "_").lower()
    else:
        safe_name = raw_name.replace(" ", "-").replace("_", "-").lower()

    if safe_name != raw_name:
        print(f"  {Colors.YELLOW}↳ Adjusted directory name to: {safe_name}{Colors.END}")

    if os.path.exists(safe_name):
        print(f"\n{Colors.RED}✖ Error: Directory '{safe_name}' already exists.{Colors.END}\n")
        return None

    readme_title, readme_description, readme_overview = get_readme_data(raw_name)

    if lang_name == "Go (Golang)":
        context['module'] = get_module_go(safe_name)
    elif lang_name == "Java":
        context['user'], context['gui_choice'] = get_java_data()

    option_license = add_license()
    lic_map = {"1": "MIT", "2": "Apache", "3": "GNU GPL", "4": "None"}
    selected_license = lic_map.get(option_license, "None")

    use_docker = get_docker_choice()

    try:
        print(f"\n{Colors.DIM}⚙ Building project...{Colors.END}")
        project_dir = safe_name

        if lang_name == "Go (Golang)":
            project_dir = setup_func(safe_name, readme_title, readme_description, readme_overview, context['module'], author, selected_license, year, use_docker)
        elif lang_name == "Java":
            project_dir = setup_func(safe_name, readme_title, readme_description, readme_overview, context['user'], context['gui_choice'], author, selected_license, year, use_docker)
        else:
            project_dir = setup_func(safe_name, readme_title, readme_description, readme_overview, author, selected_license, year, use_docker)

        spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        for i in range(12):
            sys.stdout.write(f"\r{Colors.CYAN}{spinner[i % len(spinner)]}{Colors.END} {Colors.DIM}Applying templates...{Colors.END}")
            sys.stdout.flush()
            time.sleep(0.08)

        sys.stdout.write(f"\r{Colors.GREEN}✔{Colors.END} {Colors.DIM}Project structure generated.{Colors.END}\n")

        git_status = git_automation(project_dir)
        save_project(project_dir, lang_name, selected_license, author, os.path.abspath(project_dir))

        print(f"\n{Colors.GREEN}✔{Colors.END} {Colors.BOLD}Done! Project '{project_dir}' is ready.{Colors.END}")
        print(f"  {Colors.DIM}↳ Author:{Colors.END} {author}")
        print(f"  {Colors.DIM}↳ Language:{Colors.END} {lang_color}{lang_name}{Colors.END}")
        print(f"  {Colors.DIM}↳ License:{Colors.END} {selected_license}")
        print(f"  {Colors.DIM}↳ Git:{Colors.END} {'Initialized' if git_status else 'Skipped'}")
        print(f"  {Colors.DIM}↳ Path:{Colors.END} {os.path.abspath(project_dir)}")

        print(f"\n{Colors.BOLD}Next steps:{Colors.END}")
        print(f"  cd {project_dir}")
        print(f"  code .\n")

        return project_dir

    except Exception as e:
        print(f"\n{Colors.RED}✖ Unexpected error: {e}{Colors.END}\n")
        return None