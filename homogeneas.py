from sympy import *
def is_homogeneous( eq):
    # asumir que c es real, no se
    if simplify( eq - eq.subs([(x,c*x ),(y, c*x) ] ) == 0:
        return True
    else:
        return False
        
