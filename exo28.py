"""Écrire un programme Python qui permet d'inverser les chiffres d'un entier N saisi par l'utilisateur. Par exemple  N=35672  le résultat affiché doit être 27653. """

n=int(input("Veuillez saisir un entier à plusieurs chiffres : "))
r=0

while n > 0:
    r = r * 10
    r = r + n % 10
    n = int(n/10)
    
print(r)