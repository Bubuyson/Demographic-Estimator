import os
import random
import shutil

def create_validation_set(training_dir, validation_dir, validation_split=0.2):
    # Create the validation directory
    if not os.path.exists(validation_dir):
        os.makedirs(validation_dir)

    # Loop over each emotion category in the training directory
    for category in os.listdir(training_dir):
        category_dir = os.path.join(training_dir, category)
        
        # Create a corresponding directory in the validation directory
        validation_category_dir = os.path.join(validation_dir, category)
        if not os.path.exists(validation_category_dir):
            os.makedirs(validation_category_dir)
        
        # Get all the images in this category
        images = os.listdir(category_dir)
        random.shuffle(images)  # Shuffle the images to ensure random selection
        
        # Determine the number of images to move to validation
        num_validation_images = int(validation_split * len(images))
        
        # Move the images
        for i in range(num_validation_images):
            image = images[i]
            src = os.path.join(category_dir, image)
            dest = os.path.join(validation_category_dir, image)
            shutil.move(src, dest)

# Assuming the structure of your dataset directory is as follows:
# ./emotion_/Training/<emotion_category>/
# And you want to create a corresponding structure for validation:
# ./emotion_/Validation/<emotion_category>/

# Specify the paths
train_dir = './emotion_/Training'
val_dir = './emotion_/Validation'

# Create the validation set
create_validation_set(train_dir, val_dir, validation_split=0.2)

# Remember to replace './emotion_/Training' and './emotion_/Validation'
# with the actual paths to your training and validation directories.
