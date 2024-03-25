# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 20:54:46 2018

@author: Ching
"""

class dblistnode():
    def __init__(self, data):
        self.data = data
        self.llink= self
        self.rlink= self
        
class dblinkedlist():
    def __init__(self):
        self.head = dblistnode(None)
    def displyallnode(self):
        curNode = self.head.rlink
        while curNode.rlink != self.head:
            print(curNode.data)
            curNode = curNode.rlink
        print(curNode.data)
        print()
    def empty(self):
        if self.head.rlink == self.head:
            return True
        else:
            return False
    def insertAtFirstNode(self, new):
        new.rlink = self.head.rlink
        new.llink = self.head
        self.head.rlink.llink = new
        self.head.rlink = new
    def removefirstnode(self):
        if self.empty():
            print("No nodes to remove")
        else:
            removedNode = self.head.rlink
            self.head.rlink = removedNode.rlink
            removedNode.rlink.llink = self.head
            removedNode.rlink = removedNode
            removedNode.llink = removedNode

#run
a = dblinkedlist()
print(a.empty())
a.insertAtFirstNode(dblistnode(2))
a.insertAtFirstNode(dblistnode(3))
a.displyallnode()
print(a.empty())
a.removefirstnode()
a.displyallnode()