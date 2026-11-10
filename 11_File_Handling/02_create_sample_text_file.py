# Q2. Create a file "sample.txt" with the given content: "Life in the city is full of activity. Early in the morning, hundreds of people rush out of their homes. Soon, the streets are full of traffic, shops and offices open, and the day's work begins."
content = (
    "Life in the city is full of activity. Early in the morning, hundreds of people rush out of their homes.\n"
    "Soon, the streets are full of traffic, shops and offices open, and the day's work begins."
)

with open("sample.txt", "w", encoding="utf-8") as file:
    file.write(content)

print('File "sample.txt" created successfully.')
