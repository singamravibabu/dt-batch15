import numpy as np
import pandas as pd

penguins_data = pd.read_csv("penguins_size.csv")
crosstab = pd.crosstab(index=penguins_data["culmen_length_mm"],
                       columns=penguins_data["sex"])
print(crosstab)