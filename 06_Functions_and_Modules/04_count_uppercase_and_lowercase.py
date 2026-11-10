# Q4. Accept a string and count the number of upper and lower case letters.
def count_case(value):
    uppercase = sum(character.isupper() for character in value)
    lowercase = sum(character.islower() for character in value)
    return uppercase, lowercase

text = input("Enter a string: ")
upper, lower = count_case(text)
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
