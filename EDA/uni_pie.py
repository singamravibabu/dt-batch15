import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

penguins_data = pd.read_csv("penguins_size.csv")
penguins_data = penguins_data[["species", "culmen_length_mm"]]

plt.figure(figsize=(48, 24))
plt.pie(penguins_data["species"].value_counts(), 
        labels=penguins_data["species"].unique(), 
        colors=['g', 'r', 'b'])

plt.title("Proportion of Penguin Species", fontsize=40)
plt.show()