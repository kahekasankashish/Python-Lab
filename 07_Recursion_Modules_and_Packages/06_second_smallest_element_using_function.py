# Q6. Define a function that takes a list as a parameter and returns its second smallest element.
def second_smallest(values):
    distinct_values = sorted(set(values))
    if len(distinct_values) < 2:
        raise ValueError("At least two distinct elements are required")
    return distinct_values[1]

numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
try:
    print("Second smallest:", second_smallest(numbers))
except ValueError as error:
    print(error)
