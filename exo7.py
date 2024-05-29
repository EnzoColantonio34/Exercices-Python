"""Écrire un programme Python qui demande deux nombres m et n à l’utilisateur et l’informe ensuite si le produit
de ces deux nombres est positif ou négatif. On inclut dans le programme le cas où le produit peut être nul."""

m = int(input("Veuillez saisir un nombre : "))
n = int(input("Veuillez saisir un nombre : "))

result = n * m

if result < 0:
    print("Le produit est négatif")
elif result > 0:
    print("Le produit est positif")
else:
    print("Le produit est nul")