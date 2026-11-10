# Q2. Define a function that takes one number as a parameter and returns True if it is prime, otherwise False.
def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

number = int(input("Enter an integer: "))
print(is_prime(number))
