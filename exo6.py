"""Écrire un programme Python qui permet d'évaluer une note saisi au clavier 
(si la note est supérieur à 10 alors il affiche validé sinon non validé (NB : la note comprise entre 0 et 20 )."""

note = float(input("Veuillez rentrer votre note : "))

while note > 20 or note < 0:
    print("Erreur : La note doit être comprise entre 0 et 20.")
    note = float(input("Veuillez rentrer votre note : "))
else:
    if note > 10:
        print("Validé !")
    else:
        print("Non validé...")