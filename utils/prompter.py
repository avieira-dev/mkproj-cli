from utils.colors import Colors

def get_readme_data(default_name):
    print(f"\n{Colors.CYAN}Do you want to customize the README? (y/n):{Colors.END}", end=" ")
    confirm_input = input().lower().strip()

    if confirm_input == "y":
        title = input(f"{Colors.YELLOW}Title README [{default_name}]: {Colors.END}").strip() or default_name
        description = input(f"{Colors.YELLOW}Description: {Colors.END}").strip() or "Project created with mkproj-cli."
        return title, description
    
    return default_name, "Project created with mkproj-cli."