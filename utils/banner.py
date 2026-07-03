"""
FILE: banner.py
DESCRIPTION: Renders the mkproj CLI banner with a pre-computed gradient.
"""

from utils.colors import Colors

FONT = {
    "m": ["█   █", "██ ██", "█ █ █", "█   █", "█   █"],
    "k": ["█   █", "█  █ ", "███  ", "█  █ ", "█   █"],
    "p": ["████ ", "█   █", "████ ", "█    ", "█    "],
    "r": ["████ ", "█   █", "████ ", "█  █ ", "█   █"],
    "o": [" ███ ", "█   █", "█   █", "█   █", " ███ "],
    "j": ["  ███", "    █", "    █", "█   █", " ███ "],
    " ": ["     ", "     ", "     ", "     ", "     "]
}

WORD = "mkproj"
COLOR_START = (10, 42, 110)
COLOR_END = (79, 195, 247)
RESET = "\033[0m"

def _fg(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def _lerp(a, b, t):
    return round(a + (b - a) * t)

def _lerp_color(c1, c2, t):
    return tuple(_lerp(c1[i], c2[i], t) for i in range(3))

def _generate_static_banner():
    """Generates the colored banner only once during initialization."""
    rows = [""] * 5
    for index, ch in enumerate(WORD):
        glyph = FONT.get(ch, FONT[" "])
        for i in range(5):
            rows[i] += glyph[i]
            if index != len(WORD) - 1:
                rows[i] += " "

    width = len(rows[0])
    color_rows = []

    for row in rows:
        line = ""
        last_color = None
        for x, c in enumerate(row):
            if c == "█":
                t = x / max(width - 1, 1)
                color = _lerp_color(COLOR_START, COLOR_END, t)
                if color != last_color:
                    line += _fg(*color)
                    last_color = color
                line += "█"
            else:
                line += " "
        line += RESET
        color_rows.append(line)
    return color_rows

# Memory cache for the pre-rendered banner
_STATIC_BANNER_LINES = _generate_static_banner()

def print_banner(version):
    print()
    for line in _STATIC_BANNER_LINES:
        print(line)
    print()
    print(
        f"{Colors.BG_BLUE}{Colors.WHITE}{Colors.BOLD} v{version} "
        f"{Colors.END} {Colors.DIM}Developer Productivity Tool{Colors.END}\n"
    )