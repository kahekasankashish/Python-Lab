"""
Question: Write a program to display all factors of a given number.
"""

number = int(input("Enter a positive integer: "))

if number <= 0:
    print("Please enter a positive integer.")
else:
    print("Factors:")
    for factor in range(1, number + 1):
        if number % factor == 0:
            print(factor)
