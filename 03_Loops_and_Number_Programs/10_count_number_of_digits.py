"""
Question: Write a program that takes an integer as input and determines the total number of digits present in the number.
"""

number = int(input("Enter an integer: "))
print("Number of digits:", len(str(abs(number))))
