# Q2. Print the twin prime numbers between 2 to 100. Twin primes are pairs of prime numbers that have a difference of exactly two.
def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

for number in range(2, 99):
    if is_prime(number) and is_prime(number + 2):
        print((number, number + 2))
