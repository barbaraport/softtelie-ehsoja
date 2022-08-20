import tensorflow

import numpy
import matplotlib.pyplot as pyplot

classNames = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
              'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


def inspectImage(imageToInspect):
    pyplot.figure()
    pyplot.imshow(imageToInspect)
    pyplot.colorbar()
    pyplot.grid(False)
    pyplot.show()


def plot_image(i, predictions_array, true_label, img):
    true_label, img = true_label[i], img[i]
    pyplot.grid(False)
    pyplot.xticks([])
    pyplot.yticks([])

    pyplot.imshow(img, cmap=pyplot.cm.binary)

    predicted_label = numpy.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'

    pyplot.xlabel("{} {:2.0f}% ({})".format(classNames[predicted_label],
                                            100 * numpy.max(predictions_array),
                                            classNames[true_label]),
                  color=color)


def plot_value_array(i, predictions_array, true_label):
    true_label = true_label[i]
    pyplot.grid(False)
    pyplot.xticks(range(10))
    pyplot.yticks([])
    thisplot = pyplot.bar(range(10), predictions_array, color="#777777")
    pyplot.ylim([0, 1])
    predicted_label = numpy.argmax(predictions_array)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')


def testTensorflow():
    print("Tensorflow, versão ", tensorflow.__version__)

    fashionMnist = tensorflow.keras.datasets.fashion_mnist

    (trainImages, trainLabels), (testImages, testLabels) = fashionMnist.load_data()

    trainImages = trainImages / 255.0
    testImages = testImages / 255.0

    model = tensorflow.keras.Sequential([
        tensorflow.keras.layers.Flatten(input_shape=(28, 28)),
        tensorflow.keras.layers.Dense(128, activation="relu"),
        tensorflow.keras.layers.Dense(10),
    ])

    model.compile(optimizer="adam",
                  loss=tensorflow.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=["accuracy"])

    model.fit(trainImages, trainLabels, epochs=10)

    testLoss, testAccuracy = model.evaluate(testImages, testLabels, verbose=2)

    print("Acurácia do teste: ", testAccuracy)

    probabilityModel = tensorflow.keras.Sequential([
        model, tensorflow.keras.layers.Softmax()
    ])

    predictions = probabilityModel.predict(testImages)

    # Troque o valor de i, de 0 a 9999, para analisar uma imagem diferente
    i = 9999
    pyplot.figure(figsize=(6, 3))
    pyplot.subplot(1, 2, 1)
    plot_image(i, predictions[i], testLabels, testImages)
    pyplot.subplot(1, 2, 2)
    plot_value_array(i, predictions[i], testLabels)
    pyplot.show()
