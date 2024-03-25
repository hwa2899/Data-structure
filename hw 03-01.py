# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 21:12:49 2018

@author: Ching
"""
class stack():
    def __init__(self,cap):
        if cap<1:
            raise ValueError('Stack Capacity needs to be greater than 0')
        self.mystack= list([0]*cap)
        self.capacity=cap
        self.top=-1
        
    def empty(self):
        if self.top<0:
            return True
        else:
            return False
    
    def full(self):
        return self.top == self.capacity-1
    
    def Top(self):
        if self.empty():
            raise ValueError("The stack is empty")
        return self.mystack[self.top]
    
    def push(self,t):
        if self.full():
            raise ValueError("Stack full")
        self.top+=1
        self.mystack[self.top]=t
        
    def pop(self):
        if self.empty():
            raise ValueError("Stack empty, nothing to pop")
        curtop=self.top
        self.top-=1
        return self.mystack[curtop]

#obj=stack(10)
#i=0
#while 1:
#    try:
#        obj.push(1)
#        print(obj.mystack[i])
#        i+=1
#    except Exception as e:
#        print(e)
#        exit(0)