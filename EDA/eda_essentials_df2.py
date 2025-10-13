import numpy as np
import pandas as pd

marketing_data = pd.read_csv("marketing_campaign.csv")
marketing_data = marketing_data[["ID", "Year_Birth", "Education",
                 "Marital_Status", "Income", "Kidhome",
                   "Teenhome", "Dt_Customer", "Recency",
                     "NumStorePurchases", "NumWebVisitsMonth"]]

# sorting
marketing_data = marketing_data.sort_values("NumStorePurchases",
                                            ascending=False)

# Bucketing
bucketted_data = pd.cut(marketing_data["NumStorePurchases"],
       bins=[0, 4, 8, 13],
       labels=["Low", "Moderate", "High"])
print(bucketted_data.head())

# Drop duplicates
marketing_data2 = marketing_data[["Education", "Marital_Status",
                                  "Kidhome", "Teenhome"]]
marketing_data2.drop_duplicates()
print(marketing_data2)

# Dropping rows and columns
marketing_data2 = marketing_data2.dropna(labels=[499]) # dropping row
marketing_data2 = marketing_data2.drop(labels=["Education"], axis=1) # drop column
print(marketing_data2)

marketing_data["Teenhome_replaced"] = (
    marketing_data["Teenhome"]
    .replace([0, 1, 2], ["No teen", "Has teen", "Has teen"])
)
