import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

penguins_data = pd.read_csv("penguins_size.csv")
penguins_group = penguins_data.groupby("species").count()
penguins_group = penguins_group.reset_index()
plt.pie(penguins_group["culmen_length_mm"],
        labels=penguins_group["species"],
        colors=["r","g", "b"])
plt.show()