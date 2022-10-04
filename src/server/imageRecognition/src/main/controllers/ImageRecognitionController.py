from flask import Blueprint
from flask import make_response

from flask import jsonify

from src.main.services.ImageRecognition import ImageRecognition

imageRecognitionRoutes = Blueprint("imageRecognitionRoutes", __name__)


@imageRecognitionRoutes.route("/recognizeImages", methods=["POST"])
def recognize_images():
    # imagesBase64 = request.json
    # analyzedImages = analyzeBatchImages(imagesBase64)
    # response = jsonify(analyzedImages)

    ImageRecognition.recognize_images()

    return make_response(jsonify({"message": "Ok!"}), 200)
