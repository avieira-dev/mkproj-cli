import os
from utils.file_system import create_directory, create_file

GITIGNORE_CONTENT = """# Build directories
build/
bin/
out/
cmake-build-*/

# CMake files
CMakeFiles/
CMakeCache.txt
cmake_install.cmake
Makefile
install_manifest.txt

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
*.elf

# Debug / temp
*.log
*.tmp
*.temp
*.stackdump

# Coverage
*.gcda
*.gcno
*.gcov
coverage/

# Editors / IDEs
.vscode/
.idea/

# OS
*~
.DS_Store
Thumbs.db
"""

README_CONTENT = """# C Language Project

> This is your README; configure it according to your goals.
"""

MAIN_CONTENT = """#include <stdio.h>

int main(void) {
    printf("Hello, World!");
    return 0;
}
"""

def setup_c(name):
    class_name = "".join(p.capitalize() for p in name.replace("_", "-").split("-"))

    #Folders
    create_directory(os.path.join(name, "include"))
    create_directory(os.path.join(name, "src"))
    create_directory(os.path.join(name, "tests"))
    create_directory(os.path.join(name, "build"))
    create_directory(os.path.join(name, "docs"))

    cmake_content = f"""cmake_minimum_required(VERSION 3.20)
project({class_name} VERSION 0.1.0 LANGUAGES C)

set(CMAKE_C_STANDARD 17)

add_executable(${{PROJECT_NAME}} src/main.c)
"""
    
    #Files
    create_file(os.path.join(name, "CMakeLists.txt"), cmake_content)
    create_file(os.path.join(name, "README.md"), README_CONTENT)
    create_file(os.path.join(name, ".gitignore"), GITIGNORE_CONTENT)
    create_file(os.path.join(name, "src", "main.c"), MAIN_CONTENT)