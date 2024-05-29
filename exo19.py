"""Écrire un programme Python qui permet de calculer la somme S=1+2+3+4+….+ N. où N saisi au clavier par l'utilisateur.
Utilisant la boucle for."""

S = 0
N = int(input("Veuillez saisir N : "))

for i in range(1,N+1):
    S = S + i
    print(S)