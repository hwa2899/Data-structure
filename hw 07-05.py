# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 14:28:05 2018

@author: Ching
"""

def adjust(data, i, size):
    j=2*i
    temp=data[i]
    while j<=size:
        if j<size:
            if data[j]<data[j+1]:
                j+=1
        if temp>=data[j]:
            break
        else:
            data[j//2]=data[j]
            j=2*j
    data[j//2]=temp

def heapsort(data,size):
    for i in range(size//2,0,-1):
        adjust(data,i,size)
    for i in range(size-1,0,-1):
        temp=data[i+1]
        data[i+1]=data[1]
        data[1]=temp
        adjust(data,1,i)
        
#big-o O(nlogn)               
data=[0,27,7,80,5,67,18,62,24,58,25]
heapsort(data,10)
print(data)
    
