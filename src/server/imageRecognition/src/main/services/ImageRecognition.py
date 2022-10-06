import json

from keras import backend as K
from keras_preprocessing.image import img_to_array

from src.main.model.ehSoja.EhSoja import load_trained_model
from src.main.model.mrcnn.visualize import display_instances
from src.main.handlers.imageHandler import ImageHandler


class ImageRecognition:

    @staticmethod
    def recognize_images(images):
        K.clear_session()

        model = load_trained_model()
        class_names = ['background', 'pod']
        recognized_images = {}

        index = 0
        for image in images:
            pil_image = ImageHandler.convert_base_b4_to_pil_image(image)
            img_array = img_to_array(pil_image)

            results = model.detect([img_array])
            r = results[0]
            image_plt = display_instances(img_array, r['rois'], r['masks'], r['class_ids'], class_names, r['scores'])
            final_image_b64 = ImageHandler.save_to_base_64(image_plt)

            recognized_images[index] = {"image": final_image_b64}

            index += 1

        recognized_images = json.dumps(recognized_images)

        K.clear_session()

        return recognized_images
