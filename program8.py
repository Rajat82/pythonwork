# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 13:07:27 2021

@author: Rajat
"""

num= int(input("Enter a numer : "))
if num >1:
    for i in range(2,num):
        if num % i ==0:
            print(num,"is not prime")
            break
        else:
            print(num,"is prime")
            break
else:
    print(num,"is not prime")