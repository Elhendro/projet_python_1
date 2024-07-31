# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 08:54:13 2024

@author: user
"""

import math as mt
def equa(a,b,c):
    delta=b**2-4*a*c
    if delta>0:
        x1=(-b-mt.sqrt(delta))/(2*a)
        x2=(-b+mt.sqrt(delta))/(2*a)
        return x1, x2
    elif delta==0:
        x0=(-b)/(2*a)
        return x0
    else: 
        return None
a=float(input("Entrez la valeur de a: "))
b=float(input("Entrez la valeur de b: "))
c=float(input("Entrez la valeur de c: "))
S=equa(a, b, c)
if S:
    print("L'équation admet pour solution(s),",S)
else:
    print("L'équation n'admet pas de solution réelle")
