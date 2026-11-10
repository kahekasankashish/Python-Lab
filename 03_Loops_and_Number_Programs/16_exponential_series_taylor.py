"""
Question: Write a Python program to evaluate the exponential series using its Taylor series expansion. The program should compute the value of e^x up to a user-specified number of terms.
"""

import math

x = float(input("Enter x: "))
terms = int(input("Enter number of terms: "))

if terms < 1:
    print("Number of terms must be at least 1.")
else:
    total = 0.0
    term = 1.0
    for index in range(terms):
        if index == 0:
            term = 1.0
        elif index > 0:
            term *= x / index
        total += term
    print("Taylor series approximation of e^x:", total)
