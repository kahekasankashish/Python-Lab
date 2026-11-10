# Question 22: Flatten a list that may contain nested lists of arbitrary depth.
def flatten(items):
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

lst = [1, 2, [3, 4], [5, [6, 7]], 8]
print("Original list:", lst)
print("Flattened list:", flatten(lst))
