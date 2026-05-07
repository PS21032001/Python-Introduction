# checking for prime numbers
user_input = int(input("Enter the number you want to get checked."))
if 0 < user_input <= 3:
    print ("The number is a prime number")
else:
    for i in range (3, user_input-1):
        if user_input%i == 0:
            break
        print ("The given number is NOT a prime number.")
    print ("The given number is a prime number.")