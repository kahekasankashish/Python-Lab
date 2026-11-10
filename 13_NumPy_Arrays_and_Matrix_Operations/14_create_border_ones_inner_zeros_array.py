# Q14. Create a 5×5 2D array with 1s on the border and 0s inside.
import numpy as np

array = np.zeros((5, 5), dtype=int)
array[0, :] = array[-1, :] = 1
array[:, 0] = array[:, -1] = 1
print(array)
