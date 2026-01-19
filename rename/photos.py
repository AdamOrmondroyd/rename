"""
Rename images with date photo taken
YYMMDD_HHMMSS.ext
"""

import os
import sys
import time

# Set list of valid file extensions
valid_extensions = [".jpg", ".jpeg", ".png"]
valid_extensions += [".gif", ".tiff", ".webp"]
valid_extensions += [".JPG", ".JPEG"]
valid_extensions += [".mp4"]
valid_extensions += [".heic", ".HEIC", ".heif", ".HEIF"]


def rename_photos(folder_path):
    # Get all files from folder
    file_names = os.listdir(folder_path)

    # For each file
    for file_name in file_names:
        print("------------------------------------------------")

        # get the file extension
        file_ext = os.path.splitext(file_name)[1]

        # skip if the file does not have a valid file extension
        if file_ext not in valid_extensions:
            print(f"invalid extension {file_ext}")
            continue

        # old file path
        old_file_path = os.path.join(folder_path, file_name)

        print(old_file_path)
        print(os.stat(old_file_path).st_mtime)
        print(
            time.strftime(
                "%Y%m%d_%H%M%S", time.localtime(os.stat(old_file_path).st_mtime)
            )
        )
        new_file_path = os.path.join(
            folder_path,
            str(
                time.strftime(
                    "%Y%m%d_%H%M%S", time.localtime(os.stat(old_file_path).st_mtime)
                )
            )
            + file_ext,
        )
        print(new_file_path)
        os.rename(old_file_path, new_file_path)


if __name__ == "__main__":
    # If folder path argument exists then use it else current running folder
    if len(sys.argv) < 1:
        folder_path = input_file_path = sys.argv[1]
    else:
        folder_path = os.getcwd()
    rename_photos(folder_path)
