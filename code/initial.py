from shutil import ignore_patterns, copytree
from datetime import datetime, date

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



a_file = open("docs/hub/hub.md", "r")
content = a_file.readlines()

content[3] = f"years: {datetime.now().year}\n"
content[4] = f'lastupdated: "{date.today()}"\n'
a_file = open("docs/hub/hub.md", "w")
a_file.writelines(content)

a_file.close()

if __name__ == '__main__':
    oh_folders()
    edit_summary()
