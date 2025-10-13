from turtle import pen
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

penguins_data = pd.read_csv("penguins_size.csv")
penguins_data_male = penguins_data[penguins_data["sex"] == "MALE"]
penguins_data_female = penguins_data[penguins_data["sex"] == "FEMALE"]

sns.histplot(data=penguins_data_male,
            x="culmen_length_mm",
            alpha=0.5,
            color="red")
sns.histplot(data=penguins_data_female,
            x="culmen_length_mm",
            alpha=0.5,
            color="blue")
plt.show()