"""
Question: Write a program to calculate the sum of the first n natural numbers, where n is provided by the user.
"""

n = int(input("Enter n: "))
total = 0

for number in range(1, n + 1):
    total += number

print("Sum of first", n, "natural numbers:", total)
