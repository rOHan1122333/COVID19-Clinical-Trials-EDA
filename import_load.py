# Import required libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Load the dataset
df = pd.read_csv("COVID_trials.csv")

# Display basic information
print("Shape of dataset:", df.shape)
print("\nColumns in dataset:\n", df.columns.tolist())
print("\nFirst 5 rows:\n", df.head())
print("\n--- Info ---")
print(df.info())
print("\n--- Numerical Summary ---")
print(df.describe())
print("\n--- Categorical Summary ---")
print(df.describe(include="object"))
print("\n--- Missing Values ---")
print(df.isnull().sum())


