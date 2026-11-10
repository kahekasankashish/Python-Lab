# Q7. Find the greatest among three numbers using a lambda function.
greatest = lambda a, b, c: max(a, b, c)

a, b, c = map(float, input("Enter three numbers: ").split())
print("Greatest:", greatest(a, b, c))
