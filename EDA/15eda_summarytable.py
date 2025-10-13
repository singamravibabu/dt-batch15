import numpy as np
import pandas as pd

houseprices_data = pd.read_csv("HousingPricesData.csv")
described_data = houseprices_data.describe()
print(described_data)