import os
import cv2
import numpy as np
import imutils

IMAGE_SIZE = 1024

def treat_images(folder_name):
    images_path = os.listdir(folder_name)

    for image_path in images_path:
        if '.jpg' in image_path or '.png' in image_path or '.jpeg' in image_path:
            path = folder_name + "\\" + image_path
            image_to_resize = cv2.imread(path)

            original_image_height, original_image_width = image_to_resize.shape[:2]

            resized_image = image_to_resize

            if original_image_height > IMAGE_SIZE or original_image_width > IMAGE_SIZE:
                resized_image = resize(image_to_resize)

            gray_image = convert_to_gray(resized_image)
            filled_image = fill_image(gray_image)
            
            save(image_path, filled_image)


def resize(image):
    height, width = image.shape[:2]
    new_image_size = IMAGE_SIZE
    
    while new_image_size >= IMAGE_SIZE or new_image_size >= IMAGE_SIZE:

        if height > new_image_size:
            resized =  imutils.resize(image, height=new_image_size)
        elif width > new_image_size:
            resized =  imutils.resize(image, width=new_image_size)
        else:
            resized =  cv2.resize(image, width=new_image_size, height=new_image_size)
        
        new_image_size -= 2
    
    return resized


def equalize_histogram(image, clip = 1.5, tile = 8):

    lab_image = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)

    # contrast limited adaptive histogram equalization (CLAHE)
    clahe = cv2.createCLAHE(clipLimit=clip, tileGridSize=(tile,tile))

    lab_image[:,:,0] = clahe.apply(lab_image[:,:,0])

    equalized_image = cv2.cvtColor(lab_image, cv2.COLOR_LAB2RGB)

    return equalized_image


def convert_to_gray(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)


def fill_image(image):

    original_image_height, original_image_width = image.shape[:2]

    blank_image = np.zeros((1024, 1024, 3), np.uint8)
    blank_image[:, :] = (0, 0, 0)
    blank_image_height, blank_image_width = blank_image.shape[:2]

    filled_image = blank_image.copy()

    y_offset = round((blank_image_height - original_image_height) / 2)
    x_offset = round((blank_image_width - original_image_width) / 2)

    filled_image[y_offset: y_offset + original_image_height, x_offset: x_offset + original_image_width] = image.copy()

    return filled_image


def save(image_name, image):
    path = "gray/" + image_name

    print("[INFO] Saving image at: " + path)
    
    cv2.imwrite(path, image)


treat_images("train_data_without_augmentation")
