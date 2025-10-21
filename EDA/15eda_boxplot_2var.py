import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

penguins_data = pd.read_csv("penguins_size.csv")

sns.boxplot(
    data=penguins_data,
    x="species",
    y = "culmen_length_mm"
)
plt.show()