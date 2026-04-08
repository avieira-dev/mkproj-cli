import os
from utils.file_system import create_directory, create_file

GITIGNORE_CONTENT = """# Binaries for programs and plugins
*.exe
*.exe~
*.dll
*.so
*.dylib

Test binary, built with `go test -c`
*.test

# Output of the go coverage tool, produced by `go test -coverprofile`
*.out

# Dependency directories (remove the comment below to include it)
# vendor/

# IDEs
.idea/
.vscode/

# OS
*~
.DS_Store
Thumbs.db
"""

def setup_go(name, readme_title, readme_description):
    # Standard Go project layout
    create_directory(os.path.join(name, "cmd"))
    create_directory(os.path.join(name, "internal"))
    create_directory(os.path.join(name, "pkg"))

    # Initial code for cmd/main.go
    go_main = f"""package main

import "fmt"

func main() {{
    fmt.Println("Hello from {name}!")
}}
"""
    
    # Create go.mod (simulating 'go mod init')
    go_mod = f"module {name}\n\ngo 1.21\n"

    readme_content = f"""# {readme_title}

> {readme_description}

## Table of Contents
"""

    # Creating files
    create_file(os.path.join(name, "cmd", "main.go"), go_main)
    create_file(os.path.join(name, "go.mod"), go_mod)
    create_file(os.path.join(name, ".gitignore"), GITIGNORE_CONTENT)
    create_file(os.path.join(name, "README.md"), readme_content)