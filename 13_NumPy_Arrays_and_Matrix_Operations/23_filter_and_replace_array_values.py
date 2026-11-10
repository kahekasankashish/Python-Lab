# Q23. Create an array of integers; filter elements greater than a given value; replace negative values with zero; count filtered elements; display results.
import numpy as np

values = np.array(list(map(int, input("Enter integers separated by spaces: ").split())))
threshold = int(input("Enter threshold value: "))
filtered = values[values > threshold]
updated = np.where(values < 0, 0, values)
print("Original array:", values)
print("Elements greater than threshold:", filtered)
print("Array after replacing negative values with zero:", updated)
print("Number of filtered elements:", filtered.size)
