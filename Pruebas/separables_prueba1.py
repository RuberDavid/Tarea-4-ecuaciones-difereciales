from sympy import *

x,y = symbols('x y')

# Si f(x,y) = p(x)q(y) entonces f(1,1) = p(1)q(1)
# así f(1,y)f(x,1) = p(1)q(y)p(x)q(1)
# por lo tanto f(1,y)f(x,1) = f(1,1)f(x,y)

eq = exp(x)*exp(y)

# f(1,y)f(x,1)
eq_2 = eq.subs(x,1) * eq.subs(y,1)

print (eq)

# Si f(1,y)f(x,1) = f(1,1)f(x,y) entonces es separable.
if simplify(eq_2 - (eq.subs([(x,1),(y,1)])*eq)) == 0:
	print ('Es separable')
else:
	print ('No es separable')
