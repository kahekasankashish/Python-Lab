# Q7. Extract odd rows and even columns from a NumPy array.
import numpy as np

array = np.arange(1, 26).reshape(5, 5)
# Odd rows and even columns are interpreted as 1-based positions.
result = array[0::2, 1::2]
print("Original array:\n", array)
print("Odd rows and even columns:\n", result)
