import os
import shutil

# Path to the folder you want to organize
folder_path = input("Enter the folder path to organize: ")

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

# Create folders if not exist
for folder_name in file_types.keys():
    folder_dir = os.path.join(folder_path, folder_name)
    if not os.path.exists(folder_dir):
        os.makedirs(folder_dir)

# Organize files
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Get file extension
    _, extension = os.path.splitext(file)

    # Move file to respective folder
    moved = False
    for folder_name, extensions in file_types.items():
        if extension.lower() in extensions:
            shutil.move(file_path, os.path.join(folder_path, folder_name, file))
            moved = True
            break

    # If extension not matched
    if not moved:
        other_folder = os.path.join(folder_path, "Others")
        if not os.path.exists(other_folder):
            os.makedirs(other_folder)
        shutil.move(file_path, os.path.join(other_folder, file))

print("Files organized successfully!")