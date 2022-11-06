import base64
import os
import os.path
import uuid
from io import BytesIO

from PIL import Image


class ImageHandler:
    '''
    Class for handling operations with images stored in the application

    Requirements:
    You should have defined the environment variable IMAGE_FOLDER on your .env file
    to create an instance of imageHandler
    '''

    def __init__(self):
        try:
            self._resourcesFolder = "..\\..\\resources"
        except:
            raise Exception("Could not find IMAGE_FOLDER path in the env file")

    def saveImageFromPath(self, imagePath):
        '''
        Save image on IMAGE_FOLDER path with a random and unique UUID

        Parameters:
        imagePath (str): path to the image that will be saved to the application

        Return: dict
        '''
        try:
            with open(imagePath, 'rb') as photo:
                imageB64 = base64.b64encode(photo.read())
        except:
            raise Exception(f"Image could not be found at {imagePath}")
        return self.saveImage(b64=imageB64)

    def saveImage(self, b64):
        '''
          Save image on IMAGE_FOLDER path with a random and unique UUID

          Parameters:
          b64 (str): image encoded using base64 encoding

          Return: dict
        '''
        imageUUID = uuid.uuid4()
        stringUUID = str(imageUUID)

        imagePath = f"{self._resourcesFolder}\\userImages\\{stringUUID + '.jpg'}"

        # Garantindo unicidade do nome dos arquivos
        while (os.path.exists(imagePath)):
            imageUUID = uuid.uuid4()
            stringUUID = str(imageUUID)
            imagePath = f"{self._resourcesFolder}\\userImages\\{stringUUID + '.jpg'}"

        with open(imagePath, 'wb') as writeFile:
            writeFile.write(base64.decodebytes(b64))

        return {"message": f"Image Saved in {imagePath + '.jpg'}", "uuid": stringUUID}

    def getBase64(self, imagePath):
        '''
        Return base64 encoded image

        Parameters:
        uuid (str): the uuid of the image saved in the IMAGE_FOLDER

        Exception:
        Throws exception if image does not exist on IMAGE_FOLDER

        Return: str
        '''
        imagePath = f"{self._resourcesFolder}\\{imagePath}"
        print(imagePath)
        if (os.path.exists(imagePath)):
            with open(imagePath, 'rb') as photo:
                return base64.b64encode(photo.read())
        else:
            raise Exception(f"Image with in the path {imagePath}, could not be found")

    @staticmethod
    def convert_bytes_to_pil_image(image):
        byte_image = BytesIO(image.stream.read())
        return Image.open(byte_image)

    @staticmethod
    def convert_base_64_to_pil_image(im_b64):
        im_bytes = base64.b64decode(im_b64)
        im_file = BytesIO(im_bytes)
        img = Image.open(im_file)

        return img

    @staticmethod
    def save_to_base_64(image_bytes):
        plt_as_b64 = base64.b64encode(image_bytes.read()).decode("utf-8")

        return plt_as_b64
