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

def setup_cpp(name, readme_title, readme_description, readme_overview, username, license, year, docker_support = False):
    root_directory = image_docker_name = container_name = project_name_cmake = name.replace(" ", "-").replace("_", "-").lower()

    license_path = "licenses/mit.txt" if license == "MIT" else \
                   "licenses/apache.txt" if license == "Apache" else \
                   "licenses/gpl.txt" if license == "GNU GPL" else "licenses/explanation.txt"

    # Create directories
    for folder in ["src/core", "include/core", "build", "tests", "external", "assets", "docs"]:
        create_directory(os.path.join(root_directory, folder))

    # Data to fill in the templates
    context = {
        "image_docker_name": image_docker_name,
        "container_name": container_name,
        "project_name_cmake": project_name_cmake,
        "readme_title": readme_title,
        "readme_description": readme_description,
        "readme_overview": readme_overview,
        "readme_author": username,
        "year": year,
        "holder": username
    }

    # Create files
    create_from_template("cpp/cpp_cmake.txt", os.path.join(root_directory, "CMakeLists.txt"), context)
    create_from_template("cpp/cpp_gitignore.txt", os.path.join(root_directory, ".gitignore"), context)
    create_from_template("cpp/cpp_readme.txt", os.path.join(root_directory, "README.md"), context)
    create_from_template("cpp/cpp_main.txt", os.path.join(root_directory, "src", "core", "main.cpp"), context)
    create_from_template(license_path, os.path.join(root_directory, "LICENSE"), context)

    if docker_support:
        create_from_template("cpp/cpp_dockerfile.txt", os.path.join(root_directory, "Dockerfile"), context)
        create_from_template("cpp/cpp_compose.txt", os.path.join(root_directory, "compose.yaml"), context)

    return root_directory