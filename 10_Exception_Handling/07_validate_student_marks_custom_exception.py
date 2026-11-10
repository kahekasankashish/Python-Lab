# Q7. Write a Python program to input student marks. If marks are less than 0 or greater than 100, raise a user-defined exception called InvalidMarksError.
class InvalidMarksError(Exception):
    pass

try:
    marks = float(input("Enter marks of student: "))
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Invalid marks.")
    print("Valid marks:", marks)
except ValueError:
    print("Error: Marks must be a number.")
except InvalidMarksError as error:
    print(error)
