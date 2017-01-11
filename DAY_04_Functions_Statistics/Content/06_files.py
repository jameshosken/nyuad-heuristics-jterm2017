# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 15:56:21 2017

@author: james
"""

gradesList  = []


f = open("grades.txt", "r")

lines = f.readlines()

for line in lines:
    splitLine = line.split(":")
    grade = splitLine[1].strip()
    grade = int(grade)
    gradesList.append(grade)
    
    

f.close()

print(sum(gradesList)/len(gradesList))