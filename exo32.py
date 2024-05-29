"""Écrivez un programme Python pour déclarer un tableau, puis saisissez ses éléments par l'utilisateur et affichez tous les éléments négatifs."""

N = int(input("Saisir le nombre d'éléments : "))
tab=[0]*N
for i in range(N):
    tab[i]=int(input("Saisir l'élément {0} : ".format(i+1)))
for i in range(N):
    if (tab[i] < 0):
        print(tab[i])