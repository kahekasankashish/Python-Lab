# Q3. Check whether a given key already exists in a dictionary or not.
sample = {'a': 1, 'b': 2, 'c': 3}
key = input("Enter the key to search for: ")
if key in sample:
    print("Key is present")
else:
    print("Key is not present")
