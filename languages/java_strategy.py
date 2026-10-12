"""
FILE: languages/java_strategy.py
DESCRIPTION: Strategy for bootstrapping Java projects with Maven-style layout.
RESPONSIBILITIES:
  - Dynamically generate deep package structures from user domains
  - Map dots in package names to system-specific directory separators
  - Implement conditional scaffolding for Console or GUI (Swing/MVC) projects
  - Manage Java-specific boilerplate including 'package' declarations
"""

import os
from utils import (
    create_directory,
    create_from_template,
    get_license_path    
)

def get_java_structure(name, user_input, gui_choice, docker_support = False):
    project_clean = name.replace(' ', '').replace('-', '').replace('_', '').lower()

    if '.' in user_input:
        base_package = user_input.replace(' ', '').replace('-', '_')
        full_package_name = f'{base_package}.{project_clean}'
    else:
        user_clean = user_input.replace(' ', '').replace('-', '').replace('_', '')
        full_package_name = f'com.{user_clean}.{project_clean}'

    package_dir_path = full_package_name.replace('.', os.sep)
    full_package_path = os.path.join('src', 'main', 'java', package_dir_path)

    dirs = [
        full_package_path,
        os.path.join('src', 'main', 'resources')
    ]

    if gui_choice == '2':
        dirs.append(os.path.join(full_package_path, 'model'))
        dirs.append(os.path.join(full_package_path, 'view'))
        dirs.append(os.path.join(full_package_path, 'controller'))

    files = [
        os.path.join(full_package_path, 'Main.java'),
        '.gitignore',
        'README.md',
        'LICENSE'
    ]

    if docker_support:
        files.extend(['Dockerfile', 'compose.yaml'])

    return dirs, files

def setup_java(name, readme_title, readme_description, readme_overview, user_input, gui_choice, username, license, year, docker_support = False):
    project_clean = name.replace(' ', '').replace('-', '').replace('_', '').lower()
    root_directory = image_docker_name = container_name = name
    license_path = get_license_path(license)

    if '.' in user_input:
        base_package = user_input.replace(' ', '').replace('-', '_')
        full_package_name = f'{base_package}.{project_clean}'
    else:
        user_clean = user_input.replace(' ', '').replace('-', '').replace('_', '')
        full_package_name = f'com.{user_clean}.{project_clean}'

    # Convert the package (br.com.test) into folders (br/com/test)
    package_dir_path = full_package_name.replace('.', os.sep)
    full_package_path = os.path.join(root_directory, 'src', 'main', 'java', package_dir_path)

    context = {
        'java_package': f'package {full_package_name};',
        'full_package_name': full_package_name,
        'image_docker_name': image_docker_name,
        'container_name': container_name,
        'readme_title': readme_title,
        'readme_description': readme_description,
        'readme_overview': readme_overview,
        'readme_author': username,
        'year': year,
        'holder': username
    }

    create_directory(full_package_path)
    create_directory(os.path.join(root_directory, 'src', 'main', 'resources'))

    if gui_choice == '2':
        for folder in ['model', 'view', 'controller']:
            create_directory(os.path.join(full_package_path, folder))

    create_from_template('java/java_main.txt', os.path.join(full_package_path, 'Main.java'), context)  
    create_from_template('java/java_gitignore.txt', os.path.join(root_directory, '.gitignore'), context)
    create_from_template('java/java_readme.txt', os.path.join(root_directory, 'README.md'), context)
    create_from_template(license_path, os.path.join(root_directory, 'LICENSE'), context)

    if docker_support:
        create_from_template('java/java_dockerfile.txt', os.path.join(root_directory, 'Dockerfile'), context)
        create_from_template('java/java_compose.txt', os.path.join(root_directory, 'compose.yaml'), context)

    return root_directory