#Tableaux
alphabet =["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

ALPHABET =["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M" ,"N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
caracteres_interdits = [" ", ".", "'", "²", "@", "#", "~", "<", ">", ":", "/", ",","%"]

#Fonction de chiffrement
def chiffrer(mdp, d):                        #en parametre mdp le mot que l'on veut chiffrer / d le decalage / ans la sortie codé
    '''
    Entréé: mot de passe et decalage
    Sortie: code
    '''
    ans=""
    for i in range(len(mdp)):
        for p in range(26):                     #26 lettres de l'alphabet
            if mdp[i] == alphabet[p]:           #si l'indice du mdp == l'indice de l'alphabet alors ans =ans+(p+d)%26
                ans=ans+alphabet[(p+d)%26]      #p est l'indice de la lettre du mot qu'on addition au décalage d, et il y a un %26 au cas où l'addition du décalage dépasse z et puisse revenir au debut de l'alphabet
            elif mdp[i]== ALPHABET[p]:          #pour les majuscules
                    ans+= ALPHABET[(p+d)%26]
        if mdp[i]  in caracteres_interdits:     #si il y a un caratere interdit alors il est utilisé
            ans+=mdp[i]
    return ans


#Fonctions de dechiffrement
def dechiffrer(mdp, d):                           #en parametre d le decalage / ligne contient le contenu du fichier
    '''
    Entréé: decalage
    Sortie: mot de passe
    '''
    return chiffrer(mdp, -d)               #renvoie la fonction chiffrement mais avec -d



def dechiffrer_sans_d(code):                 #en parametre code qui est le mot chiffré/ texte et decalage en sortie
    '''
    Entréé: le code
    Sortie: mot de passe et le décalage
    '''
    decalage=1
    while True:
        texte=chiffrer(code,decalage)        #utilise la fonction chiffrement avec en parametre le codé et le decalage qui augmente de 1
        print(texte)
        correct=input("Ce message est-il correct(o/n)? ")
        if correct=="o":
            decalage=26-decalage                #permettra de renvoyer en sortie le decalage
            return texte

        decalage+=1                         #decalage augmente de 1 à chaque fois que l'utilisateur répond "n"
    return None, None                       #return les valeurs None si aucun décalage ne convient
