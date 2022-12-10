def exponentiation_rapide(base, exp, modulo):
    res=1
    while exp!=0:
        if exp%2:
            res*=base
        exp//=2
        base=base**2%modulo
    return res%modulo

def chiffrer(message, clef, n):
    res = ""
    for char in message:
        res+=str(exponentiation_rapide(ord(char), clef, n))+" "
    return (res)

def dechiffrer(message, clef, n):
    res = ""
    for nb in message.split(" "):
        if nb!="":
            res=res+chr(exponentiation_rapide(int(nb), clef, n))
    return res
