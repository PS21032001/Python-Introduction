#birth finder 2
from datetime import datetime

print ("\n Every input has to be exactly a number.\n")

pastyear = int(input("Enter the year you were born in.\n"))
pastmonth = int(input("Enter the month you were born in.\n"))
pastday = int(input("Enter the day you were born on.\n"))

now = datetime.now()

age_year = now.year - pastyear
age_month = now.month - pastmonth
age_day = now.day - pastday

if age_day < 0:
    age_day += 30
    age_month -= 1
if age_month < 0:
    age_month += 12
    age_year -= 1
print (f"You are {age_year} years old, {age_month} months and {age_day} days old.")
