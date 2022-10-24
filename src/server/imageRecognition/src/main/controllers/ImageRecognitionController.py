from flask import Blueprint, request
from flask import make_response

from flask import jsonify

from src.main.services.ImageRecognition import ImageRecognition

imageRecognitionRoutes = Blueprint("imageRecognitionRoutes", __name__)


@imageRecognitionRoutes.route("/recognizeImages", methods=["POST"])
def recognize_images():
    images = request.json

    recognized_images = ImageRecognition.recognize_images(images)

    return make_response(jsonify(recognized_images), 200)


@imageRecognitionRoutes.route("/countPods", methods=["POST"])
def countPodsRoute():
    responseBody = request.json

    image = responseBody["base64Image"]

    podsFound = ImageRecognition.countPods(image)

    return make_response(jsonify({"podsFound": podsFound}), 200)
