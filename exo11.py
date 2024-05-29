"""Le centre de photocopie facture 0,25 €  pour les 10 premières photocopies,
0,20 € les vingt suivantes et 0,10 € pour plus de vingt. Ecrire un programme Python qui demande à l’utilisateur
de saisir le nombre de photocopies effectuées et qui affiche la facture correspondante."""

nb_copies = int(input("Veuillez rentrer le nombre de copies qui vous souhaitez : "))
prix = 0

if nb_copies <= 10 and nb_copies > 0:
    prix = nb_copies * 0.25
elif nb_copies <= 20 and nb_copies > 10:
    prix = nb_copies * 0.20
elif nb_copies > 20:
    prix = nb_copies * 0.10

print(f"Le prix pour {nb_copies} copie(s) est {round(prix,2)} €.")