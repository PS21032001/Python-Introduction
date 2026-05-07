#swapping numbers
x = int(input("Enter x.\n"))
y = int(input("Enter y.\n"))

d = x
k = y
y = d
x = k

print ("Congrats your numbers have been swapped.")
take_value = input("Enter what you wanted to be print.")
if take_value == 'x':
    print (x)
elif take_value == 'y':
    print (y)
else:
    print ("Invalid output.")