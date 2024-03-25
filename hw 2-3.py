# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:33:49 2018

@author: Ching
"""

def uppertriangular(m):
    for i in range(5):
        for j in range(5):
            if i >j:
                if m[i][j]!=0:
                    return "Not upper triangular"
    return "Upper triangular"

def compress(m):
    array=[]
    for i in range(5):
        for j in range(5):
            if i<=j:
                array.append(m[i][j])
    return array

m=[[1,2,3,4,5],
   [0,6,7,8,9],
   [0,0,10,11,12],
   [0,0,0,13,14],
   [0,0,0,0,15]]
print(uppertriangular(m))
print(compress(m))