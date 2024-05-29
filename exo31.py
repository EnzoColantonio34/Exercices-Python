"""Écrivez un programme Python pour déclarer et initialiser un tableau, puis saisissez ses éléments à partir de l'utilisateur et affichez le tableau."""

N = int(input("Saisir le nombre d'éléments : "))
tab=[0]*N
for i in range(N):
    tab[i]=int(input("Saisir l'élément {0} : ".format(i+1)))
for i in range(N):
    print(tab[i])