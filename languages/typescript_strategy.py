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

def setup_typescript(name,  readme_title, readme_description):
    project_name = name.replace(" ", "-").replace("_", "-").lower()

    # Create directories
    for folder in ["src", "tests"]:
        create_directory(os.path.join(name, folder))

    # Data to fill in the templates
    context = {
        "project_name": project_name,
        "description": readme_description,
        "readme_title": readme_title,
        "readme_description": readme_description    
    }
    
    # Create files
    create_from_template("typescript/ts_config.txt", os.path.join(name, "tsconfig.json"), context)
    create_from_template("typescript/ts_package.txt", os.path.join(name, "package.json"), context)
    create_from_template("typescript/ts_gitignore.txt", os.path.join(name, ".gitignore"), context)
    create_from_template("typescript/ts_readme.txt", os.path.join(name, "README.md"), context)
    create_from_template("typescript/ts_index.txt", os.path.join(name, "src", "index.ts"), context)