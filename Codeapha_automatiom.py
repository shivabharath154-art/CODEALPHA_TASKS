import os
import shutil
import glob

def organize_jpg_files(source_dir, destination_dir="jpg_files_organized"):
    """
    Moves all .jpg and .jpeg files from a source directory to a
    destination directory.

    Args:
        source_dir (str): Directory to scan for image files
        destination_dir (str): Folder name where images will be moved
    """

    
    full_destination_path = os.path.join(source_dir, destination_dir)

    
    if not os.path.exists(full_destination_path):
        os.makedirs(full_destination_path)