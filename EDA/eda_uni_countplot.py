import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

penguins_data = pd.read_csv("penguins_size.csv")
sns.countplot(data=penguins_data, x="species", hue="species")
plt.show()