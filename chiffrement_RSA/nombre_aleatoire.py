import time

def nb_aleatoire(maximum=1000, reps=100):
  seed = time.time_ns()%1000000 # on prend les 6 dernier chiffres du temps (en nano secondes)
  m = 34982
  p = 1
  nb = (seed*m+p)%maximum
  for i in range(reps):
    nb = (nb*m+p)%maximum
  return nb

for i in range(20):
  print(nb_aleatoire())