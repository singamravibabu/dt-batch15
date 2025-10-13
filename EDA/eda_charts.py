from tkinter import font
import pandas as pd
import matplotlib.pyplot as plt

housing_data = pd.read_csv("HousingPricesData.csv")
housing_data = housing_data[["Zip", "Price", "Area", "Room"]]
housing_data["PriceperSqm"] = housing_data["Price"] / housing_data["Area"]
housing_data = housing_data.sort_values("Price", ascending=False)
print(housing_data)


""" x = housing_data["Zip"][0:10]
y = housing_data["Price"][0:10]
y1 = housing_data["PriceperSqm"][0:10]

plt.figure(figsize=(10, 6))
plt.bar(x, y)
plt.title("Top 10 Most Expensive Houses by Zip Code",
           fontsize=20, pad=8, color="blue")
plt.xlabel("Zip Code", fontsize=14, labelpad=8)
plt.ylabel("Price in USD", fontsize=14, labelpad=8)
plt.xticks(fontsize=12, rotation=45, ha="right")
plt.yticks(fontsize=12)
plt.show() """

x = housing_data["Zip"][0:10]
y = housing_data["Price"][0:10]
y1 = housing_data["PriceperSqm"][0:10]

fig, ax = plt.subplots(2, 2, figsize=(16, 7))
plt.subplot(2, 2, 1)
plt.bar(x, y, color="skyblue")
plt.title("Top 10 Most Expensive Houses by Zip Code",
           fontsize=10, pad=8, color="blue")
plt.xticks(rotation=45, ha="right")

plt.subplot(2, 2, 2)
plt.bar(x, y1, color="lightgreen")
plt.title("Top 10 Most Expensive Houses by Price per Sqm",
           fontsize=10, pad=8, color="green")
plt.xticks(rotation=45, ha="right")

plt.show()
