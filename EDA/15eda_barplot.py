import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

penguins_data = pd.read_csv("penguins_size.csv")

sns.barplot(
    data = penguins_data,
    x = penguins_data["species"],
    y = penguins_data["culmen_length_mm"],
    estimator=np.min
)
plt.show()