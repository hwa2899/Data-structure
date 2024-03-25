# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 17:58:01 2019

@author: Ching
"""

def lsd(a):
    result=[];
    size = len(a)
    bucket = [[] for i in range(10)] 
    for i in range(size): 
        index = a[i]%10
        t=bucket[index]
        t.append(a[i])
    for i in range(10):    
        result = result + bucket[i]
    bucket = [[] for i in range(10)] 
    for i in range(size): 
        index = int(result[i]/10)
        t=bucket[index]
        t.append(result[i])
    result=[]; 
    for i in range(10):  
        result = result + bucket[i]       
    return result
data = [1,67,33,27,12,43,58,77,25,89,11,28,39,29,17,53,38,72,29,92]  
data = lsd(data)
print(data) 