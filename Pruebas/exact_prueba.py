from sympy import *

x,y = symbols('x y')

eq = (2*x/y**3) / ( (y**2 - 3*x**2 )/y**4)

eq_2 = eq.subs(x,1)
eq_3 = eq.subs(y,1)

if eq_2.has(y) and eq_3.has(x) and (eq.func == Mul or eq.has(Pow)):
    print ("Exacta")
else:
    print("No es exacta")
