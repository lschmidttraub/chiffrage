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

def chiffrer(message, clef, n):
    '''
    Entrée: une chaîne de caractères (le message à chiffrer), un entier positif (la clef) et un modulo n 
    Sortie: le message chiffré
    '''
    res = ""
    for char in message:
        res+=str(exponentiation_rapide(ord(char), clef, n))+" "
    return (res)

def dechiffrer(message, clef, n):
    '''
    Entrée: une chaîne de caractères (le message chiffré), un entier positif (la clef) et  
    Sortie: le message dechiffré
    '''
    res = ""
    for nb in message.split(" "):
        if nb!="":
            res=res+chr(exponentiation_rapide(int(nb), clef, n))
    return res
