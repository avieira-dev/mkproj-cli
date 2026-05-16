"""
FILE: utils/history.py
DESCRIPTION: Manages persistent project history for mkproj-cli.
RESPONSIBILITIES:
  - Store project metadata in ~/.mkproj/history.json
  - Load and return existing history entries
  - Provide a safe interface that never crashes on I/O errors
"""

import json
import os
from pathlib import Path
from datetime import datetime

MKPROJ_DIR = Path.home() / ".mkproj"
HISTORY_FILE = MKPROJ_DIR / "project-history.json"

def _ensure_dir():
    MKPROJ_DIR.mkdir(exist_ok=True)

def load_history():
    try:
        if HISTORY_FILE.exists():
            return json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        pass
    return []

def save_project(name, language, license, author, path):
    _ensure_dir()

    history = load_history()
    history.append({
        "name": name,
        "language": language,
        "license": license,
        "author": author,
        "path": path,
        "created_at": datetime.now().strftime("%d-%m-%Y %H:%M")
    })

    try:
        HISTORY_FILE.write_text(json.dumps(history, indent=2), encoding="utf-8")
    except OSError:
        pass  
