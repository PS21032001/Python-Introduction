def recursion(n):
    if n <= 1:
        return n
    else:
        return (recursion(n-1) + recursion(n-2))

nterms = int(input("How many terms?"))
if nterms <= 0:
    print ("Enter a postitive integer.")
else :
    for i in range (nterms):
        print (recursion(i))

    