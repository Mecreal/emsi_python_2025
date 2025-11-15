# Projet de jeu de devinette

from random import randint

print("Bienvenue dans le jeu de devinette !")
print("J'ai choisi un nombre entre 1 et 100. Peux-tu le deviner ?")

while True:
    nombre_secret = randint(1, 100)
    for essai in range(11, 1, -1):
        print(f"Vous restez {essai - 1} essais.")
        guess = int(input("Devinez le nombre (entre 1 et 100): "))
        while not (1 <= guess <= 100):
            print("Erreur: Le nombre doit être entre 1 et 100.")
            guess = int(input("Devinez le nombre (entre 1 et 100): "))
        if guess < nombre_secret:
            print("Trop bas!")
        elif guess > nombre_secret:
            print("Trop haut!")
        else:
            print(f"Félicitations! Vous avez deviné le \
                nombre {nombre_secret} en {11 - essai} essais.")
            break
    else:
        print(f"Désolé, vous avez utilisé tous vos essais. \
            Le nombre était {nombre_secret}.")
    rejouer = input("Voulez-vous rejouer? (o/n): ").strip().lower()
    if rejouer != 'o':
        print("Merci d'avoir joué! À la prochaine.")
        break
