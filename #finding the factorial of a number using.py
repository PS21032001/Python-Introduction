#finding the factorial of a number using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial (n-1)

user_int = int(input("How many?\n"))

if user_int < 0:
    print ("Enter a valid number.")
else:
    print (factorial(user_int))