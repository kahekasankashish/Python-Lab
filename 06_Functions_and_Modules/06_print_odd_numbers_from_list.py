# Q6. Print the odd numbers from a given list by taking the list as an argument to the function.
def print_odd_numbers(numbers):
    odds = [number for number in numbers if number % 2 != 0]
    print("Odd numbers:", odds)

values = list(map(int, input("Enter integers separated by spaces: ").split()))
print_odd_numbers(values)
