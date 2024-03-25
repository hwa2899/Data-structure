# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 14:54:15 2018

@author: Ching
"""

def quicksort(d,lf,rg):
    if lf<rg:
        lf_idx=lf+1
        rg_idx=rg
        while True:
            for i in range(lf+1,rg+1):
                if d[i]>d[lf]:
                    lf_idx=i
                    break
                lf_idx += 1
            for j in range(rg,lf,-1):
                if d[j]<d[lf]:
                    rg_idx=j
                    break
                rg_idx -= 1
            if lf_idx<rg_idx:
                temp = d[lf_idx]
                d[lf_idx] = d[rg_idx]
                d[rg_idx] = temp
            else:
                break
        if lf_idx>=rg_idx:
            temp=d[lf]
            d[lf]=d[rg_idx]
            d[rg_idx]=temp
            quicksort(d,lf,rg_idx-1)
            quicksort(d,rg_idx+1,rg)
    return d

d=[38,69,21,15,43,58,77,21,83,5]
print(quicksort(d,0,9))

c=[2,3,4,5]
print(quicksort(c,0,3))

#big-o: O(nlogn)
