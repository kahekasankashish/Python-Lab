# Q12. Swap column 1 and 2 in a 2D array.
import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original array:\n", array)
array[:, [0, 1]] = array[:, [1, 0]]
print("After swapping columns 1 and 2:\n", array)
