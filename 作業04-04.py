# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 21:52:16 2018

@author: xiu
"""

class ChainNode():
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack():
    def __init__(self):
        self.top = None
    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
    def Push(self, newNode):
        newNode.next = self.top
        self.top = newNode
    def Pop(self):
        if self.isEmpty():
            return None
        popNode = self.top
        self.top = self.top.next
        popNode.next = None
        return popNode
    def Top(self):
        return self.top
    
#執行
a = Stack()
print(a.isEmpty())
a.Push(ChainNode(1))
print(a.isEmpty())
a.Push(ChainNode(2))
print(a.Top().data)
a.Pop()
print(a.Top().data)
a.Pop()