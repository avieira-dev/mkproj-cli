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
from utils.file_system import create_directory, create_from_template

def setup_java(name, readme_title, readme_description, user_input, gui_choice):
    project_clean = name.replace(" ", "").replace("-", "").replace("_", "").lower()

    if "." in user_input:
        base_package = user_input.replace(" ", "").replace("-", "_")
        full_package_name = f"{base_package}.{project_clean}"
    else:
        user_clean = user_input.replace(" ", "").replace("-", "").replace("_", "")
        full_package_name = f"com.{user_clean}.{project_clean}"

    # Convert the package (br.com.test) into folders (br/com/test)
    package_dir_path = full_package_name.replace(".", os.sep)
    full_package_path = os.path.join(name, "src", "main", "java", package_dir_path)

    # Data to fill in the templates
    context = {
        "java_package": f"package {full_package_name};",
        "readme_title": readme_title,
        "readme_description": readme_description
    }

    # Creation of folders
    create_directory(full_package_path)
    create_directory(os.path.join(name, "src", "main", "resources"))

    # Specific logic for MVC
    if gui_choice == "2":
        for folder in ["model", "view", "controller"]:
            create_directory(os.path.join(full_package_path, folder))
        
    # Creation of files from templates
    create_from_template("java/java_main.txt", os.path.join(full_package_path, "Main.java"), context)  
    create_from_template("java/java_gitignore.txt", os.path.join(name, ".gitignore"), context)
    create_from_template("java/java_readme.txt", os.path.join(name, "README.md"), context)