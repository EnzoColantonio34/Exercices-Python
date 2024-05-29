"""Écrire un programme Python pour déclarer un tableau, puis saisir ses éléments à partir de l'utilisateur et rechercher les éléments maximum et minimum dans le tableau."""

N = int(input("Saisir le nombre d'éléments : "))
tab=[0]*N

for i in range(N):
    tab[i]=int(input("Saisir l'élément {0} : ".format(i+1)))

tri = sorted(tab, reverse=True)

print("La valeur la plus grande du tableau est : ",tri[0])
print("La deuxième valeur la plus grande du tableau est : ",tri[1])