"""
Question: Write a program to find the sum of squares of the first n odd numbers.
"""

n = int(input("Enter n: "))
total = 0

for index in range(n):
    odd_number = 2 * index + 1
    total += odd_number ** 2

print("Sum of squares:", total)
