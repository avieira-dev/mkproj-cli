import os
from utils.file_system import create_directory, create_from_template

def setup_rust(name, readme_title, readme_description, username, email, license):
    name_cargo = name.replace(" ", "_").replace("-", "_").lower()

    # Crete directory
    create_directory(os.path.join(name, "src"))

    # Data to fill in the templates
    context = {
        "name_project": name_cargo,
        "author_info": f"{username} <{email}>",
        "description": readme_description,
        "license": license,
        "readme_title": readme_title,
        "readme_description": readme_description
    }

    # Create files
    create_from_template("rust/rust_cargo.txt", os.path.join(name, "Cargo.toml"), context)
    create_from_template("rust/rust_gitignore.txt", os.path.join(name, ".gitignore"), context)
    create_from_template("rust/rust_readme.txt", os.path.join(name, "README.md"), context)
    create_from_template("rust/rust_main.txt", os.path.join(name, "src", "main.rs"), context)