# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 14:33:01 2018

@author: Ching
"""

def selectionsort(data):
    size=len(data)
    for i in range(size-1):
        for j in range(i+1,size):
            if data[i]>data[j]:
                temp=data[i]
                data[i]=data[j]
                data[j]=temp
    return data

data=[18,2,20,34,12]
print(selectionsort(data))
# Big-O: O(n*n)