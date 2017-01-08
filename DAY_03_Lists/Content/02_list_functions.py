# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 10:53:24 2016

@author: jh3284
"""

mylist = [0,1,2,3,2,1,0]

print("Mylist:")
print(mylist)
print()

#Access the 3rd item in the list
print("mylist[2]")
print(mylist[2])
print()

#Add 100 to the end of the list
print ("mylist.append(100):")
mylist.append(100)
print (mylist)
print ()

#Remove anything with value 100 in the list
print ("mylist.remove(100):")
mylist.remove(100)
print (mylist)
print ()

#Count the number of 1s in the list
print ("mylist.count(1):")
print (mylist.count(1))
print()

#Remove the 1st item in the list
print ("mylist.pop(0):")
mylist.pop(0)
print (mylist)
print()

#Remove the last item in the list
print ("mylist.pop(-1):")
mylist.pop(-1)
print (mylist)
print()

#Sort the list, lowest to highest.
print ("mylist.sort()")
mylist.sort()
print (mylist)
print()

#Reverse the list
print ("mylist.reverse()")
mylist.reverse()
print (mylist)
print()

while(1):
    pass
