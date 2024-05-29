"""Écrivez un programme Python pour saisir un nombre de l'utilisateur et recherchez le premier et le dernier
chiffre d'un nombre en utilisant une boucle."""

n = int(input("Saisir un nombre : "))
dernier = n % 10
premier = n

while(premier >= 10):
    premier = premier // 10

print("Premier chiffre = ", premier)
print("Dernier chiffre = ", dernier)