# Q22. Create a 5×5 array; extract first row, last column, diagonal and center 3×3 submatrix; replace all even numbers with zero; count odd elements.
import numpy as np

array = np.arange(1, 26).reshape(5, 5)
print("Original array:\n", array)
print("First row:", array[0, :])
print("Last column:", array[:, -1])
print("Diagonal:", np.diag(array))
print("Center 3×3 submatrix:\n", array[1:4, 1:4])

updated = array.copy()
updated[updated % 2 == 0] = 0
print("After replacing even values with zero:\n", updated)
print("Number of odd elements in original array:", np.count_nonzero(array % 2 != 0))
