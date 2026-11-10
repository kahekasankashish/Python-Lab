# Q17. Transposing a matrix means flipping it over its diagonal. Write a program to transpose a matrix.
import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Original matrix:\n", matrix)
print("Transpose:\n", matrix.T)
