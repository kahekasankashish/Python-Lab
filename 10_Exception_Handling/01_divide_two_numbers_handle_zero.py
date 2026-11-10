# Q1. Write a Python program to divide two numbers entered by the user. Handle the exception if the denominator is zero.
try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
