#check for leap year excluding centuries and numbers divisible by 4
from datetime import datetime
user_input = int(input("What year do you want to check?"))
if user_input % 100 == 0:
    print ("Fun Fact - Century years aren't leap years.")
elif user_input % 4 == 0:
    print ("It is a leap year.")
else:
    print ("This is not a leap year.")




