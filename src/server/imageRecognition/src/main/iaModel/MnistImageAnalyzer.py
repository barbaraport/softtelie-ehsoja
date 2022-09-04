import tensorflow

from src.main.iaModel.ImageAnalyzer import ImageAnalyzer


class MnistImageAnalyzer(ImageAnalyzer):
    def __init__(self):
        fashionMnist = tensorflow.keras.datasets.fashion_mnist

        (trainImages, trainLabels), (testImages, testLabels) = fashionMnist.load_data()

        classNames = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                      'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

        trainImages = trainImages / 255.0

        modelLayers = [
                tensorflow.keras.layers.Flatten(input_shape=(28, 28)),
                tensorflow.keras.layers.Dense(128, activation="relu"),
                tensorflow.keras.layers.Dense(10),
                tensorflow.keras.layers.Softmax()
        ]

        super().__init__("mnistModel", classNames, trainImages, trainLabels, modelLayers)
