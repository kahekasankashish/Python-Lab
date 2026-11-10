# Q1. Write a code to convert a 1D array to a 2D array with 2 rows.
import numpy as np

values = np.array([1, 2, 3, 4, 5, 6])
if values.size % 2 != 0:
    raise ValueError("The number of elements must be even to reshape into 2 rows.")
result = values.reshape(2, -1)
print(result)
