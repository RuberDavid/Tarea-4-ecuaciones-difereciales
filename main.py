

#       TAREA 4
#

from sympy import *

# < >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >
def is_separable( eq ):
    """
    Return True if the equation is separable, False if it is not.
    If 	f(x,y) = p(x)q(y) then f(1,1) = p(1)q(1)
    so 		f(1,y)f(x,1) = p(1)q(y)p(x)q(1)
    therefore 	f(1,y)f(x,1) = f(1,1)f(x,y)
    name: is_separable
    @param expression
    @return bool
    """
    x,y = symbols('x y')
    
    # f(1,y)f(x,1)
    eq_2 = eq.subs(x,1)*eq.subs(y,1)
    
    # if f(1,y)f(x,1) = f(1,1)f(x,y) is separable
    if simplify( eq_2 - (eq.subs([(x,1),(y,1)])*eq) ) == 0:
        return True
    else:
        return False
	
# < >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >

def is_exact( eq ):
    x,y = symbols('x y')

    eq_2 = eq.subs(x,1)
    eq_3 = eq.subs(y,1)

    if eq_2.has(y) and eq_3.has(x) and eq.has(Pow) :
        return True
    else:
        return False


# < >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >

def is_linear( eq ):
    
    x,y = symbols('x y')

    eq_2 = eq.subs(x,0)
    eq_3 = eq.subs(x,1)

    if eq_2 == 0 and (eq_3.has(y) and not eq_3.has(x)) :
        return True
    else:
        return False

# < >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >

def is_bernoulli( eq ):


    return False

# < >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >

def is_linCoefs( eq ):
    
    return False

# < >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >

def is_homogeneous( eq ):
    return False

# < >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >

def show_resources():
    #TODO
    doc = "oli :3"
    print(doc)

# < >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >

def how_to_solve( type_of_eq ):
    '''
    type_of_eq is a string with one on these values : exact, separable, linear, bernoulli
    '''
    #exact =
    #separable =
    #linear = 
    #dictionary data structure for "manual"
    #TODO te falta ponerlo de a devis crack B)
    man = {
            "exact" : "Exact Man",
            "separable" : "sep man",
            "linear" : "lin",
            "bernoulli" : "bern",
            "homogeneous" : "homogen",
            "linear_coeficients" : "lin coefs"
            }

    print( man[ type_of_eq ] )

# < >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >

def evaluate( eq ):
    '''
    Revisa la ecuación  hasta encontrar 
    su tipo, si no : despliegla referencias y recursos
    '''

    if is_separable( eq ):
        type_of_eq = 'separable'
    elif is_exact( eq ):
        type_of_eq = 'exact'
    elif is_linear( eq ):
        type_of_eq = 'linear'
    elif is_bernoulli( eq ):
        type_of_eq = 'bernoulli'
    elif is_linCoefs( eq ):
        type_of_eq = 'linear_coeficients'
    elif is_homogeneous( eq ):
        type_of_eq = 'homogeneous'
    else:
        show_resources()
        return

    how_to_solve( type_of_eq )
    return


# < >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >

def main():
    x,y = symbols('x y')
    eq = 1
    #pa que imprima bonito
    init_printing(use_unicode=True)
    
    #TODO, presentación

    #lee la ecuación y traduce a un tipo simbólico de sympy
    eq = sympify(input('Escribe tu ecuación: ')) 

    #introducir 0 para terminar ejecución
    while( eq != 0 ): 
               #TODO verificar valides de entrada
        evaluate( eq )
        eq = sympify(input('Escribe tu ecuación: ')) 

if __name__ == '__main__':
    main()

