#trying to get add a number
user_input = int(input("Enter the number you want to be incremented.\n"))
inc_input = int(input("How many times do you want the number to be incremented.\n\n"))
for _ in range (inc_input):
    user_input += 1
    print (user_input)