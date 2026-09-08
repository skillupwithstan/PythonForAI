import cv2
import numpy as np
from PIL import Image

# 1. Load an image using OpenCV
# Replace 'input_image.jpg' with a path to any image file on your system
image_path = 'input_image.jpg'
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Could not find or open the image at '{image_path}'")
    print("Creating a dummy placeholder image for demonstration instead...")
    # Generate a solid blue 400x400 placeholder image matrix if file is missing
    image = np.zeros((400, 400, 3), dtype=np.uint8)
    image[:] = [255, 0, 0] # BGR color format: Blue=255, Green=0, Red=0

# 2. Basic Image Handling (Resizing)
# Resize the image down to standard 300x300 pixel square dimensions
resized_image = cv2.resize(image, (300, 300))

# 3. Color Space Conversion
# OpenCV uses BGR by default; convert it to Grayscale for feature analysis
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# 4. Computer Vision Algorithm: Canny Edge Detection
# Low and High threshold parameters find strong structural boundaries/lines
edges = cv2.Canny(gray_image, threshold1=100, threshold2=200)

print(edges)

# 5. Saving the Output using Pillow (PIL)
# Convert the OpenCV matrix back to a PIL object to save or view safely
output_pil_image = Image.fromarray(edges)
output_pil_image.save('detected_edges.jpg')

print("Success! Processed image and saved structural boundaries to 'detected_edges.jpg'.")
