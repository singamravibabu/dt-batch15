import pandas as pd

marketing_data = pd.read_csv("marketing_campaign.csv")
marketing_data = marketing_data[["ID", "Year_Birth", "Education",
                 "Marital_Status", "Income",
                   "Kidhome", "Teenhome", "Dt_Customer",
                     "Recency", "NumStorePurchases", "NumWebVisitsMonth"]]

Kh_webvisits = marketing_data.groupby("Kidhome")["NumWebVisitsMonth"].sum()
print(Kh_webvisits)

# APPENDING
append1 = pd.read_csv("marketing_campaign_append1.csv")
append2 = pd.read_csv("marketing_campaign_append2.csv")
marketing_append = pd.concat([append1, append2]) # combine the rows of two dataframes
print(marketing_append)

# CONCATENATION
concat1 = pd.read_csv("marketing_campaign_concat1.csv")
concat2 = pd.read_csv("marketing_campaign_concat2.csv")
marketing_concat = pd.concat([concat1, concat2], axis=1) # combine the columns of two dataframes
print(marketing_concat)

# MERGING
merge1 = pd.read_csv("marketing_campaign_merge1.csv")
merge2 = pd.read_csv("marketing_campaign_merge2.csv")
marketing_merged = pd.merge(merge1, merge2, on="ID")
print(marketing_merged)
