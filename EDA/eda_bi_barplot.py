from turtle import pen
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

penguins_data = pd.read_csv("penguins_size.csv")
penguins_data = penguins_data[["species",
                                 "culmen_length_mm",
                                 "sex"]]

plt.figure(figsize=(24, 12))
sns.barplot(data=penguins_data, 
            x="species", 
            y="culmen_length_mm", 
            estimator=np.median)
plt.show()
