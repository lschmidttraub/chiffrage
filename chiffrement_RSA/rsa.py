import secrets
from chiffrement_RSA.nombres_premiers import *
from chiffrement_RSA.arithmetique_modulaire import *
from chiffrement_RSA.exponentiation import *

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
