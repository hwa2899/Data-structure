# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 14:26:03 2018

@author: Ching
"""

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        isswap=False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
#                temp = alist[i]
#                alist[i] = alist[i+1]
#                alist[i+1] = temp
                isswap=True
        if not isswap:
            break


alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

#Big-O: O(n*n)