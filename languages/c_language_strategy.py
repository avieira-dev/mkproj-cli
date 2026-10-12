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
from utils import (
    create_directory,
    create_from_template,
    get_license_path    
)

def get_c_structure(docker_support = False):
    dirs = [
        'include',
        'src',
        'tests',
        'build',
        'docs'
    ]

    files = [
        'CMakeLists.txt',
        '.gitignore',
        'README.md',
        'src/main.c',
        'LICENSE'    
    ]

    if docker_support:
        files.extend(['Dockerfile', 'compose.yaml'])

    return dirs, files


def setup_c(name, readme_title, readme_description, readme_overview, username, license, year, docker_support = False):
    root_directory = name
    container_name = project_name_cmake = image_docker_name = name.replace(' ', '-').replace('_', '-').lower()
    license_path = get_license_path(license)

    for folder in ['include', 'src', 'tests', 'build', 'docs']:
        create_directory(os.path.join(root_directory, folder))

    context = {
        'project_name_cmake': project_name_cmake,
        'readme_title': readme_title,
        'readme_description': readme_description,
        'readme_overview': readme_overview,
        'readme_author': username,
        'container_name': container_name,
        'image_docker_name': image_docker_name,
        'year': year,
        'holder': username
    }

    create_from_template('c_language/c_cmake.txt', os.path.join(root_directory, 'CMakeLists.txt'), context)
    create_from_template('c_language/c_gitignore.txt', os.path.join(root_directory, '.gitignore'), context)
    create_from_template('c_language/c_readme.txt', os.path.join(root_directory, 'README.md'), context)
    create_from_template('c_language/c_main.txt', os.path.join(root_directory, 'src', 'main.c'), context)
    create_from_template(license_path, os.path.join(root_directory, 'LICENSE'), context)

    if docker_support:
        create_from_template('c_language/c_dockerfile.txt', os.path.join(root_directory, 'Dockerfile'), context)
        create_from_template('c_language/c_compose.txt', os.path.join(root_directory, 'compose.yaml'), context)

    return root_directory