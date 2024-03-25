# -*- coding: utf-8 -*-

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self, LastNode):
        self.last = LastNode
        if LastNode != None:
            self.last.next = self.last
    def displyAllNode(self):
        curNode = self.last.next
        while curNode.next != self.last.next:
            print(curNode.data)
            curNode = curNode.next
        print(curNode.data)
        print()
    def isEmpty(self):
        if self.last == None:
            return True
        else:
            return False
    def insertAtFirstNode(self, newNode):
        newNode.next = self.last.next
        self.last.next = newNode
    def removeFirstNode(self):
        removedNode = self.last.next
        self.last.next = removedNode.next
        removedNode.next = None
    def insertNode(self, curNode, newNode):
        newNode.next = curNode.next
        curNode.next = newNode
    def insertAtLastNode(self, newNode):
        newNode.next = self.last.next
        self.last.next = newNode
        self.last = newNode
    def removeLastNode(self):
        curNode = self.last
        nextNode = self.last.next
        while nextNode.next != self.last.next:
            curNode = nextNode
            nextNode = nextNode.next
        curNode.next = self.last.next
        self.last = curNode
    def concatenate(self, b):
        if self.isEmpty():
            self.last = b.last
        elif not b.isEmpty():
            temp = self.last.next
            self.last.next = b.last.next
            b.last.next = temp
            self.last = b.last
                        
    def inverse(self):
        if not self.isEmpty():
            preNode = self.last
            curNode = self.last.next
            nextNode = curNode.next
            while nextNode != self.last.next:
                curNode.next = preNode
                preNode = curNode
                curNode = nextNode
                nextNode = nextNode.next
            curNode.next = preNode
            self.last = nextNode
    def length(self):
        curNode = self.last.next
        count = 1
        while curNode.next != self.last.next:
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