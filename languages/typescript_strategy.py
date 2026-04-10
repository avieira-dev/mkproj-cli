import os
from utils.file_system import create_directory, create_file

GITIGNORE_CONTENT = """# Dependencies
node_modules/
/dist
/build

# Environment files
.env
.env.local
.env.*.local

# IDEs and editors
.vscode/
.idea/
*.swp
*.swo

# Operating System and logs
.DS_Store
Thumbs.db
*.log
npm-debug.log*
yarn-debug.log*
"""

TSCONFIG_CONTENT = """{
  "compilerOptions": {
    "target": "ES2020",
    "module": "CommonJS",
    "rootDir": "./src",
    "outDir": "./dist",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
"""

def setup_typescript(name,  readme_title, readme_description):
    safe_name = name.replace(" ", "-").replace("_", "-").lower()

    # Directories
    create_directory(os.path.join(name, "src"))
    create_directory(os.path.join(name, "tests"))

    # Contents of package.json 
    package_json = f"""{{
"name": "{safe_name}",
"version": "1.0.0",
"description": "{readme_description}",
"main": "dist/index.js",
"scripts": {{
    "build": "tsc",
    "dev": "ts-node src/index.ts",
    "start": "node dist/index.js"
}},
"license": "ISC"
    }}
"""
    
    # Content of index.ts
    index_ts = 'console.log("Hello from TypeScript!");\\n'

    # README content
    readme_content = f"""# {readme_title}

> {readme_description}

## Table of Contents
- [Usage](#usage)

## Usage
1. **Install the dependencies:**

    ```bash
    npm install -D typescript ts-node @types/node
    ```

2. Development (Rapid):

    ```bash
    npm run dev
    ```

3. Production (Final):

    ```bash
    npm run build
    npm start
    ```
"""
    
    # Files
    create_file(os.path.join(name, "package.json"), package_json)
    create_file(os.path.join(name, "tsconfig.json"), TSCONFIG_CONTENT)
    create_file(os.path.join(name, "src", "index.ts"), index_ts)
    create_file(os.path.join(name, "README.md"), readme_content)
    create_file(os.path.join(name, ".gitignore"), GITIGNORE_CONTENT)