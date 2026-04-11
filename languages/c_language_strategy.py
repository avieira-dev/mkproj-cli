import os
from utils.file_system import create_directory, create_from_template

def setup_c(name, readme_title, readme_description):
    class_name = "".join(p.capitalize() for p in name.replace("_", "-").split("-"))

    # Create directories
    for folder in ["include", "src", "tests", "build", "docs"]:
        create_directory(os.path.join(name, folder))

    # Data to fill in the templates
    context = {
        "project_name": class_name,
        "readme_title": readme_title,
        "readme_description": readme_description  
    }

    # Create files
    create_from_template("c_language/c_cmake.txt", os.path.join(name, "CMakeLists.txt"), context)
    create_from_template("c_language/c_gitignore.txt", os.path.join(name, ".gitignore"), context)
    create_from_template("c_language/c_readme.txt", os.path.join(name, "README.md"), context)
    create_from_template("c_language/c_main.txt", os.path.join(name, "src", "main.c"), context)