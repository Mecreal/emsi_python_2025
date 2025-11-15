# factorel en python

n = int(input("Entrez un nombre pour calculer sa factorielle: "))
if n < 0:
    print("La factorielle n'est pas définie pour les nombres négatifs.")
else:
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"{n}! = {fact}")