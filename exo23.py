"""Écrivez un programme Python pour entrer un nombre et vérifiez si le nombre est parfait ou non.
Un nombre parfait est un entier positif qui est égal à la somme de ses diviseurs positifs appropriés.
Par exemple: 6 est le premier nombre parfait
Les diviseurs appropriés de 6 sont 1, 2, 3.
Somme de ses diviseurs stricts = 1 + 2 + 3 = 6.
Par conséquent, 6 est un nombre parfait."""

num = int(input("Saisir un nombre : "))
somme = 0
for i in range(1, num):
    if (num % i == 0):
        somme += i

if (somme == num):
    print(num, "est un nombre parfait.")
else:
    print(num, "n'est pas un nombre parfait.")