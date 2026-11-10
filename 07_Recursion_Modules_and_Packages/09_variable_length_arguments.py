# Q9. Define a Python function that takes variable-length arguments and prints them.
def display_values(*args):
    for value in args:
        print(value)

display_values(10, 20, 30, "Python")
