import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
df = pd.read_csv("COVID_trials.csv")

# Step 3: Handling Missing Data

# 1. Calculate missing data percentage
missing_data = df.isnull().mean() * 100
print("\n--- Percentage of Missing Data ---")
print(missing_data.sort_values(ascending=False))

# 2. Drop columns with >90% missing values
high_missing_cols = missing_data[missing_data > 90].index
print("\n--- Dropping High Missing Columns ---")
print(high_missing_cols)
df.drop(columns=high_missing_cols, inplace=True)

# 3. Fill missing categorical features with 'Missing <col>'
categorical_features = df.select_dtypes(include="object").columns
for col in categorical_features:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(f"Missing {col}")

# 4. Fill missing numerical features with median
numerical_features = df.select_dtypes(exclude="object").columns
for col in numerical_features:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].median())

# 5. Verify no missing values
print("\n--- Missing Values After Cleaning ---")
print(df.isnull().sum())


