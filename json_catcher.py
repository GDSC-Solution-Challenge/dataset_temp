import os

def get_labeled_json_files(base_folder):
    labeled_json_files = []

    for root, dirs, files in os.walk(base_folder):
        for file in files:
            if file.endswith(".json"):
                sample_file = file.replace(".json", ".jpg")
                sample_path = os.path.join(root, sample_file)
                if os.path.exists(sample_path):
                    labeled_json_files.append(os.path.join(root, file))

    return labeled_json_files
first_folder = "H:\Trashdata\생활 폐기물 이미지\data_not_augumented"
first_directories = [d for d in os.listdir(first_folder) if os.path.isdir(os.path.join(first_folder, d))]


# Example usage:
base_folder = "/path/to/your/dataset"
labeled_json_files = get_labeled_json_files(base_folder)

print("Labeled JSON files:")
for file in labeled_json_files:
    print("-", file)