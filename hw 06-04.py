# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 18:31:40 2019

@author: Ching
"""


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = Node(None)
    def insertAtLastNode(self, newNode):
        curNode = self.head
        while curNode.next != None:
            curNode = curNode.next
        curNode.next = newNode
class Graph():
    def __init__(self, nv):
        self.n = nv
        self.headNodes = [None] * nv
        self.visited = [False] * nv
    def DFS_do(self, v):
        self.visited[v] = True
        print(v)
        curNode = self.headNodes[v].head.next
        while curNode != None:
            if not self.visited[curNode.data]:
                self.DFS_do(curNode.data)
            curNode = curNode.next
    def DFS(self):
        self.DFS_do(0)

#run
L0 = LinkedList()
L0.insertAtLastNode(Node(1))
L0.insertAtLastNode(Node(2))
L1 = LinkedList()
L1.insertAtLastNode(Node(0))
L1.insertAtLastNode(Node(3))
L1.insertAtLastNode(Node(4))
L2 = LinkedList()
L2.insertAtLastNode(Node(0))
L2.insertAtLastNode(Node(5))
L2.insertAtLastNode(Node(6))
L3 = LinkedList()
L3.insertAtLastNode(Node(1))
L3.insertAtLastNode(Node(7))
L4 = LinkedList()
L4.insertAtLastNode(Node(1))
L4.insertAtLastNode(Node(7))
L5 = LinkedList()
L5.insertAtLastNode(Node(2))
L5.insertAtLastNode(Node(7))
L6 = LinkedList()
L6.insertAtLastNode(Node(2))
L6.insertAtLastNode(Node(7))
L7 = LinkedList()
L7.insertAtLastNode(Node(3))
L7.insertAtLastNode(Node(4))
L7.insertAtLastNode(Node(5))
L7.insertAtLastNode(Node(6))
g = Graph(8)
g.headNodes = [L0, L1, L2, L3, L4, L5, L6, L7]
g.DFS()
