import os
import shutil
import random

def create_age_directories(base_path, age_ranges):
    for category in ['Training', 'Validation', 'Test']:
        for age_range in age_ranges:
            dir_path = os.path.join(base_path, category, age_range)
            os.makedirs(dir_path, exist_ok=True)

def get_age_range(age):
    if age <= 2:
        return '0-2'
    elif age <= 9:
        return '3-9'
    elif age <= 19:
        return '10-19'
    elif age <= 29:
        return '20-29'
    elif age <= 39:
        return '30-39'
    elif age <= 49:
        return '40-49'
    elif age <= 59:
        return '50-59'
    elif age <= 69:
        return '60-69'
    else:
        return '70+'

def copy_files_to_age_directory(source_base, dest_base, age, file_names, splits=(0.7, 0.2, 0.1)):
    age_range = get_age_range(age)
    for file_name in file_names:
        rand_num = random.random()
        if rand_num < splits[0]:
            dest_category = 'Training'
        elif rand_num < splits[0] + splits[1]:
            dest_category = 'Validation'
        else:
            dest_category = 'Test'
        
        shutil.copy(os.path.join(source_base, str(age).zfill(3), file_name),
                    os.path.join(dest_base, dest_category, age_range, file_name))

def main():
    source_base_path = './face_age'
    dest_base_path = './ages_new_split'
    age_ranges = ['0-2', '3-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70+']

    create_age_directories(dest_base_path, age_ranges)

    for age_dir in os.listdir(source_base_path):
        if not age_dir.isdigit():
            continue
        age = int(age_dir)
        file_names = os.listdir(os.path.join(source_base_path, age_dir))
        copy_files_to_age_directory(source_base_path, dest_base_path, age, file_names)

if __name__ == "__main__":
    main()
