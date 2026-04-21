from utils.colors import Colors

def get_user_data():
    print(f"\n{Colors.PURPLE}?{Colors.END} {Colors.BOLD}Configure pyproject.toml?{Colors.END} {Colors.DIM}(y/n){Colors.END}", end=" ")

    if input().lower().strip() == "y":
        user = input(f"  {Colors.DIM}↳{Colors.END} Username: ").strip() or "Your Name"
        mail = input(f"  {Colors.DIM}↳{Colors.END} Email: ").strip() or "you@example.com"
        return user, mail
    
    return "Your Name", "you@example.com"

def get_web_data():
    print(f"\n{Colors.PURPLE}?{Colors.END} {Colors.BOLD}Would you like to add your name to the package.json file?{Colors.END} {Colors.DIM}(y/n){Colors.END}", end=" ")

    if input().lower().strip() == "y":
        user = input(f"  {Colors.DIM}↳{Colors.END} Username: ").strip() or "Your Name"
        return user
    
    return "Your Name"


def get_readme_data(default_name):
    print(f"{Colors.PURPLE}?{Colors.END} {Colors.BOLD}Customize README?{Colors.END} {Colors.DIM}(y/n){Colors.END}", end=" ")

    if input().lower().strip() == "y":
        title = input(f"  {Colors.DIM}↳{Colors.END} Title [{default_name}]: ").strip() or default_name
        desc = input(f"  {Colors.DIM}↳{Colors.END} Description: ").strip() or "Project created with mkproj-cli."
        return title, desc
    
    return default_name, "Project created with mkproj-cli."

def get_module_go(default_name):
    print(f"\n{Colors.PURPLE}?{Colors.END} {Colors.BOLD}Use GitHub as Go module?{Colors.END} {Colors.DIM}(y/n){Colors.END}", end=" ")

    if input().lower().strip() == "y":
        repo = input(f"  {Colors.DIM}↳{Colors.END} Repo path: ").replace("https://", "").strip() or default_name
        return repo
    
    return default_name

def get_java_data():
    user = "user"
    print(f"\n{Colors.PURPLE}?{Colors.END} {Colors.BOLD}Developer/Org name or Domain?{Colors.END} {Colors.DIM}(y/n){Colors.END}", end=" ")

    if input().lower().strip() == "y":
        user = input(f"  {Colors.DIM}↳{Colors.END} Domain (ex: br.com.mywebsite): ").strip().lower() or "user"

    print(f"\n{Colors.PURPLE}?{Colors.END} {Colors.BOLD}Select Java template?{Colors.END} {Colors.DIM}(y/n){Colors.END}", end=" ")

    if input().lower().strip() == "y":
        print(" 1) Console Application (Simple)")
        print(" 2) GUI Application (Swing/MVC structure)")
        gui_choice = input(f"  {Colors.DIM}↳{Colors.END} Enter selection (default: 1): ") or "1"

        if gui_choice in ["1", "2"]:
            return user, gui_choice
        
    return user, "1"