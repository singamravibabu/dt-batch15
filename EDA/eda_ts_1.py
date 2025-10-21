import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose


dates = pd.date_range(
    start="2018-1-1",
    end="2023-12-31",
    freq="ME"
)
sales = 200 + 20 * np.sin(2 * np.pi * dates.month / 12) + \
    np.random.normal(0, 5, len(dates))
df = pd.DataFrame({
    "Date": dates,
    "Sales": sales
})
df = df.set_index("Date")
# print(df)

# sns.lineplot(data=df, x=df.index, y="Sales")
# plt.show()
# df["Month"] = df.index.month
# sns.boxplot(data=df, x=df.Month, y=df.Sales)
# plt.show()
# df["Year"] = df.index.year
# sns.boxplot(data=df, x=df.Year, y=df.Sales)
# plt.show()
np.random.seed(42)
trend = np.linspace(100, 300, len(dates))
seasonality = 30 * np.sin(2 * np.pi * dates.month / 12)
noise = np.random.normal(0, 8, len(dates))
print(noise)
sales = trend + seasonality + noise
df = pd.DataFrame({
    "Date": dates,
    "Sales": sales
})
df = df.set_index("Date")
# print(df.shape)
# df = df.set_index("Date")
# sns.lineplot(data=df, x=df.index, y="Sales")
# plt.show()
df["RollingMean"] = df["Sales"].rolling(window=12, center=True).mean()
# print(df)
df["Month"] = df.index.month
monthly_avg = df.groupby("Month")["Sales"].mean()
plt.figure(figsize=(40,20))
# sns.lineplot(data=df, x=df.index, y="Sales")
#sns.lineplot(data=df, x=df.index, y="RollingMonth")
# plt.show()
df["Year"] = df.index.year
yearly_avg = df.groupby("Year")["Sales"].mean()
'''sns.lineplot(
    x=yearly_avg.index,
    y=yearly_avg.values,
    marker='o'
)'''


df["Detrended"] = df["Sales"] - df["RollingMean"]
'''sns.lineplot(data=df, x=df.index, y="Detrended")
plt.axhline(0, color="red", linestyle="--")
plt.show()'''


decomposition = seasonal_decompose(
    df["Sales"], 
    model="additive",
    period=12)
# decomposition.plot()
df["Trend"] = decomposition.trend
df["Seasonal"] = decomposition.seasonal
df["Residual"] = decomposition.resid

print(df[["Sales", "Trend", "Seasonal", "Residual"]].head(15))

'''decomposition_mul = seasonal_decompose(
    df["Sales"], 
    model="multiplicative",
    period=12)
decomposition_mul.plot()'''

df["Month"] = df.index.month
'''seasonal_pattern = df.groupby("Month")["Seasonal"].mean()
plt.plot(seasonal_pattern.index, seasonal_pattern.values)
plt.show()'''

# plt.figure(figsize=(40,20))
df["SMA_12"] = df["Sales"].rolling(window=12).mean()
df["SMA_6"] = df["Sales"].rolling(window=6).mean()
df["SMA_3"] = df["Sales"].rolling(window=3).mean()
'''sns.lineplot(x=df.index, y="Sales", data=df)
sns.lineplot(x=df.index, y="SMA_12", data=df, color="red")
sns.lineplot(x=df.index, y="SMA_6", data=df, color="green")
sns.lineplot(x=df.index, y="SMA_3", data=df, color="blue")
plt.legend()
plt.show()'''

df["ES_0.3"] = df["Sales"].ewm(alpha=0.3, adjust=False).mean()
df["ES_0.5"] = df["Sales"].ewm(alpha=0.5, adjust=False).mean()
df["ES_0.8"] = df["Sales"].ewm(alpha=0.8, adjust=False).mean()
df["ES_1.0"] = df["Sales"].ewm(alpha=1.0, adjust=False).mean()
'''sns.lineplot(x=df.index, y="Sales", data=df)
sns.lineplot(x=df.index, y="ES_0.3", data=df, color="red")
sns.lineplot(x=df.index, y="ES_0.5", data=df, color="green")
sns.lineplot(x=df.index, y="ES_0.8", data=df, color="blue")
sns.lineplot(x=df.index, y="ES_1.0", data=df, color="orange")
plt.show()'''

from statsmodels.tsa.stattools import adfuller

result = adfuller(df['Sales'])
print('ADF Statistic:', result[0])
print('p-value:', result[1])
for key, value in result[4].items():
    print(f'Critical Value ({key}): {value}')
