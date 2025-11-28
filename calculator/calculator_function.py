import numpy as np

# get the current date
date_today = np.datetime64('today', 'D')

print("Today's date:")
print(date_today)

# peliminary datse for testing
date = '2025-10-10'

# convert the dates to numpy datetime64 objects
date1 = np.datetime64(date_today)
date2 = np.datetime64(date)

# calculate the difference in days
num_of_days = date1 - date2

#output
print(f"Number of days between today and the entered date: {num_of_days} ")

# removed user input for testing purposes
