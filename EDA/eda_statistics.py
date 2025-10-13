import numpy as np
import pandas as pd
from scipy import stats

covid_data = pd.read_csv("covid-data.csv")
covid_data = covid_data[["iso_code", "continent", "location", 
            "date", "total_cases", "new_cases"]]

# Mean
mean_value = np.mean(covid_data["new_cases"])
print("Mean of new cases:", mean_value)

# Median
median_value = np.median(covid_data["new_cases"])
print("Median of new cases:", median_value)

# Mode
mode_value = stats.mode(covid_data["new_cases"])
print("Mode of new cases:", mode_value[0])

# Variance
variance_value = np.var(covid_data["new_cases"])
print("Variance of new cases:", variance_value)

# Standard Deviation
std_value = np.std(covid_data["new_cases"])
print("Standard Deviation of new cases:", std_value)

# Range
min_value = np.min(covid_data["new_cases"])
max_value = np.max(covid_data["new_cases"])
range_value = max_value - min_value
print("Range of new cases:", range_value)

# Percentiles
percentile_60 = np.percentile(covid_data["new_cases"], 60)
print("60th Percentile of new cases:", percentile_60)

# Quartiles
Q1 = np.percentile(covid_data["new_cases"], 25)
Q3 = np.percentile(covid_data["new_cases"], 75)
print("Quartiles of new cases: Q1 =", Q1, ", Q3 =", Q3)

# Interquartile Range (IQR)
iqr_value = stats.iqr(covid_data["new_cases"])
print("Interquartile Range of new cases:", iqr_value)