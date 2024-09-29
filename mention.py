# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 10:09:32 2024

@author: user
"""


note = float(input("Entrez votre note s'il vous plait "))

if note <= 9 and note>=0 :
    print("Recalé")
elif note >=10 and note <12:
    print("Admis mention passable")
elif note >=12 and note <14:
    print("Admis mention assez bien")
elif note >=14 and note <16:
    print("Admis mention bien")
elif note >=16 and note <18:
    print("Admis mention très bien")
elif note >=18 and note <=20:
    print("Admis mention excéllente")
else :
    print ("Vous avez entré une note impossible")
    