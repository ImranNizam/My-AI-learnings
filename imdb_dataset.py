# -*- coding: utf-8 -*-
"""IMDB Dataset.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZYAefW6ZYoXlw9xwBix2cPTZarDWrm5E
"""

from keras.datasets import imdb
from keras import models
from keras import layers
import numpy as np

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words = 10000)


def vectorize_data(sequences, dimension=10000):
  results = np.zeros((len(sequences), dimension))
  for i, sequence in enumerate(sequences):
    for item in sequence:
      results[i, item] = 1
  return results

train_data = vectorize_data(train_data)
test_data = vectorize_data(test_data)
train_labels = np.asarray(train_labels).astype('float32')
test_labels = np.asarray(test_labels).astype('float32')

network = models.Sequential()

network.add(layers.Dense(4, activation='relu', input_shape=((10000,))))
network.add(layers.Dense(4, activation='relu'))
network.add(layers.Dense(4, activation='relu'))
network.add(layers.Dense(1, activation='sigmoid'))

network.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
network.fit(train_data, train_labels, epochs=5)

a,b = network.evaluate(test_data, test_labels)

print(a,b)

print(train_data[0])
print(train_labels[0])
