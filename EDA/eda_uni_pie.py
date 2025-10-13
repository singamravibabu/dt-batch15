import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

penguins_data = pd.read_csv("penguins_size.csv")
penguins_group = penguins_data.groupby("species").count()
penguins_group = penguins_group.reset_index()
print(penguins_group)

plt.figure(figsize=(8, 6))
plt.pie(penguins_group["culmen_length_mm"],
        labels=penguins_group["species"]
)
plt.title("Penguin Species Distribution")
plt.show()