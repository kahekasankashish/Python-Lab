"""
Question: Write a Python program to evaluate the cosine series using Taylor series expansion. The program should compute cos(x) up to a user-specified number of terms.
"""

import math

x = float(input("Enter x in radians: "))
terms = int(input("Enter number of terms: "))

if terms < 1:
    print("Number of terms must be at least 1.")
else:
    total = 0.0
    term = 1.0
    for index in range(terms):
        if index == 0:
            term = 1.0
        else:
            term *= -(x * x) / ((2 * index - 1) * (2 * index))
        total += term
    print("Taylor series approximation of cos(x):", total)
