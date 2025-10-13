import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

penguins_data = pd.read_csv("penguins_size.csv")

plt.figure(figsize=(8, 6))
ax = sns.scatterplot(data=penguins_data,
                     x = "culmen_length_mm",
                     y = "body_mass_g",
                     hue="species"
)
ax.set_title("Culmen Length vs Body Mass")
plt.show()