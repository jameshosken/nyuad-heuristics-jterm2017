# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 11:19:33 2017

@author: james
"""

#How to access items in a list

myList = ["apples", "oranges", "grapes"]


#Method 1: for {item} in {list}
for fruit in myList:
    print(fruit)
    
"""
This method loops through each item in the list, 
and for that iteration assigns that particular item to the name 'fruit'.
"""

#####################

#Method 2: list[index]
item1 = myList[0]
item2 = myList[1]

print(item1)
print(item2)
print(myList[2])  

"""
This method uses the [n] brackets to access the 'n'th item in the list.
""" 

#Method 3 (hybrid): for i in range(len(list))
for i in range(len(myList)):
    print(myList[i])

"""
This method is an extension of method 2,
in that it uses the [] brackets to access 
items at a certain place in the list. Unlike method 2,
however, this method loops through each item in the list
"""
    
#Discuss: Benifits of each method
    
while(1):
    pass
