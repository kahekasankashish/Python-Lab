# Question 2: Input two numbers and design a calculator using +, -, *, %, and / operators.
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
if b != 0:
    print("Modulus:", a % b)
    print("Division:", a / b)
else:
    print("Modulus and division are undefined because the second number is zero.")
