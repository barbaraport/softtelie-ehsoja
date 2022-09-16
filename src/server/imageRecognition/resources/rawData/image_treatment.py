import os
import cv2
import numpy as np
from PIL import Image


def fill_and_resize_from_folder(folder_name):
    images_path = os.listdir(folder_name)

    for image_path in images_path:
        image_to_resize = cv2.imread(folder_name + "\\" + image_path)
        original_image_height, original_image_width = image_to_resize.shape[:2]

        blank_image = np.zeros((1100, 1100, 3), np.uint8)
        blank_image[:, :] = (0, 0, 0)
        blank_image_height, blank_image_width = blank_image.shape[:2]

        filled_image = blank_image.copy()

        y_offset = round((blank_image_height - original_image_height) / 2)
        x_offset = round((blank_image_width - original_image_width) / 2)

        filled_image[y_offset: y_offset + original_image_height, x_offset: x_offset + original_image_width]\
            = image_to_resize.copy()

        save(image_path, filled_image)


def resize(image):
    return image.resize((512, 512), Image.Resampling.LANCZOS)


def save(image_name, image):
    cv2.imwrite("../trainData/images/" + image_name, image)


fill_and_resize_from_folder("01_SELECT21")
fill_and_resize_from_folder("01_SELECT22")
