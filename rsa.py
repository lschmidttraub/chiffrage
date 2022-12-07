# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 11:51:32 2022

@author: LSCHMIDT-TRAUB
"""
import secrets

def is_prime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = int(n**0.5)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

def next_prime(num):
    if (not num & 1) and (num != 2):
        num += 1
    if is_prime(num):
        num += 2
    while True:
        if is_prime(num):
            break
        num += 2
    return num

def pgcd(a,b):
    a,b=max(a,b), min(a,b)
    r=a%b
    if r==0:
        return b
    return pgcd(b,r)

def ppcm(a,b):
    return int(a*b/pgcd(a,b))

def coefficient_bezout(a,b):
    r1, r2 = a,b
    s1, s2 = 1,0
    # t1, t2 = 0,1
    while r2!=0:
        q=r1//r2
        r1,r2 = r2, r1-q*r2
        s1,s2 = s2, s1-q*s2
        #t1,t2 = t2, t1-q*t2
    return s1 #, t1


def chiffrer(message, clef, n):
    res = ""
    for char in message:
        res+=str((ord(char)**clef)%n)+" "
    return (res)

def dechiffrer(message, clef, n):
    res = ""
    for nb in message.split(" "):
        if nb!="":
            res=res+chr((int(nb)**clef)%n)
    return res



p = secrets.randbelow(10**3)
q = secrets.randbelow(10**3)
p=next_prime(p)
q=next_prime(q)

n=p*q
lam=ppcm(p-1,q-1)
exp_public=2**16+1
exp_prive=coefficient_bezout(exp_public, lam)
print(exp_prive)
if exp_prive<0:
    exp_prive+=lam
print(exp_prive)

message="Inshallah ça marche !/.,_'é#@"
m=chiffrer(message, exp_public, n)
assert dechiffrer(m, exp_prive, n)==message