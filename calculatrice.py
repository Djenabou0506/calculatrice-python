import math

# Fonctions de calcul
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erreur: division par zéro"
    return a / b

def puissance(a, b):
    return a ** b

def racine_carree(a):
    if a < 0:
        return "Erreur: nombre négatif"
    return math.sqrt(a)

def modulo(a, b):
    return a % b
<<<<<<< HEAD

def factorielle(n):
    if n < 0:
        return "Erreur : la factorielle n'est pas définie pour les nombres négatifs"
    if n == 0 or n == 1:
        return 1
    return n * factorielle(n - 1)

# Code de test
if __name__ == "__main__":
    print("Addition: 5 + 3 =", addition(5, 3))
    print("Soustraction: 5 - 3 =", soustraction(5, 3))
    print("Multiplication: 5 * 3 =", multiplication(5, 3))
    print("Division: 5 / 3 =", division(5, 3))
    print("Puissance: 5 ** 3 =", puissance(5, 3))
    print("Racine carrée: 5 =", racine_carree(5))
    print("Modulo: 5 % 2 =", modulo(5, 2))
    print("Factorielle: 5! =", factorielle(5))
=======
if __name__ == "__main__":
    print("modulo: 5 % 3 =", modulo(5, 3))

def factorielle(n):
    ...

>>>>>>> e858643b2ee0b3c9e511e11225143d4c54e07375
