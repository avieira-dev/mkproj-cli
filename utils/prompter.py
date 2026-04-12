from utils.colors import Colors

def get_user_data():
    print(f"\n{Colors.CYAN}Would you like to enter your name and email into the file 'pyproject.toml'? (y/n):{Colors.END}", end = " ")
    confirm_input = input().lower().strip()

    if confirm_input == "y":
        username = input(f"{Colors.YELLOW}Username: {Colors.END}").strip() or "Your Name"
        email = input(f"{Colors.YELLOW}Email: {Colors.END}").strip() or "you@example.com"
        return username, email
    
    return "Your Name", "you@example.com"

def get_readme_data(default_name):
    print(f"\n{Colors.CYAN}Do you want to customize the README? (y/n):{Colors.END}", end = " ")
    confirm_input = input().lower().strip()

    if confirm_input == "y":
        title = input(f"{Colors.YELLOW}Title README [{default_name}]: {Colors.END}").strip() or default_name
        description = input(f"{Colors.YELLOW}Description: {Colors.END}").strip() or "Project created with mkproj-cli."
        return title, description
    
    return default_name, "Project created with mkproj-cli."