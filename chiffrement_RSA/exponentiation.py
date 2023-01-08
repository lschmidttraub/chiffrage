def exponentiation_rapide(base, exp, modulo):
    '''
    Entrée: une base (int), un exposant (int) et un modulo (int)
    Sortie: la valeur (base**exponent)%modulo
    '''
    res=1
    while exp!=0:
        if exp%2:
            res*=base
        exp//=2
        base=base**2%modulo
    return res%modulo
