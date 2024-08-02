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


def rgb_to_grayscale(rgb_matrix):
    """
    Converts an n x n grid of RGB values to a grayscale n x n grid.
   """
    grayscale_matrix = np.dot(rgb_matrix[..., :3], [0.2989, 0.5870, 0.1140])

    return grayscale_matrix
