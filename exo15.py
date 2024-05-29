"""Écrire un programme Python permettant de calculer la somme S= 1+2+3+...+ 10. Utilisant la boucle while.  """

i = 0
result = 0

while i < 11:
    result = result + i
    i += 1

print(result)