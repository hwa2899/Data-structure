# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 21:41:26 2018

@author: Ching
"""

#def calPostfix(str):
#    stack = []
#    for item in str.split():
#        if item in "*/+-":
#            temp = eval("{}{}{}".format(stack[-2], item, stack[-1]))
#            stack.pop()
#            stack.pop()
#            stack.append(temp)
#        else:
#            stack.append(item)
#    return stack[-1]
#
#
#print(calPostfix("10 8 + 6 5 * -"))
#
class Stack():
    def __init__(self, cap):
        assert cap>= 1, "StackCapacity需大於0"
        self.capacity = cap
        self.myStack = [None] * self.capacity
        self.top = -1
    def isEmpty(self):
        if self.top < 0:
            return True
        else:
            return False
    def Top(self):
        assert not self.isEmpty(), "目前Stack是空的!"
        return self.myStack[self.top]
    def Push(self, value):
        self.top = self.top + 1
        self.myStack[self.top] = value
    def Pop(self):
        assert not self.isEmpty(), "目前Stack是空的，沒有物件可pop!"
        curTop = self.top
        self.top = self.top - 1
        return self.myStack[curTop]
    def Sec_top(self):
        return self.myStack[self.top - 1]

def Add(a, b):
    return a + b
def Subtract(a, b):
    return a - b
def Multiply(a, b):
    return a * b
def Divide(a, b):
    return a / b

Operator = ["+","-","*","/"]
            
def Eval(Expression_e):
    e = Expression_e.split()
    stack = Stack(len(e))
    for x in e:
        if x not in Operator:
            x = float(x)
            stack.Push(x)
        else:
            if x == "+":
                temp = Add(stack.Sec_top(), stack.Top())
            elif x == "-":
                temp = Subtract(stack.Sec_top(), stack.Top())
            elif x == "*":
                temp = Multiply(stack.Sec_top(), stack.Top())
            else:
                temp = Divide(stack.Sec_top(), stack.Top())
            stack.Pop()
            stack.Pop()
            stack.Push(temp)
    return stack.Top()

#執行            
print(Eval("10 8 + 6 5 * -"))