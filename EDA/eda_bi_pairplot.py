import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

penguins_data = pd.read_csv("penguins_size.csv")
penguins_data = penguins_data[["species", 
                               "culmen_length_mm", 
                               "body_mass_g",
                               "sex"]]

plt.figure(figsize=(48, 24))
sns.pairplot(data=penguins_data, hue="sex")
plt.show()