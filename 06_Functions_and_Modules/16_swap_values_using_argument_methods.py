# Q16. Swap the values between two numbers. Create a menu for: (a) positional arguments, (b) variable arguments, (c) keyword arguments, and (d) returning the swapped values in two variables.
def swap_positional(first, second):
    return second, first

def swap_variable(*values):
    if len(values) != 2:
        raise ValueError("Exactly two values are required")
    return values[1], values[0]

def swap_keyword(*, first, second):
    return second, first

def swap_and_return(first, second):
    first, second = second, first
    return first, second

print("1. Swap using positional arguments")
print("2. Swap using variable arguments")
print("3. Swap using keyword arguments")
print("4. Return swapped values in two variables")
choice = input("Enter your choice (1-4): ").strip()
a = input("Enter first value: ")
b = input("Enter second value: ")

if choice == '1':
    a, b = swap_positional(a, b)
elif choice == '2':
    a, b = swap_variable(a, b)
elif choice == '3':
    a, b = swap_keyword(first=a, second=b)
elif choice == '4':
    a, b = swap_and_return(a, b)
else:
    print("Invalid choice")
    raise SystemExit

print("After swapping:")
print("First value:", a)
print("Second value:", b)
