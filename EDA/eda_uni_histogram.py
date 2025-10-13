from tkinter import font
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

penguins_data = pd.read_csv("penguins_size.csv")
penguins_data = penguins_data[["species", "culmen_length_mm"]]

plt.figure(figsize=(48, 24))
ax = sns.histplot(data=penguins_data,
                   x=penguins_data["culmen_length_mm"],
                   hue=penguins_data["species"])
ax.set_xlabel("culmen_length_mm", fontsize=10)
ax.set_ylabel("count", fontsize=10)
ax.set_title("Histogram of culmen_length_mm", fontsize=20)
plt.show()