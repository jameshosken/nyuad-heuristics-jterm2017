# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 11:38:16 2017

@author: james
"""
#Add items to list using while loop

myList = []

userInput = ""

while(userInput != "done"):
    userInput = input("Add a new item to your list")
    
    if(userInput != "done"):
        myList.append(userInput)
        
print("Your final list is: ")
print(myList)

while(1):
    pass