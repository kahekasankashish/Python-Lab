# Q10. Find the first ten Fibonacci numbers using both recursive and non-recursive functions.
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(count):
    sequence = []
    first, second = 0, 1
    for _ in range(count):
        sequence.append(first)
        first, second = second, first + second
    return sequence

print("Recursive:", [fibonacci_recursive(index) for index in range(10)])
print("Non-recursive:", fibonacci_iterative(10))
