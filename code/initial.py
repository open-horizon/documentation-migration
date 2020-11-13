from  shutil import ignore_patterns, copytree

ignore_list = [".git", "images", "quick_start", "nl", "api", "cli", "tools"]

def oh_folders(*args):
    src = "/home/edeediong/Documents/Open Source/docs"
    dest = "docs/"
    copytree(src, dest, ignore=ignore_patterns(*ignore_list), dirs_exist_ok=True)


with open("docs/SUMMARY.md", "r+") as opened_file:
    summary = opened_file.readlines()

    for line in summary:
        if any(ext in line for ext in ignore_list):
            print(line)
            summary.remove(line) #TODO figure out why this isn't exactly working
