# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 00:05:46 2021

@author: Rajat
"""

#reverse a phrase

def rev_pharse(phrase):
    list1=phrase.split()
    list1.reverse()
    revpharse ="".join(list1)
    return revpharse



a=str(input("enter a string"))
print(rev_pharse(a))