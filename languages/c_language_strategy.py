"""
FILE: languages/c_language_strategy.py
DESCRIPTION: Strategy for bootstrapping C language projects with CMake.
RESPONSIBILITIES:
  - Create a standard C project structure (src, include, build)
  - Setup a cross-platform build system using CMakeLists.txt
  - Normalize project identifiers to PascalCase for headers and build targets
  - Generate a clean main.c entry point and base documentation
"""

import os
from utils.file_system import create_directory, create_from_template

def setup_c(name, readme_title, readme_description, readme_overview, username, license, year, docker_support = False):
    root_directory = name.replace(" ", "_").replace("-", "_").lower()
    container_name = project_name_cmake = image_docker_name = name.replace(" ", "-").replace("_", "-").lower()

    license_path = "licenses/mit.txt" if license == "MIT" else \
                   "licenses/apache.txt" if license == "Apache" else \
                   "licenses/gpl.txt" if license == "GNU GPL" else "licenses/explanation.txt"

    # Create directories
    for folder in ["include", "src", "tests", "build", "docs"]:
        create_directory(os.path.join(root_directory, folder))

    # Data to fill in the templates
    context = {
        "project_name_cmake": project_name_cmake,
        "readme_title": readme_title,
        "readme_description": readme_description,
        "readme_overview": readme_overview,
        "readme_author": username,
        "container_name": container_name,
        "image_docker_name": image_docker_name,
        "year": year,
        "holder": username
    }

    # Create files
    create_from_template("c_language/c_cmake.txt", os.path.join(root_directory, "CMakeLists.txt"), context)
    create_from_template("c_language/c_gitignore.txt", os.path.join(root_directory, ".gitignore"), context)
    create_from_template("c_language/c_readme.txt", os.path.join(root_directory, "README.md"), context)
    create_from_template("c_language/c_main.txt", os.path.join(root_directory, "src", "main.c"), context)
    create_from_template(license_path, os.path.join(root_directory, "LICENSE"), context)

    if docker_support:
        create_from_template("c_language/c_dockerfile.txt", os.path.join(root_directory, "Dockerfile"), context)
        create_from_template("c_language/c_compose.txt", os.path.join(root_directory, "compose.yaml"), context)

    return root_directory