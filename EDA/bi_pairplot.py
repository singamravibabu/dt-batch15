import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

penguins_data = pd.read_csv("penguins_size.csv")
penguins_data = penguins_data[["species", 
                               "culmen_length_mm", 
                               "body_mass_g", "culmen_depth_mm", 
                               "sex"]]

plt.figure(figsize=(20, 10))
sns.pairplot(data=penguins_data)
plt.show()