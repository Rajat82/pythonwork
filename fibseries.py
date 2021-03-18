# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:24:35 2021

@author: Rajat
"""
#fibonacci series function
def gen_fib():
    
    i = 1
    if count == 0:
        fib = []
    elif count == 1:
        fib = [0]
    elif count == 2:
        fib = [0,1]
    elif count > 2:
        fib = [0,1]
        while i < (count - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1

    return fib
        
count = int(input("How many fibonacci numbers would you like to generate? "))
print(gen_fib())