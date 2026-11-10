# Q14. Define a recursive function to print the Fibonacci series using recursion and a dictionary.
memo = {0: 0, 1: 1}

def fibonacci(n):
    if n not in memo:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]

terms = int(input("Enter number of terms: "))
if terms < 0:
    print("Number of terms cannot be negative")
else:
    print("Fibonacci series:", [fibonacci(index) for index in range(terms)])
