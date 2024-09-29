# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 20:05:48 2024

@author: user
"""

#création d'un dictionnaire age

age = {"hendrick": 37, "juliette" : 35, "houefa" : 10, "juliano" : 14, "bignon" : 5}

# acceder à un élément du dictionnaire

age["hendrick"]

# ajout d'un élément au dictionnaire

age["arnaud"]=37

print(age)

#modification du dictionnaire

age["arnaud"] = age["arnaud"]+1

print(age)

#vérification

"hendrick" in age

"bigno" in age

# vérification de la longueur du dictionnaire

len(age)

#suppression d'un élément du dictionnaire

del age["arnaud"]
print(age)

#connaitre les clés et les valeurs du dictionnaire

age.keys()

age.values()

