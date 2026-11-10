# Q9. Write a code to extract all numbers from an array that are between 5 and 10 (inclusive).
import numpy as np

array = np.array([2, 5, 7, 10, 12, 8, 4, 11])
print(array[(array >= 5) & (array <= 10)])
