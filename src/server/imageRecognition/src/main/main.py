from flask import Flask

from controllers.ImageRecognitionController import imageRecognitionRoutes


def initialize_server():
    application = Flask(__name__)

    application.register_blueprint(imageRecognitionRoutes)

    application.run(host="0.0.0.0", port=5000)


def main():
    initialize_server()


if __name__ == "__main__":
    main()
