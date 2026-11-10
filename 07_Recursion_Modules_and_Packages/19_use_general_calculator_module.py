# Q19. Create a module for a general calculator and use its functionality through the module.
import general_calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Addition:", general_calculator.add(a, b))
print("Subtraction:", general_calculator.subtract(a, b))
print("Multiplication:", general_calculator.multiply(a, b))
try:
    print("Division:", general_calculator.divide(a, b))
except ZeroDivisionError as error:
    print(error)
