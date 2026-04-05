import os
from utils.file_system import create_directory, create_file

GITIGNORE_CONTENT = """# Java - Compiled files (Byte-code)
*.class
*.log
*.ctxt

# Package Files (Binaries)
*.jar
*.war
*.nar
*.ear
*.zip
*.tar.gz
*.rar

# Build directories (Maven / Gradle / Bin)
bin/
build/
target/
out/
.gradle/
.m2/

# IDEs and Editors (VS Code, IntelliJ, Eclipse)
.settings/
.project
.classpath
.factorypath
.idea/
*.iml
*.iws
.vscode/

# OS and Crash logs
.DS_Store
Thumbs.db
hs_err_pid*
replay_pid*
"""

README_CONTENT = """# Java Project

> This is your README; configure it according to your goals.
"""

def setup_java(name):
    # Package configuration
    user_part = input("Enter developer/org name (default: user): ").strip().lower() or "user"
    user_clean = user_part.replace("-", "_").replace(" ", "")
    project_clean = name.replace("-", "_").replace(" ", "")

    # Project type
    print("\nSelect Java template:")
    print(" 1) Console Application (Simple)")
    print(" 2) GUI Application (Swing/MVC structure)")
    gui_choice = input("Enter selection (default: 1): ") or "1"

    # Basic paths (Standard: src/main/java/...)
    package_rel_path = os.path.join("src", "main", "java", "com", user_clean, project_clean)
    full_package_path = os.path.join(name, package_rel_path)

    # Creation of the common structure
    create_directory(full_package_path)
    create_directory(os.path.join(name, "src", "main", "resources"))

    # Initial code (Fixed Java syntax and f-string)
    java_content = f"""package com.{user_clean}.{project_clean};

/**
 * Main entry point for the {name} application.
 */
public class Main {{
    public static void main(String[] args) {{
        // Print a welcome message to the console
        System.out.println("Hello from {name}!");
    }}
}}
"""

    # Specific logic
    if gui_choice == "2":
        # Structure for GUI (MVC) - Joining paths correctly
        create_directory(os.path.join(full_package_path, "view"))
        create_directory(os.path.join(full_package_path, "controller"))
        create_directory(os.path.join(full_package_path, "model"))
        
    # Create the Main.java file
    create_file(os.path.join(full_package_path, "Main.java"), java_content)

    # General files
    create_file(os.path.join(name, ".gitignore"), GITIGNORE_CONTENT)
    create_file(os.path.join(name, "README.md"), README_CONTENT)