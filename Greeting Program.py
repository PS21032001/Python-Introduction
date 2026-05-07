#Greeting Program
current_time = int(input("What time is it?\n"))
if 0000 <= current_time < 1200:
    print ("Good Morning")
elif 1200 <= current_time <  1800:
    print ("Good Afternoon")
elif 1800 <= current_time <2359:
    print ("Good Evening")
else:
    print ("good luck traversing weird times, space monkey")