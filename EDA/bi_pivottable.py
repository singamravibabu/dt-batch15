import numpy as np
import pandas as pd

penguins_data = pd.read_csv("penguins_size.csv")

pivot_table = pd.pivot_table(data=penguins_data, index="species", columns="sex",
               values=["culmen_length_mm", "body_mass_g"], aggfunc=np.mean)
print(pivot_table)