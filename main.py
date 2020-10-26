#       TAREA 4
#

from sympy import *

# < >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >
def is_separable( eq ):
    '''
	[Function]
	#	Return True if the equation is separable, False if it is not.
	# 	If f(x,y) = p(x)q(y) then f(1,1) = p(1)q(1)
	# 	so 			f(1,y)f(x,1) = p(1)q(y)p(x)q(1)
	# 	therefore 	f(1,y)f(x,1) = f(1,1)f(x,y)
	#	name: is_separable
	#  	@param expression
	#  	@return bool
	'''
	# f(1,y)f(x,1)
	eq_2 = eq.subs(x,1) * eq.subs(y,1)

	# if f(1,y)f(x,1) = f(1,1)f(x,y) is separable
	if simplify( eq_2 - (eq.subs([(x,1),(y,1)])*eq) ) == 0:
		return True
	else:
		return False

# < >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >


def show_resources():
    #TODO
    print("aguantaaaaaaaa")

def evaluate( eq ):
    '''
    Revisa la ecuación  hasta encontrar 
    su tipo, si no : despiegla referencias y recursos
    '''
    
    if is_separable( eq ):
        #función para imprimir indicaciones
    else:
        show_resources()





def main():
    x,y = symbols('x y')

    eq = sympify(input('Escribe tu ecuación: '))
    #TODO verificar valides de entrada

    evaluate( eq )

if __name__ == '__main__':
    main()
