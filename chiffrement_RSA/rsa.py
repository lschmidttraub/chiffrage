import secrets
from nombres_premiers import *
from arithmetique_modulaire import *
from chiffrage import *


def generer_clefs(maximum, clef_publique=2**16+1):
    '''
    Entrée: une valeur maximale pour les nombres premiers p et q, une clef publique
    Sortie: un modulo n, la clef publique et la clef privée
    '''
    p = secrets.randbelow(maximum)
    q = secrets.randbelow(maximum)
    p=prochain_nb_premier(p)
    q=prochain_nb_premier(q)
    n=p*q
    lam=ppcm(p-1,q-1)
    clef_privee=coefficient_bezout(clef_publique, lam)
    if clef_privee<0:
        clef_privee+=lam
    return n, clef_publique, clef_privee

"""
n, clef_publique, clef_privee = generer_clefs(10**4)

message="Inshallah ça marche !/.,_'é#@"
m=chiffrer(message, clef_publique, n)
assert dechiffrer(m, clef_privee, n) == message
"""
