import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller

date_rng = pd.date_range(
    start="2018-1-1",
    end="2023-12-31",
    freq="ME"
)

sales = 200 + 20 * np.sin(2 * np.pi + date_rng.month / 12 ) + \
    np.random.normal(0, 5, len(date_rng))

df = pd.DataFrame(
    {
        "Date": date_rng,
        "Sales": sales
    }
)

df = df.set_index("Date")

# sns.lineplot(data=df, x=df.index, y="Sales")
# plt.show()

df["Month"] = df.index.month
# sns.boxplot(data=df, x=df.Month, y="Sales")
# plt.show()

df["Year"] = df.index.year
# sns.boxplot(data=df, x=df.Year, y="Sales")
# plt.show()

np.random.seed(42)
trend = np.linspace(100, 300, len(date_rng))
seasonality = 30 * np.sin(2 * np.pi * date_rng.month / 12)
noise = np.random.normal(0, 8, len(date_rng))

sales = trend + seasonality + noise
df = pd.DataFrame(
    {
        "Date": date_rng,
        "Sales": sales
    }
)
df = df.set_index("Date")
# sns.lineplot(data=df, x=df.index, y="Sales")
# plt.show()
df["RollingMean"] = df["Sales"].rolling(window=12, center=True).mean()

# sns.lineplot(data=df, x=df.index, y="Sales")
# sns.lineplot(data=df, x=df.index, y="RollingMean")
plt.show()

df["Month"] = df.index.month
monthly_avg = df.groupby("Month")["Sales"].mean()

'''sns.lineplot(
    x=monthly_avg.index,
    y=monthly_avg.values,
    marker="o"
)
plt.show()'''

df["Year"] = df.index.year
yearly_avg = df.groupby("Year")["Sales"].mean()

'''sns.lineplot(
    x=yearly_avg.index,
    y=yearly_avg.values,
    marker="o"
)
plt.show()'''

df["Detrended"] = df["Sales"] - df["RollingMean"]
'''sns.lineplot(data=df, x=df.index, y="Detrended")
plt.axhline(0, color="red", linestyle="--")
plt.show()'''

decomposition = seasonal_decompose(
    df["Sales"],
    model="additive",
    period=12
)
# decomposition.plot()

df["Trend"] = decomposition.trend
df["Seasonal"] = decomposition.seasonal
df["Residual"] = decomposition.resid

'''print(df[["Sales", "Trend", "Seasonal", "Residual"]])'''




'''decomposition_mul = seasonal_decompose(
    df["Sales"],
    model="multiplicative",
    period=12
)
decomposition_mul.plot()
plt.show()'''

df["Month"] = df.index.month
seasonal_pattern = df.groupby("Month")["Seasonal"].mean()
'''plt.plot(seasonal_pattern.index, seasonal_pattern.values, marker='o')
plt.show()'''

df["SMA_12"] = df["Sales"].rolling(window=12).mean()
df["SMA_6"] = df["Sales"].rolling(window=6).mean()
df["SMA_3"] = df["Sales"].rolling(window=3).mean()
'''sns.lineplot(x=df.index, y="Sales", data=df)
sns.lineplot(x=df.index, y="SMA_12", data=df, color="red")
sns.lineplot(x=df.index, y="SMA_6", data=df, color="green") 
sns.lineplot(x=df.index, y="SMA_3", data=df, color="black")
plt.legend()
plt.show()'''

df["ES_0.3"] = df["Sales"].ewm(alpha=0.3, adjust=False).mean()
df["ES_0.5"] = df["Sales"].ewm(alpha=0.5, adjust=False).mean()
df["ES_0.8"] = df["Sales"].ewm(alpha=0.8, adjust=False).mean()
df["ES_1.0"] = df["Sales"].ewm(alpha=1.0, adjust=False).mean()
'''sns.lineplot(x=df.index, y="Sales", data=df, color="blue", adjust=False)
sns.lineplot(x=df.index, y="ES_0.3", data=df, color="red")
sns.lineplot(x=df.index, y="ES_0.5", data=df, color="green")
sns.lineplot(x=df.index, y="ES_0.8", data=df, color="black")
sns.lineplot(x=df.index, y="ES_1.0", data=df, color="orange")
plt.show()'''



'''result = adfuller(df['Sales'])
print('ADF Statistic:', result[0])
print('p-value:', result[1])
for key, value in result[4].items():
    print(f'Critical Value ({key}): {value}')'''

df["FirstDiff"] = df["Sales"].diff(12)
sns.lineplot(data=df, x=df.index, y="FirstDiff")
plt.show()