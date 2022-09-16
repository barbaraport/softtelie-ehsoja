import os.path
import tensorflow


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class ImageAnalyzer(metaclass = Singleton):
    def __init__(self, analyzerName, imageClasses, trainImages, trainLabels, modelLayers):
        self._analyzerName = analyzerName
        self._imageClasses = imageClasses
        self._trainImages = trainImages
        self._trainLabels = trainLabels

        self._modelsFolder = "../../resources/models/"

        isModelAlreadyCreated = os.path.isdir(self._modelsFolder + self._analyzerName)

        if isModelAlreadyCreated:
            self._model = tensorflow.keras.models.load_model(self._modelsFolder + self._analyzerName)

        else:
            self._modelLayers = modelLayers

            self._model = initializeRecognitionModel(self._modelLayers, self._trainImages, self._trainLabels)

            self._model.save(self._modelsFolder + analyzerName)



    def analyzeImages(self, images):
        predictions = self._model.predict(images)

        return predictions


def initializeModel(modelLayers):
    model = tensorflow.keras.Sequential(modelLayers)

    return model


def fitModel(model, trainEpochs, trainImages, trainLabels):
    model.fit(trainImages, trainLabels, epochs=trainEpochs)


def initializeRecognitionModel(modelLayers, trainImages, trainLabels):
    model = initializeModel(modelLayers)

    model.compile(optimizer="adam",
                  loss=tensorflow.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=["accuracy"])

    fitModel(model, 5, trainImages, trainLabels)

    return model
