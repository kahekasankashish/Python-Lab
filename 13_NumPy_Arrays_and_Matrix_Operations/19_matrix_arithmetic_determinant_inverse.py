# Q19. Input two matrices; perform addition, subtraction and multiplication; find transpose of both; compute determinant and inverse if possible; display results neatly.
import numpy as np

rows_a = int(input("Enter rows of matrix A: "))
cols_a = int(input("Enter columns of matrix A: "))
rows_b = int(input("Enter rows of matrix B: "))
cols_b = int(input("Enter columns of matrix B: "))

def read_matrix(rows, cols, name):
    print(f"Enter {rows} rows for matrix {name}, with {cols} space-separated values per row:")
    data = []
    for index in range(rows):
        row = list(map(float, input(f"{name} row {index + 1}: ").split()))
        if len(row) != cols:
            raise ValueError(f"Each row of {name} must contain exactly {cols} values.")
        data.append(row)
    return np.array(data)

A = read_matrix(rows_a, cols_a, "A")
B = read_matrix(rows_b, cols_b, "B")

print("A + B:")
if A.shape == B.shape:
    print(A + B)
else:
    print("Not possible: matrix dimensions must match.")

print("A - B:")
if A.shape == B.shape:
    print(A - B)
else:
    print("Not possible: matrix dimensions must match.")

print("A × B:")
if cols_a == rows_b:
    print(A @ B)
else:
    print("Not possible: columns of A must equal rows of B.")

print("Transpose of A:\n", A.T)
print("Transpose of B:\n", B.T)

for name, matrix in (("A", A), ("B", B)):
    if matrix.shape[0] != matrix.shape[1]:
        print(f"Determinant and inverse of {name}: not possible for a non-square matrix.")
        continue
    determinant = np.linalg.det(matrix)
    print(f"Determinant of {name}: {determinant:.6g}")
    if np.isclose(determinant, 0):
        print(f"Inverse of {name}: does not exist (singular matrix).")
    else:
        print(f"Inverse of {name}:\n", np.linalg.inv(matrix))
