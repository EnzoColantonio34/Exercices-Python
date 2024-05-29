"""Écrire un programme Python pour déclarer un tableau, puis saisir ses éléments à partir de l'utilisateur et rechercher les éléments maximum et minimum dans le tableau."""

N = int(input("Saisir le nombre d'éléments : "))
tab=[0]*N

for i in range(N):
    tab[i]=int(input("Saisir l'élément {0} : ".format(i+1)))

print(f"La valeur maximale du tableau est : {max(tab)}")
print(f"La valeur minimale du tableau est : {min(tab)}")