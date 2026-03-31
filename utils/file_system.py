import os
from pathlib import Path

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def create_file(path, content=""):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)