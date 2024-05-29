"""Écrire un un programme Python qui permet d'afficher si un nombre entier saisi au clavier est pair ou impair. """

nombre = int(input("Veuillez saisir un nombre : "))

if nombre % 2 == 0:
    print(f"{nombre} est PAIR")
else:
    print(f"{nombre} est IMPAIR")