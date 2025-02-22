import os
import datetime

def rename_files(folder_path, prefix="file", file_extension=None, use_timestamp=False):
    """Rename files in the folder with a prefix and optional timestamp, filtering by extension."""
    if not os.path.exists(folder_path):
        print("❌ Folder does not exist!")
        return

    files = sorted(os.listdir(folder_path))  # Sort files alphabetically

    # Filter files based on extension if specified
    if file_extension:
        files = [f for f in files if f.endswith(file_extension)]

    if not files:
        print("⚠ No files found to rename!")
        return

    print(f"Found {len(files)} files to rename.\n")

    for index, filename in enumerate(files, start=1):
        file_ext = os.path.splitext(filename)[1]  # Get file extension
        timestamp = datetime.datetime.now().strftime("%Y%m%d") if use_timestamp else ""
        new_name = f"{prefix}_{timestamp}_{index}{file_ext}" if use_timestamp else f"{prefix}_{index}{file_ext}"

        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)

        # Ask for confirmation before renaming
        print(f"Rename: {filename} ➝ {new_name} ? (y/n): ", end="")
        choice = input().strip().lower()
        if choice == "y":
            os.rename(old_path, new_path)
            print(f"✅ Renamed: {filename} ➝ {new_name}")
        else:
            print(f"❌ Skipped: {filename}")

# Example usage
folder = "C:/Users/HP/Desktop/File_Organizer/FilesToRename" # Change this to your folder path
rename_files(folder, prefix="document", file_extension=".txt", use_timestamp=True)
