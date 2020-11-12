from  shutil import ignore_patterns, copytree


ignore_list = [".git", "images", "quick_start", "nl", "api", "cli", "tools"]

def oh_folders():
    src = "/home/edeediong/Documents/Open Source/docs"
    dest = "/home/edeediong/transpose/"
    copytree(src, dest, ignore=ignore_patterns(*ignore_list))
