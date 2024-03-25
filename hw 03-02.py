# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 21:53:28 2018

@author: Ching
"""

#str = input()
#
#def toPostfix(str):
#    stable = {'*': 2, '/': 2, '%': 2, '+': 3, '-': 3, '(': 8}
#    itable = {'*': 2, '/': 2, '%': 2, '+': 3, '-': 3, '(': 0}
#    stack = []
#    for char in str:
#        if char in "+-*/(":
#            if len(stack):
#                if stable[stack[-1]] <= itable[char]:
#                    print(stack[-1], end="")
#                    stack.pop()
#            stack.append(char)
#        elif char == ')':
#            while stack[-1] != '(':
#                print(stack[-1], end="")    # A*(B+C)*D
#                stack.pop()
#            stack.pop()
#        else:
#            print(char, end="")
#
#    while len(stack):
#        print(stack[-1], end="")
#        stack.pop()
#
#
#toPostfix(str)

class Stack():
    def __init__(self, cap):
        assert cap >= 1, "StackCapacity需大於0"
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

def Postfix(string):
    stack = Stack(len(string))
    stack.Push("#")
    for x in string:
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