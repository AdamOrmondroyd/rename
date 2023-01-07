"""
Rename screenshots to YYMMDD_HHMMSS.ext format
"""

import os
import sys


def rename_screenshots(folder_path):
    filelist = os.listdir(folder_path)

    for oldname in filelist:
        all_spaces = oldname.replace("-", " ").replace(".", " ")
        x = all_spaces.split()
        if x[0] == "Screenshot":
            newname = f"{x[1]}{x[2]}{x[3]}_{x[5]}{x[6]}{x[7]}.png"
            os.rename(oldname, newname)

        if x[0] == "Screen" and x[1] == "Recording":
            newname = f"{x[2]}{x[3]}{x[4]}_{x[6]}{x[7]}{x[8]}.mov"
            os.rename(oldname, newname)


if __name__ == "__main__":
    # If folder path argument exists then use it else current running folder
    if len(sys.argv) < 1:
        folder_path = input_file_path = sys.argv[1]
    else:
        folder_path = os.getcwd()
    rename_screenshots(folder_path)
