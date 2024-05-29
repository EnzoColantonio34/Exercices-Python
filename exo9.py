"""Écrire un programme Python qui permet de calculer la moyenne de trois entiers saisis par l'utilisateur."""

nombre_1 = int(input("Veuillez rentrer un entier : "))
nombre_2 = int(input("Veuillez rentrer un entier : "))
nombre_3 = int(input("Veuillez rentrer un entier : "))

moyenne = (nombre_1 + nombre_2 + nombre_3) / 3

print("La moyenne est : ",round(moyenne,1))