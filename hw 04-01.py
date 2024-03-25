# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 16:20:59 2018

@author: Ching
"""

class node():
    def __init__(self,d):
        self.data=d
        self.next=None
class singlelink():
    def __init__(self,firstnode):
        self.head=firstnode
        
    def displyallnode(self):
        curNode = self.head
        while curNode.next != None:
            print(curNode.data)
            curNode = curNode.next
        print(curNode.data)
        print()
        
    def empty(self):
        if self.head==None:
            return True
        else:
            return False
        
    def insertatfirst(self,new):
        if self.empty():
            self.head=new
        else:
            new.next=self.head
            self.head=new
    def removefirstnode(self):
        if self.empty():
            print("Empty")
        else:
            removednode =self.head
            self.head=self.head.next
            removednode.next =None
            
    def insertnode(self,curnode,new):
        new.next=curnode.next
        curnode.next=new
        
    def insertatlastnode(self,new):
        curnode=self.head
        while curnode.next!=None:
            curnode=curnode.next
        curnode.next=new

    def removeLastNode(self):
        curNode = self.head
        nextNode = self.head.next
        while nextNode.next != None:
            curNode = nextNode
            nextNode = nextNode.next
        curNode.next = None
            
    def concatenate(self,b):
        if self.empty():
            self.head=b.head
        elif not b.empty():
            curnode=self.head
            while curnode.next!=None:
                curnode=curnode.next
            curnode.next=b.head
    def inverse(self):
        if not self.empty():
            prenode=None
            nextnode=self.head.next
            curnode=self.head
            while nextnode!=None:
                curnode.next=prenode
                prenode=curnode
                curnode=nextnode
                nextnode=nextnode.next
            curnode.next=prenode
            self.head=curnode
    def length(self):
        if self.empty():
            return 0
        else:
            count=1
            curnode=self.head
            while curnode.next!=None:
                count+=1
                curnode=curnode.next
            return count
        
a=singlelink(None)
node1=node(1)
a.insertatfirst(node1)
a.insertatfirst(node(2))
a.insertatfirst(node(3))

a.displyallnode()
a.removefirstnode()
a.displyallnode()

a.insertatlastnode(node(4))
a.displyallnode()
a.removeLastNode()
a.displyallnode()

b = singlelink(node(5))
a.concatenate(singlelink(node(5)))
a.displyallnode()   

a.inverse()
a.displyallnode()
a.insertnode(node1, node(6))
a.displyallnode()
print(a.length()) 