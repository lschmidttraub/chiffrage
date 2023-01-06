#Fonction ecrtiture/lecture de fichier
def ajouter_fichier(a):
    with open('fichier.txt','a') as f:
        f.write(a)

def lire_fichier(a):
    with open('fichier.txt','r') as f:
        ligne=f.read()

#Fonction de Cryptage
def chiffrement(mdp, d):
    ans=""
    for i in range(len(mdp)):
        for p in range(26):
            if mdp[i] == alphabet[p]:
                ans=ans+alphabet[(p+d)%26]
            elif mdp[i]== ALPHABET[p]:
                    ans+= ALPHABET[(p+d)%26]
        if mdp[i]  in caracteres_interdits:
            ans+=mdp[i]
    ajouter_fichier(ans)
    return ans

#Fonctions de Decryptage
def dechiffrement(d):
    with open('fichier.txt','r') as f:
        ligne=f.read()
    return chiffrement(ligne, -d)



def dechiffrement_sans_d(code):
    '''
    Entréé: le code
    '''
    '''
    Sortie: mot de passe et le decalage
    '''
    fini=False
    decalage=1
    while True:
        texte=chiffrement(code,decalage)
        print(texte)
        correct=input("Ce message est-il correct(o/n)? ")
        if correct=="o":
            ajouter_fichier(texte)
            decalage=26-decalage
            return texte, decalage

        decalage+=1


#Tableaux
alphabet =["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

ALPHABET =["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M" ,"N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
caracteres_interdits = [" ", ".", "'", "²", "@", "#", "~", "<", ">", ":", "/", ","]
