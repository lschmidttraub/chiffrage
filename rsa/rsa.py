# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 11:51:32 2022

@author: LSCHMIDT-TRAUB
"""
import secrets
from rsa.nombres_premiers import *
from rsa.arithmetique_modulaire import *
from rsa.chiffrage import *



p = secrets.randbelow(10**3)
q = secrets.randbelow(10**3)
p=prochain_nb_premier(p)
q=prochain_nb_premier(q)

n=p*q
lam=ppcm(p-1,q-1)
exp_public=2**16+1
exp_prive=coefficient_bezout(exp_public, lam)
if exp_prive<0:
    exp_prive+=lam

message="Inshallah ça marche !/.,_'é#@"
m=chiffrer(message, exp_public, n)
assert dechiffrer(m, exp_prive, n)==message