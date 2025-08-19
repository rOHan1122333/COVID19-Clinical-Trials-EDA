# COVID19-Clinical-Trials-EDA
📖 Project Overview
This project explores COVID-19 clinical trials data using Python. The dataset comes from ClinicalTrials.gov and helps us understand:
Trial status & phases
emographics (age, gender)
Geographic trends (which countries contributed most)
Time trends (how trials evolved over 2020–2022)

🛠️ Setup Instructions
1️⃣ Install Required Libraries
Run this in your terminal (PowerShell / CMD):
pip install pandas numpy matplotlib seaborn


2️⃣ Project Files Overview
COVID_trials.csv → The dataset
import_load.py → Load dataset & initial exploration
Data_exploration.py → Handle missing data
uni_analysis.py → Univariate analysis (Status, Phases, Age, Gender)
bi_analysis.py → Bivariate analysis (Status vs Phases, etc.)
time_series.py → Time trends (started vs completed trials)
geo_trend.py → Geographic trends (top countries)
conclusion.py → Final summary & insights

🚀 Step-by-Step Execution
Step 1: Import & Explore Data
Run:python import_load.py
✔️ Loads the dataset, shows shape, columns, missing values, and summary stats.

Step 2: Handle Missing Data
Run:python Data_exploration.py
✔️ Drops columns with excessive missing data (e.g., Results First Posted, Study Documents).
✔️ Fills missing categorical values → "Missing <col>".
✔️ Fills missing numeric values → median.

Step 3: Univariate Analysis
Run:python uni_analysis.py
✔️ Visualizes:
Status of clinical trials
Trial phases distribution
Age group distribution
Gender distribution

Step 4: Bivariate Analysis
Run:python bi_analysis.py
✔️ Shows:
Status vs Phases (stacked bar chart)
Sample Conditions vs Outcome Measures
Enrollment distribution by Status (boxplot)

Step 5: Time Series Analysis
Run:python time_series.py
✔️ Trends over time:
Number of trials started per month
Completion dates trend
Comparison → Started vs Completed

Step 6: Geographic Trends
Run:python geo_trend.py
✔️ Visualizes Top 15 contributing countries (bar chart).
✔️ Prints top 10 country trial counts.

Step 7: Conclusion & Insights
Run:python conclusion.py
✔️ Prints structured insights:
Data quality & cleaning steps
Status and phase distribution
Demographics overview
Geographic trends
Time trends

✅ Sample Insights (from results)
Most trials are Completed or Recruiting. Phase 2 & Phase 3 dominate.
Trials mainly target Adults and often All genders.
USA, France, UK, Italy, Spain lead in contributions.
A surge of trials in 2020, with completions peaking 2021–2022.
