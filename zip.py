from zipfile import ZipFile
import os

# with compression password
def zip_folder(folder_path, zip_name):
    with ZipFile(zip_name, 'w') as zip_file:
        for foldername, subfolders, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                arcname = os.path.relpath(file_path, folder_path)
                zip_file.write(file_path, arcname)
        



def find_folder_with_string(base_path, target_string):
    matching_folders = [os.path.join(base_path, foldername)
                        for foldername in os.listdir(base_path)
                        if os.path.isdir(os.path.join(base_path, foldername)) and target_string in foldername]
                        

    return matching_folders

# # Example usage
# base_directory = "./"
# target_substring = "_inst"

# result = find_folder_with_string(base_directory, target_substring)

# for i in result:
#     folder_to_zip = i
#     zip_filename =i +".zip"
#     zip_folder(folder_to_zip, zip_filename)

def create_backup_folder():
    backup_folder = "./backup"  
    os.makedirs(backup_folder, exist_ok=True)
    return backup_folder


def copy_folders(src_folder, dest_folder, folders_to_copy):
     for folder in folders_to_copy:
        src_path = os.path.join(src_folder, folder)
        dest_path = os.path.join(dest_folder, folder)

        try:
            shutil.copytree(src_path, dest_path)
            print(f"Folder '{folder}' copied successfully.")
        except Exception as e:
            print(f"Error copying folder '{folder}': {e}")