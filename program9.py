'''Write a program (function!) that takes a
 list and returns a new list that contains
 all the elements of the first list minus
 all the duplicates.'''

def Remove(mylist):
    
     newlist=[]
     for i in mylist:
        if i not in newlist:
            newlist.append(i)
     return newlist
         

mylist=[1,1,2,2,3,4,5,6,6,7]
    
print(Remove(mylist))