# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 15:09:09 2018

@author: Ching
"""

class maxheap():
    def __init__(self,capacity):
        self.c=capacity
        self.heap=[[] for i in range(capacity)]
        self.heapsize=0
        
    def empty(self):
        if self.heapsize==0:
            return True
        else:
            return False
    def full(self):
        if self.heapsize==self.c:
            return True
        else:
            return False
    def push(self,val):
        if self.full():
            print("Heap full, can't push")
            return
        self.heapsize+=1
        curindex=self.heapsize
        while curindex!=1 and self.heap[curindex//2]<val:
            self.heap[curindex]= self.heap[curindex//2]
            curindex=curindex//2
        self.heap[curindex]=val
    def pop(self):
        if self.empty():
            print("Heap empty, can't pop")
            return
        lastnode=self.heap[self.heapsize]
        self.heapsize-=1
        curnode=1
        child=2
        while child<=self.heapsize:
            if child<self.heapsize and self.heap[child]<self.heap[child+1]:
                child+=1
            elif lastnode>=self.heap[child]:
                break
            curnode=child
            child=child*2
        self.heap[curnode]=lastnode
    def printnode(self):
        for i in range(1,self.heapsize+1):
            print(str(self.heap[i])+",")
        print()
        
a=maxheap(16)
a.push(48)
a.push(33)
a.push(78)
a.push(11)
a.pop()
a.printnode()