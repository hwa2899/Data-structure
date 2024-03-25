# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 07:55:56 2018

@author: Ching
"""

#class animal():
#    def move():
#        print("move")
#
#class cat(animal):
#    def move():
#        print("jump")
#
#class tiger(cat):
#    def move():
#        print("run")
#    def skill():
#        print("prey")
#        
#animal.move()
#cat.move()
#tiger.move()
#tiger.skill()

#class demo():
#    def __init__(self):
#        self.divisor=1
#    def setdivisor(self,divisor):
#        if divisor==0:
#            print("Divisor can't be 0!")
#        else:
#            self.divisor=divisor
#    def datahiding(self, dividend):
#        result=dividend/self.divisor
#        print(result)
#
#ch00demo=demo()
#ch00demo.setdivisor(0)
#ch00demo.datahiding(50)

#class demo():
#    divisor=1
#    def setdivisor(self,divisor):
#        if divisor==0:
#            print("Divisor can't be 0!")
#        else:
#            self.divisor=divisor
#    def datahiding(self, dividend):
#        result=dividend/self.divisor
#        print(result)
#
#ch00demo=demo()
#ch00demo.setdivisor(0)
#ch00demo.datahiding(50)

#def selectionsort(data,n):
#    for i in range(n):
#        minimum=i
#        for j in range(i,n):
#            if data[j]<data[minimum]:
#                minimum=j
#        data[i],data[minimum]=data[minimum],data[i]
##        temp=data[i]
##        data[i]=data[minimum]
##        data[minimum]=temp
#    return data
#
#data=[2,8,5,4,7]
#print(selectionsort(data,5))    
#

def binarysearch(a,target):
    targetindex=-1
    mid=-1
    lower=0
    upper=len(a)-1
    while lower<=upper:
        mid=(lower+upper)//2
        if target>a[mid]:
            lower=mid+1
        elif target<a[mid]:
            upper=mid-1
        else:
            targetindex=mid
            break
    return targetindex

a=[1,2,3,4]
print(binarysearch(a,4))