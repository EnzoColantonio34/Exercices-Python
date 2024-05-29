"""Écrivez un programme Python pour entrer un nombre de l'utilisateur et comptez le nombre de chiffres
dans l'entier donné en utilisant une boucle."""

num = int(input("Saisir un nombre : "))
compteur = 0
while (num != 0):
    compteur += 1
    num //= 10
print("Nombre de chiffres : ",compteur)