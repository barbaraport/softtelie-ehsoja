import json
from math import floor

from keras import backend as K
from keras_preprocessing.image import img_to_array

from src.main.handlers.imageHandler import ImageHandler
from src.main.model.ehSoja.EhSoja import load_trained_model
from src.main.model.mrcnn.visualize import display_instances


class ImageRecognition:

    @staticmethod
    def recognize_images(images):
        K.clear_session()

        model = load_trained_model()
        class_names = ['background', 'pod']
        recognized_images = {}

        index = 0
        for image in images:
            pil_image = ImageHandler.convert_base_64_to_pil_image(image)
            img_array = img_to_array(pil_image)

            results = model.detect([img_array], verbose=1)
            r = results[0]
            image_plt = display_instances(img_array, r['rois'], r['masks'], r['class_ids'], class_names, r['scores'])
            final_image_b64 = ImageHandler.save_to_base_64(image_plt)

            recognized_images[index] = {"image": final_image_b64}

            index += 1

        recognized_images = json.dumps(recognized_images)

        K.clear_session()

        return recognized_images

    @staticmethod
    def extractInformation(base_64_image, plantHeight):
        K.clear_session()

        model = load_trained_model()

        pil_image = ImageHandler.convert_base_64_to_pil_image(base_64_image)
        img_array = img_to_array(pil_image)

        results = model.detect([img_array])[0]

        pods_found = len(results["rois"])

        grainsFound = 0

        for boundingBox in results["rois"]:
            grainsFound += ImageRecognition._calculateGrainsFromBoundingBox(boundingBox, plantHeight)

        K.clear_session()

        extractedData = {
            "podsFound": pods_found,
            "grainsFound": grainsFound
        }

        return extractedData

    @staticmethod
    def _calculateGrainsFromBoundingBox(boundingBox, plantHeight):
        imageHeight = 1024
        AVERAGE_CM_POD_DIAMETER = 1.5

        pixelSize = plantHeight / imageHeight

        y1, x1, y2, x2 = boundingBox

        shape1 = abs(y1 - y2)
        shape2 = abs(x1 - x2)

        pod_shape = [shape1, shape2]

        height = max(pod_shape)
        width = min(pod_shape)

        pod_shape = [height, width]

        height, width = pod_shape

        real_height = height * pixelSize
        real_width = width * pixelSize

        real_shape = [real_height, real_width]

        seeds_quantity = 0

        height, _ = real_shape
        pod_seeds = floor(height / AVERAGE_CM_POD_DIAMETER)

        seeds_quantity += pod_seeds

        return seeds_quantity
