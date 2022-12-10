# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 11:51:32 2022

@author: LSCHMIDT-TRAUB
"""
import secrets
from nombres_premiers import *
from arithmetique_modulaire import *
from chiffrage import *


def generer_clefs():
    p = secrets.randbelow(10**3)
    q = secrets.randbelow(10**3)
    p=prochain_nb_premier(p)
    q=prochain_nb_premier(q)

    n=p*q
    lam=ppcm(p-1,q-1)
    clef_public=2**16+1
    clef_prive=coefficient_bezout(clef_public, lam)
    if clef_prive<0:
        clef_prive+=lam
    return n, clef_public, clef_prive

n, clef_public, clef_prive = generer_clefs()

message="Inshallah ça marche !/.,_'é#@"
m=chiffrer(message, clef_public, n)
assert dechiffrer(m, clef_prive, n) == message