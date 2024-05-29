"""Écrire un programme Python permettant d’afficher le mois en lettre selon le numéro saisi au clavier.
(Si l’utilisateur tape 1 le programme affiche janvier, si 2 affiche février, si 3 affiche mars... )."""

i = int(input("Veuillez saisir le numéro du mois que vous souhaitez : "))

while i < 1 or i > 12:
    print("Erreur : Le numéro doit être entre 1 et 12.")
    i = int(input("Veuillez saisir le numéro du mois que vous souhaitez : "))

mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]

print(mois[i-1])