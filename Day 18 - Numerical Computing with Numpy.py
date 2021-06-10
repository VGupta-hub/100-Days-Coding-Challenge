!pip install numpy

import numpy as np

Numpy arrays can be created using the np.array function

kanto = np.array([73, 67, 43])

kanto

type(kanto)

# Operating on Numpy arrays

We can now compute the dot product of the two vectors using the np.dot function.

weights = np.array([0.3, 0.2, 0.5])

np.dot(kanto,weights)

kanto*weights

in the above, the vectors are multiplied with each other(0.3*21.9,0.2*13.4,0.5*21.5).
We can take the sum of the number calculated by calling the.sum() function.

(kanto*weights).sum()

# Multi-dimensional Numpy Arrays

climate_data = np.array([[73,67,43],
                        [91,88,64],
                        [87,134,57],
                        [102,43,37],
                        [69,96,70]])

climate_data

Numpy arrays can have any number of dimesions and different lengths along each dimension. We can inspect the length along each dimension using the .shape property of an array.

climate_data.shape

weights

weights.shape

