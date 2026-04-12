import os
import sys
import time
from utils.colors import Colors
from utils.prompter import get_readme_data, get_user_data
from languages import (
    setup_python, setup_cpp, setup_c, 
    setup_web, setup_java, setup_go,
    setup_rust, setup_typescript
)

# Mapping of available language strategies
STRATEGIES = {
    "1": ("Python", setup_python),
    "2": ("C++", setup_cpp),
    "3": ("C", setup_c),
    "4": ("Java", setup_java),
    "5": ("Go (Golang)", setup_go),
    "6": ("Web (HTML/CSS/JS)", setup_web),
    "7": ("Rust", setup_rust),
    "8": ("TypeScript (Node.js)", setup_typescript)
}

def command_new():
    # Check if project name was provided
    if len(sys.argv) < 3:
        print(f"{Colors.YELLOW}Usage: mkproj new <project_name>{Colors.END}")
        return
    
    name = sys.argv[2].strip()

    # Check for empty string
    if not name:
        print(f"{Colors.RED}Error: Project name cannot be empty.{Colors.END}")
        return
    
    # Check if directory already exists
    if os.path.exists(name):
        print(f"\n{Colors.RED}Error: Directory '{name}' already exists!{Colors.END}")
        return
    
    print(f"{Colors.CYAN}Creating project:{Colors.END} {Colors.BOLD}{name}{Colors.END}\n")

    # Styled Menu 
    print(f"{Colors.BOLD}{Colors.YELLOW}Select the language strategy:{Colors.END}")
    
    border = f"{Colors.BLUE}+------------------------------------------+{Colors.END}"
    print(border)

    for key, (lang_name, _) in STRATEGIES.items():
        name_padding = lang_name.ljust(37)
        
        line = (
            f"{Colors.BLUE}|{Colors.END}"               
            f"{Colors.CYAN}{Colors.BOLD}  {key}){Colors.END} "
            f"{name_padding}"                           
            f"{Colors.BLUE}|{Colors.END}"               
        )
        print(line)

    print(border)

    choice = input(f"\n{Colors.GREEN}λ{Colors.END} {Colors.BOLD}Enter selection:{Colors.END} ")

    if choice in STRATEGIES:
        lang_name, setup_func = STRATEGIES[choice]

        readme_title, readme_description = get_readme_data(name)

        if lang_name == "Python":
            username, email = get_user_data()

        try:
            print(f"\n{Colors.YELLOW}⚙ Generating {Colors.BOLD}{lang_name}{Colors.END} structure...{Colors.END}")

            if lang_name == "Python":
                setup_python(name, readme_title, readme_description, username, email)
            else:
                setup_func(name, readme_title, readme_description)
            
            spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

            for i in range(20):
                char = spinner[i % len(spinner)]
                sys.stdout.write(f"\r{Colors.CYAN}{char} Finishing touches...{Colors.END}")
                sys.stdout.flush()
                time.sleep(0.1)
            
            sys.stdout.write("\r" + " " * 40 + "\r")
            sys.stdout.flush()
            
            print(f"{Colors.GREEN}✔ Success!{Colors.END} Project {Colors.BOLD}{name}{Colors.END} is ready.")
            print(f"{Colors.BLUE}→ Next step:{Colors.END} cd {name}\n")
            
        except Exception as e:
            print(f"\n{Colors.RED}✖ An unexpected error occurred: {e}{Colors.END}")
    else:
        print(f"{Colors.RED}Invalid choice!{Colors.END}")