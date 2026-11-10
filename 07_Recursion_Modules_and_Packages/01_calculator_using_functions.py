# Q1. Read two numbers and a character (+, -, *, /), then perform the corresponding calculation using a separate function for each operation.
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operation (+, -, *, /): ").strip()
operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
if operator not in operations:
    print("Invalid operator")
else:
    try:
        print("Result:", operations[operator](a, b))
    except ZeroDivisionError as error:
        print(error)
