"""Écrivez un programme Python, entrez deux nombres de l'utilisateur et trouvez le plus grand diviseur commun
en utilisant la boucle for."""

num1 = int(input("Veuillez saisir un nombre : "))
num2 = int(input("Veuillez saisir un nombre : "))

min = num1 if (num1 < num2) else num2

for i in range(1, min+1):
    if (num1 % i == 0 and num2 % i == 0):
        pgcd = i
print("PGCD de {0} et {1} = {2}".format(num1, num2, pgcd))