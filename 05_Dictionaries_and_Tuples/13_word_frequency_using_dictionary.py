# Q13. Program to count and display the frequency of a word appearing in a given string using a dictionary.
text = input("Enter a string: ")
word_to_count = input("Enter the word whose frequency you want: ").strip().lower()
words = [word.strip(".,!?;:\"'()[]{}").lower() for word in text.split()]
frequency = {}
for word in words:
    if word:
        frequency[word] = frequency.get(word, 0) + 1
print(f"Frequency of '{word_to_count}':", frequency.get(word_to_count, 0))
