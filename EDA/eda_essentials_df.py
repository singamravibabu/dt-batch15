import numpy as np
import pandas as pd

marketing_data = pd.read_csv("marketing_campaign.csv")
marketing_data = marketing_data[["ID", "Year_Birth", "Education",
                 "Marital_Status", "Income", "Kidhome",
                   "Teenhome", "Dt_Customer", "Recency", 
                   "NumStorePurchases", "NumWebVisitsMonth"]]

# groupby Kidhome
Kh_data = marketing_data.groupby("Kidhome")["NumWebVisitsMonth"].sum()
print(Kh_data)

###### Appending
marketing_append1 = pd.read_csv("marketing_campaign_append1.csv")
marketing_append2 = pd.read_csv("marketing_campaign_append2.csv")
appended_data = pd.concat([marketing_append1, marketing_append2])
print(appended_data)

###### Concatenation
marketing_concat1 = pd.read_csv("marketing_campaign_concat1.csv")
marketing_concat2 = pd.read_csv("marketing_campaign_concat2.csv")
concat_data = pd.concat([marketing_concat1, marketing_concat2], axis=1)
print(concat_data)

###### Merging
data1 = pd.read_csv("marketing_campaign_merge1.csv")
data2 = pd.read_csv("marketing_campaign_merge2.csv")
merge_dataset = pd.merge(data1, data2, on="ID")
print(merge_dataset)

