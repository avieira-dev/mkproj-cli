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
from utils import (
    create_directory,
    create_from_template,
    get_license_path    
)

def get_python_structure(name, docker_support = False):
    default_directory = name.replace(' ', '-').replace('_', '-').lower()
    dirs = [
        f'src/{default_directory}', 
        'tests', 
        'docs', 
        'scripts', 
        'assets'
    ]

    files = [
        'pyproject.toml',
        'README.md',
        '.gitignore',
        f'src/{default_directory}/main.py',
        'LICENSE'
    ]

    if docker_support:
        files.extend(['Dockerfile', 'compose.yaml'])

    return dirs, files

def setup_python(name, readme_title, readme_description, readme_overview, username, email, license, year, docker_support = False):
    root_directory = name
    default_directory = project_name_toml = container_name = image_docker_name = name.replace(' ', '-').replace('_', '-').lower()
    license_path = get_license_path(license)

    for folder in [f'src/{default_directory}', 'tests', 'docs', 'scripts', 'assets']:
        create_directory(os.path.join(root_directory, folder))

    context = {
        'readme_title': readme_title,
        'readme_description': readme_description,
        'readme_overview': readme_overview,
        'readme_author': username,
        'project_name_toml': project_name_toml,
        'description_toml': readme_description,
        'name': username,
        'email': email,
        'default_directory': default_directory,
        'image_docker_name': image_docker_name,
        'container_name': container_name,
        'year': year,
        'holder': username
    }

    create_from_template('python/py_project.txt', os.path.join(root_directory, 'pyproject.toml'), context)
    create_from_template('python/py_readme.txt', os.path.join(root_directory, 'README.md'), context)
    create_from_template('python/py_gitignore.txt', os.path.join(root_directory, '.gitignore'), context)
    create_from_template('python/py_main.txt', os.path.join(root_directory, f'src/{default_directory}', 'main.py'), context)
    create_from_template(license_path, os.path.join(root_directory, 'LICENSE'), context)

    if docker_support:
        create_from_template('python/py_dockerfile.txt', os.path.join(root_directory, 'Dockerfile'), context)
        create_from_template('python/py_compose.txt', os.path.join(root_directory, 'compose.yaml'), context)

    return root_directory