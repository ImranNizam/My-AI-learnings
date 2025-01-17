# -*- coding: utf-8 -*-
"""MNIST Dataset.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1f3rkbZ6d68tPAjZ_RXq5OP9fpRNfGUBy
"""

from keras.datasets import mnist
from keras.utils import to_categorical
from keras import models
from keras import layers
from matplotlib import pyplot as plt

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print('Label of the below shown picture is ',train_labels[0])
plt.imshow(train_images[0])
plt.show()

'''
train_images = train_images.reshape((60000, 28*28))
train_images = train_images.astype('float32')/255

test_images = test_images.reshape((10000, 28*28))
test_images = test_images.astype('float32')/255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

network = models.Sequential()

network.add(layers.Dense(512, activation = 'relu', input_shape = (28*28,)))
network.add(layers.Dense(10, activation = 'softmax'))

network.compile(optimizer = 'rmsprop', loss = 'categorical_crossentropy', metrics = ['accuracy'])

network.fit(train_images, train_labels, epochs = 5, batch_size = 128)

a, b = network.evaluate(test_images, test_labels)

print(a,b)
'''