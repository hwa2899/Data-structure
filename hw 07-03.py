# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 14:39:17 2018

@author: Ching
"""

def insertionsort(data):
    size=len(data)
    for i in range(size):
        temp=data[i]
        j=i-1
        while j>=0 and temp<data[j]:
            data[j+1]=data[j]
            j-=1
        data[j+1]=temp
    return data

data=[25,37,18,21,5,21]
print(insertionsort(data))

#big-o: O(n*n)