import pandas as pd
import numpy as np

# Load datasets
df_80 = pd.read_csv("task2_dashboard\\data\\Churn Prdiction Data\\churn-bigml-80.csv")
df_20 = pd.read_csv("task2_dashboard\\data\\Churn Prdiction Data\\churn-bigml-20.csv")

print("churn 80.csv shape :", df_80.shape)
print("churn 20.csv shape :", df_20.shape)

# Verify both have the same columns
print("\nSame columns ?", df_80.columns.tolist() == df_20.columns.tolist())

df = pd.concat([df_80, df_20], ignore_index=True)

print(f"\n Merged dataset shape : {df.shape}")
print(f"Expected rows : {len(df_80) + len(df_20)}")
df.head()

# Check data types and missing values
print("Data types :\n", df.dtypes)
print("\nMissing values :\n", df.isnull().sum())
print("\nUnique values per column :")
for col in df.columns:
    print(f"   {col} : {df[col].nunique()} unique values")


# Verify distribution is consistent
print("\nChurn distribution after merge :")
print(df["Churn"].value_counts())
print(f"\nChurn rate : {df['Churn'].value_counts(normalize=True) * 100}")

# 1. Standardize column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# 2. Check and remove duplicates
duplicates = df.duplicated().sum()
print(f"Duplicates : {duplicates}")
df = df.drop_duplicates()

# 3. Convert Churn to binary
df["churn_binary"] = df["churn"].map({True: 1, False: 0})

# 4. Create tenure groups based on account length
df["account_group"] = pd.cut(
    df["account_length"],
    bins=[0, 50, 100, 150, 250],
    labels=["Short (0-50)", "Medium (50-100)",
            "Long (100-150)", "Very Long (150+)"]
)

# 5. Total minutes (day + eve + night + intl)
df["total_minutes"] = (df["total_day_minutes"] +
                       df["total_eve_minutes"] +
                       df["total_night_minutes"] +
                       df["total_intl_minutes"])

# 6. Total charges (day + eve + night + intl)
df["total_charges"] = (df["total_day_charge"] +
                       df["total_eve_charge"] +
                       df["total_night_charge"] +
                       df["total_intl_charge"])



# 7. Total calls
df["total_calls"] = (df["total_day_calls"] +
                     df["total_eve_calls"] +
                     df["total_night_calls"] +
                     df["total_intl_calls"])

print("total_charges dtype :", df["total_charges"].dtype)
print("total_minutes dtype :", df["total_minutes"].dtype)
print("total_calls dtype   :", df["total_calls"].dtype)

print("\nSample total_charges :")
print(df["total_charges"].head())

print("\nStats :")
print(df[["total_charges", "total_minutes", "total_calls"]].describe().round(2))

# 8. Customer service calls group
df["service_calls_group"] = pd.cut(
    df["customer_service_calls"],
    bins=[-1, 1, 3, 5, 10],
    labels=["0-1 calls", "2-3 calls",
            "4-5 calls", "6+ calls"]
)

print(" Cleaning done")
print(f"Final shape : {df.shape}")
print(f"\nNew columns added : {['churn_binary', 'account_group', 'total_minutes', 'total_charges', 'total_calls', 'service_calls_group']}")
print(df.head())

#KPIs
total_customers    = len(df)
churn_rate         = df["churn_binary"].mean() * 100
avg_charges        = df["total_charges"].mean()
avg_account_length = df["account_length"].mean()
avg_service_calls  = df["customer_service_calls"].mean()
intl_plan_churn    = df[df["international_plan"] == "Yes"]["churn_binary"].mean() * 100

print(" Key Metrics :")
print(f"   Total Customers       : {total_customers:,}")
print(f"   Churn Rate            : {churn_rate:.2f}%")
print(f"   Avg Total Charges     : ${avg_charges:.2f}")
print(f"   Avg Account Length    : {avg_account_length:.1f} days")
print(f"   Avg Service Calls     : {avg_service_calls:.2f}")
print(f"   Intl Plan Churn Rate  : {intl_plan_churn:.2f}%")

df.to_csv("task2_dashboard\\results\\churn_clean.csv", index=False , sep=";",decimal=",")
print(" churn_clean.csv exported — ready for Power BI !")
print(f"\nFinal columns :")
for col in df.columns:
    print(f"   {col}")