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
    clef_prive=coefficient_bezout(clef_publique, lam)
    if clef_prive<0:
        clef_prive+=lam
    return n, clef_publique, clef_prive

"""
n, clef_publique, clef_prive = generer_clefs(10**4)

message="Inshallah ça marche !/.,_'é#@"
m=chiffrer(message, clef_publique, n)
assert dechiffrer(m, clef_prive, n) == message
"""
