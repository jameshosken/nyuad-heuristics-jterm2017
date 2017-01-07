# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 02:10:04 2017

@author: james
"""

current = 0
total = 0
count = 0

while(current != -1):
    current = int(input("Enter new number. Enter '-1' to end: "))
   
    if(current > 0):
        total = total + current
        count = count + 1

#Average numbers out. Convert to float for decimal precision.
average = float(total) / count        
print("Average is: " + str(average) + ", with a count of " + str(count))

while(1):
    pass

   
	