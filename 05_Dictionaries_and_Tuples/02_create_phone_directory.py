# Q2. Create a phone directory of your friends and display it.
phone_directory = {}
while True:
    name = input("Enter friend's name (or 'done' to finish): ").strip()
    if name.lower() == "done":
        break
    phone = input("Enter phone number: ").strip()
    phone_directory[name] = phone
print("\nPhone directory:")
for name, phone in phone_directory.items():
    print(f"{name}: {phone}")
