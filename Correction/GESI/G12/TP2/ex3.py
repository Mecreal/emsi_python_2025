# année bissextile
print("Vérification d'une année bissextile")

annee = int(input("Entrez une année: "))

if annee % 4 == 0:
    if annee % 100 == 0:
        if annee % 400 == 0:
            print(f"{annee} est une année bissextile.")
        else:
            print(f"{annee} n'est pas une année bissextile.")
    else:
        print(f"{annee} est une année bissextile.")
else:
    print(f"{annee} n'est pas une année bissextile.")