# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 13:28:56 2017

@author: james
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 02:10:04 2017

@author: james
"""

#Empty list to populate during our loop.
grades = []
current = 0

while(current != -1):
    current = int(input("Enter new grade. Enter '-1' to end: "))
   
    if(current > 0):
        grades.append(current)

#Average numbers out. Convert to float for decimal precision.
average = sum(grades)/len(grades)       
print("Average is: " + str(average) + ", with a count of " + str(len(grades)))

while(1):
    pass

   
	