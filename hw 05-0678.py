# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 21:13:54 2018

@author: Ching
"""

class treenode():
    def __init__(self,key):
        self.key=key
        self.leftchild=None
        self.rightchild=None
        
class binarytree():
    def __init__(self):
        self.root=None
    def insert(self,node):
        curnode=self.root
        parentnode=None
        while curnode!=None:
            parentnode=curnode
            if node.key==curnode.key:
                return False
            elif node.key<curnode.key:
                curnode=curnode.leftchild
            else:
                curnode=curnode.rightchild
        curnode=node
        if self.root==None:
            self.root=curnode
        elif curnode.key<parentnode.key:
            parentnode.leftchild=curnode
        else:
            parentnode.rightchild=curnode
        return True
    
    def findkeynode(self,key):
        return self.findrecursive(self.root,key)
    
    def findrecursive(self,curnode,key):
        if curnode==None:
            return None
        elif key==curnode.key:
            return curnode
        elif key<curnode.key:
            return self.findrecursive(curnode.leftchild,key)
        else:
            return self.findrecursive(curnode.rightchild,key)
    
    def notrecursive(self,curnode,key):
        while curnode!=None:
            if curnode.key==key:
                return curnode
            elif key<curnode.key:
                curnode=curnode.leftchild
            else:
                curnode=curnode.rightchild
        return None

#run
b=binarytree()
b.insert(treenode(33))
b.insert(treenode(78))
b.insert(treenode(11))
b.insert(treenode(48))
b.insert(treenode(20))

result=b.notrecursive(b.root,48)
if result!=None:
    print(result.key)
else:
    print(result)
    
result=b.notrecursive(b.root,49)
if result!=None:
    print(result.key)
else:
    print(result)
    
result=b.findkeynode(48)
if result!=None:
    print(result.key)
else:
    print(result)
  
result=b.findkeynode(49)
if result!=None:
    print(result.key)
else:
    print(result)
    
A=treenode(33)
B=treenode(78)
C=treenode(11)
D=treenode(48)
E=treenode(20)
F=treenode(55)
G=treenode(35)
H=treenode(99)
A.leftchild=C
A.rightchild=B
B.leftchild=D
B.rightchild=H
C.rightchild=E
D.leftchild=G
D.rightchild=F
tree=binarytree()
tree.root=A
print(tree.findkeynode(11))
print(C)