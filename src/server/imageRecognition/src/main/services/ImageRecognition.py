import base64
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
        results = {}

        index = 0
        for image in images:
            decoded_image = base64.b64decode(image)
            pil_image = img_to_array(decoded_image)

            results = model.detect([pil_image])
            r = results[0]
            image_plt = display_instances(pil_image, r['rois'], r['masks'], r['class_ids'], class_names, r['scores'])
            final_image_b64 = ImageHandler.save_to_base_64(image_plt)

            classes = r['class_ids']
            print("Total Objects found", len(classes))

            results = {
                index: {
                    "results": r,
                    "image": final_image_b64
                }
            }

        results = json.dumps(results)

        K.clear_session()

        return results

