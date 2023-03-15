import math
a = int(input("Value of A:"))
b = int(input("Value of B:"))
c = int(input("Value of C:"))
quadrat_pos = (-b+(b**2-4*a*c)**0.5)/(2*a)
quadrat_neg = (-b-(b**2-4*a*c)**0.5)/(2*a)
print((quadrat_pos))
print((quadrat_neg))
