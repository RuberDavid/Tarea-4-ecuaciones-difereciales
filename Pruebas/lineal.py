from sympy import *

x,y = symbols('x y')

eq = 1/(2*x**3 + 9*x**4 + 30*x) + ((6*x**2 + 36*x*3 + 30)/(2*x**3 + 9*x**4 + 30*x))*y

eq_2 = eq.subs(x,1)
eq_3 = eq.subs(y,0)
	
if eq_2.has(y) and eq_3 != 0:
    print ("Es Lineal")
else:
    print("No es Lineal")
