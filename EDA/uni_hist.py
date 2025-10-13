import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

penguins_data = pd.read_csv("penguins_size.csv")
penguins_data = penguins_data[["species", "culmen_length_mm"]]

plt.figure(figsize=(48,24))
ax = sns.histplot(data=penguins_data,
                   x=penguins_data["culmen_length_mm"],
                   hue=penguins_data["species"])
ax.set_title("Culmen Length Distribution", fontsize=25)
ax.set_xlabel("Culmen Length (mm)", fontsize=12)
ax.set_ylabel("Frequency", fontsize=12)
plt.show()