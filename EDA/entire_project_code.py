# Creating a complete, runnable Python script for the Time Series EDA project.
# This will:
# - Build the DataFrame from the provided CSV text
# - Execute all 8 analysis steps (visualization, decomposition, smoothing, stationarity checks,
#   differencing, and correlation/lag analysis)
# - Produce plots (each figure separate) and key statistical outputs (ADF test)
#
# NOTE: This code runs inside the notebook environment and will display plots inline.
# If you want to save plots to files, uncomment the plt.savefig(...) lines.
#
# Charts are created with matplotlib (no seaborn plotting) in order to comply with the notebook plotting rules.
# You can copy this code into a .py file or Jupyter notebook and run it locally as well.

from io import StringIO
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Statsmodels for decomposition, ADF, and ACF/PACF
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller, ccf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Prepare dataset from provided CSV text
csv_text = """Date,Sales,Advertising,Footfall
2015-01,205,25,310
2015-02,208,24,312
2015-03,212,26,315
2015-04,220,27,318
2015-05,230,28,322
2015-06,235,27,325
2015-07,242,29,330
2015-08,245,29,333
2015-09,248,30,335
2015-10,255,32,340
2015-11,275,35,355
2015-12,295,38,370
2016-01,215,26,320
2016-02,218,25,323
2016-03,223,26,326
2016-04,235,28,330
2016-05,240,29,334
2016-06,248,28,337
2016-07,255,30,340
2016-08,258,30,343
2016-09,265,32,348
2016-10,278,34,355
2016-11,300,38,370
2016-12,320,42,385
2017-01,225,28,328
2017-02,228,27,330
2017-03,235,29,334
2017-04,245,30,338
2017-05,255,31,342
2017-06,260,30,345
2017-07,268,32,350
2017-08,272,32,354
2017-09,275,33,358
2017-10,288,36,365
2017-11,315,40,380
2017-12,335,45,395
2018-01,238,30,335
2018-02,242,29,338
2018-03,248,31,341
2018-04,258,32,345
2018-05,265,33,349
2018-06,272,32,352
2018-07,278,34,356
2018-08,282,34,360
2018-09,288,36,364
2018-10,305,38,370
2018-11,335,43,388
2018-12,355,47,405
2019-01,250,32,342
2019-02,255,31,345
2019-03,260,33,348
2019-04,270,34,352
2019-05,278,35,356
2019-06,285,34,358
2019-07,292,36,362
2019-08,295,36,365
2019-09,300,38,368
2019-10,320,41,376
2019-11,350,46,395
2019-12,370,50,410
2020-01,265,33,348
2020-02,270,32,350
2020-03,255,30,320
2020-04,200,20,250
2020-05,210,21,260
2020-06,240,25,290
2020-07,260,27,310
2020-08,270,28,320
2020-09,280,30,330
2020-10,295,33,345
2020-11,320,38,360
2020-12,340,42,380
2021-01,275,35,340
2021-02,280,34,345
2021-03,285,36,350
2021-04,295,37,355
2021-05,305,38,360
2021-06,312,37,365
2021-07,320,39,370
2021-08,328,40,375
2021-09,335,42,380
2021-10,355,45,390
2021-11,385,50,405
2021-12,405,54,420
2022-01,310,40,370
2022-02,318,39,375
2022-03,325,41,380
2022-04,335,42,385
2022-05,345,43,390
2022-06,352,42,395
2022-07,360,44,400
2022-08,370,45,405
2022-09,380,46,410
2022-10,400,49,425
2022-11,435,54,450
2022-12,460,58,475
2023-01,370,47,420
2023-02,378,46,425
2023-03,385,48,430
2023-04,395,49,435
2023-05,410,50,440
2023-06,420,49,445
2023-07,430,51,450
2023-08,445,53,460
2023-09,470,57,480
2023-10,505,68,520
2023-11,550,75,560
2023-12,580,80,585
"""

# Read into DataFrame
df = pd.read_csv(StringIO(csv_text), parse_dates=['Date'])
df.set_index('Date', inplace=True)
df.index = pd.to_datetime(df.index)  # ensure proper datetime index

