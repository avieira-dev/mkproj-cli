import os
from utils.file_system import create_directory, create_file

GITIGNORE_CONTENT = """# Build 
/target/

# Compiler temporary files
**/*.rs.bk

# IDE / Editor
.vscode/
.idea/
*.vcxproj*
*.sln
*.user
*.filters

# OS
*~
.DS_Store
Thumbs.db
.cache/
"""

MAIN_CONTENT = """fn main() {
    println!("Hello from Rust!");
}
"""

def setup_rust(name, readme_title, readme_description):
    # Replace spaces and hyphens with underscores and convert to lowercase
    name_cargo = name.replace(" ", "_").replace("-", "_").lower()

    # Folders
    create_directory(os.path.join(name, "src"))

    cargo_toml = f"""[package]
name = "{name_cargo}"
version = "0.1.0"
edition = "2021"

[dependencies]
"""
    
    readme_content = f"""# {readme_title}

> {readme_description}

## Table of Contents
"""

    # Files
    create_file(os.path.join(name, ".gitignore"), GITIGNORE_CONTENT)
    create_file(os.path.join(name, "README.md"), readme_content)
    create_file(os.path.join(name, "Cargo.toml"), cargo_toml)
    create_file(os.path.join(name, "src", "main.rs"), MAIN_CONTENT)