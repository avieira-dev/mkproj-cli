"""
FILE: utils/config.py
DESCRIPTION: Manages global configuration for mkproj-cli.
RESPONSIBILITIES:
  - Read configuration from ~/.mkproj/config.json
  - Write configuration to ~/.mkproj/config.json
  - Provide default values when config does not exist
"""

import json
from pathlib import Path

MKPROJ_DIR = Path.home() / ".mkproj"
CONFIG_FILE = MKPROJ_DIR / "config.json"

DEFAULT_CONFIG = {
    "author": "",
    "email": ""
}

def read_config():
    try:
        if CONFIG_FILE.exists():
            return json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        pass
    return dict(DEFAULT_CONFIG)

def write_config(data):
    try:
        MKPROJ_DIR.mkdir(exist_ok=True)
        CONFIG_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")
    except OSError:
        pass