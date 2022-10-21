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
        jours = print("")

    if temps[1] == 1:
        heures = str(temps[1]) + " heure"
    elif temps[1] > 1:
        heures = str(temps[1]) + " heures"
    else:
        heures = print("")

    if temps[2] == 1:
        minutes = str(temps[2]) + " minute"
    elif temps[2] > 1:
        minutes = str(temps[2]) + " minutes"
    else:
        minutes = print("")

    if temps[3] == 1:
        secondes = str(temps[3]) + " seconde"
    elif temps[3] > 1:
        secondes = str(temps[3]) + " secondes"
    else:
        secondes = print("")

    return (jours, heures, minutes, secondes)


afficheTemps((1, 0, 14, 23))


# demande du temps à l'utilisateur

def demandeTemps():
    jour_demande = int(input("Combien de jours ?"))
    heure_demande = int(input("Combien d'heures ?"))
    minute_demande = int(input("Combien de minutes ?"))
    seconde_demande = int(input("Combien de secondes ?"))

    while heure_demande >= 24:
        heure_demande = int(input("Réessayer! Combien d'heures ?"))
    while minute_demande >= 60:
        minute_demande = int(input("Réessayer! Combien de minutes ?"))
    while seconde_demande >= 60:
        seconde_demande = int(input("Réessayer! Combien de secondes ?"))

    return (jour_demande, heure_demande, minute_demande, seconde_demande)


afficheTemps(demandeTemps())


# la somme de 2 temps


def sommeTemps(temps1, temps2):
    temps1_seconde = tempsEnSeconde(temps1)
    temps2_seconde = tempsEnSeconde(temps2)
    somme_temps_s = temps1_seconde + temps2_seconde

    somme_temps_t = secondeEnTemps(somme_temps_s)

    somme_temps = afficheTemps(somme_temps_t)

    print(somme_temps)


sommeTemps((2, 3, 4, 25), (5, 22, 57, 1))


# calcul d'un pourcentage de temps


def proportionTemps(temps, proportion):
    temps_s = tempsEnSeconde(temps)

    protemps = temps_s * proportion

    protemps = secondeEnTemps(protemps)

    return protemps


print(afficheTemps(proportionTemps((2, 0, 36, 0), 0.2)))
