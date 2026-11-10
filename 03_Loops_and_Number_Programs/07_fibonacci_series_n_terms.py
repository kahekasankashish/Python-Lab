"""
Question: Write a program to display the Fibonacci series up to the n-th term.
"""

n = int(input("Enter the number of terms: "))
a, b = 0, 1

for _ in range(max(0, n)):
    print(a, end=" ")
    a, b = b, a + b
print()
