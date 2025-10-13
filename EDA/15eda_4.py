from matplotlib import markers
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
housing_data = pd.read_csv("HousingPricesData.csv")
housing_data = housing_data[["Zip", "Price", "Area", "Room"]]
housing_data = housing_data.sort_values("Price", ascending=False)
housing_data["PriceperSqm"] = housing_data["Price"] / housing_data["Area"]

# Select the first few rows of the dataset
x = housing_data["Zip"][0:10]
y = housing_data["Price"][0:10]
y1 = housing_data["PriceperSqm"][0:10]

fig, ax = plt.subplots(2, 2, figsize=(40, 20))
plt.subplot(2, 2, 1)
plt.bar(x, y, color="orange")
plt.legend(["Price"])
plt.subplot(2, 2, 2)
plt.plot(x, y1, color="green",
          linestyle="-", linewidth=3,
          marker='s', markersize=10)
plt.legend(["Price per Sqm"])
plt.subplot(2, 2, 3)
plt.scatter(x, y, color="red")
plt.legend(["Price"])
plt.subplot(2, 2, 4)
plt.barh(x, y1, color="blue")
plt.legend(["Price per Sqm"])
plt.show()