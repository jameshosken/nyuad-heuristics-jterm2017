# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 11:33:31 2017

@author: james
"""


classSize = int(input("How many people in the class? "))

runningTotal = 0

for i in range(classSize):
    currentGrade = int(input("Grade of person " + str(i+1) + ": "))
    runningTotal = runningTotal + currentGrade
    
print("Average grade = " + str(runningTotal/classSize))


while(1):
    pass