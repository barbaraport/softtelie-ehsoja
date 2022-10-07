import numpy
import tensorflow
from matplotlib import pyplot

from src.main.model.MnistImageAnalyzer import MnistImageAnalyzer


def analyze(analyzer, indexToAnalyze, classNames, testImages, testLabels):
    analysisResults = analyzer.analyzeImages(testImages)

    mostAccurate = numpy.argmax(analysisResults[indexToAnalyze])

    print(f"Predição: {mostAccurate} / {classNames[mostAccurate]} | "
          f"Real: {testLabels[indexToAnalyze]} / {classNames[mostAccurate]}")

    pyplot.imshow(testImages[indexToAnalyze], cmap=pyplot.cm.binary)
    pyplot.show()


def testMnistImageAnalyzer():
    fashionMnist = tensorflow.keras.datasets.fashion_mnist

    (trainImages, trainLabels), (testImages, testLabels) = fashionMnist.load_data()

    testImages = testImages / 255.0

    classNames = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                  'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    analyzer = MnistImageAnalyzer()

    analyze(analyzer, 0, classNames, testImages, testLabels)


if __name__ == "__main__":
    testMnistImageAnalyzer()
