'''
Class for handling operations with images stored in the application

Requirements:
You should have defined the environment variable IMAGE_FOLDER on your .env file 
to create an instance of imageHandler
'''

import os, os.path, base64, uuid

class imageHandler():
  def __init__(self):
    try:
      self._imageFolder = os.environ['IMAGE_FOLDER']
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
    imagePath = f"{self._imageFolder}/{stringUUID}"
    
    # Garantindo unicidade do nome dos arquivos
    while(os.path.exists(imagePath)):
      imageUUID = uuid.uuid4()
      stringUUID = str(imageUUID)
      imagePath = f"{self._imageFolder}{stringUUID+'.jpg'}"

    with open(stringUUID, 'wb') as writeFile:
      writeFile.write(base64.b64decode(b64))

    return {"message": f"Image Saved in {imagePath+'.jpg'}", "uuid": stringUUID}

  def getBase64(self, uuid):
    '''
    Return base64 encoded image

    Parameters:
    uuid (str): the uuid of the image saved in the IMAGE_FOLDER

    Exception:
    Throws exception if image does not exist on IMAGE_FOLDER

    Return: str
    '''
    imagePath = f"{self._imageFolder}/{uuid}.jpg"
    if(os.path.exists(imagePath)):
      with open(imagePath, 'rb') as photo:
        return str(base64.b64encode(photo.read()))
    else:
      raise Exception(f"Image with UUID {uuid}, could not be found")