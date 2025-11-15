from random import randint


print("Bienvenue dans le jeu de devinette!")

print("Je pense a un nombre et vous devez le deviner.")
nombre_a_deviner = randint(1, 100)

nombre_de_tentatives = 0
devine = False

while not devine and nombre_de_tentatives < 10:
    nombre_de_tentatives += 1
    print(f"Tentative {nombre_de_tentatives}/10")
    nombre_utilisateur = int(input("Entrez votre nombre (entre 1 et 100): "))

    if nombre_utilisateur < nombre_a_deviner:
        print("Trop bas! Essayez encore.")
    elif nombre_utilisateur > nombre_a_deviner:
        print("Trop haut! Essayez encore.")
    else:
        devine = True
        print(f"Felicitation! Vous avez devine le nombre {nombre_a_deviner} en {nombre_de_tentatives} tentatives.")

if not devine:
    print(f"Dommage! Le nombre a deviner etait {nombre_a_deviner}. Mieux vaut chance la prochaine fois!")