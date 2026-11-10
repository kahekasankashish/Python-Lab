# Q6. Read and display only the first 2 lines of sample.txt.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        for _ in range(2):
            line = file.readline()
            if not line:
                break
            print(line, end="")
except FileNotFoundError:
    print('sample.txt not found. Run Q2 first to create it.')
