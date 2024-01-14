import cv2
from matplotlib import pyplot as plt

def process_image(input_image_name):
    # Read the input image
    input_image = cv2.imread("./static/uploads/" + input_image_name)

    # Your image processing logic goes here
    # For example, let's convert the image to grayscale
    processed_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    # Save the processed image
    cv2.imwrite("./static/uploads/processed_" + input_image_name, processed_image)
