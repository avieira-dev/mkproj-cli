import sys
from languages.python_strategy import setup_python

languages = {
    "1": ("Python", setup_python)    
}

def command_new():
    if len(sys.argv) < 3:
        print("Usage: mkproj new <project_name>")
        return
    
    name = sys.argv[2]
    print(f"Creating project: {name}\n")


    print("Select the language:")
    for key, (lang_name, _) in languages.items():
        print(f"[{key}, {lang_name}]")

    choice = input("Enter selection: ")

    if choice in languages:
        _, setup_func = languages[choice]
        try:
            setup_func(name)
            print("\nProject created successfully!")
        except FileExistsError:
            print("\nError: Directory already exists!")

    else:
        print("Invalid choice!")