# Calculatrice simple


print("Programme de calculatrice simple")

nbr1 = float(input("Entrez le premier nombre : "))
nbr2 = float(input("Entrez le deuxième nombre : "))

operator = input("""Choisissez l'opération à effectuer:
1 : addition
2 : soustraction
3 : multiplication
4 : division
5 : modulo
6 : puissance""")

if operator == '1': print(f"{nbr1} + {nbr2} = {nbr1 + nbr2}")
elif operator == '2': print(f"{nbr1} - {nbr2} = {nbr1 - nbr2}")
elif operator == '3': print(f"{nbr1} * {nbr2} = {nbr1 * nbr2}")   
elif operator == '4':
    if nbr2 != 0: print(f"{nbr1} / {nbr2} = {nbr1 / nbr2}")
    else: print("Erreur : Division par zéro")
elif operator == '5': 
    if nbr2 != 0: print(f"{nbr1} % {nbr2} = {nbr1 % nbr2}")
    else: print("Erreur : Division par zéro")
elif operator == '6': print(f"{nbr1} ** {nbr2} = {nbr1 ** nbr2}")