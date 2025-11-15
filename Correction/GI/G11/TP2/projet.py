# Jeu de devinette en Python

from random import randint

secret_number = randint(1, 100)

print("Bienvenue dans le jeu de devinette!")
print("Je pense a un nombre entre 1 et 100. Pouvez-vous le deviner?")

while True:
    for attempt in range(1, 11):
        print(f"Tentative {attempt}/10")
        guess = int(input("Entrez votre nombre: "))
        if guess < secret_number:
            print("Trop bas! Essayez encore.")
        elif guess > secret_number:
            print("Trop haut! Essayez encore.")
        else:
            print(f"Felicitation! Vous avez devine le nombre {secret_number} en {attempt} tentatives.")
            break
    else:
        print(f"Dommage! Le nombre a deviner etait {secret_number}. Mieux vaut chance la prochaine fois!")
    
    play_again = input("Voulez-vous jouer a nouveau? (oui/non): ").strip().lower()
    if play_again != 'oui':
        print("Merci d'avoir joue! A bientot!")
        break
    else:
        secret_number = randint(1, 100)
        print("Un nouveau nombre a ete choisi. Bonne chance!")