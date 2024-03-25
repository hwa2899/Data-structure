# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 22:22:06 2018

@author: xiu
"""

class ChainNode():
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue():
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self):
        if self.front == None:
            return True
        else:
            return False
    def Push(self, newNode):
        if self.front == None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
    def Pop(self):
        if self.isEmpty():
            return None
        popNode = self.front
        if self.front == self.rear:
            self.front = None
            self.rear =None
        else:
            self.front = self.front.next
            popNode.next = None
        return popNode
    def Front(self):
        return self.front
    def Rear(self):
        return self.rear
    
#執行
a = Queue()
print(a.isEmpty())
a.Push(ChainNode(1))
print(a.isEmpty())
a.Push(ChainNode(2))
print(a.Front().data)
print(a.Rear().data)
a.Pop()
print(a.Front().data)
print(a.Rear().data)