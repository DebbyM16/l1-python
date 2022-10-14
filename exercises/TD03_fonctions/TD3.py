# conversion du temps en secondes

def tempsEnSeconde(temps):
    jour = temps[0] * 24 * 3600
    heure = temps[1] * 3600
    minute = temps[2] * 60
    seconde = temps[3]
    conversion1 = jour + heure + minute + seconde
    return conversion1


temps = (3, 23, 1, 34)
print(type(temps))
print(tempsEnSeconde(temps), "secondes")


# conversion des secondes en temps


def secondeEnTemps(seconde):
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


# affichage du temps

def afficheTemps(temps):
    if temps[0] == 1:
        jours = str(temps[0]) + " jour"
    elif temps[0] > 1:
        jours = str(temps[0]) + " jours"
    else:
        jours = print()

    if temps[1] == 1:
        heures = str(temps[1]) + " jour"
    elif temps[1] > 1:
        heures = str(temps[1]) + " jours"
    else:
        heures = print()

    if temps[2] == 1:
        minutes = str(temps[2]) + " jour"
    elif temps[2] > 1:
        minutes = str(temps[2]) + " jours"
    else:
        minutes = print()

    if temps[3] == 1:
        secondes = str(temps[3]) + " jour"
    elif temps[3] > 1:
        secondes = str(temps[3]) + " jours"
    else:
        secondes = print()

    print(jours, heures, minutes, secondes)


afficheTemps((1, 0, 14, 23))


# demande du temps à l'utilisateur

def demandeTemps():
    

afficheTemps(demandeTemps())