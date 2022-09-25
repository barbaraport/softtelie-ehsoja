from flask import Blueprint
from flask import request
from flask import jsonify

from src.main.services.ImageAnalyzer import analyzeBatchImages

imageAnalyzerRoutes = Blueprint("imageAnalyzerRoutes", __name__)


@imageAnalyzerRoutes.route("/analyzeImages", methods = ["POST"])
def analyzeImages():
    imagesBase64 = request.json

    analyzedImages = analyzeBatchImages(imagesBase64)

    response = jsonify(analyzedImages)

    return response
