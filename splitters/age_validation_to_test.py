import os
import shutil

# Define the paths
validation_path = './ages/Validation'
test_path = './ages/Test'

# Create the "Test" folder if it doesn't exist
os.makedirs(test_path, exist_ok=True)

# Define the age categories
ages = ["0-2", "3-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "more than 70"]

# Define the fraction of validation data to move to the test set (1/3)
validation_fraction = 1/3

# Iterate through each age category
for age in ages:
    age_validation_path = os.path.join(validation_path, age)
    age_test_path = os.path.join(test_path, age)
    
    # Create the age-specific "Test" folder if it doesn't exist
    os.makedirs(age_test_path, exist_ok=True)

    # List all files in the age-specific validation folder
    files = os.listdir(age_validation_path)
    
    # Calculate the number of files to move to the test set (one-third of the validation set)
    num_files_to_move = int(len(files) * validation_fraction)

    # Move the files to the test set
    files_to_move = files[:num_files_to_move]
    for file in files_to_move:
        src = os.path.join(age_validation_path, file)
        dst = os.path.join(age_test_path, file)
        shutil.move(src, dst)

print("One-third of the validation dataset has been moved to the 'Test' folder.")
