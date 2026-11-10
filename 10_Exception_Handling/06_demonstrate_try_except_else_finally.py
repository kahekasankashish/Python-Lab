# Q6. Write a Python program demonstrating the use of try, except, else, and finally blocks.
try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    result = numerator / denominator
except ValueError:
    print("Error: Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("Result:", result)
finally:
    print("Finally block executed.")
