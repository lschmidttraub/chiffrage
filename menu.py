from chiffrement_RSA import rsa
from chiffre_de_Cesar import Cesar
from chiffre_de_Vigenere import Vigenere

#Fonctions ecrtiture/lecture de fichier
def ajouter_fichier(a):
    with open('message.txt','w') as f:
        f.write(a)

def lire_fichier():
    with open('message.txt','r') as f:
        ligne=f.read()
    return ligne

boucle = True
while boucle:
  option1 = input("Choisissez une fonctionalité (Entrez q pour quitter): \n 1) Chiffrer ou déchiffrer un message \n 2) Chiffrer ou déchiffrer le contenu du fichier message.txt \n 3) Lire le contenu du fichier message.txt\n")
  while option1 not in ["1", "2", "3", "q"]:
      option1 = input("Veuillez choisir une fonctionnalité valide: \n")
  if option1 == "q":
    print("Au revoir!")
    boucle = False
  elif option1 == "3":
    print(lire_fichier()+"\n")
  else:
    if option1 == "1":
      message = input("Entrez votre message: ")
    if option1 == "2":
      message = lire_fichier()

    option2 = input("Voulez vous chiffrer(1) ou déchiffrer(2) ce message? ")
    while option2 not in ["1", "2"]:
      option2 = input("Veuillez entrer un choix valide: ")
    methode = input("Choisissez une méthode de cryptage : \n 1: Chiffre de César \n 2: Chiffre de Vigenère \n 3: Chiffrement RSA\n")
    while methode not in ["1", "2", "3"]:
      methode = input("Veuillez choisir une méthode valide: \n")
    if methode == "1":
      if option2 == "1":
        decalage = int(input("Entrez un décalage: "))
        resultat = Cesar.chiffrer(message, decalage)
      elif option2=="2":
        option3 = input("Avez-vous un décalage(o/n)? ")
        if option3 == "n":
          resultat = Cesar.dechiffrer_sans_d(message)
        else:
          decalage = int(input("Entrez un décalage: "))
          resultat = Cesar.dechiffrer(message, decalage)
    elif methode == "2":
      clef = input("Entrez une clef: ")
      if option2 == "1":
        resultat = Vigenere.chiffrer(message, clef)
      elif option2 == "2":
        resultat = Vigenere.dechiffrer(message, clef)
    else:
      if option2 == "1":
        maximum = int(input("Choisissez une valeur maximale pour les nombres premiers p et q (un nombre plus grand est plus sécurisé mais prend plus longtemps à calculer): "))
        n, clef_publique, clef_privee = rsa.generer_clefs(maximum)
        print("n = ", n, "\nclef publique = ", clef_publique, "\nclef privée = ", clef_privee)
        resultat =  rsa.chiffrer(message, clef_publique, n)
      elif option2 == "2":
        n = int(input("Entrez la valeur de n: "))
        clef_privee = int(input("Entrez la valeur de la clef privée: "))
        resultat = rsa.dechiffrer(message, clef_privee, n)
    
      
    print("Voici le résultat:\n", resultat)
    stocker = input("Voulez-vous stocker ce résultat dans le fichier message.txt? (o/n) ")
    if(stocker == "o"):
      ajouter_fichier(resultat)
    print("Merci d'avoir joué\n\n")
