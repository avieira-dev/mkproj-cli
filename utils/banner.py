"""
FILE: banner.py
DESCRIPTION: Renders the mkproj CLI banner in blue using ANSI colors.
"""

from utils.colors import Colors

def print_banner(version):
    banner = fr"""{Colors.BLUE}{Colors.BOLD}
           _                    _
 _ __ ___ | | ___ __  _ __ ___ (_)
| '_ ` _ \| |/ / '_ \| '__/ _ \| |
| | | | | |   <| |_) | | | (_) | |
|_| |_| |_|_|\_\ .__/|_|  \___// |
               |_|            |__/ 
"""
    
    print(banner)
    print(f"{Colors.BG_BLUE}{Colors.WHITE}{Colors.BOLD} v{version} " 
          f"{Colors.END} {Colors.DIM}Developer Productivity Tool{Colors.END}\n")