# Quick display of the first rows
print("First 8 rows of the dataset:")
display_df = df.head(8)
import ace_tools as tools; tools.display_dataframe_to_user("Monthly Retail Sales (head)", display_df)

# STEP 1: Visualize time series (line plot) and box plots by month/year
plt.figure(figsize=(10,4))
plt.plot(df.index, df['Sales'])
plt.title('Monthly Sales (2015-2023)')
plt.xlabel('Date')
plt.ylabel('Sales (thousands USD)')
plt.grid(True)
plt.show()

# Box plot by month
df['Month'] = df.index.month
plt.figure(figsize=(10,4))
plt.boxplot([df[df['Month']==m]['Sales'].values for m in range(1,13)], labels=list(range(1,13)))
plt.title('Sales Distribution by Month (1=Jan, 12=Dec)')
plt.xlabel('Month')
plt.ylabel('Sales (thousands USD)')
plt.show()

# Box plot by year
df['Year'] = df.index.year
years = sorted(df['Year'].unique())
plt.figure(figsize=(10,4))
plt.boxplot([df[df['Year']==y]['Sales'].values for y in years], labels=years)
plt.title('Sales Distribution by Year')
plt.xlabel('Year')
plt.ylabel('Sales (thousands USD)')
plt.xticks(rotation=45)
plt.show()

# STEP 2: Spotting patterns - rolling mean to highlight trend
df['RollingMean_12'] = df['Sales'].rolling(window=12).mean()

plt.figure(figsize=(10,4))
plt.plot(df.index, df['Sales'], label='Original')
plt.plot(df.index, df['RollingMean_12'], label='12-month Rolling Mean')
plt.title('Sales with 12-month Rolling Mean')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()

# STEP 3: Decomposition (additive) - period=12 for monthly data
decomp = seasonal_decompose(df['Sales'], model='additive', period=12)
# Plot decomposition components (each on separate figure to follow plotting rule)
plt.figure(figsize=(10,3))
plt.plot(df.index, df['Sales'])
plt.title('Observed Series')
plt.grid(True)
plt.show()

plt.figure(figsize=(10,3))
plt.plot(df.index, decomp.trend)
plt.title('Trend Component')
plt.grid(True)
plt.show()

plt.figure(figsize=(10,3))
plt.plot(df.index, decomp.seasonal)
plt.title('Seasonal Component')
plt.grid(True)
plt.show()

plt.figure(figsize=(10,3))
plt.plot(df.index, decomp.resid)
plt.title('Residual Component')
plt.grid(True)
plt.show()

# STEP 4: Moving Average smoothing (3,6,12) - show each in its own plot
df['SMA_3'] = df['Sales'].rolling(window=3).mean()
df['SMA_6'] = df['Sales'].rolling(window=6).mean()
df['SMA_12'] = df['Sales'].rolling(window=12).mean()

plt.figure(figsize=(10,4))
plt.plot(df.index, df['Sales'], label='Original')
plt.plot(df.index, df['SMA_3'], label='3-month MA')
plt.title('3-month Moving Average (comparison)')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10,4))
plt.plot(df.index, df['Sales'], label='Original')
plt.plot(df.index, df['SMA_6'], label='6-month MA')
plt.title('6-month Moving Average (comparison)')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10,4))
plt.plot(df.index, df['Sales'], label='Original')
plt.plot(df.index, df['SMA_12'], label='12-month MA')
plt.title('12-month Moving Average (comparison)')
plt.legend()
plt.grid(True)
plt.show()

# STEP 5: Exponential smoothing via ewm and simple exp smoothing from statsmodels
df['ES_alpha_0.3'] = df['Sales'].ewm(alpha=0.3, adjust=False).mean()
df['ES_alpha_0.6'] = df['Sales'].ewm(alpha=0.6, adjust=False).mean()

plt.figure(figsize=(10,4))
plt.plot(df.index, df['Sales'], label='Original')
plt.plot(df.index, df['ES_alpha_0.3'], label='Exp Smoothing alpha=0.3')
plt.plot(df.index, df['ES_alpha_0.6'], label='Exp Smoothing alpha=0.6')
plt.title('Exponential Smoothing Comparison')
plt.legend()
plt.grid(True)
plt.show()

