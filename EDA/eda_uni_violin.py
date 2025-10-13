import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

housing_data = pd.read_csv("HousingPricesData.csv")
housing_data = housing_data[["Zip", "Price", "Area", "Room"]]
plt.figure(figsize=(48, 24))
ax = sns.violinplot(data=housing_data,
                 x=housing_data["Price"])
ax.set_xlabel("Price", fontsize=10)
ax.set_title("Violin Plot of House Prices", fontsize=20)
plt.show()