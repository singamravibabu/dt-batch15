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
y1 = housing_data["PriceperSqm"][0:10]*75

plt.figure(figsize=(20, 8))
plt.bar(x, y, color="orange")
plt.scatter(x, y1, color="green", s=100)
plt.title("10 Most Expensive Houses", fontsize=20, color="blue")
plt.xlabel("ZIP", fontsize=15)
plt.ylabel("PRICE", fontsize=15)
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.show()
