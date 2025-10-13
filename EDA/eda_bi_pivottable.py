import numpy as np
import pandas as pd

penguins_data = pd.read_csv("penguins_size.csv")
pivot_data =pd.pivot_table(data=penguins_data, index="species",
               values="body_mass_g", aggfunc=np.mean)
print(pivot_data)