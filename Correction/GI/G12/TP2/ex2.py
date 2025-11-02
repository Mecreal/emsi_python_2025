# Calcule IMC

print("Calcul de l'IMC (Indice de Masse Corporelle)")

poids = float(input("Entrez votre poids en kilogrammes (kg) : "))
taille = float(input("Entrez votre taille en mètres (m) : "))

if taille <= 0 or poids <= 0:
    print("Erreur : La taille et le poids doivent être des valeurs positives.")
else:
    imc = poids / taille**2
    
    if imc < 18.5:
        categorie = "Maigreur"
    elif 18.5 <= imc < 25:
        categorie = "Corpulence normale"
    elif 25 <= imc < 30:
        categorie = "Surpoids"
    else:
        categorie = "Obésité"

    print(f"Votre IMC est de {imc:.2f}: {categorie}")