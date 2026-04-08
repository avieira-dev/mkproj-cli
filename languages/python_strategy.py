import os
from utils.file_system import create_directory, create_file

GITIGNORE_CONTENT = """# Compiled files
__pycache__/
*.py[cod]
*$py.class
*.so
*.pyd

# Virtual environments
.venv/
venv/
ENV/
env/
.env

# Distribution and packaging
dist/
build/
eggs/
.eggs/
*.egg-info/
*.egg
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/
.tox/

# IDEs and editors
.vscode/
.idea/
*.swp
*.swo

# Operating System and logs
.DS_Store
Thumbs.db
*.log
"""

def setup_python(name, readme_title, readme_description):
    # Folders
    create_directory(os.path.join(name, "src", "app"))
    create_directory(os.path.join(name, "tests"))
    create_directory(os.path.join(name, "docs"))

    readme_content = f"""# {readme_title}

> {readme_description}

## Table of Contents
"""

    # Files
    create_file(os.path.join(name, "src", "app", "main.py"), 'print("Hello World")\n')
    create_file(os.path.join(name, ".gitignore"), GITIGNORE_CONTENT)
    create_file(os.path.join(name, "README.md"), readme_content)
