#finding the sum of natural numbers

def natty_nums(n):
    n = natty_input
    m = n-1 
    n = n + m
natty_input = int(input("How many numbers do you need?"))
for i in range(natty_input):
    natty_nums(i)