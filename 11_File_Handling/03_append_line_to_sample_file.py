# Q3. Append the following line to sample.txt: "The city now throbs with activity, and it is full of noise."
line = "The city now throbs with activity, and it is full of noise.\n"

try:
    with open("sample.txt", "a", encoding="utf-8") as file:
        file.write(line)
    print("Line appended successfully.")
except OSError as error:
    print("Unable to append to sample.txt:", error)
