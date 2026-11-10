# Q11. Write a Python program that accepts a number from the user. If the number is negative, raise a user-defined exception called NegativeNumberError.
class NegativeNumberError(Exception):
    pass

try:
    number = float(input("Enter a number: "))
    if number < 0:
        raise NegativeNumberError("Negative Number.")
    print("Valid number:", number)
except ValueError:
    print("Error: Please enter a valid number.")
except NegativeNumberError as error:
    print(error)
