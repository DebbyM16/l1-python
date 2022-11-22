# Problème de Syracuse

def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    L_syracuse = [n]
    while n != 1:
        if n % 2 == 0:
            n = n//2
            L_syracuse.append(n)
        else:
            n = (n * 3) + 1
            L_syracuse.append(n)
    return L_syracuse


print(syracuse(3))

# Conjecture de Collatz


def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 1 à n_max """
    for i in range(1, n_max):
        L_collatz = syracuse(i)
    if L_collatz[-1] == 1:
        collatz = True
    else:
        collatz = False
    return collatz


print(testeConjecture(10000))

# Temps de vol


def tempsVol(n):
    """ Retourne le temps de vol de n """
    L_vol = syracuse(n)

    return len(L_vol)-1


print("Le temps de vol de", 3, "est", tempsVol(3))

# Temps de vol jusqu'à n_max


def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    Tps_vol = [tempsVol(i) for i in range(1, n_max+1)]

    return Tps_vol


print(tempsVolListe(100))

# l'atitude d'un nombre


def altitude(n_donne):
    """ Retourne le nombre avec le plus grand temps de vol """
    tps_vol = []
    for i in range(1, n_donne + 1):
        vol = tempsVol(i)
        tps_vol.append(vol)
        tps_vol1 = sorted(tps_vol)
        print(tps_vol1)

    return tps_vol1[n_donne-1]


print(altitude(100))
