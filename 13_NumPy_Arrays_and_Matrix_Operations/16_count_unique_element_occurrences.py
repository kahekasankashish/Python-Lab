# Q16. Count the number of occurrences of each unique element.
import numpy as np

array = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
unique, counts = np.unique(array, return_counts=True)
for value, count in zip(unique, counts):
    print(f"{value}: {count}")
