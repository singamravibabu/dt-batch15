import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

penguins_data = pd.read_csv("penguins_size.csv")

plt.figure(figsize=(10, 6))
ax = sns.histplot(data=penguins_data,
                  x=penguins_data["culmen_length_mm"])
ax.set_title("Culmen Length Histogram")
ax.set_xlabel("Culmen Length (mm)")
ax.set_ylabel("Frequency")
plt.show()