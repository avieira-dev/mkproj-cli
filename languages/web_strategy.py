import os
from utils.file_system import create_directory, create_file

GITIGNORE_CONTENT = """# Dependencies
node_modules/

# Build
dist/
build/

# Environment files
.env
.env.local
.env.*.local

# Logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*

# OS
*~
.DS_Store
Thumbs.db

# Editors / IDEs
.vscode/
.idea/

# Temporary files
*.tmp
*.temp

# Cache
.cache/
.parcel-cache/

# Coverage (tests)
coverage/

# Lock files
package-lock.json
yarn.lock
pnpm-lock.yaml
"""

README_CONTENT = """# Web Project

> This is your README; configure it according to your goals.
"""

INDEX_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{project_name}</title>
    <link rel="stylesheet" href="./assets/css/style.css">
</head>
<body>
    <h1>Project: {project_name}</h1>
    <script src="./assets/js/script.js"></script>
</body>
</html>
"""

CSS_WEB = """/* Global Styles */
html {
    box-sizing: border-box;
}

*,
*::before,
*::after {
    box-sizing: inherit;
    margin: 0;
    padding: 0;
}

body {
    background: #0f172a;
    color: #e5e7eb;
    display: flex;
    justify-items: center;
    align-items: center;
}

h1 {
    font-size: 24px;
    font-weight: bold;
}
"""

SCRIPT_WEB = """// Main JavaScript
alert('Hello, Web Project!');
"""

PACKAGE_JSON = """{{
    "name": "{name}",
    "version": "1.0.0",
    "description": "Web project"
}}
"""

def setup_web(name):
    # Folders
    create_directory(os.path.join(name, "src", "assets", "css"))
    create_directory(os.path.join(name, "src", "assets", "js"))
    create_directory(os.path.join(name, "src", "assets", "images"))
    create_directory(os.path.join(name, "src", "assets", "fonts"))
    create_directory(os.path.join(name, "src", "assets", "favicon"))
    create_directory(os.path.join(name, "src", "assets", "icons"))
    create_directory(os.path.join(name, "src", "components"))
    create_directory(os.path.join(name, "src", "pages"))

    # Files
    create_file(os.path.join(name, "src", "index.html"), INDEX_HTML.format(project_name = name))
    create_file(os.path.join(name, "src", "assets", "css", "style.css"), CSS_WEB)
    create_file(os.path.join(name, "src", "assets", "js", "script.js"), SCRIPT_WEB)
    create_file(os.path.join(name, "README.md"), README_CONTENT)
    create_file(os.path.join(name, ".gitignore"), GITIGNORE_CONTENT)
    create_file(os.path.join(name, "package.json"), PACKAGE_JSON.format(name = name))