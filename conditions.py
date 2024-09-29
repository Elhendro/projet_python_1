# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 17:56:57 2024

@author: user
"""

#exemple 1

x=17
if x<=15 :
    print("x est un nombre inférieur ou égal à 15")
else:
    print("x est un nombre supérieur à 15")
    
#exemple 2

x=15

y=x%2

if y==0 :
    print("x est un nombre pair")
else:
    print("x est un nombre impair")
    
#exemple 3

note = 32

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
    print ("Veuillez entrer une note valide svp!")
