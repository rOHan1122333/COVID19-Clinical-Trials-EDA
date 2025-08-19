import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
df = pd.read_csv("COVID_trials.csv")

# Helper function for bar plots
def plot_bar(column, title, xlabel):
    plt.figure(figsize=(12,6))
    sns.countplot(data=df, x=column, order=df[column].value_counts().index, palette="viridis")
    plt.title(title, fontsize=14)
    plt.xlabel(xlabel)
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.show()

# 1. Status of Clinical Trials
plot_bar("Status", "Status of Clinical Trials", "Trial Status")

# 2. Phases of Clinical Trials
plot_bar("Phases", "Distribution of Trial Phases", "Trial Phase")

# 3. Age Group Distribution
plot_bar("Age", "Age Group Distribution", "Age Group")

# 4. Gender Distribution
plot_bar("Gender", "Gender Distribution", "Gender")
