"""Écrire un programme Python qui demande l'âge d'un enfant et permet d'informer de sa catégorie sachant que les catégories
sont les suivantes:"""
"poussin de 6 a 7 ans"   
"pupille de 8 a 9 ans "   
"minime de 10 a 11 ans "  
" cadet après 12 ans"

age = int(input("Veuillez rentrer votre age : "))

if age >= 6 and age <= 7:
    print("Vous êtes un poussin.")
elif age >= 8 and age <= 9:
    print("Vous êtes une pupille.")
elif age >= 10 and age <= 11:
    print("Vous êtes un minime.")
elif age >= 12 :
    print("Vous êtes un cadet.")
else :
    print("Erreur : l'age minimum est 6 ans.")