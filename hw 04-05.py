# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 21:41:49 2018

@author: Ching
"""

class chainnode():
    def __init__(self, data):
        self.data = data
        self.next = None
        
class queue():
    def __init__(self):
        self.front = None
        self.rear = None
    def empty(self):
        if self.front == None:
            return True
        else:
            return False
    def push(self, newNode):
        if self.front == None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
    def pop(self):
        if self.empty():
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
    
#run
a = queue()
print(a.empty())
a.push(chainnode(1))
print(a.empty())
a.push(chainnode(2))
print(a.Front().data)
print(a.Rear().data)
a.pop()
print(a.Front().data)
print(a.Rear().data)