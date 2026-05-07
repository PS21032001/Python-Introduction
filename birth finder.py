from datetime import datetime
print ("\n Every input has to strictly be a number.\n ")
now = datetime.now()
pastyear_int = int (input ("What year were you born in?\n"))
if pastyear_int > now.year:
    print ("Your age is fugazzi and so are you.")
else:
    pastmonth_int = int (input ("What month were you born in?\n"))
    pastday_int = int (input ("What day were you born on?\n"))
    month_or_months = now.month - pastmonth_int
    if month_or_months == 1:
        print (f"\nCongratulations you are {now.year - pastyear_int} years, {month_or_months} month, and {now.day - pastday_int} days old...")
    else:
        print (f"\nCongratulations you are {now.year - pastyear_int} years, {month_or_months} months, and {now.day - pastday_int} days old...")
    print(f" ...and the current time is {now}\n")