# Q9. Select rows where age is between 2 and 4 inclusive.
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

print(birds[birds["age"].between(2, 4, inclusive="both")])
