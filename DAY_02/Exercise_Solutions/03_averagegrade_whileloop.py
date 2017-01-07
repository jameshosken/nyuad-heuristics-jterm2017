# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 11:53:25 2017

@author: james
"""

#Average grade
current = 0
total = 0
count = 0

#Use "-1" as the exit condition; if user enters -1, stop looping
while(current != -1):

    current = int(input("Enter new grade. Enter '-1' to end: "))
    
    if(current > 0):
        total = total + current
        count = count + 1
        print("Grade submitted!")
   
    

#Average numbers out. Convert to float for decimal precision.
average = float(total) / count        
print("Average is: " + str(average) + ", with a count of " + str(count))


while(1):
    pass
