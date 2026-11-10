# Q7. Display the total number of lines, words and characters in sample.txt.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()

    line_count = len(content.splitlines())
    word_count = len(content.split())
    character_count = len(content)

    print("Total lines:", line_count)
    print("Total words:", word_count)
    print("Total characters:", character_count)
except FileNotFoundError:
    print('sample.txt not found. Run Q2 first to create it.')
