import numpy as np
import pandas as pd

penguins_data = pd.read_csv("penguins_size.csv")

pt_data = pd.pivot_table(
    penguins_data,
    index="species",
    columns=["island", "sex"],
    values="culmen_length_mm",
    aggfunc=np.max
)
print(pt_data)