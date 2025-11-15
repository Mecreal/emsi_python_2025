# Jeu de deviner un nombre entre 1 et 100

from random import randint

print("Bienvenue dans le jeu de devinette !")
print("J'ai choisi un nombre entre 1 et 100. Peux-tu le deviner ?")

while True:
    nombre_secret = randint(1, 100)
    for attempt in range(1, 11):
        print(f"Essai {attempt}/ 10.")        
        guess = int(input(f"Quel est ton choix ? "))
        while not (1 <= guess <= 100):
            print("Erreur : Le nombre doit être entre 1 et 100.")
            guess = int(input(f"Quel est ton choix ? "))

        if guess < nombre_secret:
            print("Trop bas ! Essaie encore.")
        elif guess > nombre_secret:
            print("Trop haut ! Essaie encore.")
        else:
            print(f"Félicitations ! Tu as deviné le nombre {nombre_secret} en {attempt} essais.")
            break
    else:
        print(f"Désolé, tu as utilisé tous tes essais. Le nombre était {nombre_secret}.")

    replay = input("Veux-tu rejouer ? (o/n) : ").strip().lower()
    if replay != 'o':
        print("Merci d'avoir joué ! À la prochaine.")
        break