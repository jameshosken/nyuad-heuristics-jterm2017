# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 13:52:16 2017

@author: james
"""

f = open("things.txt", "r")

print(f)

print(f.read())

lines = f.readlines()

for i in range(len(lines)):
    print("Line " + str(i) + " is: " + lines[i])
f.close()