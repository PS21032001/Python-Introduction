def rec_natty(n):
    if n <= 1:
        return n
    else:
        return n + rec_natty(n-1)

natty_input = int(input("How many numbers do you want?"))
print (rec_natty(natty_input))