# Q8. Find the common items between two arrays.
import numpy as np

first = np.array([1, 2, 3, 4, 5])
second = np.array([3, 4, 5, 6, 7])
print("Common items:", np.intersect1d(first, second))
