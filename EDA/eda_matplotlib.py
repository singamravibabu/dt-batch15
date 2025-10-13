import pandas as pd
import matplotlib.pyplot as plt

housing_data = pd.read_csv("HousingPricesData.csv")
housing_data = housing_data[["Zip", "Price", "Area", "Room"]]
housing_data["PriceperSqm"] = housing_data["Price"] / housing_data["Area"]
sorted_data = housing_data.sort_values("Price", ascending=False)

x = sorted_data["Zip"][0:10]
y = sorted_data["Price"][0:10]
y1 = sorted_data["PriceperSqm"][0:10]* 50

plt.figure(figsize=(48, 24))
plt.bar(x, y, color="red")
plt.plot(x, y1, color="blue", marker="o", markersize=10)
plt.title("10 Most Expensive Houses", fontsize=20, color="red")
plt.xlabel("Zip Code", fontsize=16, color="blue")
plt.ylabel("Price in $", fontsize=16, color="blue")
plt.xticks(fontsize=15, rotation=45)
plt.yticks(fontsize=10)
plt.legend(["Price", "PriceperSqm"], fontsize=16)
plt.show()

'''x = sorted_data["Zip"][0:10]
y = sorted_data["Price"][0:10]
y1 = sorted_data["PriceperSqm"][0:10]

fig, ax = plt.subplots(2, 2, figsize=(48, 24))
plt.subplot(2, 2, 1)
plt.bar(x, y, color="red")
plt.subplot(2, 2, 2)
plt.barh(x, y1, color="blue")
plt.subplot(2, 2, 3)
plt.plot(x, y, color="red")
plt.subplot(2, 2, 4)
plt.scatter(x, y1, color="blue")

plt.show()'''