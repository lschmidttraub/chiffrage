def vigenere(mot, c):
    '''
    Entréé: un mot et une clé en majuscules sans espaces ou caractères spéciaux
    '''
    clef = c
    while len(clef)<len(mot):
        clef+= c

    res=""
    for i in range(len(mot)):
        decalage = ord(clef[i])-ord("A")
        res+=chr((ord(mot[i])-ord("A")+decalage)%26+ord("A"))
    return res


def vigenere_espaces(mot, c):
    '''
    Entréé: un mot et une clé en majuscules avec espaces ou caractères spéciaux
    '''

    res=""
    indice=0
    for i in range(len(mot)):
        if mot[i]!=' ':
            decalage = ord(c[indice%len(c)])-ord("A")
            res+=chr((ord(mot[i])-ord("A")+decalage)%26+ord("A"))
            indice+=1
        else:
            res+=" "

    return res

caracteres_interdits = [" ", ".","'"]

def vigenere_min_maj(mot, c):
    '''
    Entréé: un mot et une clé
    '''

    res=""
    indice=0
    for i in range(len(mot)):
        if not mot[i] in caracteres_interdits:
            if ord(mot[i])<=ord("Z"):
                x="A"
            else:
                x="a"
            decalage = ord(c[indice%len(c)])-ord("A")
            res+=chr((ord(mot[i])-ord(x)+decalage)%26+ord(x))
            indice+=1
        else:
            res+=mot[i]

    return res