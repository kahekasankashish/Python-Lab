# Q5. Display the contents of sample.txt line by line.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
except FileNotFoundError:
    print('sample.txt not found. Run Q2 first to create it.')
