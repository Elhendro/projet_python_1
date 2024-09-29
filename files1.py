# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:34:32 2024

@author: user
"""

file_input=open('C:/Users/user/Desktop/Python/days.txt','r')
file_input0=open('C:/Users/user/Desktop/Python/read.txt','r')
liste=file_input0.readlines()
hend=file_input.read()
print(liste)
print(hend)
file_input.close()
file_input0.close()