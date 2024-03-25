# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 22:50:59 2018

@author: xiu
"""

class Stack():
    def __init__(self, stackCapacity):
        assert stackCapacity >= 1, "StackCapacity需大於0"
        self.capacity = stackCapacity
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

def isp(operator):
    if operator == "*" or operator == "/":
        return 2
    elif operator == "+" or operator == "-":
        return 3
    elif operator == "(" or operator == "#":
        return 8
def icp(operator):
    if operator == "*" or operator == "/":
        return 2
    elif operator == "+" or operator == "-":
        return 3
    elif operator == "(":
        return 0

Operator = ["+", "-", "*", "/", "(", ")", "#"]

def Postfix(E):
    stack = Stack(len(E))
    stack.Push("#")
    for x in E:
        if x not in Operator:
            print(x)
        elif x == ")":
            while stack.Top() != "(":
                print(stack.Top())
                stack.Pop()
            stack.Pop()
        else:
            while isp(stack.Top()) <= icp(x):
                print(stack.Top())
                stack.Pop()
            stack.Push(x)
    while not stack.isEmpty():
        print(stack.Top())
        stack.Pop()
        
#執行
Postfix("A*(B+C)*D")
#Postfix("a*(b+c*d)/e-f")