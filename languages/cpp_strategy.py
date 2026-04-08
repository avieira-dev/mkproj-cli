import os
from utils.file_system import create_directory, create_file

GITIGNORE_CONTENT = """# Build directories
build/
bin/
out/
dist/
cmake-build-*/

# CMake files
CMakeFiles/
CMakeCache.txt
cmake_install.cmake
Makefile
install_manifest.txt

# Useful for tooling (ignore if not using clangd)
compile_commands.json

# Compilation artifacts
*.o
*.obj
*.a
*.lib

# Shared libraries / executables
*.so
*.so.*
*.dll
*.dylib
*.exe
*.out
*.app
*.elf

# Debug / temp
*.log
*.tmp
*.temp
*.stackdump

# Coverage / profiling
*.gcda
*.gcno
*.gcov
coverage/

# Dependencies (common in C++)
/vcpkg_installed/
/conan/

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

MAIN_CONTENT = """#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
"""

def setup_cpp(name, readme_title, readme_description):
    class_name = "".join(p.capitalize() for p in name.replace("_", "-").split("-"))

    # Folders
    create_directory(os.path.join(name, "src", "core"))
    create_directory(os.path.join(name, "include", "core"))
    create_directory(os.path.join(name, "build"))
    create_directory(os.path.join(name, "tests"))
    create_directory(os.path.join(name, "external"))
    create_directory(os.path.join(name, "assets"))
    create_directory(os.path.join(name, "docs"))

    cmake_content = f"""cmake_minimum_required(VERSION 3.20)
project({class_name} VERSION 0.1.0)

set(CMAKE_CXX_STANDARD 17)

add_executable(${{PROJECT_NAME}} src/main.cpp)
"""
    
    readme_content = f"""# {readme_title}

> {readme_description}

## Table of Contents
"""

    # Files
    create_file(os.path.join(name, "CMakeLists.txt"), cmake_content)
    create_file(os.path.join(name, "README.md"), readme_content)
    create_file(os.path.join(name, ".gitignore"), GITIGNORE_CONTENT)
    create_file(os.path.join(name, "src", "main.cpp"), MAIN_CONTENT)