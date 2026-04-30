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

def setup_go(name, readme_title, readme_description, module, username, license, year):
    project_dir = name.replace(" ", "-").replace("_", "-").lower()

    license_path = "licenses/mit.txt" if license == "MIT" else \
                   "licenses/apache.txt" if license == "Apache" else \
                   "licenses/gpl.txt" if license == "GNU GPL" else "licenses/explanation.txt"

    # Create directories
    for folder in ["cmd", "internal", "pkg"]:
        create_directory(os.path.join(project_dir, folder))

    # Data to fill in the templates
    context = {
        "module": module,
        "readme_title": readme_title,
        "readme_description": readme_description,
        "year": year,
        "holder": username
    }

    # Create files
    create_from_template("go/go_mod.txt", os.path.join(project_dir, "go.mod"), context)
    create_from_template("go/go_gitignore.txt", os.path.join(project_dir, ".gitignore"), context)
    create_from_template("go/go_readme.txt", os.path.join(project_dir, "README.md"), context)
    create_from_template("go/go_main.txt", os.path.join(project_dir, "cmd", "main.go"), context)
    create_from_template(license_path, os.path.join(project_dir, "LICENSE"), context)