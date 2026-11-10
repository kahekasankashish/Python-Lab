# Question 16: Add two matrices.
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
print("Enter the first matrix row by row:")
a = [list(map(int, input().split())) for _ in range(rows)]
print("Enter the second matrix row by row:")
b = [list(map(int, input().split())) for _ in range(rows)]
if any(len(row) != cols for row in a + b):
    print("Each row must contain exactly", cols, "elements.")
else:
    result = [[a[i][j] + b[i][j] for j in range(cols)] for i in range(rows)]
    print("Sum of matrices:")
    for row in result:
        print(*row)
