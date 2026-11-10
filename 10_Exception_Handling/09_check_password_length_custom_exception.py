# Q9. Write a Python program to check the password entered by a user. If the password length is less than 8 characters, raise a user-defined exception called WeakPasswordError.
class WeakPasswordError(Exception):
    pass

try:
    password = input("Enter password: ")
    if len(password) < 8:
        raise WeakPasswordError("Weak Password")
    print("Password length is valid.")
except WeakPasswordError as error:
    print(error)
