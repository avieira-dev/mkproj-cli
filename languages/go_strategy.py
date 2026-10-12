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
from utils import (
    create_directory,
    create_from_template,
    get_license_path
)

def get_go_structure(docker_support = False):
    dirs = [
        'cmd',
        'internal',
        'pkg'
    ]

    files = [
        'go.mod',
        '.gitignore',
        'README.md',
        'cmd/main.go',
        'LICENSE'
    ]

    if docker_support:
        files.extend(['Dockerfile', 'compose.yaml'])

    return dirs, files

def setup_go(name, readme_title, readme_description, readme_overview, module, username, license, year, docker_support = False):
    root_directory = image_docker_name = container_name = project_name_go = name
    license_path = get_license_path(license)

    for folder in ['cmd', 'internal', 'pkg']:
        create_directory(os.path.join(root_directory, folder))

    context = {
        'readme_title': readme_title,
        'readme_description': readme_description,
        'readme_overview': readme_overview,
        'readme_author': username,
        'module_path': module,
        'project_name_go': project_name_go,
        'image_docker_name': image_docker_name,
        'container_name': container_name,
        'year': year,
        'holder': username
    }

    create_from_template('go/go_mod.txt', os.path.join(root_directory, 'go.mod'), context)
    create_from_template('go/go_gitignore.txt', os.path.join(root_directory, '.gitignore'), context)
    create_from_template('go/go_readme.txt', os.path.join(root_directory, 'README.md'), context)
    create_from_template('go/go_main.txt', os.path.join(root_directory, 'cmd', 'main.go'), context)
    create_from_template(license_path, os.path.join(root_directory, 'LICENSE'), context)

    if docker_support:
        create_from_template('go/go_dockerfile.txt', os.path.join(root_directory, 'Dockerfile'), context)
        create_from_template('go/go_compose.txt', os.path.join(root_directory, 'compose.yaml'), context)

    return root_directory