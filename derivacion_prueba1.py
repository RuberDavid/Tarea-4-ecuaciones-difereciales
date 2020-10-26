from sympy import *

x = Symbol('x')
y = Symbol('y')

ecuation = sympify(input('Escribe tu ecuación: '))

while ecuation.subs([(x,0),(y,1)]) == 0:
	ecuation = diff(ecuation,x)
	print(ecuation)
  
