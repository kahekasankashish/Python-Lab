# Q4. Write a Python program to open and read a file. Handle the exception if the file does not exist.
filename = input("Enter file name: ")
try:
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: File not found.")
