import numpy as np
import pandas as pd
from scipy import stats

marketing_data = pd.read_csv("marketing_campaign.csv")
marketing_data = marketing_data[["ID", "Year_Birth", "Education", 
                "Marital_Status", "Income", "Kidhome", 
                "Teenhome", "Dt_Customer", "Recency",
                  "NumStorePurchases", "NumWebVisitsMonth"]]

marketing_data = marketing_data.sort_values("NumStorePurchases", ascending=False)
print(marketing_data)

####### Categorizing Data
categorical_data = pd.cut(x=marketing_data["NumStorePurchases"], 
    bins=[0,4,8,13], 
    labels=["Low", "Medium", "High"])
print(categorical_data)

###### Drop duplicates
marketing_data2 = marketing_data[["Education", "Marital_Status",
                                  "Kidhome", "Teenhome"]]
print(marketing_data2)
marketing_data2 = marketing_data2.drop_duplicates()
print(marketing_data2)

###### Dropping rows and columns
marketing_data3 = marketing_data2.drop(labels=[499], axis=0) # drop row with index 1
marketing_data3 = marketing_data3.drop(labels=["Education"], axis=1)
print(marketing_data3)