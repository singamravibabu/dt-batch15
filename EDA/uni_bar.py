import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

penguins_data = pd.read_csv("penguins_size.csv")

plt.figure(figsize=(48, 24))
ax = sns.countplot(data=penguins_data,
                    x=penguins_data["species"],
                    hue=penguins_data["species"])
ax.set_title("Count of Penguin Species", fontsize=40)
ax.set_xlabel("Species", fontsize=32)
ax.set_ylabel("Count", fontsize=32)
plt.show()