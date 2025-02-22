import os
import shutil

# Define folder paths
DOWNLOADS_FOLDER = r"C:\Users\HP\Desktop"  # Change this to the folder you want to organize

# File type categories
FILE_CATEGORIES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".java", ".cpp", ".html", ".css", ".js"]
}

# Function to organize files
def organize_files():
    for filename in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, filename)

        if os.path.isfile(file_path):  # Check if it's a file
            file_ext = os.path.splitext(filename)[1]  # Get file extension

            for category, extensions in FILE_CATEGORIES.items():
                if file_ext.lower() in extensions:
                    category_folder = os.path.join(DOWNLOADS_FOLDER, category)
                    os.makedirs(category_folder, exist_ok=True)  # Create category folder if it doesn't exist
                    shutil.move(file_path, category_folder)  # Move file
                    print(f"Moved: {filename} → {category_folder}")
                    break

if __name__ == "__main__":
    organize_files()
    print("✅ File organization completed!")
