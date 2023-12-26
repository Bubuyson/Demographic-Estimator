
import os
import shutil

def combine_directories(source1, source2, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

    for item in os.listdir(source1):
        src_path = os.path.join(source1, item)
        dest_path = os.path.join(destination, item)
        if os.path.isdir(src_path):
            if not os.path.exists(dest_path):
                shutil.copytree(src_path, dest_path)
            else:
                # If the directory already exists in the destination, copy individual files
                for file in os.listdir(src_path):
                    shutil.copy(os.path.join(src_path, file), dest_path)

    for item in os.listdir(source2):
        src_path = os.path.join(source2, item)
        dest_path = os.path.join(destination, item)
        if os.path.isdir(src_path):
            if not os.path.exists(dest_path):
                shutil.copytree(src_path, dest_path)
            else:
                # If the directory already exists in the destination, copy individual files
                for file in os.listdir(src_path):
                    shutil.copy(os.path.join(src_path, file), dest_path)

def combine_datasets(base_dir1, base_dir2, combined_dir):
    for category in ['Training', 'Validation', 'Test']:
        source1 = os.path.join(base_dir1, category)
        source2 = os.path.join(base_dir2, category)
        destination = os.path.join(combined_dir, category)

        combine_directories(source1, source2, destination)

# Define the base directories
base_dir1 = 'ages'
base_dir2 = 'ages_new_split'
combined_dir = 'ages_combined'

# Combine the datasets
combine_datasets(base_dir1, base_dir2, combined_dir)

