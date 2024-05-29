"""Écrivez un programme Python pour saisir le numéro de l'utilisateur et vérifiez que le numéro est palindrome ou non, en utilisant une boucle."""

n = int(input("Saisir un nombre : "))
num = n
inverse = 0
while(n != 0):
    inverse = (inverse * 10) + (n % 10)
    n //= 10
if(inverse == num):
    print(num,"est palindrome.")
else:
    print(num,"n'est pas palindrome.")