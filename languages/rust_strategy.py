"""
FILE: languages/rust_strategy.py
DESCRIPTION: Strategy for bootstrapping Rust binary projects.
RESPONSIBILITIES:
  - Create the standard Rust project layout (Cargo.toml and src/main.rs)
  - Normalize project names to snake_case for Cargo compatibility
  - Format author information (Name <email>) and license metadata
  - Generate base templates for immediate compilation with 'cargo run'
"""

import os
from utils import (
    create_directory,
    create_from_template,
    get_license_path    
)

def get_rust_structure(docker_support = False):
    dirs = ['src']

    files = [
        'Cargo.toml',
        '.gitignore',
        'README.md',
        'src/main.rs',
        'LICENSE'    
    ]

    if docker_support:
        files.extend(['Dockerfile', 'compose.yaml'])

    return dirs, files

def setup_rust(name, readme_title, readme_description, readme_overview, username, email, license, year, docker_support = False):
    root_directory = name_project_cargo = directory_name = image_docker_name = container_name = name
    license_path = get_license_path(license)

    create_directory(os.path.join(root_directory, 'src'))

    context = {
        'name_project': name_project_cargo,
        'author_info': f'{username} <{email}>',
        'cargo_description': readme_description,
        'license': license,
        'image_docker_name': image_docker_name,
        'container_name': container_name,
        'directory_name': directory_name,
        'readme_title': readme_title,
        'readme_description': readme_description,
        'readme_overview': readme_overview,
        'readme_author': username,
        'year': year,
        'holder': username
    }

    create_from_template('rust/rust_cargo.txt', os.path.join(root_directory, 'Cargo.toml'), context)
    create_from_template('rust/rust_gitignore.txt', os.path.join(root_directory, '.gitignore'), context)
    create_from_template('rust/rust_readme.txt', os.path.join(root_directory, 'README.md'), context)
    create_from_template('rust/rust_main.txt', os.path.join(root_directory, 'src', 'main.rs'), context)
    create_from_template(license_path, os.path.join(root_directory, 'LICENSE'), context)

    if docker_support:
        create_from_template('rust/rust_dockerfile.txt', os.path.join(root_directory, 'Dockerfile'), context)
        create_from_template('rust/rust_compose.txt', os.path.join(root_directory, 'compose.yaml'), context)

    return root_directory