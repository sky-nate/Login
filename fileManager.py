import os
import shutil

def organize_files(source_folder):
    # Create folders for different file types
    image_folder = os.path.join(source_folder, 'Images')
    document_folder = os.path.join(source_folder, 'Documents')
    video_folder = os.path.join(source_folder, 'Videos')
    other_folder = os.path.join(source_folder, 'Other')

    folders = [image_folder, document_folder, video_folder, other_folder]

    # Create folders if they don't exist
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # Iterate through files in the source folder
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Determine the file type based on the extension
            _, extension = os.path.splitext(filename)
            extension = extension.lower()

            # Organize files into respective folders
            if extension in ['.jpg', '.png', '.gif']:
                shutil.move(file_path, image_folder)
            elif extension in ['.doc', '.pdf', '.txt']:
                shutil.move(file_path, document_folder)
            elif extension in ['.mp4', '.avi', '.mkv']:
                shutil.move(file_path, video_folder)
            else:
                shutil.move(file_path, other_folder)

if __name__ == "__main__":
    # Specify the source folder to organize
    source_folder = '/path/to/source/folder'

    # Call the function to organize files
    organize_files(source_folder)
