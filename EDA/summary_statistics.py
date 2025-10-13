import numpy as np
import pandas as pd
from scipy import stats

covid_data = pd.read_csv("covid-data.csv")
covid_data = covid_data[["iso_code", "continent",
             "location", "date", 
             "total_cases", "new_cases"]]

# Mean of new cases
mean_value = np.mean(covid_data["new_cases"])
print("Mean of new cases:", mean_value)

# Median of new cases
median_value = np.median(covid_data["new_cases"])
print("Median of new cases:", median_value)

# Mode of new cases
mode_value = stats.mode(covid_data["new_cases"])
print("Mode of new cases:", mode_value[0])

# Variance of new cases
var_value = np.var(covid_data["new_cases"])
print("Variance of new cases:", var_value)

# Standard Deviation of new cases
std_dev_value = np.std(covid_data["new_cases"])
print("Standard Deviation of new cases:", std_dev_value)

# Range of new cases
min_value = np.min(covid_data["new_cases"])
max_value = np.max(covid_data["new_cases"])
range_value = max_value - min_value
print("Range of new cases:", range_value)

# Percentiles of new cases
percentile_60 = np.percentile(covid_data["new_cases"], 60)
print("60th Percentile of new cases:", percentile_60)

# Quartiles of new cases
q3 = np.quantile(covid_data["new_cases"], 0.75)
print("Third Quartile (Q3) of new cases:", q3)

# Interquartile Range (IQR) of new cases
IQR = stats.iqr(covid_data["new_cases"])
print("Interquartile Range (IQR) of new cases:", IQR)