from chiffrement_RSA import rsa
from chiffre_de_Cesar import Cesar
from chiffre_de_Vigenere import Vigenere

# Fonctions ecrtiture/lecture de fichier
def ajouter_fichier(a):
    with open('message.txt','w') as f:
        f.write(a)

def lire_fichier():
    with open('message.txt','r') as f:
        ligne=f.read()
    return ligne

# Menu
boucle = True
while boucle:   #On répète le programme jusqu'à ce que l'utilisateur quitte
  option1 = input("Choisissez une fonctionalité (Entrez q pour quitter): \n 1) Chiffrer ou déchiffrer un message \n 2) Chiffrer ou déchiffrer le contenu du fichier message.txt \n 3) Lire le contenu du fichier message.txt\n")
  # On attend que l'utilisateur entre une réponse valide
  while option1 not in ["1", "2", "3", "q"]:
      option1 = input("Veuillez choisir une fonctionnalité valide: \n")
  if option1 == "q":
    print("Au revoir!")
    # On arrête la boucle si l'utilisateur entre "q"
    boucle = False
  elif option1 == "3":
    # On affiche le contenu du fichier message.txt
    print(lire_fichier()+"\n")
  else:
    # On trouve d'abord la valeur du message à chiffrer/déchiffrer
    if option1 == "1":
      message = input("Entrez votre message: ")
    if option1 == "2":
      message = lire_fichier()

    # On demande à l'utilisateur s'il veut chiffrer ou déchiffrer ce message, puis on demande la méthode de chiffrage
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
        # Si l'utilisateur veut déchiffrer avec le chiffre de César, on lui demande s'il connaît le décalage
        option3 = input("Avez-vous un décalage(o/n)? ")
        # S'il n'a pas de décalage, on fait appel à la fonction dechiffrer_sans_d()
        if option3 == "n":
          resultat = Cesar.dechiffrer_sans_d(message)
        # Sinon, on fait un déchiffrage normal
        else:
          decalage = int(input("Entrez un décalage: "))
          resultat = Cesar.dechiffrer(message, decalage)
    elif methode == "2":
      # On demande la clef de chiffrage, puis on chiffre ou on déchiffre en fonction du choix de l'utilisateur
      clef = input("Entrez une clef: ")
      if option2 == "1":
        resultat = Vigenere.chiffrer(message, clef)
      elif option2 == "2":
        resultat = Vigenere.dechiffrer(message, clef)
    else:
      # Si l'utilisateur veut chiffrer le message, on génère et on affiche les clefs et la valeur de n
      if option2 == "1":
        maximum = int(input("Choisissez une valeur maximale pour les nombres premiers p et q (un nombre plus grand est plus sécurisé mais prend plus longtemps à calculer): "))
        n, clef_publique, clef_privee = rsa.generer_clefs(maximum)
        print("n = ", n, "\nclef publique = ", clef_publique, "\nclef privée = ", clef_privee)
        resultat =  rsa.chiffrer(message, clef_publique, n)
      # S'il veut déchiffrer le message, on lui demande la valeur de la clef privée et la valeur de n
      elif option2 == "2":
        n = int(input("Entrez la valeur de n: "))
        clef_privee = int(input("Entrez la valeur de la clef privée: "))
        resultat = rsa.dechiffrer(message, clef_privee, n)
    
      
    print("Voici le résultat:\n", resultat)
    # On demande à l'utilisateur s'il veut stocker le résultat dans le fichier message.txt
    stocker = input("Voulez-vous stocker ce résultat dans le fichier message.txt? (o/n) ")
    if(stocker == "o"):
      ajouter_fichier(resultat)
    print("Merci d'avoir joué\n\n")
