# Q2. Write a program to find the largest of three numbers using nested conditional operators.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
largest = a if a > b and a > c else (b if b > c else c)
print("Largest number:", largest)
