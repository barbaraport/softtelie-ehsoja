from keras_preprocessing.image import load_img, img_to_array

from src.main.iaModel.EhSojaConfig import EhSojaConfig
from src.main.services.mrcnn.model import MaskRCNN
from src.main.services.mrcnn.visualize import display_instances


class ImageRecognition:

    @staticmethod
    def recognize_images():
        config = EhSojaConfig()
        model = MaskRCNN(mode="inference", config=config, model_dir="logs")
        model.load_weights("./mask_rcnn_shapes_0006.h5", by_name=True)

        class_names = ['BG', 'pod']

        img = load_img('image.jpg')
        img = img_to_array(img)

        results = model.detect([img], verbose=0)
        r = results[0]
        display_instances(img, r['rois'], r['masks'], r['class_ids'], class_names, r['scores'])

        classes = r['class_ids']
        print("Total Objects found", len(classes))
        for i in range(len(classes)):
            print(class_names[classes[i]])
