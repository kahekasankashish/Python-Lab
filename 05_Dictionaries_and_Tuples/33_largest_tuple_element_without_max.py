# Q33. Display the largest number of a tuple without using max(); input tuple values from the keyboard.
numbers = tuple(map(float, input("Enter numbers separated by spaces: ").split()))
if not numbers:
    print("The tuple is empty")
else:
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    print("Largest number:", largest)
