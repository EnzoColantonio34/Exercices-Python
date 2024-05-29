"""Écrivez un programme Python pour déclarer un tableau, puis saisissez ses éléments à partir de l'utilisateur et comptez le nombre d'éléments pairs et impairs dans ce tableau."""

N = int(input("Saisir le nombre d'éléments : "))
tab=[0]*N
pair = 0
impair = 0

for i in range(N):
    tab[i]=int(input("Saisir l'élément {0} : ".format(i+1)))
for i in range(N):
    if tab[i] % 2 == 0:
        pair += 1
    else :
        impair += 1

print(f"Dans ce tableau il y a {pair} nombres PAIR(s)")
print(f"Dans ce tableau il y a {impair} nombres IMPAIR(s)")
