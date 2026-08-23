"""
FILE: robot.py
DESCRIPTION: Renders the welcome robot ASCII art in blue and the speech bubble in white.
"""

from utils.colors import Colors

def print_robot():
    robot = f"""{Colors.BLUE}{Colors.BOLD}
     ┌────────┐    {Colors.WHITE}{Colors.BOLD}┌──────────────────────┐{Colors.BLUE}{Colors.BOLD}          
     │ │ O  O │  {Colors.WHITE}{Colors.BOLD}/ │  Welcome to mkproj!  │{Colors.BLUE}{Colors.BOLD}
     │ │ ==== │ {Colors.WHITE}{Colors.BOLD}/  └──────────────────────┘{Colors.BLUE}{Colors.BOLD}
   ┌─┐─────────┐
   │ │  [] .[] │   
   │ │  []:.[] │   
   │ │         │ 
   └─┘─────────┘
   ┌─┘        └─┐
   └─O=O====O=O─┘
{Colors.END}"""
    
    print(robot)