import os
import sys
from languages import setup_python, setup_cpp, setup_c, setup_web, setup_java, setup_go

STRATEGIES = {
    "1": ("Python", setup_python),
    "2": ("C++", setup_cpp),
    "3": ("C", setup_c),
    "4": ("Java", setup_java),
    "5": ("Web (HTML, CSS and JS)", setup_web),
    "6": ("Go (Golang)", setup_go)   
}

def command_new():
    if len(sys.argv) < 3:
        print("Usage: mkproj new <project_name>")
        return
    
    name = sys.argv[2].strip()

    if not name:
        print("Error: Project name cannot be empty.")
        return
    
    if os.path.exists(name):
        print(f"\nError: Directory '{name}' already exists!")
        return
    
    print(f"Creating project: {name}\n")


    print("Select the language:")
    for key, (lang_name, _) in STRATEGIES.items():
        print(f"  {key}) {lang_name}")

    choice = input("Enter selection: ")

    if choice in STRATEGIES:
        _, setup_func = STRATEGIES[choice]
        try:
            setup_func(name)
            print("\nProject created successfully!")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

    else:
        print("Invalid choice!")