# Q12. Write a program to find the sum of digits of a number using recursion.
def sum_of_digits(number):
    number = abs(number)
    if number < 10:
        return number
    return number % 10 + sum_of_digits(number // 10)

number = int(input("Enter an integer: "))
print("Sum of digits:", sum_of_digits(number))
