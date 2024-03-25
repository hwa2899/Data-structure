# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 14:45:37 2019

@author: Ching
"""

def msd(a):
    result=[];
    size = len(a)
    ten = [[] for i in range(10)] 
    for i in range(size): 
        index = a[i]//10
        t=ten[index]
        t.append(a[i])
    tens = len(ten)
    for i in range(tens):     
        sorted(ten[i])
        teni = ten[i]
        isize = len(teni)
        for j in range(isize):
            result.append(teni[j])
    return result
        
data = [1,67,33,27,12,43,58,77,25,89,11,28,39,29,17,53,38,72,29,92] 
data = msd(data)
print(data)  


 