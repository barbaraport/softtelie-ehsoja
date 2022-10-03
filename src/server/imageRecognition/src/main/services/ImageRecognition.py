from keras_preprocessing.image import load_img, img_to_array

from mrcnn.visualize import display_instances
from mrcnn.config import Config
from mrcnn import model as modellib


class myMaskRCNNConfig(Config):
    # give the configuration a recognizable name
    NAME = "MaskRCNN_inference"

    # set the number of GPUs to use along with the number of images
    # per GPU
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

    # number of classes (we would normally add +1 for the background
    # but the background class is *already* included in the class
    # names)
    NUM_CLASSES = 1 + 1


class ImageRecognition:

    def recognizeImages(self, images):
        config = myMaskRCNNConfig()
        model = modellib.MaskRCNN(mode="inference", config = config, model_dir="logs")
        model.load_weights("shapes_0005.h5", by_name = True)

        class_names = ['BG', 'pod']

        img = load_img('')
        img = img_to_array(img)

        results = model.detect([img], verbose=0)
        r = results[0]
        display_instances(img, r['rois'], r['masks'], r['class_ids'], class_names, r['scores'])

        classes = r['class_ids']
        print("Total Objects found", len(classes))
        for i in range(len(classes)):
            print(class_names[classes[i]])
