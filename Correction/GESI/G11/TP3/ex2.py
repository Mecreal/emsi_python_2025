# labyrinthe

from random import randint
from time import sleep


print("Bienvenue dans le jeu labyrinthe !")

case = 1
conteur = 1
while True:

    print(f"tour {conteur}")
    conteur += 1
    sleep(0.5)
    pas = randint(1, 6)
    case += pas
    if case == 50:
        print("Gangez")
        break
    elif case > 50:
        case -= pas 
    else:
        if case % 7 == 0:
            case -=pas
            case -= 3
            print(f"Le nombre multiple de 7 punition - 3 : Case = {case}")
        elif case % 13 == 0:
            print("Nombre multiple de 13 : sautez ")
            case -= pas
            continue
    print(f"Vous etes dans la case {case}")
