from chiffrement_RSA import rsa, chiffrage
from chiffre_de_Cesar import Cesar
from chiffre_de_Vigenere import Vigenere

choix = input("Choisissez une méthode de cryptage (Entrez q pour quitter): \n 1: Chiffre de César \n 2: Chiffre de Vigenère \n 3: Chiffrement RSA\n")

if choix == "q":
  print("au revoir")
elif choix == "1":
  
elif choix == "2":
  
elif choix == "3":
  maximum = int(input("Choisissez une valeur maximale pour les nombres premiers p et q (un nombre plus grand est plus sécurisé mais prend plus longtemps à calculer): ")
  n, clef_publique, clef_prive = generer_clefs(maximum)
  fonction = input("Choisissez une fonctionalité (Entrez q pour retourner au menu): \n 1) Chiffrer ou déchiffrer un message \n 2) Chiffrer ou déchiffrer le contenu du fichier message.txt \n")
  if option == "q":
  elif option == "1":
    message = input("Entrez votre message: ")
  elif option == "2":
    message = 
  
  option2 = input("Voulez vous chiffrer(1) ou déchiffrer(2) ce message")
  if option2 == "1":
    res = rsa.chiffrer(message, clef_publique, n)
  elif option2 == "2":
    res = rsa.chiffrer(message, clef_privee, n)
  print("Voici le résultat:\n", message)
  stocker = input("Voulez-vous stocker ce résultat dans le fichier message.txt? (o/n) ")
  if(stocker == "o"):
