# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 01:45:30 2017

@author: james
"""

enteringData = True
myNumber = 0

while(enteringData):
    
    try:
        myNumber = int(input("Enter a number: "))
        enteringData = False
    except:
        print("Please enter JUST a number, dammit.")
        

print("Great, you made it. Your number is: " + str(myNumber))