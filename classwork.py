# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 14:12:01 2018

@author: Ching
"""
import numpy as np

arr=np.array([[1,0,0,0,5],
             [0,6,0,0,9],
             [0,0,0,11,0],
             [0,0,0,0,0],
             [0,0,0,0,15]])
def sparsematrix():
    for i in range(5):
        for j in range(5):
            if arr[i][j]!=0:
                row.append(i+1)
                col.append(j+1)
                val.append(arr[i][j])
                
def transpose(a):
    ar=[]
    for k in range(5):
        ar.append([])
    for i in range(5):
        for j in range(5):
            ar[i].append(a[j][i])
    for row in ar:
        print(' '.join([str(elem) for elem in row]))
                
row=[]
col=[]
val=[]

transpose(arr)
sparsematrix()
b=np.array([row,col,val])
print(b)
