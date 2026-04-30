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

def setup_c(name, readme_title, readme_description, username, license, year):
    class_name = "".join(p.capitalize() for p in name.replace("_", "-").split("-"))

    license_path = "licenses/mit.txt" if license == "MIT" else \
                   "licenses/apache.txt" if license == "Apache" else \
                   "licenses/gpl.txt" if license == "GNU GPL" else "licenses/explanation.txt"

    # Create directories
    for folder in ["include", "src", "tests", "build", "docs"]:
        create_directory(os.path.join(name, folder))

    # Data to fill in the templates
    context = {
        "project_name": class_name,
        "readme_title": readme_title,
        "readme_description": readme_description,
        "year": year,
        "holder": username
    }

    # Create files
    create_from_template("c_language/c_cmake.txt", os.path.join(name, "CMakeLists.txt"), context)
    create_from_template("c_language/c_gitignore.txt", os.path.join(name, ".gitignore"), context)
    create_from_template("c_language/c_readme.txt", os.path.join(name, "README.md"), context)
    create_from_template("c_language/c_main.txt", os.path.join(name, "src", "main.c"), context)
    create_from_template(license_path, os.path.join(name, "LICENSE"), context)