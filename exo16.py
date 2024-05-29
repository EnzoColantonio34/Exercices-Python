"""Écrire un programme Python permettant de calculer la somme S=1+2+3+...+ N,  où N saisi par l’utilisateur.
Utilisant la  boucle while. """

i = 1
n = int(input("Veuillez saisir N : "))
result = 0

while i < n+1 :
    result = result + i
    i += 1
    print(result)