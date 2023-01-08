from chiffrement_RSA import rsa
from chiffre_de_Cesar import Cesar
from chiffre_de_Vigenere import Vigenere

#Fonction ecrtiture/lecture de fichier
def ajouter_fichier(a):
    with open('message.txt','w') as f:
        f.write(a)

def lire_fichier():
    with open('message.txt','r') as f:
        ligne=f.read()
    return ligne

loop1 = True
while loop1:
  option1 = input("Choisissez une fonctionalité (Entrez q pour quitter): \n 1) Chiffrer ou déchiffrer un message \n 2) Chiffrer ou déchiffrer le contenu du fichier message.txt \n 3) Lire le contenu du fichier message.txt\n")
  if option1 == "q":
    print("Au revoir!")
    loop1 = False
  elif option1 == "3":
    print(lire_fichier())
  elif option1 in ["1", "2"]:
    if option1 == "1":
      message = input("Entrez votre message: ")
    if option1 == "2":
      message = lire_fichier()


    methode = input("Choisissez une méthode de cryptage : \n 1: Chiffre de César \n 2: Chiffre de Vigenère \n 3: Chiffrement RSA\n")
    while methode not in ["1", "2", "3"]:
      methode = input("Veuillez choisir une méthode valide: \n")
    if methode == "1":
      decalage = int(input("Entrez un décalage: "))
    elif methode == "2":
      clef = input("Entrez une clef: ")
    
    option2 = input("Voulez vous chiffrer(1) ou déchiffrer(2) ce message?")
    
    if option2 == "1":
      if methode == "1":
        resultat = Cesar.chiffrer(message, decalage)
      elif methode == "2":
        resultat = Vigenere.chiffrer(message, clef)
      else:
        maximum = int(input("Choisissez une valeur maximale pour les nombres premiers p et q (un nombre plus grand est plus sécurisé mais prend plus longtemps à calculer): "))
        n, clef_publique, clef_privee = rsa.generer_clefs(maximum)
        print("n = ", n, "\nclef publique = ", clef_publique, "\nclef privée = ", clef_privee)
        resultat =  rsa.chiffrer(message, clef_publique, n)
    elif option2 == "2":
      if methode == "1":
        resultat = Cesar.dechiffrer(message, decalage)
      if methode == "2":
        resultat = Vigenere.dechiffrer(message, clef)
      else:
        n = int(input("Entrez la valeur de n: "))
        clef_privee = int(input("Entrez la valeur de la clef privée: "))
        resultat = rsa.dechiffrer(message, clef_privee, n)
    else:
      print("Veuillez entrer un choix valide.")
    print("Voici le résultat:\n", resultat)
    stocker = input("Voulez-vous stocker ce résultat dans le fichier message.txt? (o/n) ")
    if(stocker == "o"):
      ajouter_fichier(resultat)
    print("Merci d'avoir joué\n\n")
  else:
    print("Veuillez entrer un texte valide.")
