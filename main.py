#       TAREA 4
#

from sympy import *

def is_separable( eq ):
    #si eq es separable, regresa True, False de lo contrario
    return True #TODO Modifcame prroooo

def show_resources():
    #TODO
    print("ahorita no joven")

def evaluate( eq ):
    '''
    Revisa la ecuación  hasta encontrar 
    su tipo, si no : despiegla referencias y recursos
    '''
    
    if is_separable( eq ):
        #función para imprimir indicaciones
        print('es separable equis de') #TODOBorrame prro
    else:
        show_resources()





def main():
    x,y = symbols('x y')
    eq = 1
    #pa que imprima bonito
    init_printing(use_unicode=True)

    #introducir 0 para terminar ejecución
    while( eq != 0 ): 
        eq = sympify(input('Escribe tu ecuación: '))
        #TODO verificar valides de entrada

        evaluate( eq )

if __name__ == '__main__':
    main()
