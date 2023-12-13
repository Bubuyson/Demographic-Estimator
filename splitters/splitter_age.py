import os
import shutil
import pandas as pd

# Define the file paths
train_csv_path = './fairface_label_train.csv'
val_csv_path = './fairface_label_val.csv'
train_images_path = './train'
val_images_path = './val'

# Read the CSV files
train_df = pd.read_csv(train_csv_path)
val_df = pd.read_csv(val_csv_path)

# Define the age categories
ages = ["0-2", "3-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "more than 70"]

# Define the new folder paths
new_folder_path = './ages'
new_training_folder = os.path.join(new_folder_path, 'Training')
new_validation_folder = os.path.join(new_folder_path, 'Validation')

# Create the base folders and age-specific subdirectories
os.makedirs(new_training_folder, exist_ok=True)
os.makedirs(new_validation_folder, exist_ok=True)
for age in ages:
    os.makedirs(os.path.join(new_training_folder, age), exist_ok=True)
    os.makedirs(os.path.join(new_validation_folder, age), exist_ok=True)

# Function to distribute images into corresponding age folders
def distribute_images_by_age(df, images_path, training_folder, validation_folder):
    for index, row in df.iterrows():
        # Determine if the image is for training or validation
        folder = training_folder if 'train' in row['file'] else validation_folder

        # Define the source and destination paths
        src = os.path.join(images_path, row['file'].split('/')[-1])
        age = row['age']
        dst = os.path.join(folder, age, row['file'].split('/')[-1])

        # Copy the image to the new folder
        if os.path.exists(src):
            shutil.copy(src, dst)

# Distribute train and validation images by age groups
distribute_images_by_age(train_df, train_images_path, new_training_folder, new_validation_folder)
distribute_images_by_age(val_df, val_images_path, new_training_folder, new_validation_folder)

# Return the path to the new directory
new_folder_path
