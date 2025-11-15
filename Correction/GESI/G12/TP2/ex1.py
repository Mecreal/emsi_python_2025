# pair et impair

print("Vérificateur de nombre pair ou impair")
nbr  = int(input("Entrez un nombre: "))
if nbr % 2 == 0:
    print(f"{nbr} est un nombre pair.")
else:
    print(f"{nbr} est un nombre impair.")


# 2nd version
print("Vérificateur de nombre pair ou impair - Version 2")
nbr  = int(input("Entrez un nombre: "))

resultat = "pair" if nbr % 2 == 0 else "impair"
print(f"{nbr} est un nombre {resultat}.")
