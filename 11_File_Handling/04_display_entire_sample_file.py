# Q4. Display the contents of sample.txt.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print('sample.txt not found. Run Q2 first to create it.')
