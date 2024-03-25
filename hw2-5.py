# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 16:01:30 2018

@author: Ching
"""

class term():
    def __init__(self,coef,exp):
        self.coef=coef
        self.exp=exp
    def show(self):
        print([self.coef,self.exp])

def polynomial(p1,p2):
    final=[]
    firstp=0
    secp=0
    firstterm=len(p1)
    secterm=len(p2)
    
    while(firstp<firstterm) and (secp<secterm):
        if p1[firstp].exp==p2[secp].exp:
            t=p1[firstp].coef+p2[secp].coef
            final.append(term(t,p1[firstp].exp))
            firstp=firstp+1
            secp=secp+1
        elif p1[firstp].exp<p2[secp].exp:
            final.append(term(p2[secp].coef,p2[secp].exp))
            secp+=1
        else:
            final.append(term(p1[firstp].coef,p1[firstp].exp))
            firstp+=1
    
    while firstp<firstterm:
        final.append(term(p1[secp].coef,p1[secp].exp))
        firstp+=1
        
    while secp<secterm:
        final.append(term(p2[secp].coef,p2[secp].exp))
        secp+=1
    return final
#run
p1 = [term(8,2), term(5,0)] 
p2 = [term(3,3), term(2,2), term(1,1), term(1,0)]
final=polynomial(p1,p2)
for i in final:
    i.show()
print()
