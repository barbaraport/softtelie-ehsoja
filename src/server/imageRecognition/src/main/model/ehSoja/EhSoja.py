import os

from src.main.model.mrcnn.config import Config
from src.main.model.mrcnn.model import MaskRCNN


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


def load_trained_model():
    project_root = os.getcwd()
    trained_model_directory = project_root + "\\model\\trainedModel\\"

    config = EhSojaConfig()
    model = MaskRCNN(mode="inference", config=config, model_dir="logs")
    model.load_weights(trained_model_directory + "mask_rcnn_shapes_0006.h5", by_name=True)

    return model
