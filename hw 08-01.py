# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 15:14:54 2018

@author: Ching
"""

key=['GA','D','A','G','L','A2','A1','A3','A4','Z','ZA','E']
bucket=[None]*26

for i in key:
    index=ord(i[0])-65
    while bucket[index]!=None:
        index=(index+1)%26
    bucket[index]=i
print(bucket)

def find(key):
    ind=ord(key[0])-65
    index=0
    while bucket[index]!=key and index<25:
        