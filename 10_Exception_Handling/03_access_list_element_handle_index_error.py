# Q3. Write a Python program to access an element from a list using an index provided by the user. Handle the exception if the index is out of range.
values = [1, 2, 3, 4]
try:
    index = int(input("Enter the index: "))
    print("Element:", values[index])
except ValueError:
    print("Error: Index must be an integer.")
except IndexError:
    print("Error: Index is out of range.")
