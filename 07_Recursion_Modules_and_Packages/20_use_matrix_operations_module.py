# Q20. Create a module for matrix operations and use its functionality through the module.
import matrix_operations

first = [[1, 2], [3, 4]]
second = [[5, 6], [7, 8]]
print("First matrix:", first)
print("Second matrix:", second)
print("Addition:", matrix_operations.add_matrices(first, second))
print("Transpose of first matrix:", matrix_operations.transpose(first))
