# Q5. Take a list of numbers and return a new list which contains only the distinct elements of the first list.
def distinct_elements(numbers):
    result = []
    for number in numbers:
        if number not in result:
            result.append(number)
    return result

values = list(map(float, input("Enter numbers separated by spaces: ").split()))
print("Distinct elements:", distinct_elements(values))
