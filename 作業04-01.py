# -*- coding: utf-8 -*-

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self, FirstNode):
        self.head = FirstNode
    def displyAllNode(self):
        curNode = self.head
        while curNode.next != None:
            print(curNode.data)
            curNode = curNode.next
        print(curNode.data)
        print()
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    def insertAtFirstNode(self, newNode):
        newNode.next = self.head
        self.head = newNode
    def removeFirstNode(self):
        removedNode = self.head
        self.head = self.head.next
        removedNode.next = None
    def insertNode(self, curNode, newNode):
        newNode.next = curNode.next
        curNode.next = newNode
    def insertAtLastNode(self, newNode):
        curNode = self.head
        while curNode.next != None:
            curNode = curNode.next
        curNode.next = newNode
    def removeLastNode(self):
        curNode = self.head
        nextNode = self.head.next
        while nextNode.next != None:
            curNode = nextNode
            nextNode = nextNode.next
        curNode.next = None
    def concatenate(self, b):
        if self.isEmpty():
            self.head = b.head
        elif not b.isEmpty():
            curNode = self.head
            while curNode.next != None:
                curNode = curNode.next
            curNode.next = b.head
    def inverse(self):
        if not self.isEmpty():
            preNode = None
            nextNode = self.head.next
            curNode = self.head
            while nextNode != None:
                curNode.next = preNode
                preNode = curNode
                curNode = nextNode
                nextNode = nextNode.next
            curNode.next = preNode
            self.head = curNode
    def length(self):
        curNode = self.head
        count = 1
        while curNode.next != None:
            count += 1
            curNode = curNode.next
        return count
           
#執行
a = LinkedList(None)
print(a.isEmpty())
node1 = Node(1)
a = LinkedList(node1)
 
a.insertAtFirstNode(Node(2))
a.insertAtFirstNode(Node(3))
a.displyAllNode()
a.removeFirstNode()
a.displyAllNode()

a.insertAtLastNode(Node(4))
a.displyAllNode()
a.removeLastNode()
a.displyAllNode()

b = LinkedList(Node(5))
a.concatenate(b)
a.displyAllNode()   

a.inverse()
a.displyAllNode()
a.insertNode(node1, Node(6))
a.displyAllNode()
print(a.length()) 