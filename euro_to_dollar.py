# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 20:25:03 2024

@author: user
"""

"""
Écrivez un programme qui affiche une table de conversion de sommes d’argent exprimées en
euros, en dollars canadiens. La progression des sommes de la table sera « géométrique »,
comme dans l’exemple ci-dessous :
1 euro(s) = 1.65 dollar(s)
2 euro(s) = 3.30 dollar(s)
4 euro(s) = 6.60 dollar(s)
8 euro(s) = 13.20 dollar(s)
etc. (S’arrêter à 16384 euros.)
"""

n = 1

while (n<9930):
    s = n*1.65
    print(n, "euro(s) = ", s,  "dollar(s)")
    n = n + 1