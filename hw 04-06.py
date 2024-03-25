# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 22:02:58 2018

@author: Ching
"""

class termnode():
    def __init__(self, ncoef, nexp):
        self.coef = ncoef
        self.exp = nexp
        self.next = None
        
class Polynomial():
    def __init__(self):
        self.dummyNode = termnode (None, -1)
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
             newNode = termnode(t, A.exp)
             C.addATermNode(newNode)
             A = A.next
             B = B.next
         elif A.exp < B.exp:
             t = B.coef
             newNode = termnode(t, B.exp)
             C.addATermNode(newNode)
             B = B.next
         else:
             t = A.coef
             newNode = termnode(t, A.exp)
             C.addATermNode(newNode)
             A = A.next
     while A.coef != None:
         t = A.coef
         newNode = termnode(t, A.exp)
         C.addATermNode(newNode)
         A = A.next
     while B.coef != None:
         t = B.coef
         newNode = termnode(t, B.exp)
         C.addATermNode(newNode)
         B = B.next
     return C

#run
A = Polynomial()
A.addATermNode(termnode(3, 14))
A.addATermNode(termnode(2, 8))
A.addATermNode(termnode(1, 0))
B = Polynomial()
B.addATermNode(termnode(8, 14))
B.addATermNode(termnode(-3, 10))
B.addATermNode(termnode(10, 6))
C = Polynomial_add(A.front, B.front)
c = C.front.next
while c.coef != None:
    print(c.coef,c.exp)
    c = c.next