# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 21:20:29 2018

@author: Ching
"""

class chainnode():
    def __init__(self, data):
        self.data = data
        self.next = None
        
class stack():
    def __init__(self):
        self.top = None
    def empty(self):
        if self.top == None:
            return True
        else:
            return False
    def push(self, newNode):
        newNode.next = self.top
        self.top = newNode
    def pop(self):
        if self.empty():
            return None
        popNode = self.top
        self.top = self.top.next
        popNode.next = None
        return popNode
    def Top(self):
        return self.top
    
#run
a = stack()
print(a.empty())
a.push(chainnode(2))
print(a.empty())
a.push(chainnode(3))
print(a.Top().data)
a.pop()
print(a.Top().data)
a.pop()
print(a.empty())