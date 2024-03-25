# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 16:06:28 2018

@author: Ching
"""

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        isswap=False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
                isswap=True
        if not isswap:
            break
#                temp = alist[i]
#                alist[i] = alist[i+1]
#                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)