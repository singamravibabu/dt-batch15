import pandas as pd

marketing_data = pd.read_csv("marketing_campaign.csv")
marketing_data = marketing_data[["ID", "Year_Birth", "Education",
                 "Marital_Status", "Income", "Kidhome", 
                 "Teenhome", "Dt_Customer", "Recency",
                 "NumStorePurchases", "NumWebVisitsMonth"]]

# SORTING BY 'NumStorePurchases' IN DESCENDING ORDER
marketing_data = marketing_data.sort_values("NumStorePurchases", ascending=False)

# CATEGORIZING DATA BASED ON 'NumStorePurchases'
StorePurchases_data = pd.cut(x=marketing_data["NumStorePurchases"],
       bins=[0, 4, 8, 13],
       labels=["Low", "Moderate", "High"])

# REMOVE DUPLICATE DATA
marketing_data2 = marketing_data[["Education", "Marital_Status",
                                   "Kidhome", "Teenhome"]]
marketing_data2 = marketing_data2.drop_duplicates()

# DROPPING ROWS AND COLUMNS
marketing_data2 = marketing_data2.drop(labels=[2237], axis=0)
marketing_data2 = marketing_data2.drop(labels=["Teenhome"], axis=1)
print(marketing_data2)

# REPLACING DATA
marketing_data["Teenhome_replaced"] = marketing_data["Teenhome"].replace([0, 1, 2], 
                                   ["Has no teen", "Has teen", "Has teen"])

marketing_data["Income"] = marketing_data["Income"].fillna(0)
marketing_data["Income"] = marketing_data["Income"].astype(int)

print(marketing_data.dtypes)