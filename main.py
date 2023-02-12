import os
import random
import shutil

def random_file_from_folder(folder_path):
    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    return random.choice(files)

def random_file_from_folders(base_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for folder in os.listdir(base_folder):
        folder_path = os.path.join(base_folder, folder)
        if os.path.isdir(folder_path):
            selected_file = random_file_from_folder(folder_path)
            file_name = os.path.basename(selected_file)
            output_file = os.path.join(output_folder, file_name)
            shutil.copy2(selected_file, output_file)
            print("Copied file from '{}' to '{}'".format(selected_file, output_file))

first_folder = "H:\Trashdata\생활 폐기물 이미지\Validation"
first_directories = [d for d in os.listdir(first_folder) if os.path.isdir(os.path.join(first_folder, d))]

print(first_directories)
output_folder = "H:\Trashdata\생활 폐기물 이미지\data_not_augumented"
# Example usage:
for dir_1 in first_directories:
    base_folder = "H:\Trashdata\생활 폐기물 이미지\Validation\{}".format(dir_1)
    output_folder = "H:\Trashdata\생활 폐기물 이미지\data_not_augumented\{}".format(dir_1)
    random_file_from_folders(base_folder, output_folder)