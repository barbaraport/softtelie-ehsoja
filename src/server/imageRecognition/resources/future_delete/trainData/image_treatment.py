import os
import cv2
import numpy as np
from PIL import Image


def treat_images(folder_name):
    images_path = os.listdir(folder_name)

    for image_path in images_path:
        image_to_resize = cv2.imread(folder_name + "\\" + image_path)
        print(image_to_resize)
        equalize_histogram(image_to_resize)
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


def equalize_histogram(image): 
    # load the source image
    # img = cv2.imread('nature_org.jpg')
    img = image

    # convert it to grayscale
    img_yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)

    # apply histogram equalization 
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
    hist_eq = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    # display both images (original and equalized)
    cv2.imshow("equalizeHist", np.hstack((img, hist_eq)))
    cv2.waitKey(0)


def resize(image):
    return image.resize((512, 512), Image.Resampling.LANCZOS)


def save(image_name, image):
    cv2.imwrite("../images/" + image_name, image)


treat_images("stage1_train/images")
