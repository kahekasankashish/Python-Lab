# Q4. Find the factorial of an integer using a function.
def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative integers")
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result

number = int(input("Enter a non-negative integer: "))
try:
    print("Factorial:", factorial(number))
except ValueError as error:
    print(error)
