# File Organizer Script

A simple Python script to organize files in a directory into subfolders based on their file extensions.

## Features
- Automatically creates subfolders for each file extension.
- Moves files into their corresponding subfolders.
- Handles edge cases like hidden files and duplicate filenames.

## Usage
1. Clone the repository:

   git clone https://github.com/Bihan-Banerjee/segregate-files-script.git

2. Navigate to the project directory:

   cd file-organizer

3. Run the script:
 
   python segregate_files.py

4. Enter the path to the directory you want to organize when prompted.

## Example
  
  If your directory contains:

  file1.txt
  
  file2.jpg
  
  file3.png
  
  After running the script, it will be organized as:

  /txt/file1.txt
  
  /jpg/file2.jpg
  
  /png/file3.png
