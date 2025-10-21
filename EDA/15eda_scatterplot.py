import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

penguins_data = pd.read_csv("penguins_size.csv")

sns.scatterplot(data=penguins_data,
                x = "culmen_length_mm",
                y = "body_mass_g",
                hue="species")
plt.show()