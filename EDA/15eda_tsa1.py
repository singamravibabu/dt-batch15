import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

date_rng =pd.date_range(start="2015-1-1", end="2023-12-31", freq="ME")
np.random.seed(42)
sales = 200 + 20 * np.sin( 2 * np.pi * date_rng.month / 12 ) + \
      np.random.normal(0, 5, len(date_rng))

# Create DataFrame
df = pd.DataFrame(
    {"Date": date_rng,
     "Sales": sales}
)
df = df.set_index("Date")

'''sns.lineplot(x=df.index, y=df["Sales"])
plt.show()'''

df["Month"] = df.index.month
df["Year"] = df.index.year

'''sns.boxplot(x=df["Month"], y=df["Sales"])
plt.show()'''

'''sns.boxplot(x=df["Year"], y=df["Sales"])
plt.show()'''

# upward trend
trend = np.linspace(100, 300, len(date_rng))
# yearly seasonality
seasonality = 30 * np.sin(2 * np.pi * date_rng.month/12)
# random noise
noise = np.random.normal(0, 8, len(date_rng))
sales = trend + seasonality + noise

# Create DataFrame
df = pd.DataFrame(
    {"Date": date_rng,
     "Sales": sales}
)
df = df.set_index("Date")

'''sns.lineplot(x=df.index, y=df["Sales"])
plt.show()'''

df["RollingMean"] = df["Sales"].rolling(window=12, center=True).mean()

sns.lineplot(x=df.index, y=df["Sales"])
sns.lineplot(x=df.index, y=df["RollingMean"])
plt.show()