# Exercise 1: Print current date and time in Python
import datetime
# print date and time
print(datetime.datetime.now())
# print time only
print(datetime.datetime.now().time())
# print date only
print(datetime.datetime.now().date())

# Exercise 2: Convert string into a datetime object
# date_string = "Feb 25 2020 4:20PM"
# date_time_object = datetime.(date_string,'%b %d %Y %I:%M%p')
# print(date_time_object)

# Exercise 3: Subtract a week (7 days)  from a given date in Python
from datetime import datetime, timedelta
todays_date = datetime.now().date()
print('Todays date is :',todays_date)

days_to_subtract = 7
result_date = todays_date - timedelta(days=days_to_subtract)
print('Before date :',result_date)

# Exercise 4: Print a date in a the following format
# Day_name  Day_number  Month_name  Year

# Exercise 10: Calculate number of days between two given dates

date_1 = datetime(2020, 2, 25)
date_2 = datetime(2020, 9, 17)
date_1 = datetime(2020, 2, 25).date()
date_2 = datetime(2020, 9, 17).date()

delta = None
if date_1 > date_2:
    print('date_1 is greater ')
    delta = date_1 - date_2
else:
    print('date_2 is greater')
    delta = date_2 - date_1

print('Difference is',delta.days,'days')