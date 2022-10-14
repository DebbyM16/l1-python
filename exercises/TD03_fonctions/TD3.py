
def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps."""
    jour = temps[0] * 24 * 3600
    heure = temps[1] * 3600
    minute = temps[2] * 60
    seconde = temps[3]
    conversion1 = jour + heure + minute + seconde
    return conversion1


temps = (3, 23, 1, 34)
print(type(temps))
print(tempsEnSeconde(temps), "secondes")


def secondeEnTemps(seconde):
    """Renvoie le temps qui correspond au nombre de seconde."""
    jours = seconde // (24 * 3600)
    heures = (seconde % (24 * 3600)) // 3600
    minutes = (seconde % 3600) // 60
    secondes = seconde % 60
    conversion2 = (jours, heures, minutes, secondes)
    return conversion2


temps = secondeEnTemps(100000)
print(temps[0], "jours", end=" ")
print(temps[1], "heures", end=" ")
print(temps[2], "minutes", end=" ")
print(temps[3], "secondes", end=" ")
