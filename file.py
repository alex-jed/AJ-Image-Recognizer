import numpy as np
import os
from PIL import Image

print("READS/WRITES FILES")

def get_image(image_filename):

    """
    Converts an image to a matrix of RGB values.
    """

    directory_name = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(directory_name, f"{image_filename}.png")

    with Image.open(image_path) as img:
        img = img.convert('RGB')
        rgb_matrix = np.array(img)

    return rgb_matrix
