# Q24. Create a 2D array with months and sales (user inputs); calculate total yearly sales; find month with highest and lowest sales; compute average monthly sales; identify months with below-average sales.
import numpy as np

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
sales = []
for month in months:
    sales.append(float(input(f"Enter sales for {month}: ")))

sales_array = np.array(sales)
monthly_data = np.column_stack((np.array(months), sales_array.astype(str)))
total = sales_array.sum()
average = sales_array.mean()
highest_index = int(np.argmax(sales_array))
lowest_index = int(np.argmin(sales_array))

print("Month-wise sales:")
for month, amount in zip(months, sales_array):
    print(f"{month}: {amount:.2f}")
print(f"Total yearly sales: {total:.2f}")
print(f"Highest sales: {months[highest_index]} ({sales_array[highest_index]:.2f})")
print(f"Lowest sales: {months[lowest_index]} ({sales_array[lowest_index]:.2f})")
print(f"Average monthly sales: {average:.2f}")
print("Months with below-average sales:", [month for month, amount in zip(months, sales_array) if amount < average])
