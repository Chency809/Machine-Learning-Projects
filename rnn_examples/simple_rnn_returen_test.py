#!/usr/bin/env python3
# @Time    : 6/9/2020 6:49 PM
# @Author  : Chency Liu
# @School  : Cornell College
# @FileName: simple_rnn_returen_test.py
# @Software: PyCharm
# @Github  : https://github.com/Chency809?tab=repositories

# Import tensorflow and related libraries
import tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, SimpleRNNCell
import numpy as np

# Intialize the constant parameters
SAMPLE = 20
TIME_STEPS = 10
FEATURES = 100

# Create x, y for train
x = np.random.random((SAMPLE, TIME_STEPS, FEATURES)).astype(np.float32)
y = np.random.random((TIME_STEPS, FEATURES))

# Try different types of rnn architecture
simple_rnn = SimpleRNN(5)
output = simple_rnn(x)
print("Many to one: ", output.shape)

simple_rnn_return = SimpleRNN(5, return_sequences = True)
output = simple_rnn_return(x)
print("Many to Many", output.shape)

simple_rnn = SimpleRNN(5)
output = simple_rnn(np.random.random((SAMPLE, 1, FEATURES)).astype(np.float32))
print("One to one:", output.shape)
