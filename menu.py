from chiffrement_RSA import rsa
from chiffre_de_Cesar import Cesar
from chiffre_de_Vigenere import Vigenere

choix = input("Choisissez une méthode de cryptage (Entrez q pour quitter): \n 1: Chiffre de César \n 2: Chiffre de Vigenère \n 3: Chiffrement RSA\n")

if choix == "q":
  print("au revoir")
elif choix == "1":
  
elif choix == "2":
  
elif choix == "3":
  n, clef_publique, clef_prive = generer_clefs(10**4)
  fonction = input("Choisissez une fonctionalité (Entrez q pour retourner au menu): \n 1) Chiffrer un message \n 2) Déchiffrer un message \n")
  
  
