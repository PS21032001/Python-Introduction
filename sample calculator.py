while True:
    choice = int (input("Choose 1 to add, 2 to subtract, 3 to multiply, 4 to divide."))
    if choice == "1":
        int_a = int(input("Input number 1."))
        int_b = int(input("Input number 2."))
        print (int_a + int_b)
    elif choice == "2":
        int_a = int(input("Input number 1."))
        int_b = int(input("Input number 2."))
        print (int_a - int_b)
    elif choice == "3":
        int_a = int(input("Input number 1."))
        int_b = int(input("Input number 2."))
        print (int_a * int_b)
    elif choice == "4":
        int_a = int(input("Input number 1."))
        int_b = int(input("Input number 2."))
        print (int_a / int_b)
    else:
        print ("Enter a valid operator.")