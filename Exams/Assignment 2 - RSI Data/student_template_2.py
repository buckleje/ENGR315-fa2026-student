"""
CULMINATING ASSIGNMENT 2: RSI

Create a program which will provide answers to the tasks posed in the assignment description.

For this assignment, you will start from scratch with this blank template.
It is your reponsibility to include all necessary program components in this file.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.

The relevant data file is named "all_participant_data_rsi.csv" and is located in data > drop-jump.

All file paths need to be relative and execute from this file's directory;
the Visual Studio Code setting "Python > Terminal: Execute in File Dir" 
must be enabled in File > Preferences > Settings.

See Canvas for additional requirements.
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp, norm, chisquare
import scipy.stats as stats

# Load RSI data
df = pd.read_csv("../../data/drop-jump/all_participant_data_rsi.csv")


# Set significance level
alpha = 0.05



# TASK 1: Paired T-test

# Select all force plate rsi measurments
force_plate_rsi = df["force_plate_rsi"].to_numpy()
# Select all accelermometer rsi measurments
accelerometer_rsi = df["accelerometer_rsi"].to_numpy()

# Calculate the difference between the two
difference = force_plate_rsi - accelerometer_rsi

# Perform a two sided t-test using the differences
t_value, p_value = ttest_1samp(difference, popmean=0)

# Print t-test results
print("TASK 1: Paired T-test")
print("Null Hypothesis: The average difference is zero.")
print("Alternative Hypothesis: The average difference is not zero.")
print("T-value:", t_value)
print("P-value:", p_value)

# Determine whether or not to reject the null hypothesis
if p_value < alpha:
    print("Reject the null hypothesis. The two methods produce significantly different RSI measurments.")
else:
    print("Fail to reject the null hypothesis. There is no statistically significant difference between the average rsi measurments.")



# TASK 2: Normal Distribution and Chi^2 Test

# Fit a normal distribution to the accelerometer RSI data
fitted_mean, fitted_std = norm.fit(accelerometer_rsi)

# Create evenly spaced bins
bins = np.linspace(fitted_mean - 2 * fitted_std, fitted_mean + 2 * fitted_std, 9)
# Include all values so we still catch values that are outside 2 standard deviations
bins = np.r_[-np.inf, bins, np.inf]

# Count how many measurements are in each bin
observed_counts, bin_boundaries = np.histogram(accelerometer_rsi, bins=bins)

# Calculate the expected counts for each bin by subtracting the chance it will be below the lower edge from the chance it will be below the upper edge
bin_probabilities = norm.cdf(bins[1:], loc=fitted_mean, scale=fitted_std) - norm.cdf(bins[:-1], loc=fitted_mean, scale=fitted_std)
# Multiply the probability of each bin by the total number of measurments to get the expected totals
expected_counts = bin_probabilities * len(accelerometer_rsi)

# Perform the Chi^2 Test
chi_squared, p_value = chisquare(observed_counts, expected_counts, ddof=2)

# Print Chi^2 results
print("\nTASK 2: Normal Distribution and Chi^2 Test")
print("Null Hypothesis: The accelerometer RSI data follow a normal distribution.")
print("Alternative Hypothesis: The accelerometer RSI data do not follow a normal distribution.")
print("Chi^2 value:", chi_squared)
print("P-value:", p_value)

# Determine whether or not to reject the null hypothesis
if p_value < alpha:
    print("Reject the null hypothesis. The accelerometer data does not follow a normal distribution.")
else:
    print("Fail to reject the null hypothesis. There is insufficient evidence that the accelerometer RSI data differ from a normal distribution")

# Create the histogram of the accelerometer RSI data
plt.hist(accelerometer_rsi, bins=15, label="Accelerometer RSI")

# Create the normal fitted distribution curve to overlay on top of the histogram
x = np.linspace(min(accelerometer_rsi), max(accelerometer_rsi), 500) # Generate x-values
bin_width = (max(accelerometer_rsi) - min(accelerometer_rsi)) / 15 # calculate bin width

# Generate the y-values by multiplying the probabliltiy density, measurement count, and bin width
y = norm.pdf(x, loc=fitted_mean, scale=fitted_std) * len(accelerometer_rsi) * bin_width 
plt.plot(x, y, label="Fitted Normal Distribution") # Create the plot

# Label graph
plt.title("Accelerometer Normal Distribution RSI Fit")
plt.xlabel("Accelerometer RSI")
plt.ylabel("Number of Measurments")
plt.legend()
plt.show()



# TASK 3: Participant F's 95% Confidence intervals

# Select participant F's measurments (search for entries in the trial column that start with F)
participant_F = df[df["trial"].str[0] == "F"]

# Print participant F's data
print("\nTask 3: Participant F 95% Confidence Intervals")
print(participant_F)

# Calculate the mean and standard deviation for the force plate and accelerometer for person F
force_plate_f_mean = participant_F["force_plate_rsi"].mean()
force_plate_f_std = participant_F["force_plate_rsi"].std()

accelerometer_f_mean = participant_F["accelerometer_rsi"].mean()
accelerometer_f_std = participant_F["accelerometer_rsi"].std()

# Print the means for the accelerometer and force plate data for participant F to have more context for the confidence intervals
print("Participant F force plate mean: ", force_plate_f_mean)
print("Participant F accelerometer mean: ", accelerometer_f_mean)

# Calculate the number of trials for Participant F
n = len(participant_F)

# Standard error for accelerometer and force plate
force_plate_f_error = force_plate_f_std / np.sqrt(n)
accelerometer_f_error = accelerometer_f_std / np.sqrt(n)

# Calculate the critical t-value. Use 0.975 because t.ppf() finds the t value corresponding to the probability on its left.
t_critical = stats.t.ppf(0.975, df=n-1) # Using 0.975 accounts for that extra 2.5% on the far left that will be outside out confidence interval

# Force plate confidence interval
force_plate_lower = force_plate_f_mean - t_critical * force_plate_f_error
force_plate_upper = force_plate_f_mean + t_critical * force_plate_f_error
# Accelerometer confidence interval
accelerometer_lower = accelerometer_f_mean - t_critical * accelerometer_f_error
accelerometer_upper = accelerometer_f_mean + t_critical * accelerometer_f_error

# Print confidence intervals
print("Force Plate 95% Confidence Interval:", force_plate_lower, force_plate_upper)
print("Accelerometer 95% Confidence Interval:", accelerometer_lower, accelerometer_upper)