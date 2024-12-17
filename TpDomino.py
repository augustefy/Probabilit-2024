import random
import numpy as np
import matplotlib.pyplot as plt

def creeJeuDomino():
    d = []
    for i in range(7):
        for j in range(i, 7):
            d.append((i, j))
    return d

def simulerPartie(nPartie):
    jeu = creeJeuDomino()
    totalDouble = 0
    for _ in range(nPartie):
        main = random.sample(jeu, 7)
        double = sum(1 for x, y in main if x == y)
        totalDouble += double
    
    return totalDouble / nPartie

def calculTheoriqueDoubles():
    nbDoubles = 7
    totalDominos = 28
    tailleMain = 7
    
    E = (tailleMain * nbDoubles) / totalDominos # E = espérance
    return E



print("Jeu de dominos complet:", creeJeuDomino())
    
moyenneEmpirique = simulerPartie(10000)
print(f"\nMoyenne empirique de doubles par main: {moyenneEmpirique}")
    
esperanceTheorique = calculTheoriqueDoubles()
print(f"Espérancede double par main: {esperanceTheorique}")
