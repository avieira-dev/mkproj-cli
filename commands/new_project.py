"""
FILE: commands/new_project.py
DESCRIPTION: Orchestrator for the project creation workflow.
RESPONSIBILITIES:
  - Validate project names and directory availability
  - Render the interactive CLI menu for language selection
  - Coordinate data collection via prompter and route to specific language strategies
  - Provide visual feedback (spinners/summaries) and final Git automation
  - Handle the high-level project assembly sequence
"""

import os
import sys
import time
from utils.colors import Colors
from utils.prompter import (
    get_readme_data, get_user_data, 
    get_module_go, get_java_data,
    get_web_data, get_rust_data,
    git_automation)
from languages import (
    setup_python, setup_cpp, setup_c, 
    setup_web, setup_java, setup_go,
    setup_rust, setup_typescript
)

STRATEGIES = {
    "1": ("Python", setup_python, "🐍"),
    "2": ("C++", setup_cpp, "💻"),
    "3": ("C", setup_c, "⚙️ "),
    "4": ("Java", setup_java, "☕"),
    "5": ("Go (Golang)", setup_go, "🐹"),
    "6": ("Web (HTML/CSS/JS)", setup_web, "🌐"),
    "7": ("Rust", setup_rust, "🦀"),
    "8": ("TypeScript (Node)", setup_typescript, "🟦")
}

def command_new():
    if len(sys.argv) < 3:
        print(f"{Colors.YELLOW}Usage: mkproj new <project_name>{Colors.END}")
        return None
    
    name = sys.argv[2].strip()
    if not name or os.path.exists(name):
        print(f"\n{Colors.RED}✖ Error: Project name invalid or directory exists.{Colors.END}")
        return None
    
    print(f"{Colors.CYAN}🚀 Creating project:{Colors.END} {Colors.BOLD}{name}{Colors.END}\n")

    WIDTH = 45
    print(f"{Colors.BLUE}┌{'─' * (WIDTH-2)}┐{Colors.END}")
    header_text = " Select Strategy:"
    print(f"{Colors.BLUE}│{Colors.END} {Colors.BOLD}{header_text.ljust(WIDTH-4)}{Colors.END} {Colors.BLUE}│{Colors.END}")
    print(f"{Colors.BLUE}├{'─' * (WIDTH-2)}┤{Colors.END}")

    for key, (lang_name, _, icon) in STRATEGIES.items():
        offset = 1 if len(icon) == 1 else 0
        
        if lang_name == "C":
            offset = 1
        
        prefix = f"  {Colors.CYAN}{key}){Colors.END} {icon} "
        padding_size = WIDTH - len(lang_name) - 11 + offset
        padding = " " * padding_size
        
        print(f"{Colors.BLUE}│{Colors.END}{prefix}{lang_name}{padding}{Colors.BLUE}│{Colors.END}")

    print(f"{Colors.BLUE}└{'─' * (WIDTH-2)}┘{Colors.END}")

    choice = input(f"\n{Colors.GREEN}❯{Colors.END} {Colors.BOLD}Selection:{Colors.END} ")

    if choice in STRATEGIES:
        lang_name, setup_func, _ = STRATEGIES[choice]
        readme_title, readme_description = get_readme_data(name)

        context = {}
        if lang_name == "Python": context['user'], context['email'] = get_user_data()
        elif lang_name == "Go (Golang)": context['module'] = get_module_go(name)
        elif lang_name == "Java": context['user'], context['gui_choice'] = get_java_data()
        elif lang_name == "Web (HTML/CSS/JS)": context['user'] = get_web_data()
        elif lang_name == "Rust": context['user'], context['email'], context['license'] = get_rust_data()

        try:
            print(f"\n{Colors.YELLOW}⚙ Building project...{Colors.END}")
            
            # Setup execution
            if lang_name == "Python": setup_python(name, readme_title, readme_description, context['user'], context['email'])
            elif lang_name == "Go (Golang)": setup_go(name, readme_title, readme_description, context['module'])
            elif lang_name == "Java": setup_java(name, readme_title, readme_description, context['user'], context['gui_choice'])
            elif lang_name == 'Web (HTML/CSS/JS)': setup_web(name, readme_title, readme_description, context['user'])
            elif lang_name == 'Rust': setup_rust(name, readme_title, readme_description, context['user'], context['email'], context['license'])
            else: setup_func(name, readme_title, readme_description)

            spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
            for i in range(12):
                sys.stdout.write(f"\r{Colors.CYAN}{spinner[i % len(spinner)]}{Colors.END} {Colors.DIM}Applying templates...{Colors.END}")
                sys.stdout.flush()
                time.sleep(0.08)
            
            sys.stdout.write(f"\r{Colors.GREEN}✔{Colors.END} Project structure generated!     \n")

            # Git automation
            git_status = git_automation(name)

            # Final summary
            print(f"\n{Colors.BLUE}✔ {Colors.END}{Colors.CYAN}Done! Project {Colors.BOLD}{name}{Colors.END} is ready.{Colors.END}")
            print(f"  {Colors.DIM} Language: {Colors.END}{lang_name}")
            print(f"  {Colors.DIM} Git: {Colors.END}{'Initialized ✔' if git_status else 'Skipped ⚪'}")
            print(f"  {Colors.DIM} Path: {Colors.END}{os.path.abspath(name)}")

            print(f"\n{Colors.BLUE}🚀 Next steps:{Colors.END}")
            print(f"  {Colors.CYAN} $ cd{Colors.END} {name}")
            print(f"  {Colors.CYAN} $ code .{Colors.END}\n")
            
            return name
        except Exception as e:
            print(f"\n{Colors.RED}✖ Unexpected error: {e}{Colors.END}")
            return None
    else:
        print(f"{Colors.RED}✖ Invalid choice!{Colors.END}")
        return None