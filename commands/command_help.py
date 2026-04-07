from utils.colors import Colors

def command_help():
    print(f"{Colors.YELLOW}Usage: {Colors.END}mkproj <command> [arguments]\n")

    # Available commands
    print(f"{Colors.BOLD}Available Commands:{Colors.END}")
    print(f" {Colors.GREEN}new <name>{Colors.END} Starts the interactive project generator")
    print(f" {Colors.GREEN}help, -h, --help{Colors.END} Shows this help message\n")

    # Examples
    print(f"{Colors.BOLD}Examples:{Colors.END}")
    print(f" $ mkproj new my-awesome-app")
    print(f" $ mkproj --help\n")

    print(f"{Colors.BLUE}Created by Alexandre Vieira (https://github.com/avieira-dev){Colors.END}\n")