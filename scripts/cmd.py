import os
from rename.rename_photos import rename_photos
from rename.rename_screenshots import rename_screenshots


def cmd_rename_photos():
    rename_photos(os.getcwd())
    
def cmd_rename_screenshots():
    rename_screenshots(os.getcwd())
