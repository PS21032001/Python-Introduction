user_input = int(input("Tell me the number."))
if user_input < 2:
    print ("The number is NOT prime.")
else:
    is_prime = True
    for i in range (2, user_input):
        if user_input%i == 0:
            is_prime = False
            break
    
    if is_prime == True:
        print ("The number is PRIME")
    else:
        print ("The number is NOT PRIME")