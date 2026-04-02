import os
import sys
import languages

languages = {
    "1": ("Python", languages.setup_c),
    "2": ("C++", languages.setup_cpp),
    "3": ("C", languages.setup_c)    
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
    for key, (lang_name, _) in languages.items():
        print(f"  {key}) {lang_name}")

    choice = input("Enter selection: ")

    if choice in languages:
        _, setup_func = languages[choice]
        try:
            setup_func(name)
            print("\nProject created successfully!")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

    else:
        print("Invalid choice!")