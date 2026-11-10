# Q15. Sort the rows of a 2D array based on the values of the second column.
import numpy as np

array = np.array([[3, 8, 1], [2, 4, 9], [5, 6, 7]])
result = array[array[:, 1].argsort()]
print("Original array:\n", array)
print("Sorted by second column:\n", result)
