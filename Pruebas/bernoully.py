from sympy import *

x,y = symbols('x y')

eq = 3*x**2*y+2*x*y

eq_2 = eq.subs(y,0)
eq_3 = eq.subs(x,1)
eq_4 = eq.subs(y,1)

if eq_2 == 0 and eq_3 != 0 and eq_4 != 0 and is_separable(eq) == false:
    print ("Es Bernoulli")
else:
    print("No Bernoulli")
