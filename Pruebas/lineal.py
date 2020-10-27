
from sympy import *

x,y = symbols('x y')

# (x**3+2*x*y)/(y*x)
# -(y/x)
# -(2*x*E**y+E*x)/((x**2+1)*E**y)

eq = x*2 -x*y

eq_2 = eq.subs(x,0)
eq_3 = eq.subs(y,0)
	
if eq_2.has(y) and eq_3 != 0:
    print ("Es Lineal")
else:
    print("No es Lineal")

    
