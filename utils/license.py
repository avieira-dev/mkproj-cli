"""
FILE: utils/license.py
DESCRIPTION: Maps user-selected license names to their respective template file paths.
RESPONSIBILITIES:
  - Return the correct relative path for MIT, Apache, or GNU GPL licenses
  - Fallback to the explanation template for unhandled or 'None' licenses
"""

def get_license_path(license_name):
    if license_name == 'MIT':
        return 'licenses/mit.txt'
    elif license_name == 'Apache':
        return 'licenses/apache.txt'
    elif license_name == 'GNU GPL':
        return 'licenses/gpl.txt'
    else:
        return 'licenses/explanation.txt'