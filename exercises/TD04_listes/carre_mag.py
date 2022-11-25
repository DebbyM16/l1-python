# Carré magique

carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
carre_pas_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 7, 13]]


def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    print(carre[0])
    print(carre[1])
    print(carre[2])
    print(carre[3])
    print(end="\n")


afficheCarre(carre_mag)
afficheCarre(carre_pas_mag)

# Test des lignes du carré magique


def testLignesEgales(carre):
    """Donne la somme d'une ligne de la liste, sinon -1"""
    ligne1 = sum(carre[0])
    ligne2 = sum(carre[1])
    ligne3 = sum(carre[2])
    ligne4 = sum(carre[3])

    if ligne1 == ligne2 == ligne3 == ligne4:
        return ligne1
    else:
        return -1


print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))

# Test des colonnes du carré magique


def testColonnesEgales(carre):
    """Donne la somme d'une colonne de la liste, sinon -1"""
    colonne1 = carre[0][0] + carre[1][0] + carre[2][0] + carre[3][0]
    colonne2 = carre[0][1] + carre[1][1] + carre[2][1] + carre[3][1]
    colonne3 = carre[0][2] + carre[1][2] + carre[2][2] + carre[3][2]
    colonne4 = carre[0][3] + carre[1][3] + carre[2][3] + carre[3][3]

    if colonne1 == colonne2 == colonne3 == colonne4:
        return colonne1
    else:
        return -1


print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))

# Test des diagonales du carré magique


def testDiagonalesEgales(carre):
    """Donne la somme d'une diagonale de la liste, sinon -1"""
    diagonale1 = carre[0][0] + carre[1][1] + carre[2][2] + carre[3][3]
    diagonale2 = carre[0][-1] + carre[1][-2] + carre[2][-3] + carre[3][-4]

    if diagonale1 == diagonale2:
        return diagonale1
    else:
        return -1


print(testDiagonalesEgales(carre_mag))
print(testDiagonalesEgales(carre_pas_mag))
