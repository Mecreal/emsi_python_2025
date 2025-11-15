# Calculator de IMC
print("Bienvenue dans le calculateur d'IMC!")

poids = float(input("Entrez votre poids en kilogrammes (kg): "))
taille = float(input("Entrez votre taille en mètres (m): "))

if taille <= 0 or poids <= 0:
    print("Erreur: Le poids et la taille doivent être des valeurs positives.")
else:
    imc = poids / taille**2

    if imc < 18.5:
        categorie = "Maigreur"
    elif 18.5 <= imc < 24.9:
        categorie = "Normale"
    elif 25 <= imc < 29.9:
        categorie = "Surpoids"
    else:
        categorie = "Obésité"
    print(f"Votre IMC est de {imc:.2f}, Catégorie: {categorie}.")

