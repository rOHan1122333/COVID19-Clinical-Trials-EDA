import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("COVID_trials.csv")
# Step 7: Conclusion & Insights

def project_conclusion():
    print("========== PROJECT CONCLUSION ==========\n")
    
    print("1. Data Quality")
    print("- Columns with excessive missing values (e.g., 'Results First Posted', 'Study Documents') were dropped.")
    print("- Remaining missing values were imputed (categorical -> 'Missing <col>', numeric -> median).")
    
    print("\n2. Trial Status")
    print("- Majority of trials are either 'Completed' or 'Recruiting'.")
    print("- Some trials are still 'Not yet recruiting' or 'Withdrawn'.")
    
    print("\n3. Trial Phases")
    print("- Phase 2 and Phase 3 trials dominate COVID-19 research.")
    print("- A smaller number of Phase 1 and Phase 4 studies exist.")
    
    print("\n4. Demographics")
    print("- Most studies target 'Adult' populations.")
    print("- Gender distribution shows trials often recruit 'All' genders.")
    
    print("\n5. Geographic Trends")
    print("- USA, France, UK, Italy, and Spain contributed the highest number of trials.")
    print("- Developing countries (India, Brazil, Egypt, etc.) also made significant contributions.")
    
    print("\n6. Time Trends")
    print("- Number of trials rapidly increased in 2020 during the pandemic peak.")
    print("- Completion rates began catching up in 2021–2022.")
    
    print("\n========== END OF SUMMARY ==========")

# Call function
project_conclusion()

