# Q20. Create a 1D array of n elements (user input), reshape it into a 2D array, flatten it, sort elements ascending and descending, and find maximum, minimum and their indices.
import numpy as np

n = int(input("Enter number of elements: "))
if n <= 0:
    raise ValueError("Number of elements must be positive.")
values = np.array(list(map(float, input(f"Enter {n} numbers: ").split())))
if values.size != n:
    raise ValueError(f"Please enter exactly {n} numbers.")

rows = int(input("Enter number of rows for reshaping: "))
if rows <= 0 or n % rows != 0:
    raise ValueError("Rows must be positive and divide the number of elements exactly.")

matrix = values.reshape(rows, n // rows)
flattened = matrix.flatten()
ascending = np.sort(flattened)
descending = ascending[::-1]
maximum = flattened.max()
minimum = flattened.min()

print("2D array:\n", matrix)
print("Flattened array:", flattened)
print("Ascending:", ascending)
print("Descending:", descending)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Index/indices of maximum in flattened array:", np.where(flattened == maximum)[0])
print("Index/indices of minimum in flattened array:", np.where(flattened == minimum)[0])
