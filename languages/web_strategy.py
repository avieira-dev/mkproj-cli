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
from utils.file_system import create_directory, create_from_template

def setup_web(name, readme_title, readme_description, username):
    project_name_json = name.replace(" ", "-").replace("_", "-").lower()
    project_name_index = " ".join(word.capitalize() for word in name.replace("-", " ").replace("_", " ").split())

    # Create directories
    for folder in ["src/assets/css", "src/assets/js", "src/assets/images", "src/assets/fonts", "src/assets/favicon", "src/assets/icons", "src/components", "src/pages"]:
        create_directory(os.path.join(name, folder))

    # Data to fill in the templates
    context = {
        "project_name_json": project_name_json,
        "username": username,
        "project_name_index": project_name_index,
        "readme_title": readme_title,
        "readme_description": readme_description
    }

    # Create files
    create_from_template("web/web_index.txt", os.path.join(name, "src", "index.html"), context)
    create_from_template("web/web_style.txt", os.path.join(name, "src", "assets", "css", "style.css") , context)
    create_from_template("web/web_javascript.txt", os.path.join(name, "src", "assets", "js", "script.js"), context)
    create_from_template("web/web_readme.txt", os.path.join(name, "README.md"), context)
    create_from_template("web/web_gitignore.txt", os.path.join(name, ".gitignore"), context)
    create_from_template("web/web_json.txt", os.path.join(name, "package.json"), context)