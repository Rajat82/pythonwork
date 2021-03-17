
"""Create a program that asks the user to enter
 their name and their age. Print out a message
 addressed to them that tells them the year that 
 they will turn 100 years old."""

username=input("Enter User Name")
userage=eval(input("Enter User Age"))
currentyear=eval(input("enter the current year"))
leftage=100-userage
fAge=currentyear+leftage

print("The year you will turn 100 years ") 
print(fAge)