# problème de Syracuse

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
    L_collatz = syracuse(n_max)
    if L_collatz[-1] == 1:
        collatz = True
    else:
        collatz = False
    return collatz


print(testeConjecture(10000))

