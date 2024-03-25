# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 10:17:19 2018

@author: Ching
"""

def transpose(a):
    ar=[]
    for k in range(n):
        ar.append([])
    for i in range(n):
        for j in range(m):
            ar[i].append(a[j][i])
    for row in ar:
        print(' '.join([str(elem) for elem in row]))

m,n=3,4 #m for row n for column
a=[[11,12,13,14],
   [21,22,23,24],
   [31,32,33,34]]
transpose(a)
