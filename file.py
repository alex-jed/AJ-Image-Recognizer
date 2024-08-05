import csv

import numpy as np
import os
from PIL import Image
import matplotlib.pyplot as plt

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


def display_grayscale_image(grayscale_matrix):
    """
    Creates a tkinter window displaying an n x n grid of grayscale values.
    """

    plt.imshow(grayscale_matrix, cmap='gray', interpolation='nearest')
    plt.title("Grayscale Matrix")
    plt.show()

def write_heatmap(heatmap, filename):
    """
    Writes an n x n grid of numbers to a CSV file.
    """

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in heatmap:
            writer.writerow(row)
    print("HEATMAP UPDATED")


def read_heatmap(filename):
    """
    Reads a CSV file and saves it as a 2D array.
   """

    filename = str(filename) + " heatmap"

    grid = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            grid.append([int(value) if value.isdigit() else float(value) for value in row])

    return np.array(grid)


def reset_heatmap(image, filename):
    grid = []
    for i in range(image):
        new_line = []
        for j in range(image):
            new_line.append(0)
        grid.append(new_line)

    write_heatmap(grid, filename)


def display_rbg_image(rbg_matrix):
    plt.imshow(rbg_matrix)
    plt.title("RGB Matrix")
    plt.axis('off')
    plt.show()
