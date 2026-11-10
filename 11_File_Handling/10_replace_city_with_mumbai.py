# Q10. Replace every occurrence of the word "city" in mumbai.txt with "Mumbai".
try:
    with open("mumbai.txt", "r", encoding="utf-8") as file:
        content = file.read()

    updated_content = content.replace("city", "Mumbai")

    with open("mumbai.txt", "w", encoding="utf-8") as file:
        file.write(updated_content)

    print('Every occurrence of "city" has been replaced with "Mumbai" in mumbai.txt.')
except FileNotFoundError:
    print('mumbai.txt not found. Run Q9 first to create it.')
except OSError as error:
    print("File operation failed:", error)
