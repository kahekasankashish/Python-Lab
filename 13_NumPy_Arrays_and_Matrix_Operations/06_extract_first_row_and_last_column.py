# Q6. Create a 4×4 array and extract its first row and last column.
import numpy as np

array = np.arange(1, 17).reshape(4, 4)
print("Array:\n", array)
print("First row:", array[0, :])
print("Last column:", array[:, -1])
