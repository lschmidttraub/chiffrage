alphabet =["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def fichier(a):
    with open('fichier.txt','a') as f:
        f.write(a)

def chiffrement(mdp, d):
    ans=""
    for i in range(len(mdp)):
        for p in range(26):
            if mdp[i] == alphabet[p]:
                ans=ans+alphabet[(p+d)%26]
    with open('fichier.txt','a') as f:
        f.write(ans)
    return ans

def dechiffrement(d):
    with open('fichier.txt','r') as f:
        ligne=f.read()
    return chiffrement(ligne, -d)


def d_sans_d(mdp):
    fini=False
    decalage=1
    while True:
        texte=chiffrement(mdp,decalage)
        print(texte)
        correct=input("Ce message est-il correct(o/n)? ")
        if correct=="o":
            with open('fichier.txt','a') as f:
                f.write(texte)
            return texte
        decalage+=1
