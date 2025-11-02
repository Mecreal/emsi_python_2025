# IMC calculator

print("Bienvenue dans le calculateur d'IMC")

poids = float(input("Entrez votre poids en kg: "))
taille = float(input("Entrez votre taille en mètres: "))

if taille > 0 and poids > 0:
    imc = poids / (taille ** 2)
    if imc < 18.5:
        categorie = "Maigreur"
    elif 18.5 <= imc < 24.9:
        categorie = "Normal"
    elif 25 <= imc < 29.9:
        categorie = "Surpoids"
    else:
        categorie = "Obésité"

    print(f"Votre IMC est de {imc:.2f}: {categorie}")
else:
    print("Erreur: Les valeurs de poids et de taille doivent être positives.")