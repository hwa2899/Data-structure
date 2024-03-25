# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 15:43:59 2018

@author: xiu
"""

class TermNode():
    def __init__(self, ncoef, nexp):
        self.coef = ncoef
        self.exp = nexp
        self.next = None
        
class Polynomial():
    def __init__(self):
        self.dummyNode = TermNode (None, -1)
        self.front = self.dummyNode
        self.rear = self.dummyNode
        self.rear.next = self.dummyNode
    def addATermNode(self, newNode):
        self.rear.next = newNode
        self.rear = newNode
        self.rear.next = self.dummyNode
        
def Polynomial_add(A, B):
     C = Polynomial()
     A = A.next
     B = B.next
     while A.coef != None and B.coef != None:
         if A.exp == B.exp:
             t = A.coef + B.coef
             newNode = TermNode(t, A.exp)
             C.addATermNode(newNode)
             A = A.next
             B = B.next
         elif A.exp < B.exp:
             t = B.coef
             newNode = TermNode(t, B.exp)
             C.addATermNode(newNode)
             B = B.next
         else:
             t = A.coef
             newNode = TermNode(t, A.exp)
             C.addATermNode(newNode)
             A = A.next
     while A.coef != None:
         t = A.coef
         newNode = TermNode(t, A.exp)
         C.addATermNode(newNode)
         A = A.next
     while B.coef != None:
         t = B.coef
         newNode = TermNode(t, B.exp)
         C.addATermNode(newNode)
         B = B.next
     return C

#執行
A = Polynomial()
A.addATermNode(TermNode(3, 14))
A.addATermNode(TermNode(2, 8))
A.addATermNode(TermNode(1, 0))
B = Polynomial()
B.addATermNode(TermNode(8, 14))
B.addATermNode(TermNode(-3, 10))
B.addATermNode(TermNode(10, 6))
C = Polynomial_add(A.front, B.front)
c = C.front.next
while c.coef != None:
    print(c.coef,c.exp)
    c = c.next