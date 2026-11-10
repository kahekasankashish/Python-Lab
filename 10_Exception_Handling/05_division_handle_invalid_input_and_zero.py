# Q5. Write a program that takes two inputs and performs division. Handle both invalid input and division by zero.
try:
    numerator = float(input("Enter a number: "))
    denominator = float(input("Enter another number: "))
    result = numerator / denominator
except ValueError:
    print("Error: Invalid input for division.")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
else:
    print("Result:", result)
