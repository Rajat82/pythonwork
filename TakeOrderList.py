# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 23:44:51 2021

@author: Rajat
"""

#program to write a function to take a order list
mylist=[]
n=int(input("enter the number of element"))
for i in range(0,n):
    listele=eval(input("enter the element"))
    mylist.append(listele)
    mylist.sort()
    

print(mylist)