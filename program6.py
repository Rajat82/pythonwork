# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 13:04:32 2021

@author: Rajat
"""

def is_Palindrome(string):
    return string == string[::-1]

inputstring=input("Enter a string : ")
result= is_Palindrome(inputstring)

if result:
    print(inputstring,"is palindrome")
    
else:
    print("Not a palindrome")
