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
from utils.file_system import create_directory, create_from_template

def setup_typescript(name, readme_title, readme_description, readme_overview, username, license, year, docker_support = False):
    root_directory = project_name_ts = image_docker_name = container_name = name.replace(" ", "-").replace("_", "-").lower()

    license_path = "licenses/mit.txt" if license == "MIT" else \
                   "licenses/apache.txt" if license == "Apache" else \
                   "licenses/gpl.txt" if license == "GNU GPL" else "licenses/explanation.txt"

    # Create directories
    for folder in ["src", "tests"]:
        create_directory(os.path.join(root_directory, folder))

    # Data to fill in the templates
    context = {
        "image_docker_name": image_docker_name,
        "container_name": container_name,
        "project_name_ts": project_name_ts,
        "ts_description": readme_description,
        "readme_title": readme_title,
        "readme_description": readme_description,
        "readme_overview": readme_overview,
        "readme_author": username,
        "year": year,
        "holder": username
    }
    
    # Create files
    create_from_template("typescript/ts_config.txt", os.path.join(root_directory, "tsconfig.json"), context)
    create_from_template("typescript/ts_package.txt", os.path.join(root_directory, "package.json"), context)
    create_from_template("typescript/ts_gitignore.txt", os.path.join(root_directory, ".gitignore"), context)
    create_from_template("typescript/ts_readme.txt", os.path.join(root_directory, "README.md"), context)
    create_from_template("typescript/ts_index.txt", os.path.join(root_directory, "src", "index.ts"), context)
    create_from_template(license_path, os.path.join(root_directory, "LICENSE"), context)

    if docker_support:
        create_from_template("typescript/ts_dockerfile.txt", os.path.join(root_directory, "Dockerfile"), context)
        create_from_template("typescript/ts_compose.txt", os.path.join(root_directory, "compose.yaml"), context)

    return root_directory