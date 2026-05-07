while True:
    choice = float(input("Choose 1 to add, 2 to subtract, 3 to multiply, 4 to divide and 5 to exit \n"))
    if choice == 1:
        int_a = float(input("Input number 1. \n"))
        int_b = float(input("Input number 2. \n"))
        print (int_a + int_b)
    elif choice == 2:
        int_a = float(input("Input number 1. \n"))
        int_b = float(input("Input number 2. \n"))
        print (int_a - int_b)
    elif choice == 3:
        int_a = float(input("Input number 1. \n"))
        int_b = float(input("Input number 2. \n"))
        print (int_a * int_b)
    elif choice == 4:
        int_a = float(input("Input number 1. \n"))
        int_b = float(input("Input number 2. \n"))
        if int_b == 0:
            print ("Infinite.\n")
        else:
            print (int_a/int_b)
    elif choice == 5:
        break
    else:
        print ("Enter a valid operator.")