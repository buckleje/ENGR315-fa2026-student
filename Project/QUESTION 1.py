import pandas as pd 
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# STEP 1: LOAD DATA

df = pd.read_excel("stock portfolio performance data set.xlsx", sheet_name="all period", header=1) # load the "all period" tab of the excel file into a pandas dataframe

df.columns = df.columns.str.strip() # remove random extra spaces from column headers

# STEP 2: COUNT HOW MANY CRITERIA ARE IN EACH PORTFOLIO

criteria = ["Large B/P", "Large ROE", "Large S/P", "Large Return Rate in the last quarter", "Large Market Value", "Small systematic Risk"] # examine just these columns

df["criteria_count"] = (df[criteria] > 0).sum(axis=1) # count how many criteria of each strategy have a nonzero value and store it
# STEP 3: GROUP PORTFOLIOS BY NUMBER OF CRITERIA

Group_1 = df[df["criteria_count"] == 1] # keep only the rows where there is 1 criterion
Group_2 = df[df["criteria_count"] == 2] # keep only the rows where there are 2 criteria
Group_3 = df[df["criteria_count"] == 3] # keep only the rows where there are 3 criteria
Group_4 = df[df["criteria_count"] == 4] # keep only the rows where there are 4 criteria
Group_5 = df[df["criteria_count"] == 5] # keep only the rows where there are 5 criteria
Group_6 = df[df["criteria_count"] == 6] # keep only the rows where there are 6 criteria

print("Strategies with 1 criterion:", len(Group_1))
print("Strategies with 2 criteria:", len(Group_2))
print("Strategies with 3 criteria:", len(Group_3))
print("Strategies with 4 criteria:", len(Group_4))
print("Strategies with 5 criteria:", len(Group_5))
print("Strategies with 6 criteria:", len(Group_6))

# STEP 4: CALCULATE STATISTICS

# Mean
mean_1 = Group_1["Annual Return"].mean()
mean_2 = Group_2["Annual Return"].mean()
mean_3 = Group_3["Annual Return"].mean()
mean_4 = Group_4["Annual Return"].mean()
mean_5 = Group_5["Annual Return"].mean()
mean_6 = Group_6["Annual Return"].mean()

# Standard Deviation
std_1 = Group_1["Annual Return"].std()
std_2 = Group_2["Annual Return"].std()
std_3 = Group_3["Annual Return"].std()
std_4 = Group_4["Annual Return"].std()
std_5 = Group_5["Annual Return"].std()
std_6 = Group_6["Annual Return"].std()

# Range
range_1 = Group_1["Annual Return"].max() - Group_1["Annual Return"].min()
range_2 = Group_2["Annual Return"].max() - Group_2["Annual Return"].min()
range_3 = Group_3["Annual Return"].max() - Group_3["Annual Return"].min()
range_4 = Group_4["Annual Return"].max() - Group_4["Annual Return"].min()
range_5 = Group_5["Annual Return"].max() - Group_5["Annual Return"].min()
range_6 = Group_6["Annual Return"].max() - Group_6["Annual Return"].min()

print("\n1 Criterion - Mean:", mean_1, "Standard Deviation:", std_1, "Range:", range_1)
print("2 Criterion - Mean:", mean_2, "Standard Deviation:", std_2, "Range:", range_2)
print("3 Criterion - Mean:", mean_3, "Standard Deviation:", std_3, "Range:", range_3)
print("4 Criterion - Mean:", mean_4, "Standard Deviation:", std_4, "Range:", range_4)
print("5 Criterion - Mean:", mean_5, "Standard Deviation:", std_5, "Range:", range_5)
print("6 Criterion - Mean:", mean_6, "Standard Deviation:", std_6, "Range:", range_6)

# STEP 5: MAKE A BOX PLOT OF INVESTMENT CRITERIA VS % ANNUAL RETURN

plt.boxplot([Group_1["Annual Return"] * 100, Group_2["Annual Return"] * 100, Group_3["Annual Return"] * 100, Group_4["Annual Return"] * 100,
             Group_5["Annual Return"] * 100, Group_6["Annual Return"] * 100], showmeans=True)

plt.xlabel("Number of Investment Criteria")
plt.ylabel("Annual Return (%)")
plt.title("Annual Return by Number of Investment Criteria")
plt.show()

# STEP 6: SEPARATE THE DATA INTO 1 VS MULTIPLE GROUPS TO RUN A T-TEST

one_criterion = Group_1["Annual Return"] # group with 1 criterion

multiple_criterion = df[df["criteria_count"] > 1]["Annual Return"] # if there are multiple criteria, save the annual return value

print("\nStrategies with 1 criterion:", len(Group_1))
print("Strategies with multiple criterion:", len(multiple_criterion))

# STEP 7: RUN A TWO-SAMPLE T-TEST

alpha = 0.05

t_value, p_value = ttest_ind(one_criterion, multiple_criterion, equal_var=False) # conduct the t-test not assuming their variance is the same

print("\nT-Test Results Comparing 1 Criterion vs Multiple Criterion")
print("T-value:", t_value)
print("P-value:", p_value)

if p_value < alpha:
    print("Reject the null hypothesis. There is a statistically significant difference in mean annual return.")
else: 
    print("Fail to reject the null hypothesis")