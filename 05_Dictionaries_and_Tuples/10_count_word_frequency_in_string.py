# Q10. Count and display the frequency of each word appearing in a given string using a dictionary.
sentence = input("Enter a string: ")
frequency = {}
for word in sentence.split():
    word = word.strip(".,!?;:\"'()[]{}").lower()
    if word:
        frequency[word] = frequency.get(word, 0) + 1
for word, count in frequency.items():
    print(f"{word}: {count}")
