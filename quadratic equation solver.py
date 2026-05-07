#quadratic equation solver
import cmath as cm
a = int(input("Enter a\n"))
b = int(input("Enter b\n"))
c = int(input("Enter c\n"))

d = cm.sqrt(b*b - 4*a*c)

formula_positive = (-b+d)/(2*a)
formula_negative = (-b-d)/(2*a)

print(f"The zeroes are {formula_positive} and {formula_negative}.")