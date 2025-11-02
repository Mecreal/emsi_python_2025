# calculatrice simple

print("Bienvenue dans la calculatrice simple!")

nombre1 = float(input("Entrez le premier nombre: "))
nombre2 = float(input("Entrez le deuxième nombre: "))

operation = int(input("""Choisissez une operation:
1. Addition (+)
2. Soustraction (-)
3. Multiplication (*)
4. Division (/)
5. Modulo (%)
6. Exponentiation (**)
Entrez le symbole de l'opération: """))


if operation == 1:print(f"{nombre1} + {nombre2} = {nombre1 + nombre2}")
elif operation == 2: print(f"{nombre1} - {nombre2} = {nombre1 - nombre2}")
elif operation == 3: print(f"{nombre1} * {nombre2} = {nombre1 * nombre2}")
elif operation == 4:
    if nombre2 == 0:
        print("Erreur: Division par zéro n'est pas permise.")
    else:
        print(f"{nombre1} / {nombre2} = {nombre1 / nombre2}")
elif operation == 5 and nombre2 != 0: print(f"{nombre1} % {nombre2} = {nombre1 % nombre2}")
elif operation == 6: print(f"{nombre1} ** {nombre2} = {nombre1 ** nombre2}")
else: print("Opération invalide ou bien non prise en charge.")