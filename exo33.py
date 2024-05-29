"""Écrire un programme Python pour déclarer un tableau, puis saisir ses éléments à partir de l'utilisateur et trouver la somme des éléments du tableau."""

N = int(input("Saisir le nombre d'éléments : "))
tab=[0]*N
somme = 0

for i in range(N):
    tab[i]=int(input("Saisir l'élément {0} : ".format(i+1)))
for i in range(N):
    somme = somme + tab[i]

print(f"La somme des éléments est : {somme}")