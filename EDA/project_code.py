# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller, ccf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

df = pd.read_csv("dataset.csv", parse_dates=["Date"])
df = df.set_index("Date")

## POINT 1
# sns.lineplot(data=df, x=df.index, y="Sales")
# plt.show()
sns.boxplot(data=df, x=df.index.month, y="Sales")
plt.show()