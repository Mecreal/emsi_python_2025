# Annee bisextile

print("Vérificateur d'année bissextile")

annee = int(input("Entrez une année: "))

if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
    print(f"L'année {annee} est une année bissextile.")
else:
    print(f"L'année {annee} n'est pas une année bissextile.")

# Methode 2 directe


print("Vérificateur d'année bissextile (Méthode 2)")

if  annee % 4 ==0:
    if annee % 100 ==0:
        if annee % 400 ==0:
            print(f"L'année {annee} est une année bissextile.")
        else:
            print(f"L'année {annee} n'est pas une année bissextile.")
    else:
        print(f"L'année {annee} est une année bissextile.")
else:
    print(f"L'année {annee} n'est pas une année bissextile.")