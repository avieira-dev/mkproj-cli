"""
FILE: languages/cpp_strategy.py
DESCRIPTION: Strategy for bootstrapping C++ projects with CMake support.
RESPONSIBILITIES:
  - Implement a standard C++ directory layout (src, include, build, external)
  - Normalize project names to PascalCase for class-like naming conventions
  - Setup the CMake build system configuration (CMakeLists.txt)
  - Organize source code (src/core) and headers (include/core) separation
"""

import os
from utils.file_system import create_directory, create_from_template

def setup_cpp(name, readme_title, readme_description, username, license, year):
    class_name = "".join(p.capitalize() for p in name.replace("_", "-").split("-"))

    license_path = "licenses/mit.txt" if license == "MIT" else \
                   "licenses/apache.txt" if license == "Apache" else \
                   "licenses/gpl.txt" if license == "GNU GPL" else "licenses/explanation.txt"

    # Create directories
    for folder in ["src/core", "include/core", "build", "tests", "external", "assets", "docs"]:
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
    create_from_template("cpp/cpp_cmake.txt", os.path.join(name, "CMakeLists.txt"), context)
    create_from_template("cpp/cpp_gitignore.txt", os.path.join(name, ".gitignore"), context)
    create_from_template("cpp/cpp_readme.txt", os.path.join(name, "README.md"), context)
    create_from_template("cpp/cpp_main.txt", os.path.join(name, "src", "core", "main.cpp"), context)
    create_from_template(license_path, os.path.join(name, "LICENSE"), context)
    