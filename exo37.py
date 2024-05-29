"""Écrivez un programme Python pour déclarer deux tableaux, puis entrez les éléments du premier tableau de l'utilisateur et copiez tous ses éléments dans le deuxième tableau."""

N = int(input("Saisir le nombre d'éléments : "))
tab1 = [0]*N
tab2 = [0]*N

for i in range(N):
    tab1[i]=int(input("Saisir l'élément {0} : ".format(i+1)))
    tab2[i] = tab1[i]

print(tab1,tab2)