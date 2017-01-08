# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 11:20:33 2017

@author: james
"""
#Reverse List
myList = [4,2,6,3,7,4,8,5]
reverseList = myList[::-1]
print("Reverse List")
print(myList)
print(reverseList)

print("----")

#Reverse Sort (highest to lowest)
myList = [3,2,5,4,1,5]
reverseSortList = sorted(myList, reverse=True)
print("Reverse Sort (highest to lowest)")
print(myList)
print(reverseSortList)

print("----")

#Access specific 
myList = ["one", "two", "three", "four"]
print("First item:")
print(myList[0])

print("Last item:")
print(myList[len(myList)-1])
#OR (easier)
print(myList[-1])

print("----")

#Sum all items in list (requires number type)
myList = [1,2,3,4,5,6,7,8,9]
print(sum(myList))

print("----")

#Split a string into a list
myString = "This is a sentence that I shall split"
words = myString.split(" ")
print(myString)
print(words)


while(1):
    pass