# -*- coding: utf-8 -*-
"""Reuters Dataset.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1t8s-W0F70N_kT0ANOCd553UJ_tX7j6Ze
"""

from keras.datasets import reuters
from keras import models
from keras import layers
from keras.utils import to_categorical
import numpy as np

(train_data, train_labels), (test_data, test_labels) = reuters.load_data(num_words=10000)

'''
library = reuters.get_word_index()
reverse_word_index = dict([(number, word) for (word, number) in library.items()])
decoded_words = ' '.join([reverse_word_index.get(i-3, '?') for i in train_data[0]])
print(decoded_words)
'''

def vectorize_data(samples, dimension=10000):
  result = np.zeros((len(samples), dimension))
  for i, sample in enumerate(samples):
    for item in sample:
      result[i][item] = 1
  return result

train_data = vectorize_data(train_data)
test_data = vectorize_data(test_data)
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

network = models.Sequential()

network.add(layers.Dense(64, activation='relu', input_shape=((10000,))))
network.add(layers.Dense(64, activation='relu'))
network.add(layers.Dense(46, activation='softmax'))
network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
network.fit(train_data, train_labels, epochs=10, batch_size=128)
a,b = network.evaluate(test_data, test_labels)
print(a,b)