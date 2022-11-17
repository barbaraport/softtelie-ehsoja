import os
import platform

from src.main.model.mrcnn.config import Config
from src.main.model.mrcnn.model import MaskRCNN


class EhSojaConfig(Config):
    """Configuration for training on the dataset.
    Derives from the base Config class and overrides values specific
    to the dataset.
    """
    BACKBONE = "resnet50"

    # Give the configuration a recognizable name
    NAME = "shapes"

    # Train on 1 GPU and 1 images per GPU. We can put multiple images on each
    # GPU. Batch size is (GPUs * images/GPU).
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

    BATCH_SIZE = 32

    # Number of classes (including background)
    NUM_CLASSES = 2

    # Steps per epoch
    STEPS_PER_EPOCH = 500

    # Image resize mode
    # No changes to the image
    IMAGE_RESIZE_MODE = "square"
    IMAGE_MAX_DIM = 1024
    IMAGE_MIN_DIM = 1024

    # Minimum probability value to accept a detected instance
    # ROIs below this threshold are skipped
    DETECTION_MIN_CONFIDENCE = 0.6

    # Non-maximum suppression threshold for detection
    DETECTION_NMS_THRESHOLD = 0.1

    # Length of square anchor side in pixels
    RPN_ANCHOR_SCALES = (8, 16, 32, 64, 128)

    # Non-max suppression threshold to filter RPN proposals.
    # You can increase this during training to generate more proposals.
    RPN_NMS_THRESHOLD = 0.1


def load_trained_model():
    project_root = os.getcwd()
    trained_model_directory = ""

    operational_system = platform.system()

    if operational_system == "Linux":
        trained_model_directory = os.path.join(project_root, "src", "main", "model", "trainedModel/")
    elif operational_system == "Windows":
        trained_model_directory = os.path.join(project_root, "model", "trainedModel/")
    else:
        raise 'idk which operational system u r using :('

    config = EhSojaConfig()
    model = MaskRCNN(mode="inference", config=config, model_dir="logs")
    model.load_weights(trained_model_directory + "mask_rcnn_shapes_0006.h5", by_name=True)

    return model
