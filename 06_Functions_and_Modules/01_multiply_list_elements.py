# Q1. Multiply the numbers present in a list and display the final product.
def multiply_list(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

values = list(map(float, input("Enter numbers separated by spaces: ").split()))
print("Product:", multiply_list(values))
