def premier(n):
    '''
    Entrée: un entier positif n
    Sortie: une valeur booléenne qui indique la primauté de n
    '''
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limite = int(n**0.5)
    for i in range(5, limite+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

def prochain_nb_premier(n):
    '''
    Entrée: un nombre entier positif n
    Sortie: le premier nombre premier p supérieur à n
    '''
    if (not n%2) and (n != 2):
        n += 1
    if premier(n):
        n += 2
    while True:
        if premier(n):
            break
        n += 2
    return n
