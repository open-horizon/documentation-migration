from  shutil import ignore_patterns, copytree

ignore_list = [".git", "images", "quick_start", "nl", "api", "cli", "tools"]

def oh_folders(src, dest):
    src = "/home/edeediong/Documents/Open Source/docs"
    dest = "docs/"
    copytree(src, dest, ignore=ignore_patterns(*ignore_list), dirs_exist_ok=True)
