# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 14:16:45 2018

@author: Ching
"""

#Fibonacci 遞迴演算

def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(5))

#Fibonacci 非遞迴
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else: 
        prev2=0
        prev1=1
        i=2
        for i in range(n):
            item=prev1+prev2
            prev2=prev1
            prev1=item
        return item
print(fibonacci(5))


