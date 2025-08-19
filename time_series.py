import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv("COVID_trials.csv")

# Ensure date columns are in datetime format
df['Start Date'] = pd.to_datetime(df['Start Date'], errors='coerce')
df['Primary Completion Date'] = pd.to_datetime(df['Primary Completion Date'], errors='coerce')
df['Completion Date'] = pd.to_datetime(df['Completion Date'], errors='coerce')

# 1. Trials started over time (monthly)
trials_over_time = df['Start Date'].dt.to_period('M').value_counts().sort_index()
trials_over_time.plot(kind='line', figsize=(12,6), marker='o')
plt.title("COVID-19 Clinical Trials Started Over Time")
plt.xlabel("Start Month")
plt.ylabel("Number of Trials")
plt.grid(True)
plt.show()

# 2. Primary Completion Dates distribution
completion_over_time = df['Primary Completion Date'].dt.to_period('M').value_counts().sort_index()
completion_over_time.plot(kind='line', figsize=(12,6), marker='o', color='green')
plt.title("COVID-19 Trials Primary Completion Over Time")
plt.xlabel("Completion Month")
plt.ylabel("Number of Trials")
plt.grid(True)
plt.show()

# 3. Compare Start vs Completion trends
plt.figure(figsize=(12,6))
trials_over_time.plot(label="Started", marker='o')
completion_over_time.plot(label="Completed", marker='s')
plt.title("Started vs Completed Trials Over Time")
plt.xlabel("Month")
plt.ylabel("Number of Trials")
plt.legend()
plt.grid(True)
plt.show()

