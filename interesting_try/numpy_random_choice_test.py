import numpy as np

# Initialize the 1-D array
a1 = np.array([1, 2, 3, 4, 5])

# Sampling
for i in range(5):
    print(np.random.choice(a1, 3, True, p = (0.9999, 0.0001, 0.0000000, 0.000000, 0)))

