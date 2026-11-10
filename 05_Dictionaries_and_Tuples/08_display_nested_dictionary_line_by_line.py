# Q8. Print a dictionary one line after the other, including the nested dictionary entries.
data = {'SAI': {'class': 'VI', 'roll': 8}, 'PRIYA': {'class': 'V', 'roll': 3}}
for name, details in data.items():
    print(name)
    for key, value in details.items():
        print(f"{key} : {value}")
