import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset.csv", parse_dates=["Date"])
df = df.set_index("Date")

## POINT 1
sns.lineplot(data=df, x=df.index, y=df["Sales"])
plt.show()

df["Month"] = df.index.month
# box plot by monthly sales