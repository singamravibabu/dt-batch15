import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

penguins_data = pd.read_csv("penguins_size.csv")
penguins_data = penguins_data[["culmen_length_mm", "body_mass_g"]]
penguins_corr = penguins_data.corr()
sns.heatmap(penguins_corr, vmin=-1, vmax=1, annot=True)
plt.show()