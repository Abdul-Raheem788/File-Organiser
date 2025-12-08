import os
import shutil

# ------------------------------
# 📌 Ask user for folder to organize
# ------------------------------
folder_path = input("Enter the folder path you want to organize: ").strip()

# Validate folder path
if not os.path.isdir(folder_path):
    print("❌ Invalid folder path.")
    exit()

# ------------------------------
# 📌 Define file categories
# ------------------------------
file_types = {
    "Documents": [".pdf", ".pptx", ".docx", ".txt"],
    "Images": [".png", ".jpg", ".jpeg"],
    "Music": [".mp3", ".wav"],
    "Code": [".py", ".html", ".js", ".css"],
}

# ------------------------------
# 📌 Determine folder for a given file extension
# ------------------------------
def get_target_folder(extension):
    for folder_name, extensions in file_types.items():
        if extension.lower() in extensions:
            return folder_name
    return "Others"  # If no category matches

# ------------------------------
# 📌 Logging system
# ------------------------------
log_file_path = os.path.join(folder_path, "Organizer_Log.txt")

def log(message):
    """Write message into log file"""
    with open(log_file_path, "a", encoding="utf-8") as logfile:
        logfile.write(message + "\n")

# ------------------------------
# 📌 Make sure folder exists
# ------------------------------
def ensure_folder(path):
    os.makedirs(path, exist_ok=True)

# ------------------------------
# 📌 Process each file
# ------------------------------
files = os.listdir(folder_path)

for file in files:
    abs_path = os.path.join(folder_path, file)

    # Skip hidden files
    if file.startswith("."):
        continue

    # Skip our own log file
    if file == "Organizer_Log.txt":
        continue

    # Skip directories (we only move files)
    if os.path.isdir(abs_path):
        continue

    # Extract extension
    filename, ext = os.path.splitext(file)

    # Determine target folder
    target_folder = get_target_folder(ext)
    target_path = os.path.join(folder_path, target_folder)

    # Create folder if missing
    ensure_folder(target_path)

    # Move file
    shutil.move(abs_path, os.path.join(target_path, file))

    # Log the operation
    log(f"{file}  →  {target_folder}")

# ------------------------------
# 📌 Finish
# ------------------------------
print("✅ Organized successfully! Check the Organizer_Log.txt file for details.")