import os
import cv2
import numpy as np
from PIL import Image


def fill_from_folder(folder_name):
    images_path = os.listdir(folder_name)

    for image_path in images_path:
        image_to_resize = cv2.imread(folder_name + "\\" + image_path)
        height, width = image_to_resize.shape[:2]

        blank_image = np.zeros((1500, 1500, 3), np.uint8)
        blank_image[:, :] = (0, 0, 0)
        bg_height, bg_width = blank_image.shape[:2]

        l_img = blank_image.copy()

        y_offset = round((bg_height - height) / 2)
        x_offset = round((bg_width - width) / 2)
        l_img[y_offset: y_offset + height, x_offset: x_offset + width] = image_to_resize.copy()

        cv2.imwrite("../train_data_fill/images/" + image_path, l_img)


def resize_from_folder(folder_name):
    images_paths = os.listdir(folder_name)

    for imagePath in images_paths:
        image = Image.open(folder_name + "/" + imagePath)

        resized_image = image.resize((256, 768), Image.Resampling.LANCZOS)

        resized_image.save("../train_data_resize/images/" + imagePath)


fill_from_folder("01_SELECT21")
fill_from_folder("01_SELECT22")

resize_from_folder("01_SELECT21")
resize_from_folder("01_SELECT22")
