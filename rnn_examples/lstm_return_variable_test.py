import tensorflow as tf
import numpy as np

# m = 1, time steps = 5, dimension = 2
input = tf.random.normal([1, 5, 2])
# print(input)

# # set output's dimension to 3
# lstm = tf.keras.layers.LSTM(3)
# output = lstm(input)
#
# print("The last output:", output.shape)
# print(output)

lstm2 = tf.keras.layers.LSTM(3, return_sequences = True, return_state = True)

a, _, c = lstm2(input)

print("The output sequence:", a.shape)
print(a)
print(_)
print(c)
