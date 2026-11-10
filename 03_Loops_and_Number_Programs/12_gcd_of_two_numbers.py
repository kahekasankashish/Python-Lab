"""
Question: Write a program that takes two numbers as input and computes their Greatest Common Divisor (GCD).
"""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
x, y = abs(a), abs(b)

while y:
    x, y = y, x % y

print("GCD:", x)
