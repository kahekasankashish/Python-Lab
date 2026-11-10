# Q22. Count tuple items and add two new items: one using concatenation and another using a built-in function.
items = (10, 20, 30)
print("Number of items:", len(items))
items = items + (40,)
print("After concatenation:", items)
temporary_list = list(items)
temporary_list.append(50)
items = tuple(temporary_list)
print("After adding with list append:", items)
