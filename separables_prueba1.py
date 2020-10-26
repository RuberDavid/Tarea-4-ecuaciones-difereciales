from sympy import *

x,y = symbols('x y')

# De la forma y'=p(x)q(y), equation=p(x)q(y)
equation= (x+y)*y

# equation.subs([(x,1),(y,y)]) podría escribirse sólo como equation.subs(x,1) pero lo expongo así por claridad.
equation2 = equation.subs([(x,1),(y,y)]) * equation.subs([(x,x),(y,1)])

k_m = equation.subs([(x,1),(y,1)])

print (equation)

if simplify((k_m*equation)-equation2)==0 :
	print ('Es separable')
else:
	print ('No es separable')

