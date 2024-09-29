# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 20:58:27 2024

@author: user
"""

"""
Le module numpy est très important
dans la datascience

"""
#importation du module numpy

import numpy as np

#création d'un tableau de données

a = np.array([1,3,5,7])
print(a)

b = np.array([[1,3,5,7],[2,4,6,8]])
print(b)

c = np.arange(15).reshape(3,5)
print(c)

d = np.arange(100).reshape(10,10)
print(d)

e = np.linspace(1,14,10)
print(e)

#dimention d'un tableau

b.shape
d.shape

# connaitre le type de données dans un tableau

b.dtype

# operations sur les tableaux

a**2
b**2

f = np.array([2,4,6,8])

a + f 

g = a - f 

print(g)

b.sum(axis = 0) #somme des colonnes
b.sum(axis = 1) #somme des lignes
