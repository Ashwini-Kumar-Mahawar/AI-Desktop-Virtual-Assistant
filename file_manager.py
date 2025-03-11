import os

def open_folder(folder_name):
    # Define paths for common folders
    folders = {
        "documents": os.path.expanduser("~/Documents"),
        "downloads": os.path.expanduser("~/Downloads"),
        "movies": os.path.expanduser("~/D:/movies"),
    }

    # Check if the folder name is recognized
    if folder_name in folders:
        # Open the folder using the default file manager
        os.startfile(folders[folder_name])
        print(f"Opening {folder_name} folder...")
    else:
        print("Folder not recognized.")