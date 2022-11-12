import os

from src.main.model.mrcnn.config import Config
from src.main.model.mrcnn.model import MaskRCNN


class EhSojaConfig(Config):
    NAME = "eS_inference"
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1
    NUM_CLASSES = 2
    DETECTION_MIN_CONFIDENCE = 0.6
    IMAGE_RESIZE_MODE = "none"
    IMAGE_MAX_DIM = 1024
    IMAGE_MIN_DIM = 1024


def load_trained_model():
    project_root = os.getcwd()
    trained_model_directory = os.path.join(project_root, "main", "model", "trainedModel/")

    config = EhSojaConfig()
    model = MaskRCNN(mode="inference", config=config, model_dir="logs")
    model.load_weights(trained_model_directory + "mask_rcnn_shapes_0006.h5", by_name=True)

    return model
