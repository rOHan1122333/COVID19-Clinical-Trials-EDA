import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("COVID_trials.csv")

# 1. Status vs Phases (stacked bar plot)
status_phase = pd.crosstab(df['Status'], df['Phases'])
status_phase.plot(kind='bar', stacked=True, figsize=(12,6), colormap="viridis")
plt.title("Status vs. Phases of Clinical Trials")
plt.xlabel("Trial Status")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# 2. Conditions vs Outcome Measures (top 10 for readability)
conditions_outcomes = df.groupby('Conditions')['Outcome Measures'].apply(lambda x: ', '.join(x.astype(str))).reset_index()

# Show only first 10 for readability
print("\n--- Conditions vs Outcome Measures (Sample) ---")
print(conditions_outcomes.head(10))

# 3. Enrollment distribution by Status (boxplot)
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x="Status", y="Enrollment")
plt.ylim(0, 5000)  # limit y-axis for readability
plt.title("Enrollment Distribution by Status")
plt.xticks(rotation=45)
plt.show()
