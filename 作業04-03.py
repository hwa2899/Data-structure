# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 15:48:55 2018

@author: User
"""

class DbListNode():
    def __init__(self, data):
        self.data = data
        self.llink= self
        self.rlink= self
        
class DBLinkedList():
    def __init__(self):
        self.head = DbListNode(None)
    def displyAllNode(self):
        curNode = self.head.rlink
        while curNode.rlink != self.head:
            print(curNode.data)
            curNode = curNode.rlink
        print(curNode.data)
        print()
    def isEmpty(self):
        if self.head.rlink == self.head:
            return True
        else:
            return False
    def insertAtFirstNode(self, newNode):
        newNode.rlink = self.head.rlink
        newNode.llink = self.head
        self.head.rlink.llink = newNode
        self.head.rlink = newNode
    def removeFirstNode(self):
        if self.isEmpty():
            print("此串列為空串列，沒有節點可刪除!")
        else:
            removedNode = self.head.rlink
            self.head.rlink = removedNode.rlink
            removedNode.rlink.llink = self.head
            removedNode.rlink = removedNode
            removedNode.llink = removedNode

#執行
a = DBLinkedList()
print(a.isEmpty())
a.insertAtFirstNode(DbListNode(1))
a.insertAtFirstNode(DbListNode(2))
a.displyAllNode()
print(a.isEmpty())
a.removeFirstNode()
a.displyAllNode()