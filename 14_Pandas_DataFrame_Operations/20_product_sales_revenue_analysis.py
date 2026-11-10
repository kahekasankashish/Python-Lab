# Q20. Create a product sales DataFrame with ProductID, ProductName, Category, Price and Quantity. Calculate total revenue, find top-selling products, filter low-sales products, group by category for total revenue, and export results to Excel.
import pandas as pd

products = pd.DataFrame({
    "ProductID": [101, 102, 103, 104, 105, 106],
    "ProductName": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", "Webcam"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Accessories", "Electronics"],
    "Price": [55000, 700, 1200, 12000, 2500, 1800],
    "Quantity": [8, 50, 30, 12, 20, 7]
})

products["Revenue"] = products["Price"] * products["Quantity"]
print("Total revenue:", products["Revenue"].sum())

maximum_quantity = products["Quantity"].max()
print("\nTop-selling product(s) by quantity sold:")
print(products[products["Quantity"] == maximum_quantity])

# The question does not define 'low sales'; here it means quantity below 10.
print("\nLow-sales products (quantity < 10):")
print(products[products["Quantity"] < 10])

print("\nRevenue by category:")
print(products.groupby("Category")["Revenue"].sum())

products.to_excel("product_sales.xlsx", index=False)
print("\nResults exported to product_sales.xlsx")
