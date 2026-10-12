"""
FILE: languages/typescript_strategy.py
DESCRIPTION: Strategy for bootstrapping TypeScript (Node.js) projects.
RESPONSIBILITIES:
  - Create the base project structure (src and tests directories).
  - Normalize project names for the package.json manifest.
  - Generate TypeScript-specific configuration (tsconfig.json).
  - Setup a ready-to-use entry point in TypeScript.
"""

import os
from utils import (
    create_directory,
    create_from_template,
    get_license_path    
)

def get_typescript_structure(docker_support = False):
    dirs = [
        'src',
        'tests'    
    ]

    files = [
        'tsconfig.json',
        'package.json',
        '.gitignore',
        'README.md',
        'src/index.ts',
        'LICENSE'    
    ]

    if docker_support:
        files.extend(['Dockerfile', 'compose.yaml'])

    return dirs, files

def setup_typescript(name, readme_title, readme_description, readme_overview, username, license, year, docker_support = False):
    root_directory = project_name_ts = image_docker_name = container_name = name
    license_path = get_license_path(license)

    for folder in ['src', 'tests']:
        create_directory(os.path.join(root_directory, folder))

    context = {
        'image_docker_name': image_docker_name,
        'container_name': container_name,
        'project_name_ts': project_name_ts,
        'ts_description': readme_description,
        'readme_title': readme_title,
        'readme_description': readme_description,
        'readme_overview': readme_overview,
        'readme_author': username,
        'year': year,
        'holder': username
    }
    
    create_from_template('typescript/ts_config.txt', os.path.join(root_directory, 'tsconfig.json'), context)
    create_from_template('typescript/ts_package.txt', os.path.join(root_directory, 'package.json'), context)
    create_from_template('typescript/ts_gitignore.txt', os.path.join(root_directory, '.gitignore'), context)
    create_from_template('typescript/ts_readme.txt', os.path.join(root_directory, 'README.md'), context)
    create_from_template('typescript/ts_index.txt', os.path.join(root_directory, 'src', 'index.ts'), context)
    create_from_template(license_path, os.path.join(root_directory, 'LICENSE'), context)

    if docker_support:
        create_from_template('typescript/ts_dockerfile.txt', os.path.join(root_directory, 'Dockerfile'), context)
        create_from_template('typescript/ts_compose.txt', os.path.join(root_directory, 'compose.yaml'), context)

    return root_directory