# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 01:06:58 2021

@author: Rajat
"""

num=eval(input("enter a number"))
res=[]
for i in range(1,10):
    res.append(num*i)
    
print(res)

#here we use with clock and open() and write() to add list into text file
with open('tableresult.txt', 'w+') as f: 
      
    # write elements of list 
    for items in res: 
        f.write('%s\n' %items) 
    
f.close()

      
