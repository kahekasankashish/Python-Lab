# Q2. Write a program to accept an integer from the user. Handle the exception if the user enters a non-integer value.
try:
    number = int(input("Enter an integer: "))
    print("Entered integer:", number)
except ValueError:
    print("Error: Please enter a valid integer.")
