"""Écrire  un programme Python  qui  permet d'échanger le contenu de deux entiers
A et B saisis par l'utilisateur. et afficher ces entiers  après l’échange."""

A = int(input("Entrez l'entier A : "))
B = int(input("Entrez l'entier B : "))

C = B
B = A
A = C

print(f"A : {A}")
print(f"B : {B}")