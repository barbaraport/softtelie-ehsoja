import PIL
from PIL import Image

import os


def resizeFromFolder(folderName):
    imagesPaths = os.listdir(folderName)

    for imagePath in imagesPaths:
        image = Image.open(folderName + "/" + imagePath)

        resizedImage = image.resize((256, 768), Image.Resampling.LANCZOS)

        resizedImage.save("../trainData/images/" + imagePath)


resizeFromFolder("01_SELECT21")
resizeFromFolder("01_SELECT22")
