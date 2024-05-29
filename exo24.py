"""Écrivez un programme Python pour saisir un nombre et calculer sa factorielle à l'aide de la boucle for.

La factorielle d'un nombre "n" est le produit de tous les entiers positifs inférieurs ou égaux à n. Il est noté n!.
Par exemple, factorielle de 5!= 1*2*3*4*5= 120."""


nombre = int(input("Veuillez saisir un nombre : "))
fact = nombre

for i in range(1,fact):
    fact = fact * i

print(f"Factorielle de {nombre}! = {fact}")