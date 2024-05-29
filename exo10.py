"""Une boutique propose à ces clients, une réduction de 15% pour les montants d’achat supérieurs à 200 €.
Écrire un programme Python permettant de saisir le prix total HT et de calculer le montant TTC en prenant en compte
la réduction et la TVA=20%."""

prix_HT = float(input("Quel est le montant de vos achats HT (en €) ? "))

prix_TTC = prix_HT * 1.2

print(f"Le prix TTC est {prix_TTC} €.")

if prix_HT > 200:
    reduction = prix_TTC * 1.15 - prix_TTC
    prix_reduc = prix_TTC - reduction
    print(f"Le prix après réductions est {round(prix_reduc,2)} €.")
else:
    print("Pas de réduction applicable...")