# Q34. Replace the last value of each tuple in the sample list with 100.
sample = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
result = [item[:-1] + (100,) for item in sample]
print(result)
