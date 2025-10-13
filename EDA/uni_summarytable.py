import numpy as np
import pandas as pd

housingprices = pd.read_csv("HousingPricesData.csv")
print(housingprices.describe())