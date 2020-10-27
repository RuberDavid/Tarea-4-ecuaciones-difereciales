


#       TAREA 4
#       por     Luis Ramos Guerrero
#               Oscar David Domínguez Dávila
#
#       instrucciones de uso en README.md
# 	o en https://github.com/RuberDavid/Tarea-4-ecuaciones-difereciales/blob/main/README.md

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
    eq_3 = eq.subs(y,0)
	
    if (eq_2.has(y) and not eq_2.has(x)) and eq_3 != 0:
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
    doc = """No hemos podido identificar el tipo de ecuación
    Quizás sea pueda llevarse a una ecuación diferencial exacta encontrando un
    factor integrante adecuado.
    Para más información se enlistarán algnos recursos en linea

    Ecuaciones diferenciales exactas
    https://es.wikipedia.org/wiki/Ecuaci%C3%B3n_diferencial_exacta

    Cálculo diferencial e integral tomo ii -Piskunov:
    http://libgen.rs/book/index.php?md5=816D73A44B45FFDF23E096F816391216
    
   	Differential equations, dynamical systems, and an introduction to chaos-Devaney et al.
    http://libgen.rs/book/index.php?md5=5B055F12AACE552EB321216F14C028E1
    
    Una serie de videos ilustrativos:
    https://www.youtube.com/playlist?list=PLZHQObOWTQDNPOjrT6KVlfJuKtYTftqH6

    también se puede recurrir al comando dsolve de sympy:
    https://docs.sympy.org/latest/tutorial/solvers.html#solving-differential-equations
    """
    print(doc)

# < >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >

def how_to_solve( type_of_eq ):
    '''
    type_of_eq is a string with one on these values : exact, separable, linear, bernoulli
    '''
    exact = """Es una ecuación exacta o total
    puede llevarse a la forma
            M(x,y)+N(x,y)y'=0

    donde las derivadas parciales
    con respecto a y y x de M y N respectivamente son iguales.
    Para resolver
    Integra N o M respecto a x o y
    se obtendrá una solución implicita
            """
            
    separable ="""Es una ecuación de variables separables
    y puede llevarse a la forma 
            y'=g(x)p(y)
   
    Para resolverla:
        multiplicar por 1/p(y)
        integrar ambos lados respecto a la única variable representada
        Se obtendrá una solución implicita
            """
    linear ="""Es una ecuación lineal
    """

    #dictionary data structure for "manual"
    man = {
            "exact" : exact,
            "separable" : separable,
            "linear" : linear,
            "bernoulli" : "bernoulli",
            "homogeneous" : "homogenea",
            "linear_coeficients" : "coeficientes lineales"
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

