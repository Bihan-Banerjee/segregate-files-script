import os
import shutil

def organize_files(directory):
    if not os.path.exists(directory):
        print("Directory not found!")
        return
    
    files_moved = 0
    for entry in os.scandir(directory):
        if entry.is_file() and not entry.name.startswith('.'): 
            file_extension = os.path.splitext(entry.name)[1][1:]  
            if file_extension:  
                folder_path = os.path.join(directory, file_extension.lower())  
                os.makedirs(folder_path, exist_ok=True)
                try:
                    shutil.move(entry.path, os.path.join(folder_path, entry.name))
                    print(f"Moved: {entry.name} -> {folder_path}")
                    files_moved += 1
                except shutil.Error as e:
                    print(f"Error moving {entry.name}: {e}")
    print(f"Organization complete. {files_moved} files moved.")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ").strip()
    if os.path.isdir(folder_path):
        organize_files(folder_path)
    else:
        print("Invalid directory path.")
