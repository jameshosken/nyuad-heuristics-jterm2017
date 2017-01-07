# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 11:23:20 2017

@author: james
"""

#Print checkerboard using for loops and print("string", end="")

for row in range(6):
    for col in range(12):
        if(row%2 == 0):
            if(col%2==0):
                print("X", end="")
            else:
                print(" ", end="")
        else:
            if(col%2==0):
                print(" ", end="")
            else:
                print("X", end="")
    print()
    
while(1):
    pass