import json

from keras import backend as K

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

            pil_image = ImageHandler.convert_base_b4_to_pil_image(image)

            results = model.detect([pil_image])
            r = results[0]
            image_plt = display_instances(pil_image, r['rois'], r['masks'], r['class_ids'], class_names, r['scores'])
            final_image_b64 = ImageHandler.save_to_base_64(image_plt)

            classes = r['class_ids']
            print("Total Objects found", len(classes))

            results = {
                index: {
                    "image": final_image_b64
                }
            }

        results = json.dumps(results)

        K.clear_session()

        return results

