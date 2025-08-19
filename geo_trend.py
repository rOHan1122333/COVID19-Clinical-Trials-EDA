import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
df = pd.read_csv("COVID_trials.csv")
# Extract "Country" from Locations column if not already done
if "Country" not in df.columns:
    df["Country"] = df["Locations"].astype(str).apply(lambda x: str(x).split(",")[-1].strip())

# Count trials per country
country_counts = df["Country"].value_counts().head(15)  # top 15 countries

# Plot
plt.figure(figsize=(12,6))
sns.barplot(x=country_counts.values, y=country_counts.index, palette="coolwarm")
plt.title("Top 15 Countries Contributing to COVID-19 Clinical Trials")
plt.xlabel("Number of Trials")
plt.ylabel("Country")
plt.show()

# Print summary
print("\n--- Top 10 Countries ---")
print(country_counts.head(10))
