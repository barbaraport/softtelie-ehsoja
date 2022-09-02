from src.server.imageRecognition.src.main.services.imageHandler import imageHandler


def convertImageToBase64Test():
    imageService = imageHandler()

    testImagePath = "rawData\\01_SELECT21\\1a444f61-6811-4c8b-adfc-f47f15c76c7e_1.jpg"

    base64String = imageService.getBase64(testImagePath)

    print(base64String)


def saveImage():
    imageService = imageHandler()

    testImagePath = "rawData\\01_SELECT21\\1a444f61-6811-4c8b-adfc-f47f15c76c7e_1.jpg"

    base64String = imageService.getBase64(testImagePath)

    response = imageService.saveImage(base64String)

    print(response)


if __name__ == "__main__":
    convertImageToBase64Test()
    saveImage()
