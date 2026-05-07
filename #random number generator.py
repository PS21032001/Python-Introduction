#random code generator
import random as random
from datetime import datetime

now = datetime.now()
seed = now.microsecond
random.seed(seed)
user_input = int(input("How many random numbers do you want?\n"))
for i in range(user_input):
    print(random.randint(1, 1000))