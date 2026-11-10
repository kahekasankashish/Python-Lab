"""
Question: Write a Python program to evaluate the sine series using Taylor series expansion. The program should compute sin(x) up to a user-specified number of terms.
"""

import math

x = float(input("Enter x in radians: "))
terms = int(input("Enter number of terms: "))

if terms < 1:
    print("Number of terms must be at least 1.")
else:
    total = 0.0
    term = x
    for index in range(terms):
        if index == 0:
            term = x
        else:
            term *= -(x * x) / ((2 * index) * (2 * index + 1))
        total += term
    print("Taylor series approximation of sin(x):", total)
