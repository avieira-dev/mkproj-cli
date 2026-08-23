"""
FILE: utils/colors.py
DESCRIPTION: Centralized ANSI escape sequences for terminal styling.
"""

class Colors:
    BLUE = '\033[94m'
    LIGHT_BLUE = '\033[38;5;39m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ORANGE = '\033[38;5;208m'
    PURPLE = '\033[95m'
    GRAY = '\033[90m'
    WHITE = '\033[97m'
    
    BG_BLUE = '\033[44m'

    BOLD = '\033[1m'
    DIM = '\033[2m'
    END = '\033[0m'