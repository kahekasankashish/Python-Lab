# Q8. Write a Python program to input age of a person. If age is less than 18, raise a user-defined exception called InvalidAgeError and display the message "Not eligible to vote".
class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise InvalidAgeError("Not eligible to vote")
    print("Eligible to vote.")
except ValueError:
    print("Error: Age must be an integer.")
except InvalidAgeError as error:
    print(error)
