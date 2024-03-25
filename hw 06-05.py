# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 18:22:24 2019

@author: Ching
"""

class node():
    def __init__(self, data):
        self.data = data
        self.next = None
class linkedlist():
    def __init__(self):
        self.head = node(None)
    def insertAtLastNode(self, newNode):
        curNode = self.head
        while curNode.next != None:
            curNode = curNode.next
        curNode.next = newNode
class Queue():
    def __init__(self, queueCapacity):
        assert queueCapacity > 0, "QueueCapacity需大於0"
        self.capacity = queueCapacity
        self.myQueue = [None] * self.capacity
        self.front = -1
        self.rear = -1
    def empty(self):
        if self.front == self.rear:
            return True
        else:
            return False
    def push(self, value):
        self.rear += 1
        self.myQueue[self.rear] = value
    def pop(self):
        self.front += 1
        return self.myQueue[self.front]
class Graph():
    def __init__(self, nv):
        self.n = nv
        self.headNodes = [None] * nv
        self.visited = [False] * nv
    def BFS(self, v):
        self.visited[v] = True
        print(v)
        queue = Queue(self.n)
        queue.push(node(v))
        while not queue.empty():
            v = queue.pop().data
            curNode = self.headNodes[v].head.next
            while curNode != None:
                if not self.visited[curNode.data]:
                    queue.push(node(curNode.data))
                    self.visited[curNode.data] = True
                    print(curNode.data)
                curNode = curNode.next
                
#執行
L0 = linkedlist()
L0.insertAtLastNode(node(1))
L0.insertAtLastNode(node(2))
L1 = linkedlist()
L1.insertAtLastNode(node(0))
L1.insertAtLastNode(node(3))
L1.insertAtLastNode(node(4))
L2 = linkedlist()
L2.insertAtLastNode(node(0))
L2.insertAtLastNode(node(5))
L2.insertAtLastNode(node(6))
L3 = linkedlist()
L3.insertAtLastNode(node(1))
L3.insertAtLastNode(node(7))
L4 = linkedlist()
L4.insertAtLastNode(node(1))
L4.insertAtLastNode(node(7))
L5 = linkedlist()
L5.insertAtLastNode(node(2))
L5.insertAtLastNode(node(7))
L6 = linkedlist()
L6.insertAtLastNode(node(2))
L6.insertAtLastNode(node(7))
L7 = linkedlist()
L7.insertAtLastNode(node(3))
L7.insertAtLastNode(node(4))
L7.insertAtLastNode(node(5))
L7.insertAtLastNode(node(6))
g = Graph(8)
g.headNodes = [L0, L1, L2, L3, L4, L5, L6, L7]
g.BFS(0)