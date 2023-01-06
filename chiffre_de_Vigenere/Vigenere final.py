#Fonctions de chiffrement

def vigenere_chiffres_min_maj(mot, c):
    '''
    Entréé: un mot sans chiffre et une clé
    '''
    res=""
    indice=0
    for i in range(len(mot)):
        if mot[i] in chiffres:
            decalage = ord(c[indice%len(c)])-ord("A")
            res+=str((int(mot[i])+decalage)%10)
            indice+=1
        else:
            if not mot[i] in caracteres_interdits:
                if ord(mot[i])<=ord("Z"):                                #on verifie si la lettre d'indice i et une majuscule ou minuscule
                    x="A"
                else:
                    x="a"
                decalage = ord(c[indice%len(c)])-ord("A")                #decalage = difference entre la valeur de "a" ou "A" et la valeur de la lettre de la clef
                res+=chr((ord(mot[i])-ord(x)+decalage)%26+ord(x))
                indice+=1
            else:
                res+=mot[i]

    return res


#Fonctions de dechiffrement
def dechiffrement_chiffres_min_maj(code, c):
    '''
    Entréé: le code obtenu et la clé
    '''
    res=""
    indice=0
    for i in range(len(code)):
        if code[i] in chiffres:
            decalage = ord(c[indice%len(c)])-ord("A")
            res+=str((int(code[i])-decalage)%10)                        #même procede que pour le chiffrement sauf que l'on inverse le décalage
            indice+=1
        else:
            if not code[i] in caracteres_interdits:
                if ord(code[i])<=ord("Z"):
                    x="A"
                else:
                    x="a"
                decalage = ord(c[indice%len(c)])-ord("A")
                res+=chr((ord(code[i])-ord(x)-decalage)%26+ord(x))
                indice+=1
            else:
                res+=code[i]

    return res


#Tableaux
caracteres_interdits = [" ", ".", "'", "²", "@", "#", "~", "<", ">", ":", "/", ", """]
chiffres=["1","2","3","4","5","6","7","8","9"]

