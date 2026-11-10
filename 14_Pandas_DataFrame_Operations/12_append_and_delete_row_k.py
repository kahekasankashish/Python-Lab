# Q12. Append a new row 'k' with your choice of values for each column, then delete that row to return the original DataFrame.
import numpy as np
import pandas as pd

data = {
    "birds": ["Cranes", "Cranes", "plovers", "spoonbills", "spoonbills",
              "Cranes", "plovers", "Cranes", "spoonbills", "spoonbills"],
    "age": [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4],
    "visits": [2, 4, 3, 4, 3, 4, 2, 2, 3, 2],
    "priority": ["yes", "yes", "no", "yes", "no", "no", "no", "yes", "no", "no"]
}
labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
birds = pd.DataFrame(data, index=labels)

new_row = pd.DataFrame(
    {"birds": ["Cranes"], "age": [2.5], "visits": [3], "priority": ["yes"]},
    index=["k"]
)
birds = pd.concat([birds, new_row])
print("After appending row k:")
print(birds)
birds = birds.drop(index="k")
print("\nAfter deleting row k:")
print(birds)
