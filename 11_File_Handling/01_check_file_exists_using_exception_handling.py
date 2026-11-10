# Q1. Write a function that takes a filename as input and returns True if the file exists and False otherwise using exception handling.
def file_exists(filename):
    try:
        with open(filename, "r", encoding="utf-8"):
            return True
    except FileNotFoundError:
        return False
    except OSError:
        return False

filename = input("Enter filename: ")
print(file_exists(filename))
