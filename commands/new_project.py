import os
import sys
import time
from utils.colors import Colors
from utils.prompter import (
    get_readme_data, get_user_data, 
    get_module_go, get_java_data,
    get_web_data)
from languages import (
    setup_python, setup_cpp, setup_c, 
    setup_web, setup_java, setup_go,
    setup_rust, setup_typescript
)

# Mapping of available language strategies
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
    
    print(f"{Colors.CYAN}🚀 Creating project:{Colors.END} {Colors.BOLD}{name}{Colors.END}\n")

    # Total internal width of the box
    WIDTH = 42

    print(f"{Colors.PURPLE}┌──────────────────────────────────────────┐{Colors.END}")

    header = " Select the language strategy:"

    print(f"{Colors.PURPLE}│{Colors.END}{Colors.BOLD}{header.ljust(WIDTH)}{Colors.END}{Colors.PURPLE}│{Colors.END}")
    
    print(f"{Colors.PURPLE}├──────────────────────────────────────────┤{Colors.END}")

    for key, (lang_name, _, icon) in STRATEGIES.items():
        base_text = f"  {key}) {lang_name}"
        padding = " " * (WIDTH - len(base_text) - 3)
        line_content = f"  {Colors.CYAN}{key}){Colors.END} {icon} {lang_name}{padding}"
        print(f"{Colors.PURPLE}│{Colors.END}{line_content}{Colors.PURPLE}│{Colors.END}")

    print(f"{Colors.PURPLE}└──────────────────────────────────────────┘{Colors.END}")

    choice = input(f"\n{Colors.GREEN}❯{Colors.END} {Colors.BOLD}Selection:{Colors.END} ")

    if choice in STRATEGIES:
        lang_name, setup_func, _ = STRATEGIES[choice]
        readme_title, readme_description = get_readme_data(name)

        # Specific data
        context = {}
        if lang_name == "Python":
            context['user_python'], context['email'] = get_user_data()
        if lang_name == "Go (Golang)":
            context['module'] = get_module_go(name)
        if lang_name == "Java":
            context['user_java'], context['gui_choice'] = get_java_data()
        if lang_name == "Web (HTML/CSS/JS)":
            context['user_web'] = get_web_data()

        try:
            print(f"\n{Colors.YELLOW}⚙ Generating {Colors.BOLD}{lang_name}{Colors.END} structure...{Colors.END}")
            
            if lang_name == "Python":
                setup_python(name, readme_title, readme_description, context['user_python'], context['email'])
            elif lang_name == "Go (Golang)":
                setup_go(name, readme_title, readme_description, context['module'])
            elif lang_name == "Java":
                setup_java(name, readme_title, readme_description, context['user_java'], context['gui_choice'])
            elif lang_name == 'Web (HTML/CSS/JS)':
                setup_web(name, readme_title, readme_description, context['user_web'])
            else:
                setup_func(name, readme_title, readme_description)

            spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
            for i in range(15):
                sys.stdout.write(f"\r{Colors.CYAN}{spinner[i % len(spinner)]} Finalizing...{Colors.END}")
                sys.stdout.flush()
                time.sleep(0.08)
            
            print(f"\r{Colors.GREEN}✔ Success!{Colors.END} Project {Colors.BOLD}{name}{Colors.END} is ready.")
            print(f"{Colors.BLUE}➜{Colors.END} {Colors.DIM}cd{Colors.END} {name}\n")
            
        except Exception as e:
            print(f"\n{Colors.RED}✖ Unexpected error: {e}{Colors.END}")
    else:
        print(f"{Colors.RED}✖ Invalid choice!{Colors.END}")