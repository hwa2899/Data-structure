# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:46:42 2018

@author: Ching
"""

class smatrix():
    def __init__(self,row,col,value):
        self.row=row
        self.col=col
        self.value=value
    def present(self):
        print([self.row,self.col,self.value])

def fast(data):
    num=len(data)
    sparseMatrix=[None]*(num-2)
    if num > 0:
        rowSize = [0] * data[1]
        rowStart = [0] * data[1]
        
        for i in range(2, num):
            rowSize[(data[i].col) - 1] = rowSize[(data[i].col) - 1] + 1
        
        rowStart[0] = 0
        for i in range(1, data[1]):
            rowStart[i] = rowStart[i - 1] + rowSize[i - 1]
            
        for i in range(2, num):
            j = rowStart[data[i].col - 1]
            item = smatrix(data[i].col, data[i].row, data[i].value)
            sparseMatrix[j] = item
            rowStart[data[i].col - 1] = rowStart[data[i].col - 1] + 1
    
    return sparseMatrix

data=[8, 7, smatrix(1,4,3), smatrix(1,6,-1), smatrix(3,3,2), smatrix(3,6,1), 
      smatrix(4,4,1),
      smatrix(5,1,2), smatrix(6,2,7), smatrix(7,5,-3), smatrix(8,7,-2)]
sparseMatrix = fast(data)
for i in sparseMatrix:
    i.present()