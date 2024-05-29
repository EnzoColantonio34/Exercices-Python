"""Écrivez un programme Python pour afficher tous les nombres impairs de 1 à n en utilisant la boucle for et while."""

n = int(input("Veuillez saisir un nombre : "))

for i in range(1,n+1):
    if i % 2 == 0:
        print(i,"PAIR")
    else:
        print(i,"IMPAIR")