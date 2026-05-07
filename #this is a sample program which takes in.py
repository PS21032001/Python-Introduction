#this is a sample program which takes in an input and prints out the desired output
while True:
    name_input = input("What is your name? \n")
    num_input = int(input("How many times do you want to print your name? \n"))
    for i in range (num_input):
        print (name_input)