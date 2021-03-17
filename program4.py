
"""Create a program that asks the user for
a number and then prints out a list of all
 the divisors of that number."""

#here we take input from user 
num=eval(input("enter a number"))
numlist=[] 
for i in range(1,num):
    if(num%i==0):
        numlist.append(i)
    
    
print(numlist)


