"""
FILE: utils/prompter.py
DESCRIPTION: Handle user interaction via terminal prompts.
RESPONSIBILITIES:
  - Manage customization of README files and strategy-specific configs
  - Automate Git repository initialization and initial commit
  - Ensure consistent terminal output styling for user inputs
"""

import os
from utils.colors import Colors
from utils.terminal_commands import run_command

def get_readme_data(default_name):
    print(f"{Colors.PURPLE}?{Colors.END} {Colors.BOLD}Customize README?{Colors.END} {Colors.DIM}(y/n){Colors.END}", end=" ")
    if input(Colors.END).lower().strip() == "y":
        title = input(f"  {Colors.DIM}↳ Title [{default_name}]: {Colors.END}").strip() or default_name
        desc = input(f"  {Colors.DIM}↳ Description: {Colors.END}").strip() or "Project created with mkproj-cli."
        return title, desc
    return default_name, "Project created with mkproj-cli."

def get_module_go(default_name):
    print(f"\n{Colors.PURPLE}?{Colors.END} {Colors.BOLD}Use GitHub as Go module?{Colors.END} {Colors.DIM}(y/n){Colors.END}", end=" ")
    if input(Colors.END).lower().strip() == "y":
        return input(f"  {Colors.DIM}↳ Repo path: {Colors.END}").replace("https://", "").strip() or default_name
    return default_name

def get_java_data():
    user = "user"
    print(f"\n{Colors.PURPLE}?{Colors.END} {Colors.BOLD}Developer Domain?{Colors.END} {Colors.DIM}(y/n){Colors.END}", end=" ")
    if input(Colors.END).lower().strip() == "y":
        user = input(f"  {Colors.DIM}↳ Domain (ex: com.app): {Colors.END}").strip().lower() or "user"

    print(f"\n{Colors.PURPLE}?{Colors.END} {Colors.BOLD}Select Java template?{Colors.END} {Colors.DIM}(y/n){Colors.END}", end=" ")
    choice = "1"
    if input(Colors.END).lower().strip() == "y":
        print(f" {Colors.DIM}1) Console  2) GUI (Swing){Colors.END}")
        choice = input(f"  {Colors.DIM}↳ Selection: {Colors.END}").strip() or "1"
    return user, choice

def git_automation(name):
    print(f"\n{Colors.PURPLE}?{Colors.END} {Colors.BOLD}Initialize Git repository?{Colors.END} {Colors.DIM}(y/n){Colors.END}", end=" ")
    if input(Colors.END).lower().strip() == "y":
        path = os.path.abspath(name)
        if run_command(["git", "init"], path):
            run_command(["git", "add", "."], path)
            run_command(["git", "commit", "-m", "chore: initial commit (mkproj)"], path)
            print(f"  {Colors.DIM}↳{Colors.END} {Colors.GREEN} Git ready!{Colors.END}")
            return True
        print(f"  {Colors.DIM}↳{Colors.END} {Colors.RED} Git failed.{Colors.END}")
    return False

def add_license():
    print(f"\n{Colors.PURPLE}?{Colors.END} {Colors.BOLD}Add a license to the project?{Colors.END} {Colors.DIM}(y/n){Colors.END}", end=" ")

    choice = "4"

    if input(Colors.END).lower().strip() == "y":
        print(f"  {Colors.DIM}1) MIT  2) Apache 2.0  3) GNU GPL v3.0  4) None{Colors.END}")
        choice = input(f"  {Colors.DIM}↳ Selection [1-4]: {Colors.END}").strip() or "1"

    return choice