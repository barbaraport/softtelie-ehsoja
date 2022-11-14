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


@imageRecognitionRoutes.route("/extractInformation", methods=["POST"])
def count_pods_route():
    response_body = request.json

    image = response_body["base64Image"]

    pods_found, grains_found = [ImageRecognition.count_pods(image),0]

    return make_response(jsonify({"podsFound": pods_found, "grainsFound": grains_found}), 200)
