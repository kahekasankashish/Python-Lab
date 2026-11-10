"""
Question: Write a program to display the multiplication tables from 1 to 10.
"""

for number in range(1, 11):
    print(f"\nMultiplication table of {number}:")
    for multiplier in range(1, 11):
        print(f"{number} x {multiplier} = {number * multiplier}")
