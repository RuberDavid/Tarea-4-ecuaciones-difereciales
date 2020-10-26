#       TAREA 4
#

from sympy import *

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
    elif 0:
    else:
        show_resources()





def main():
    x,y = symbols('x y')

    eq = sympify(input('Escribe tu ecuación: '))
    #TODO verificar valides de entrada

    evaluate( eq )

if __name__ == '__main__':
    main()
