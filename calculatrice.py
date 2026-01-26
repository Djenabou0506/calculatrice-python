import math

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

if __name__ == "__main__":
    print("Addition: 5 + 3 =", addition(5, 3))
    print("Soustraction: 5 - 3 =", soustraction(5, 3))

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erreur: division par zéro"
    return a / b

if __name__ == "__main__":
    print("multiplication: 5 * 3 =", multiplication(5, 3))
    print("division: 5 / 3 =", division(5, 3))

def puissance(a, b):
    return a ** b
if __name__ == "__main__":
    print("puissance: 5 ** 3 =", puissance(5, 3))

def racine_carree(a):
    if a < 0:
        return "Erreur: nombre négatif"
    return math.sqrt(a)

