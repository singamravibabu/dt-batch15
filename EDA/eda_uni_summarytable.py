import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

housing_data =pd.read_csv("HousingPricesData.csv")
print(housing_data.describe())