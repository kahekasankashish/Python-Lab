"""
Question: Write a program to verify whether a number input by the user is a palindrome.
"""

number = input("Enter an integer: ").strip()

if number.startswith("-"):
    print(number, "is not a palindrome.")
elif number == number[::-1]:
    print(number, "is a palindrome.")
else:
    print(number, "is not a palindrome.")
