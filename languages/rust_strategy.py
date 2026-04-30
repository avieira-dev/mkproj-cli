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
from utils.file_system import create_directory, create_from_template

def setup_rust(name, readme_title, readme_description, username, email, license, year):
    name_cargo = name.replace(" ", "_").replace("-", "_").lower()

    license_path = "licenses/mit.txt" if license == "MIT" else \
                   "licenses/apache.txt" if license == "Apache" else \
                   "licenses/gpl.txt" if license == "GNU GPL" else "licenses/explanation.txt"

    # Crete directory
    create_directory(os.path.join(name, "src"))

    # Data to fill in the templates
    context = {
        "name_project": name_cargo,
        "author_info": f"{username} <{email}>",
        "description": readme_description,
        "license": license,
        "readme_title": readme_title,
        "readme_description": readme_description,
        "year": year,
        "holder": username
    }

    # Create files
    create_from_template("rust/rust_cargo.txt", os.path.join(name, "Cargo.toml"), context)
    create_from_template("rust/rust_gitignore.txt", os.path.join(name, ".gitignore"), context)
    create_from_template("rust/rust_readme.txt", os.path.join(name, "README.md"), context)
    create_from_template("rust/rust_main.txt", os.path.join(name, "src", "main.rs"), context)
    create_from_template(license_path, os.path.join(name, "LICENSE"), context)