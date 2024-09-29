# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 10:38:22 2024

@author: user
"""

#fonctions intégrées

abs(-6)
abs(12)
sum([1,2,3,4,5])
len([1,2,3,4,5])
type([1,2,3,4,5])

#Création de fonctions

def aire_carree (c):
    aire=c**2
    return aire 

aire_carree(3)

def aire_cercle(r):
    pi=22/7
    aire= pi*r**2
    return aire

a = aire_cercle(4)
print(a)