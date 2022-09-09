import cv2
import numpy as np
import os


def fill_from_folder(folder_name):
    images_path = os.listdir(folder_name)

    for image_path in images_path:
        image_to_resize = cv2.imread(folder_name + "\\" + image_path)
        height, width = image_to_resize.shape[:2]

        blank_image = np.zeros((1100, 1100, 3), np.uint8)
        blank_image[:, :] = (0, 0, 0)
        bg_height, bg_width = blank_image.shape[:2]

        l_img = blank_image.copy()

        y_offset = round((bg_height - height) / 2)
        x_offset = round((bg_width - width) / 2)
        l_img[y_offset: y_offset + height, x_offset: x_offset + width] = image_to_resize.copy()

        cv2.imwrite("../train_data_fill/images/" + image_path, l_img)


fill_from_folder("01_SELECT21")
fill_from_folder("01_SELECT22")
