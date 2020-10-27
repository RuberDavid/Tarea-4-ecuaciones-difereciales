
from sympy import *

x,y = symbols('x y')

# (x**3+2*x*y)/(y*x)
# -(y/x)
# -(2*x*E**y+E*x)/((x**2+1)*E**y)

eq = x*2 -x*y

eq_2 = eq.subs(x,0)
eq_3 = eq.subs(x,1)

if eq_2 == 0 and (eq_3.has(y) and not eq_3.has(x)) :
    print ("Lineales")
else:
    print("No Lineales")
