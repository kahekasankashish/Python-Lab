# Q13. Create a 3×3 array of random integers and sort it row-wise.
import numpy as np

matrix = np.random.randint(1, 100, size=(3, 3))
print("Original matrix:\n", matrix)
print("Row-wise sorted matrix:\n", np.sort(matrix, axis=1))
