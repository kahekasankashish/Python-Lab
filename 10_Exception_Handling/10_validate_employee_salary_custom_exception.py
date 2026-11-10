# Q10. Write a Python program to input employee salary. If salary is less than ₹15000, raise a user-defined exception called LowSalaryError.
class LowSalaryError(Exception):
    pass

try:
    salary = float(input("Enter salary: "))
    if salary < 15000:
        raise LowSalaryError("Low Salary.")
    print("Valid salary:", salary)
except ValueError:
    print("Error: Salary must be numeric.")
except LowSalaryError as error:
    print(error)