# STEP 6: Stationarity checks - rolling stats and ADF test
roll_mean = df['Sales'].rolling(window=12).mean()
roll_std = df['Sales'].rolling(window=12).std()

plt.figure(figsize=(10,4))
plt.plot(df.index, df['Sales'], label='Original')
plt.plot(df.index, roll_mean, label='Rolling Mean (12)')
plt.plot(df.index, roll_std, label='Rolling Std (12)')
plt.title('Rolling Mean & Std Deviation')
plt.legend()
plt.grid(True)
plt.show()

# Augmented Dickey-Fuller test
adf_result = adfuller(df['Sales'])
print("ADF Statistic (original): {:.4f}".format(adf_result[0]))
print("p-value (original): {:.4f}".format(adf_result[1]))
for key, val in adf_result[4].items():
    print("Critical Value ({}): {:.4f}".format(key, val))

# STEP 7: Differencing - first order and seasonal (lag=12)
df['FirstDiff'] = df['Sales'].diff()
plt.figure(figsize=(10,4))
plt.plot(df.index, df['FirstDiff'])
plt.title('First Order Differenced Series')
plt.grid(True)
plt.show()

adf_fd = adfuller(df['FirstDiff'].dropna())
print("ADF Statistic (1st diff): {:.4f}".format(adf_fd[0]))
print("p-value (1st diff): {:.4f}".format(adf_fd[1]))

df['SeasonalDiff'] = df['Sales'].diff(12)
plt.figure(figsize=(10,4))
plt.plot(df.index, df['SeasonalDiff'])
plt.title('Seasonal Differenced Series (lag=12)')
plt.grid(True)
plt.show()

adf_sd = adfuller(df['SeasonalDiff'].dropna())
print("ADF Statistic (seasonal diff): {:.4f}".format(adf_sd[0]))
print("p-value (seasonal diff): {:.4f}".format(adf_sd[1]))

# STEP 8: Correlation plots - ACF, PACF, lag plot, heatmap and cross-correlation with advertising
# ACF plot
plt.figure(figsize=(8,4))
plot_acf(df['Sales'], lags=36)
plt.title('Autocorrelation Function (ACF) - Sales')
plt.show()

# PACF plot
plt.figure(figsize=(8,4))
plot_pacf(df['Sales'], lags=36, method='ywm')
plt.title('Partial Autocorrelation Function (PACF) - Sales')
plt.show()

# Lag plot (lag=1)
from pandas.plotting import lag_plot
plt.figure(figsize=(5,5))
lag_plot(df['Sales'])
plt.title('Lag Plot (lag=1) - Sales vs previous month')
plt.show()

# Correlation heatmap of lags 0-12
lags = 12
lagged = pd.concat([df['Sales'].shift(i) for i in range(0, lags+1)], axis=1)
lagged.columns = ['t'] + [f't-{i}' for i in range(1, lags+1)]
corr_matrix = lagged.corr()

plt.figure(figsize=(8,6))
plt.imshow(corr_matrix, aspect='auto')
plt.colorbar()
plt.title('Lag Correlation Heatmap (0 to 12)')
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=45)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
plt.show()

# Cross-correlation between Advertising and Sales (show first 12 lags)
adv = df['Advertising'].fillna(method='ffill')
sales = df['Sales']
# compute CCF manually using statsmodels' ccf function (returns correlation for non-negative lags)
cc_vals = ccf(adv, sales)[:13]

plt.figure(figsize=(8,4))
plt.bar(range(len(cc_vals)), cc_vals)
plt.title('Cross-correlation (Advertising leads Sales) - lags 0..12')
plt.xlabel('Lag (months)')
plt.ylabel('Correlation')
plt.show()

# End: show a small summary DataFrame
summary_df = df[['Sales','Advertising','Footfall','RollingMean_12','SMA_12','ES_alpha_0.3']].tail(12)
tools.display_dataframe_to_user("Summary - last 12 months (selected cols)", summary_df)

print("Analysis complete. Key outputs displayed: plots, ADF results, and summary table.")
