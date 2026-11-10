# Q21. Create coefficient matrix A and constant matrix B (user inputs), solve the system using NumPy, verify the solution by substituting back, and handle the singular matrix case.
import numpy as np

n = int(input("Enter number of variables/equations: "))
if n <= 0:
    raise ValueError("Number must be positive.")

A_rows = []
for index in range(n):
    row = list(map(float, input(f"Enter coefficients for equation {index + 1} ({n} values): ").split()))
    if len(row) != n:
        raise ValueError(f"Enter exactly {n} coefficients.")
    A_rows.append(row)
B_values = list(map(float, input(f"Enter {n} constants separated by spaces: ").split()))
if len(B_values) != n:
    raise ValueError(f"Enter exactly {n} constants.")

A = np.array(A_rows, dtype=float)
B = np.array(B_values, dtype=float)

try:
    solution = np.linalg.solve(A, B)
    print("Solution:", solution)
    print("Verification A @ solution:", A @ solution)
    print("Original constants B:", B)
    print("Verified:", np.allclose(A @ solution, B))
except np.linalg.LinAlgError:
    print("The coefficient matrix is singular; a unique solution cannot be computed.")
