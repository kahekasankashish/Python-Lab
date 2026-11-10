# Q11. Delete and insert a column in a NumPy array.
import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original array:\n", array)
column_to_delete = 1
deleted = np.delete(array, column_to_delete, axis=1)
print("After deleting column at index 1:\n", deleted)
new_column = np.array([10, 20, 30])
updated = np.insert(deleted, 1, new_column, axis=1)
print("After inserting a new column at index 1:\n", updated)
