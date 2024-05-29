"""Écrire un programme Python qui permet de calculer la valeur absolue d'un entier saisi  par l'utilisateur."""

nombre = float(input("Veuillez rentrer un entier : "))

if nombre < 0:
    print(f"La valeur absolue de {round(nombre)} est {round(-nombre)}")
else:
    print(f"La valeur absolue de {round(nombre)} est {round(nombre)}")