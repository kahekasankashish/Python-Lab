# Q14. Write a Python program for a product inventory system. If the user tries to purchase more items than available in stock, raise a user-defined exception called OutOfStockError.
class OutOfStockError(Exception):
    pass


inventory = {}
number_of_products = int(input("Enter number of products: "))

for index in range(number_of_products):
    name = input("Enter name of product: ").strip()
    stock = int(input("Enter stock: "))
    inventory[name] = stock

product = input("Enter the product you want to buy: ").strip()
try:
    if product not in inventory:
        raise OutOfStockError("Product is not available.")
    quantity = int(input("How many? "))
    if quantity <= 0:
        raise ValueError("Quantity must be positive.")
    if quantity > inventory[product]:
        raise OutOfStockError("Quantity ordered is not available.")
    inventory[product] -= quantity
    print("Purchase successful.")
    print("Remaining stock:", inventory[product])
except ValueError as error:
    print("Invalid quantity:", error)
except OutOfStockError as error:
    print(error)
