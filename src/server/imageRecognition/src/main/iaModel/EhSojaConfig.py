from src.main.services.mrcnn.config import Config


class EhSojaConfig(Config):
    # give the configuration a recognizable name
    NAME = "ehSoja_inference"

    # set the number of GPUs to use along with the number of images
    # per GPU
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

    # number of classes (we would normally add +1 for the background
    # but the background class is *already* included in the class
    # names)
    NUM_CLASSES = 1 + 1