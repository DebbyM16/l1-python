#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    conversion1=(temps[0]*24*3600)+(temps[1]*3600)+(temps[2]*60)+temps[3]

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jours=seconde//(24*3600)
    heures=(jours%(24*3600))//3600
    minutes=(heures%3600)//60
    secondes=minutes%60
    conversion2=(jours,heures,minutes,secondes)
    
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")