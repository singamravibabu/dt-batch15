import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

houseprices = pd.read_csv("HousingPricesData.csv")
sns.boxplot(data=houseprices,
            x=houseprices["Price"])
plt.show()