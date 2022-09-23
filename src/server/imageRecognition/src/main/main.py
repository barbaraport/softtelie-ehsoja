from flask import Flask

from controllers.HelloWorldController import helloWorldRoutes
from controllers.ImageAnalyzerController import imageAnalyzerRoutes


def initializeServer():
    application = Flask(__name__)

    application.register_blueprint(helloWorldRoutes)
    application.register_blueprint(imageAnalyzerRoutes)

    application.run(host = "0.0.0.0", port = 5000)


def main():
    initializeServer()


if __name__ == "__main__":
    main()
