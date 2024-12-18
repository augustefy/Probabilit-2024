def creeJeuDomino():
    d = []
    for i in range(7):
        for j in range(i, 7):
            d.append((i, j))
    return d

# Exercice 2
# Simulation pour obtenir la probabilité d'avoir un domino dans  une main de 7 dominos
# La structure de données des domjnos restant est une pile de tableau de 2 valeur


import random
import numpy as np
import matplotlib.pyplot as plt

# Exercice 1
# Dans un jeu classique il y a 28 dominos
# On crée toutes les combinaisons possibles de 0 à 6
# en évitant les doublons (j commence à i)

def creeJeuDomino():
    d = []
    for i in range(7):
        for j in range(i, 7):
            d.append((i, j))
    return d

############################################

def uneChaineDomino(nbPartie):
    X = []
    Y = []
    for p in range(nbPartie):
        dominos = creeJeuDomino()
        pile = dominos[:]
        chaine = []

        premier = pile[random.randint(0, len(pile) - 1)]
        chaine.append(premier)
        pile.remove(premier)

        nbTourNonPlace = 0

        while len(pile) > 0 and nbTourNonPlace < 28:
            dominoPile = pile[random.randint(0, len(pile) - 1)]
            pile.remove(dominoPile)

            # Conversion temporaire pour manipulation si nécessaire
            dominoPile = list(dominoPile)  # Convert tuple to list

            if chaine[0][0] == dominoPile[0] or chaine[0][0] == dominoPile[1]:
                if chaine[0][0] == dominoPile[0]:
                    dominoPile[0], dominoPile[1] = dominoPile[1], dominoPile[0]

                chaine.insert(0, tuple(dominoPile))  # Convert back to tuple if needed
                nbTourNonPlace = 0

            elif chaine[-1][1] == dominoPile[0] or chaine[-1][1] == dominoPile[1]:
                if chaine[-1][1] == dominoPile[1]:
                    dominoPile[0], dominoPile[1] = dominoPile[1], dominoPile[0]

                chaine.append(tuple(dominoPile))  # Convert back to tuple if needed
                nbTourNonPlace = 0

            elif (chaine[0][0] == dominoPile[0] or chaine[0][0] == dominoPile[1]) and \
                    (chaine[-1][1] == dominoPile[0] or chaine[-1][1] == dominoPile[1]):
                nb = random.choice([0, -1])
                chaine.insert(nb, tuple(dominoPile))  # Convert back to tuple if needed
                nbTourNonPlace = 0

            else:
                pile.append(tuple(dominoPile))  # Ensure domino added back is a tuple
                nbTourNonPlace += 1

        X.append(len(chaine))
        Y.append(sum([sum(val) for val in pile]))
    X.sort()
    Y.sort()
    return X, Y



############################################
z = uneChaineDomino(10000)
X = z[0]
Y = z[1]


#Question 1
plt.figure()
plt.title("Loi de probabilité de X")
plt.xlabel("Nombre de dominos placés")
plt.ylabel("Probabilité")
plt.hist(X, max(X), density=1)

#Question 2
plt.figure()
plt.title("Fonction de répartition de X")
plt.xlabel("Nombre de dominos placés")
plt.ylabel("Probabilité")
plt.plot(X, [x / 10000 for x in range(10000)])


# Question 3
Ex = sum(X) / 10000

#Question 4
Vx = sum([(x - Ex) ** 2 for x in X]) / 10000

print("Expectation of X : ", Ex)
print("Variance of X : ", Vx)

#Question 5

plt.figure()
plt.title("Loi de probabilité de Y")
plt.xlabel("Score restant dans la pile")
plt.ylabel("Probabilité")
plt.hist(Y, max(Y) // 2, density=1)

plt.figure()
plt.title("Fonction de répartition de Y")
plt.xlabel("Score restant dans la pile")
plt.ylabel("Probabilité")
plt.plot(Y, [y / 10000 for y in range(10000)])
plt.show()

Ey = sum(Y) / 10000
Vy = sum([(y - Ey) ** 2 for y in Y]) / 10000

print("Expectation of Y : ", Ey)
print("Variance of Y : ", Vy)

# Question 6
print("Probability of X = 28 : ", X.count(28) / 10000)

# Question 7
print("Median of Y : ", Y[10000//2])

############################################
tX = []
tY = []
essaie = 200  # Nombre d'essais

# Boucle' de simulations
for t in range(essaie):
    sizeChaine, scorePioche = uneChaineDomino(200)
    tX.append(sizeChaine)
    tY.append(scorePioche)

# Question 1
plt.figure()
plt.scatter(tX, tY)
plt.xlabel("Size chaîne (X)")
plt.ylabel("Score pile (Y)")
plt.show()


# Question 2
tX = []
tY = []
tZ = []
t=0
for t in range(essaie):
    sizeChaine, scorePioche = uneChaineDomino(200)
    tX.append(sizeChaine)
    tY.append(scorePioche)
    tZ.append(sum(sizeChaine) * sum(scorePioche))



# Calcul des espérances
esperanceX = np.mean(tX)
esperanceY = np.mean(tY)
esperanceZ = np.mean(tZ)

print("Espérance de Taille de la chaîne (X) :", esperanceX)
print("Espérance de Score de la pioche (Y) :", esperanceY)
print("Espérance de Z (X * Y) :", esperanceZ)
# Question 3
covariance = np.cov(tX, tY)[0][1]
print("La covariance entre (X) et (Y) est :", covariance)

coefCorelation = np.corrcoef(tX, tY)[0][1]
print("Le coefficient de corrélation entre Taille de la chaîne (X) et Score de la pioche (Y) est :", coefCorelation)

# Question 4
print("ALors i X augmente (taille de la chaîne), alors Y diminue (score de la pioche).")






############################################
# Tests et affichag des résultat
print("Jeu de dominos complet:", creeJeuDomino())

print(uneChaineDomino(1))



