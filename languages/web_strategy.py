"""
FILE: languages/web_strategy.py
DESCRIPTION: Strategy for bootstrapping Web projects (HTML/CSS/JS).
RESPONSIBILITIES:
  - Create a standard frontend directory structure (assets, components, pages)
  - Format project names for specific contexts (kebab-case for JSON, Title Case for HTML)
  - Map and inject user data into Web-specific templates
  - Generate core files: index.html, style.css, script.js, and package.json
"""

import os
from utils import (
    create_directory,
    create_from_template,
    get_license_path    
)

def get_web_structure(docker_support):
    dirs = [
        'src/assets/css',
        'src/assets/js',
        'src/assets/images',
        'src/assets/favicon',
        'src/components',
        'src/pages'
    ]

    files = [
        'src/index.html',
        'src/assets/css/style.css',
        'src/assets/js/script.js',
        'README.md',
        '.gitignore',
        'package.json',
        'LICENSE'    
    ]

    if docker_support:
        files.extend(['Dockerfile', 'compose.yaml'])

    return dirs, files

def setup_web(name, readme_title, readme_description, readme_overview, username, license, year, docker_support = False):
    root_directory = project_name_json = image_docker_name = container_name = name
    project_index_title = ' '.join(word.capitalize() for word in name.replace('-', ' ').replace('_', ' ').split())
    license_path = get_license_path(license)

    for folder in ['src/assets/css', 'src/assets/js', 'src/assets/images', 'src/assets/favicon', 'src/components', 'src/pages']:
        create_directory(os.path.join(root_directory, folder))

    context = {
        'project_name_json': project_name_json,
        'username': username,
        'project_index_title': project_index_title,
        'image_docker_name': image_docker_name,
        'container_name': container_name,
        'readme_title': readme_title,
        'readme_description': readme_description,
        'readme_overview': readme_overview,
        'readme_author': username,
        'year': year,
        'holder': username
    }

    create_from_template('web/web_index.txt', os.path.join(root_directory, 'src', 'index.html'), context)
    create_from_template('web/web_style.txt', os.path.join(root_directory, 'src', 'assets', 'css', 'style.css') , context)
    create_from_template('web/web_javascript.txt', os.path.join(root_directory, 'src', 'assets', 'js', 'script.js'), context)
    create_from_template('web/web_readme.txt', os.path.join(root_directory, 'README.md'), context)
    create_from_template('web/web_gitignore.txt', os.path.join(root_directory, '.gitignore'), context)
    create_from_template('web/web_json.txt', os.path.join(root_directory, 'package.json'), context)
    create_from_template(license_path, os.path.join(root_directory, 'LICENSE'), context)

    if docker_support:
        create_from_template('web/web_dockerfile.txt', os.path.join(root_directory, 'Dockerfile'), context)
        create_from_template('web/web_compose.txt', os.path.join(root_directory, 'compose.yaml'), context)

    return root_directory