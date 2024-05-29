"""Écrire un programme Python qui permet d'afficher la table de multiplication d’un entier saisie par l’utilisateur,
Utilisant la boucle for."""

N = int(input("Veuillez saisir un entier pour afficher sa table de multiplication : "))

for i in range(10):
    print(f"{i} x {N} = {i*N}")