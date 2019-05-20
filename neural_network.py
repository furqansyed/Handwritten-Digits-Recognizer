import keras
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))


'''
    Neural Network Parameters:
    input layer size => 784 
    hidden layer size => 48
    output layer size => 10
    
    Each layer will have x neurons (listed above) with an activation, bias, and weight for each corresponding neuron in
    the previous and next layer. All neurons are connected to all of the neurons in the previous & next layer. The idea
    is to sum the products of each previous neuron's activation with its corresponding weight and pass it through an 
    activation function (sigmoid in our case) to eventually reach the output layer. By backpropagating the error for 
    thousands of samples, the hope is to reduce error and improve accuracy by adjusting the weights and biases.
    
    Neural network takes in a 28x28 image of a handwritten digit, and outputs 10 values between 0-1 (corresponding
    to each possible digit). The goal is to use the MNIST training set of 60000+ images and to be able to reach 
    an accuracy of >90% with the test set using backpropagation.
'''


class NeuralNetwork:
    def __init__(self):
        self.input = np.zeros((784, 1))
        self.wh = 2 * np.random.rand(48, 784) - 1
        self.wo = 2 * np.random.rand(10, 48) - 1
        # self.b1 = np.random.rand(48, 1)
        # self.b2 = np.random.rand(10, 1)
        self.zh = np.zeros((48, 1))
        self.zo = np.zeros((10, 1))
        self.ah = np.zeros((48, 1))
        self.ao = np.zeros((10, 1))

    def feed_forward(self, data):
        """
        :param data: input image (28x28 pixels, passed as an ndarray)
        :return: none
        This function passes the input image and feeds forward to the hidden layer and ultimately the output layer
        """
        self.input = data.flatten().reshape(784, 1) / 255
        self.zh = np.dot(self.wh, self.input).reshape(48, 1)
        self.ah = sigmoid(self.zh)
        self.zo = np.dot(self.wo, self.ah)
        self.ao = sigmoid(self.zo)

    def backprop(self, label):
        """
        :param label: corresponding label for the image
        :return: none
        backprop calculates an estimation of the error/loss gradient in order to adjust the weights and biases.
        """
        learning_rate = 0.5
        y = np.zeros((10, 1))
        y[label] = 1

        # region Phase 1: Output Weights

        # cost = 0.5 * np.power((self.ao - y), 2)

        dc_dao = np.array(self.ao - y)
        dao_dzo = sigmoid_derivative(self.zo)
        dzo_dwo = self.ah

        dc_dwo = np.dot(dc_dao * dao_dzo, dzo_dwo.T)
        # dc_dwo = np.dot(dzo_dwo, (dc_dao * dao_dzo).T)

        # endregion
        # region Phase 2: Hidden Weights
        dc_dzo = dc_dao * dao_dzo
        dzo_dah = self.wo
        dc_dah = np.dot(dc_dzo.T, dzo_dah).T
        # dc_dah = np.dot(dc_dzo, dzo_dah.T)
        dah_dzh = sigmoid_derivative(self.zh)
        dzh_dwh = self.input

        dc_dwh = np.dot(dc_dah * dah_dzh, dzh_dwh.T)

        # endregion
        self.wo -= learning_rate * dc_dwo
        self.wh -= learning_rate * dc_dwh

    def train(self, inputs, labels):
        for epoch in range(60000):
            self.feed_forward(inputs[epoch])
            self.backprop(labels[epoch])

    def test(self, inputs, labels):
        success = 0
        for i in range(len(inputs)):
            self.feed_forward(inputs[i])
            if self.ao.argmax() == labels[i]:
                success += 1
            else:
                print()

        print(f'Accuracy: {success/len(inputs) * 100}%')

    def output(self, image):
        """
        :param image: 28x28 ndarray
        :return: int 0 - 9
        """
        self.feed_forward(image)
        return self.ao.argmax()

    def open_load(self):
        self.wh = np.loadtxt('weights_1.csv', delimiter=',')
        self.wo = np.loadtxt('weights_2.csv', delimiter=',')
        # self.bias_1 = np.loadtxt('bias_1.csv', delimiter=',').reshape(48, 1)
        # self.bias_2 = np.loadtxt('bias_2.csv', delimiter=',').reshape(10, 1)

    def save(self):
        np.savetxt('weights_1.csv', self.wh, delimiter=',', fmt='%f')
        np.savetxt('weights_2.csv', self.wo, delimiter=',', fmt='%f')
        # np.savetxt('bias_1.csv', self.bias_1, delimiter=',', fmt='%f')
        # np.savetxt('bias_2.csv', self.bias_2, delimiter=',', fmt='%f')


if __name__ == "__main__":
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

    # Show first training image
    # plt.imshow(x_train[0], cmap='Greys')
    # plt.show()

    neural_net = NeuralNetwork()

    neural_net.open_load()

    # neural_net.train(x_train, y_train)
    neural_net.test(x_test, y_test)
    # neural_net.save()

    data = [[1, 2], [3, 4]]
    image = np.array(data)
    # TODO: image goes here ^