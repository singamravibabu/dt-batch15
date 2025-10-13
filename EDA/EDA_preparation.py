import numpy as np
import pandas as pd
from scipy import stats

marketing_data = pd.read_csv("marketing_campaign.csv")
marketing_data = marketing_data[["ID", "Year_Birth", "Education", 
                "Marital_Status", "Income", 
                "Kidhome", "Teenhome", "Dt_Customer",
                  "Recency", "NumStorePurchases", "NumWebVisitsMonth"]]

# Groupby
Kh_webvisits = marketing_data.groupby("Kidhome")["NumWebVisitsMonth"].sum()
print(Kh_webvisits)

######### Appending
marketing_campaign_append1 = pd.read_csv("marketing_campaign_append1.csv")
marketing_campaign_append2 = pd.read_csv("marketing_campaign_append2.csv")
appended_data = pd.concat([marketing_campaign_append1,
                           marketing_campaign_append2])
print(appended_data)


######### Concatenation
marketing_campaign_concat1 = pd.read_csv("marketing_campaign_concat1.csv")
marketing_campaign_concat2 = pd.read_csv("marketing_campaign_concat2.csv")
concatenated_data = pd.concat([marketing_campaign_concat1,
                           marketing_campaign_concat2], axis=1)
print(concatenated_data)

######### Merge datasets
marketing_campaign_merge1 = pd.read_csv("marketing_campaign_merge1.csv")
marketing_campaign_merge2 = pd.read_csv("marketing_campaign_merge2.csv")
merged_data = pd.merge(marketing_campaign_merge1,
                       marketing_campaign_merge2, on="ID")
print(merged_data)