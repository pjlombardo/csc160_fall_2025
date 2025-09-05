'''
File:       U1_02_user_interaction.py
Author:     P. Lombardo
Date:       ...
Purpose:    This program will interact with a user and utilize some python
            expressions to make some computations and custom print some output.
            In particular, we ask the user for a first and last name, as well as
            the year they were born.  We print a welcome message and the approximate
            number of days, hours, and months that person has been alive.
'''
# Global Constants
CURRENT_YEAR = 2025
DAYS_IN_YEAR = 365
MONTHS_IN_YEAR = 12

# Get user information
first_name = input("What is your first name? ")
last_name = input("What is your last name?")
    # need to "force" birth_year to be an integer (int)
birth_year = int( input("What year were you born in?") )

# Compute approximate age and do time conversions
age_in_years = CURRENT_YEAR - birth_year
age_in_months = age_in_years * MONTHS_IN_YEAR
    # do the same thing, but compute number of days old
age_in_days = age_in_years * DAYS_IN_YEAR

# print our information
print("Hi," , first_name, last_name)
print("You were born in ", birth_year)
print("You are about", age_in_years, "years old.")
print("You are about", age_in_months, "months old.")
print("You are about", age_in_days, "days old.")


