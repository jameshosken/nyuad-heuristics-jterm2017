# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 14:23:25 2017
Patterns created by the class in python.

@author: james
"""

maxnum = 10
for i in range(maxnum):
    print("*" * (maxnum - i))
    
for i in range(10):
    print((10 - i) * " " + "*" * i)
    

#Truman's Algorithm
x = 1
y = 5

for i in range(12):
    print(" " * x + "*" * x)
    x=x+y
    y=y-1
    