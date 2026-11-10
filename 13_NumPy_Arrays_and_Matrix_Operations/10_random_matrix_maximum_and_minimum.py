# Q10. Create a random 3×2 matrix and find its maximum and minimum values.
import numpy as np

matrix = np.random.randint(0, 100, size=(3, 2))
print("Random matrix:\n", matrix)
print("Maximum:", matrix.max())
print("Minimum:", matrix.min())
