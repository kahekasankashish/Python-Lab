# Q8. Display the frequency of a given word in sample.txt.
import re

word = input("Enter the word to search: ").strip()
if not word:
    print("Please enter a non-empty word.")
else:
    try:
        with open("sample.txt", "r", encoding="utf-8") as file:
            content = file.read()

        pattern = rf"\b{re.escape(word)}\b"
        frequency = len(re.findall(pattern, content, flags=re.IGNORECASE))
        print(f"Frequency of '{word}':", frequency)
    except FileNotFoundError:
        print('sample.txt not found. Run Q2 first to create it.')
