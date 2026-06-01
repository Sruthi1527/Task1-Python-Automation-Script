# ==========================================
# IMPORT MODULES
# ==========================================

import os
import shutil
import logging


# ==========================================
# LOGGING CONFIGURATION
# ==========================================

logging.basicConfig(
    filename='automation_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)


# ==========================================
# FUNCTION TO SORT FILES
# ==========================================

def sort_files(folder_path):

    try:

        # Check folder exists
        if not os.path.exists(folder_path):

            print("Folder does not exist")

            return

        # Get all files
        files = os.listdir(folder_path)

        for file in files:

            file_path = os.path.join(folder_path, file)

            # Skip folders
            if os.path.isdir(file_path):

                continue

            # Get extension
            extension = file.split('.')[-1]

            # Create extension folder
            extension_folder = os.path.join(folder_path, extension)

            if not os.path.exists(extension_folder):

                os.makedirs(extension_folder)

            # Move file
            shutil.move(file_path, os.path.join(extension_folder, file))

            print(f"Moved: {file}")

            logging.info(f"Moved file: {file}")

        print("\nFiles Sorted Successfully")

    except Exception as e:

        print("Error:", e)

        logging.error(f"Error: {e}")


# ==========================================
# FUNCTION TO RENAME FILES
# ==========================================

def rename_files(folder_path):

    try:

        files = os.listdir(folder_path)

        count = 1

        for file in files:

            file_path = os.path.join(folder_path, file)

            if os.path.isdir(file_path):

                continue

            extension = file.split('.')[-1]

            new_name = f"renamed_file_{count}.{extension}"

            new_path = os.path.join(folder_path, new_name)

            os.rename(file_path, new_path)

            print(f"Renamed: {file} → {new_name}")

            logging.info(f"Renamed file: {file} to {new_name}")

            count += 1

        print("\nFiles Renamed Successfully")

    except Exception as e:

        print("Error:", e)

        logging.error(f"Error: {e}")


# ==========================================
# MAIN PROGRAM
# ==========================================

print("========== PYTHON AUTOMATION SCRIPT ==========")

print("\n1. Sort Files")
print("2. Rename Files")

choice = input("\nEnter Your Choice: ")

folder = input("Enter Folder Path: ")

if choice == '1':

    sort_files(folder)

elif choice == '2':

    rename_files(folder)

else:

    print("Invalid Choice")