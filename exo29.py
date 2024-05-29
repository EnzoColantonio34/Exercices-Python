"""Écrivez un programme Python pour saisir un nombre et calculer la somme de ses chiffres en utilisant la boucle for."""

n = int(input("Veuillez renter un entier : "))
somme = 0

while n > 0:
    somme = somme + (n % 10)
    n = n // 10

print(somme)