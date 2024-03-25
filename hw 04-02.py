# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:01:07 2018

@author: Ching
"""

class node():
    def __init__(self,d):
        self.data=d
        self.next=None
class cirlink():
    def __init__(self):
        self.head=None
    
#    def last(self):
#        curnode=self.head
#        while curnode.next!=self.head:
#            curnode=curnode.next
#        return curnode
    
    def displyallnode(self):
        curNode = self.head
        while curNode.next != self.head:
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
            self.head.next=self.head
        else:
            curnode=self.head
            while curnode.next!=self.head:
                curnode=curnode.next
            curnode.next=new
            new.next=self.head
            self.head=new
            
    def removefirstnode(self):
        if self.empty():
            print("Empty")
        else:
            curnode=self.head
            while curnode.next!=self.head:
                curnode=curnode.next
            self.head=self.head.next
            curnode.next=self.head          
            
    def insertnode(self,curnode,new):
        new.next=curnode.next
        curnode.next=new
        
    def insertatlastnode(self,new):
        curnode=self.head
        while curnode.next!=self.head:
            curnode=curnode.next
        curnode.next=new
        new.next=self.head

    def removeLastNode(self):
        curNode=self.head
        nextNode=self.head.next
        while nextNode.next!=self.head:
            curNode=nextNode
            nextNode=nextNode.next
        curNode.next=self.head
         
    def concatenate(self,b):
        if self.empty():
            self.head=b.head
        elif not b.empty():
            curnode=self.head
            while curnode.next!=self.head:
                curnode=curnode.next
            curnode.next=b.head
            curnode=b.head
            while curnode.next!=b.head:
                curnode=curnode.next
            curnode.next=self.head
            
    def inverse(self):
        if not self.empty():
            curnode=self.head
            while curnode.next!=self.head:
                curnode=curnode.next
            prenode=curnode
            nextnode=self.head.next
            curnode=self.head
            while nextnode!=self.head:
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
            while curnode.next!=self.head:
                count+=1
                curnode=curnode.next
            return count
        
a=cirlink()
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

b = cirlink()
b.insertatfirst(node(5))
a.concatenate(b)
a.displyallnode()   

a.inverse()
a.displyallnode()
a.insertnode(node1, node(6))
a.displyallnode()
print(a.length()) 