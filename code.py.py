import cv2 as cv
import os

# Function to convert image to pencil sketch
def pencil_sketch(image_path):
    # Read the input image
    image = cv.imread(image_path)

    # Convert image to grayscale
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverseImage = 255 - gray

    # Apply Gaussian Blur
    bluredImage = cv.GaussianBlur(inverseImage, (15, 15), 0, 0)

    # Create a pencil sketch using divide function
    pencilSketch = cv.divide(gray, 255 - bluredImage, scale=256)

    return pencilSketch

# Base directory where output images will be saved
base_dir = r'D:\projectssss\output_images'

# Input image file path (change this to your PNG image file)
input_image_path = r"D:\projectssss\pencil sketch\me.png.png"

# Generate pencil sketch
sketch = pencil_sketch(input_image_path)

# Display the pencil sketch (optional)
cv.imshow('Pencil Sketch', sketch)
cv.waitKey(0)  # Wait indefinitely for any key press
cv.destroyAllWindows()

# Construct output file name
input_filename = os.path.basename(input_image_path)
output_filename = os.path.splitext(input_filename)[0] + '_pencil_sketch.png'

# Construct full output path
output_path = os.path.join(base_dir, output_filename)

# Save the pencil sketch as output
success = cv.imwrite(output_path, sketch)

if success:
    print(f'Pencil sketch saved as {output_path}')
else:
    print(f'Error saving pencil sketch to {output_path}')
