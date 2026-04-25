"""
FILE: utils/file_system.py
DESCRIPTION: Core utility for file and directory manipulation.
RESPONSIBILITIES:
  - Create project directory structures recursively
  - Load and parse project templates using string substitution
  - Write final processed content to disk with UTF-8 encoding
  - Resolve absolute paths for templates regardless of execution context
"""

import os
from pathlib import Path
from string import Template

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def create_from_template(template_rel_path, target_path, variables):
    base_dir = Path(__file__).resolve().parent.parent
    full_template_path = base_dir / "templates" / template_rel_path

    if not full_template_path.exists():
        raise FileNotFoundError(f"Template not found: {full_template_path}")

    content = full_template_path.read_text(encoding='utf-8')
    template = Template(content)  
    final_output = template.substitute(variables)

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(final_output)