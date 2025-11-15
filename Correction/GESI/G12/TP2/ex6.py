# affichage infini avec boucle while

print("Calculateur Simple")

while True:
    nombre_1 = float(input("Entrez le premier nombre: "))
    nombre_2 = float(input("Entrez le deuxième nombre: "))



    somme = nombre_1 + nombre_2
    soustraction = nombre_1 - nombre_2
    multiplication = nombre_1 * nombre_2
    exponentiation = nombre_1 ** nombre_2 

    print(f"""
{nombre_1} + {nombre_2} = {somme}
{nombre_1} - {nombre_2} = {soustraction}
{nombre_1} x {nombre_2} = {multiplication}
{nombre_1} ** {nombre_2} = {exponentiation}

          """)

    if nombre_2: # nombre_2 != 0
        division_int = nombre_1 // nombre_2
        modulo = nombre_1 % nombre_2
        exponentiation = nombre_1 ** nombre_2
        print(f"""{nombre_1} / {nombre_2} = {division_int}
{nombre_1} % {nombre_2} = {modulo}
{nombre_1} ** {nombre_2} = {exponentiation}
""")
    else:
        print("Division par zero: Erreur")
