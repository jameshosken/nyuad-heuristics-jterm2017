# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 11:08:32 2017

@author: james
"""

# Creating a dictionary
grades = {"James": 75, "Ali": 85, "Susan": 90, "Scott": 92}

#Adding to dictionary
grades["Jennifer"] = 88

print(grades)

#Accessing dictionaries

## Getting specific values from keys
print(grades.get("James"))
print(grades["James"])

## Getting all keys
print()
for key in grades.keys():
    print(key)
    
## Getting all values
print(grades.values())
for val in grades.values():
    print(val)