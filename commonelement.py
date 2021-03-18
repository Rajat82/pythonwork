# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 00:26:10 2021

@author: Rajat
"""


"""write a program that returns a list
 that contains only the elements that
 are common between the lists (without duplicates). """

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
newlist=[]

for i in a:
    for j in b:
        if i==j:
            if i not in newlist:
                newlist.append(i)
            
            
            
            
print(newlist)
            