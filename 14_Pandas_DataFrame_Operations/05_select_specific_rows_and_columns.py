# Q5. Select rows [2, 3, 7] and columns ['birds', 'age', 'visits'].
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

print(birds.loc[["c", "d", "h"], ["birds", "age", "visits"]])
