"""
FILE: utils/colors.py
DESCRIPTION: Centralized ANSI escape sequences for terminal styling.
RESPONSIBILITIES:
  - Provide a consistent color palette for the CLI (Blue, Cyan, etc.)
  - Define text formatting styles (Bold, Dim, Underline)
  - Support background colors for UI elements like badges and banners
  - Enable the 'END' reset token to prevent color bleeding into user input
"""

class Colors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    
    # Background for badges
    BG_BLUE = '\033[44m'
    BG_CYAN = '\033[46m'
    WHITE = '\033[97m'