# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 14:22:41 2018

@author: Ching
"""

class Myqueue():
    def __init__(self,qcapacity):
        self.capacity=qcapacity
        self.queue=[None]*self.capacity
        self.front=-1
        self.rear=-1

    def empty(self):
        if self.front==self.rear:
            return True
        else:
            return False
    def full(self):
        if self.rear==self.capacity-1:
            return True
        else: 
            return False
    def push(self,value):
        if self.full():
            print("Full")
        else:
            self.rear+=1
            self.queue[self.rear]=value
    def pop(self):
        if self.empty():
            print("Empty")
        else:
            self.front+=1
            return self.queue[self.front]
    def Front(self):
        if self.empty():
            print("Empty")
        else:
            return self.queue[self.front+1]
    def Rear(self):
        if self.empty():
            print("Empty")
        else:
            return self.queue[self.rear]

a=Myqueue(3)
a.push(5)
a.push(4)
a.push(3)
print(a.Front())
a.pop()
print(a.Front())
#print(a.queue)
#a.push(6)
#print(a.Rear())
#print(a.Front())
#a.pop()
#a.pop()
#print(a.queue)