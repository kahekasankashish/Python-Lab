# Q8. Use lambda functions to perform various tasks like addition, subtraction, multiplication, division and modulus.
operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '%': lambda a, b: a % b
}

a, b = map(float, input("Enter two numbers: ").split())
operator = input("Choose an operator (+, -, *, /, %): ").strip()
if operator not in operations:
    print("Invalid operator")
elif operator in ('/', '%') and b == 0:
    print("Division or modulus by zero is not allowed")
else:
    print("Result:", operations[operator](a, b))
