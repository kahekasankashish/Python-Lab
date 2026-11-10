# Q9. Copy the contents of sample.txt into mumbai.txt.
try:
    with open("sample.txt", "r", encoding="utf-8") as source:
        content = source.read()

    with open("mumbai.txt", "w", encoding="utf-8") as destination:
        destination.write(content)

    print('Contents copied from sample.txt to mumbai.txt successfully.')
except FileNotFoundError:
    print('sample.txt not found. Run Q2 first to create it.')
except OSError as error:
    print("File operation failed:", error)
