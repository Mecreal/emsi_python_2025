# factoriel 

n = int(input("Entrez un entier positif: "))

if n < 0:
    print("Le nombre doit être positif.")
else:
    fact = 1
    if n == 0:
        print("Le factoriel de 0 est 1.")
    else:
        for i in range(1, n + 1):
            fact *= i
        print(f"{n}! = {fact}")