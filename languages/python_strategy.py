"""
FILE: languages/python_strategy.py
DESCRIPTION: Strategy for bootstrapping modern Python projects.
RESPONSIBILITIES:
  - Implement a clean 'src' layout for better package management
  - Normalize project and directory names (kebab-case vs snake_case)
  - Generate modern PEP 621 compliant configuration (pyproject.toml)
  - Create standard directories for documentation, scripts, and testing
"""

import os
from utils.file_system import create_directory, create_from_template

def setup_python(name, readme_title, readme_description, username, email):
    project_directory = name.replace(" ", "_").replace("-", "_").lower()
    project_name = name.replace(" ", "-").replace("_", "-").lower()

    # Create directories
    for folder in [f"src/{project_directory}", "tests", "docs", "scripts", "assets"]:
        create_directory(os.path.join(name, folder))

    # Context
    context = {
        "project_name": project_name,
        "username": username,
        "email": email,
        "readme_title": readme_title,
        "readme_description": readme_description
    }

    # Create files
    create_from_template("python/py_project.txt", os.path.join(name, "pyproject.toml"), context)
    create_from_template("python/py_readme.txt", os.path.join(name, "README.md"), context)
    create_from_template("python/py_gitignore.txt", os.path.join(name, ".gitignore"), context)
    create_from_template("python/py_main.txt", os.path.join(name, f"src/{project_directory}", "main.py"), context)
