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

def setup_go(name, readme_title, readme_description, readme_overview, module, username, license, year, docker_support = False):
    root_directory = image_docker_name = container_name = project_name_go = name.replace(" ", "-").replace("_", "-").lower()

    license_path = "licenses/mit.txt" if license == "MIT" else \
                   "licenses/apache.txt" if license == "Apache" else \
                   "licenses/gpl.txt" if license == "GNU GPL" else "licenses/explanation.txt"

    # Create directories
    for folder in ["cmd", "internal", "pkg"]:
        create_directory(os.path.join(root_directory, folder))

    # Data to fill in the templates
    context = {
        "readme_title": readme_title,
        "readme_description": readme_description,
        "readme_overview": readme_overview,
        "readme_author": username,
        "module_path": module,
        "project_name_go": project_name_go,
        "image_docker_name": image_docker_name,
        "container_name": container_name,
        "year": year,
        "holder": username
    }

    # Create files
    create_from_template("go/go_mod.txt", os.path.join(root_directory, "go.mod"), context)
    create_from_template("go/go_gitignore.txt", os.path.join(root_directory, ".gitignore"), context)
    create_from_template("go/go_readme.txt", os.path.join(root_directory, "README.md"), context)
    create_from_template("go/go_main.txt", os.path.join(root_directory, "cmd", "main.go"), context)
    create_from_template(license_path, os.path.join(root_directory, "LICENSE"), context)

    if docker_support:
        create_from_template("go/go_dockerfile.txt", os.path.join(root_directory, "Dockerfile"), context)
        create_from_template("go/go_compose.txt", os.path.join(root_directory, "compose.yaml"), context)

    return root_directory