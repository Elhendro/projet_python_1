# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 11:29:15 2024

@author: user
"""

liste = [2,3,4,2,6,"hendrick"]
liste.remove("hendrick")
liste_1 = [7,8,10,15]
liste_2 = liste + liste_1
liste_2.pop(4)
liste_2.append(45)
liste_2.sort()
liste_2.reverse()
print(liste_2)
type(liste)
sum(liste)
liste*liste_1
