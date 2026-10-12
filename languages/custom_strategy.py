"""
FILE: languages/custom_strategy.py
DESCRIPTION: Strategy for bootstrapping projects with custom directory and file structures.
RESPONSIBILITIES:
  - Create custom directory trees specified by the user
  - Create custom files specified by the user
  - Handle root directory path resolution safely
"""

import os
from utils import (
    create_directory, 
    create_file
)

def setup_custom(name, dirs, files):
    root_directory = name

    for folder in dirs:
        create_directory(os.path.join(root_directory, folder))

    for file in files:
        create_file(os.path.join(root_directory, file))

    return root_directory