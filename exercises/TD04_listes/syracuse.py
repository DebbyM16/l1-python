def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    L = [n]
    while n != 1:
        if n % 2 == 0:
            n = n//2
            L.append(n)
        else:
            n = (n * 3) + 1
            L.append(n)
    return (L)


print(syracuse(3))
