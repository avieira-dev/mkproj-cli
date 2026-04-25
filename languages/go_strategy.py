"""
FILE: languages/go_strategy.py
DESCRIPTION: Strategy for bootstrapping Go (Golang) projects.
RESPONSIBILITIES:
  - Implement the standard Go Project Layout (cmd/, internal/, pkg/)
  - Initialize the Go module system by creating the go.mod file
  - Setup a clean entry point in cmd/main.go
  - Normalize directory naming for Go workspace compatibility
"""

import os
from utils.file_system import create_directory, create_from_template

def setup_go(name, readme_title, readme_description, module):
    project_directory = name.replace(" ", "-").replace("_", "-").lower()

    # Create directories
    for folder in ["cmd", "internal", "pkg"]:
        create_directory(os.path.join(project_directory, folder))

    # Data to fill in the templates
    context = {
        "module": module,
        "readme_title": readme_title,
        "readme_description": readme_description
    }

    # Create files
    create_from_template("go/go_mod.txt", os.path.join(project_directory, "go.mod"), context)
    create_from_template("go/go_gitignore.txt", os.path.join(project_directory, ".gitignore"), context)
    create_from_template("go/go_readme.txt", os.path.join(project_directory, "README.md"), context)
    create_from_template("go/go_main.txt", os.path.join(project_directory, "cmd", "main.go"), context)