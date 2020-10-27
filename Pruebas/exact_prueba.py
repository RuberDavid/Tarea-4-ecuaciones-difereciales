
from sympy import *

x,y = symbols('x y')

# (x**3+2*x*y)/(y*x)
# -(y/x)
# -(2*x*E**y+E*x)/((x**2+1)*E**y)

eq = -(2*x+y+10)

eq_2 = eq.subs(x,1)
eq_3 = eq.subs(y,1)
print(eq)
print(eq_2)
print(eq_3)

if eq_2.has(y) and eq_3.has(x) and eq.has(Pow) :
    print ("Exacta")
else:
    print("No es exacta")
