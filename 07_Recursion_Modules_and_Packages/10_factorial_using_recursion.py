# Q10. Write a program to find the factorial of a number using recursion.
def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative integers")
    if number <= 1:
        return 1
    return number * factorial(number - 1)

number = int(input("Enter a non-negative integer: "))
try:
    print("Factorial:", factorial(number))
except ValueError as error:
    print(error)
