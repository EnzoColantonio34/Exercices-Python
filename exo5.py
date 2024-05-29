"""Écrire un programme Python qui permet d'afficher le plus grand de trois entiers saisis au clavier. """

list = []

for i in range (0, 3):
    nombre = int(input(f"Veuillez rentrer l'entier {i+1} : "))
    list.append(nombre)

print("L'entier le plus grand est : ",max(list))