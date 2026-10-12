import sys

"""
Create a program which will provide answers to the questions posed in the assignment description.
We've provided a function which will parse the NYT covid database file (named "us-counties.csv"); 
however, its correct implementation will be up to you. DO NOT MODIFY THIS FUNCTION.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.
"""


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information

    ____________________ DO NOT MODIFY THIS FUNCTION ___________________
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

### YOUR CODE HERE ###

# set up the file path
filepath = "data/covid/us-counties.csv"

# set data equal to the correct file
data = parse_nyt_data(filepath)




# QUESTION 1: When was the first positive COVID case in Harrisonburg? When was the first positive case in Rockingham County?

# Set the first case  date variables equal to 0
First_Case_Harrisonburg = 0
First_Case_Rockingham = 0

# run through all the entries and label each index to make it easier to read
for entry in data:
    date = entry[0]
    county = entry[1]
    state = entry[2]
    fips = entry[3]
    cases = entry[4]
    deaths = entry[5]

    if state == "Virginia" and cases > 0: # if there are any cases and it is in Virginia then continue

        # once it finds an entry that is also in harrisonburg, update the date variable to that date
        if county == "Harrisonburg city" and First_Case_Harrisonburg == 0: 
            First_Case_Harrisonburg = date

        # same thing for Rockingham
        elif county == "Rockingham" and First_Case_Rockingham == 0:
            First_Case_Rockingham = date

    if First_Case_Harrisonburg != 0 and First_Case_Rockingham !=0: # stop when we find the start date for each location
        break

# print start dates
print("Question 1 answers:")
print("First Harrisonburg case:", First_Case_Harrisonburg)
print("First Rockingham case:", First_Case_Rockingham)




# QUESTION 2: On what date was the greatest number of new cases reported in Harrisonburg? What date in Rockingham County?

# set initial variables equal to 0
previous_cases_Harrisonburg = 0
previous_cases_Rockingham = 0 

max_new_cases_Harrisonburg = 0
max_new_cases_Rockingham = 0

max_date_Harrisonburg = 0
max_date_Rockingham = 0

for entry in data:
    date = entry[0]
    county = entry[1]
    state = entry[2]
    fips = entry[3]
    cases = entry[4]
    deaths = entry[5]

    if state == "Virginia": # make sure the entry is in virginia

        if county == "Harrisonburg city": # make sure the entry is in Harrisonburg

            new_cases = cases - previous_cases_Harrisonburg # finds the new cases of that specific day

            if new_cases > max_new_cases_Harrisonburg: # update the max cases each time we find a bigger one
                max_new_cases_Harrisonburg = new_cases
                max_date_Harrisonburg = date

            previous_cases_Harrisonburg = cases # this becomes the values from the previous day to be used for the next day

        
        elif county == "Rockingham": # same thing for Rockingham

            new_cases = cases - previous_cases_Rockingham

            if new_cases > max_new_cases_Rockingham:
                max_new_cases_Rockingham = new_cases
                max_date_Rockingham = date

            previous_cases_Rockingham = cases

# print the date with the most new cases and the number of new cases on that day
print("\nQuestion 2 answers:")
print("Harrisonburg greatest new cases date:", max_date_Harrisonburg)
print("Harrisonburg greatest new cases:", max_new_cases_Harrisonburg)
print("Rockingham greatest new cases date:", max_date_Rockingham)
print("Rockingham greatest new cases:", max_new_cases_Rockingham)



# QUESTION 3: What was the worst seven-day period in Harrisonburg city for new COVID cases? What period in Rockingham County?

# set initial variables equal to 0
previous_cases_Harrisonburg = 0
previous_cases_Rockingham = 0 

max_7_day_cases_Harrisonburg = 0
max_7_day_cases_Rockingham = 0

max_start_date_Harrisonburg = 0
max_start_date_Rockingham = 0

max_end_date_Harrisonburg = 0
max_end_date_Rockingham = 0

seven_day_sum_Harrisonburg = 0
seven_day_sum_Rockingham = 0

# create lists so we can find the 7 day period
Harrisonburg_daily_cases = []
Rockingham_daily_cases = []

Harrisonburg_dates = []
Rockingham_dates = []

for entry in data:
    date = entry[0]
    county = entry[1]
    state = entry[2]
    fips = entry[3]
    cases = entry[4]
    deaths = entry[5]

    if state == "Virginia": # make sure the entry is in Virginia

        if county == "Harrisonburg city": # make sure the entry is in Harrisonburg

            new_cases = cases - previous_cases_Harrisonburg # finds the new cases of that specific day

            Harrisonburg_daily_cases.append(new_cases) # add the new cases for that day to the list
            Harrisonburg_dates.append(date) # add that date to the list

            # when the list becomes 7 entries long, get the sum of the 7 most recent entries
            if len(Harrisonburg_daily_cases) >= 7: #
                seven_day_sum_Harrisonburg = sum(Harrisonburg_daily_cases[-7:])

                # update the max 7 day cases each time we find a bigger one
                if seven_day_sum_Harrisonburg > max_7_day_cases_Harrisonburg: 
                    max_7_day_cases_Harrisonburg = seven_day_sum_Harrisonburg
                    max_end_date_Harrisonburg = date # the end date is the current date
                    max_start_date_Harrisonburg = Harrisonburg_dates[-7] # the start date the first in the set of seven

            previous_cases_Harrisonburg = cases # this becomes the values from the previous day to be used for the next day

        
        elif county == "Rockingham": # same thing for Rockingham

            new_cases = cases - previous_cases_Rockingham

            Rockingham_daily_cases.append(new_cases)
            Rockingham_dates.append(date)

            if len(Rockingham_daily_cases) >=7:
                seven_day_sum_Rockingham = sum(Rockingham_daily_cases[-7:])

                if seven_day_sum_Rockingham > max_7_day_cases_Rockingham:
                    max_7_day_cases_Rockingham = seven_day_sum_Rockingham
                    max_end_date_Rockingham = date
                    max_start_date_Rockingham = Rockingham_dates[-7]

            previous_cases_Rockingham = cases

# print the date with the most new cases and the number of new cases on that day
print("\nQuestion 3 answers:")
print("Harrisonburg worst 7 day period:", max_start_date_Harrisonburg, "to", max_end_date_Harrisonburg)
print("Harrisonburg worst 7 day period total:", max_7_day_cases_Harrisonburg)
print("Rockingham worst 7 day period:", max_start_date_Rockingham, "to", max_end_date_Rockingham)
print("Rockingham worst 7 day period total:", max_7_day_cases_Rockingham)