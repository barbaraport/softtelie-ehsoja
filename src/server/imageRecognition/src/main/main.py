from flask import Flask

from controllers.HelloWorldController import helloWorldRoutes


def initializeServer():
    application = Flask(__name__)

    application.register_blueprint(helloWorldRoutes)

    application.run(host = "0.0.0.0", port = 5000)


def main():
    initializeServer()


if __name__ == "__main__":
    main()
