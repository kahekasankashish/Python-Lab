# Q7. Remove a key from a dictionary.
data = {'a': 1, 'b': 2, 'c': 3}
key = input("Enter the key to remove: ")
if key in data:
    del data[key]
    print("Updated dictionary:", data)
else:
    print("Key not found")
