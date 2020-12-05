from shutil import ignore_patterns, copytree
from datetime import datetime, date
import os

ignore_list = [".git", "quick_start", "nl", "api", "cli", "tools", "integration.md", "offline_installation.md", "conrefs.yml"]

def oh_folders(*args):
    """Copies the folder from the source directory into a docs folder eliminating commercial information."""
    src = "/home/edeediong/Documents/Open Source/docs"
    dest = "docs/"
    copytree(src, dest, ignore=ignore_patterns(*ignore_list), dirs_exist_ok=True)

def edit_summary():
    """Remove references to elements in the ignore list."""
    with open("docs/SUMMARY.md", "r") as opened_file:
        summary = opened_file.readlines()

    with open("docs/SUMMARY.md", "w") as opened_file:
        for line in summary:
            if not any(ext in line for ext in ignore_list):
                opened_file.write(line)

def update_date():
    directory = "docs/"
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            a_file = open(filename, "r") #open the file and read
            content = a_file.readlines()

            content[3] = f"years: {datetime.now().year}\n"
            content[4] = f'lastupdated: "{date.today()}"\n'
            a_file = open(filename, "w") #open the same file and overrite line3 & 4
            a_file.writelines(content)

            a_file.close()

if __name__ == '__main__':
    oh_folders()
    edit_summary()
    update_date()