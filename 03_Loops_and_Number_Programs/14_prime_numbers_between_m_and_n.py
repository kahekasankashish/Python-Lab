"""
Question: Write a program to display all prime numbers between m and n, where m < n.
"""

m = int(input("Enter m: "))
n = int(input("Enter n (greater than m): "))

if m >= n:
    print("Please ensure m is less than n.")
else:
    print(f"Prime numbers between {m} and {n}:")
    for number in range(max(2, m), n + 1):
        is_prime = True
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            print(number)
