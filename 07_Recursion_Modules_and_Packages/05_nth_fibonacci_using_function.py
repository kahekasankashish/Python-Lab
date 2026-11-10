# Q5. Print the nth Fibonacci number/series using a function.
def fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    first, second = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(first)
        first, second = second, first + second
    return sequence

n = int(input("Enter number of terms: "))
try:
    print("Fibonacci series:", fibonacci(n))
except ValueError as error:
    print(error)
