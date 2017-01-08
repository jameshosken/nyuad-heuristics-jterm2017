# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 14:40:22 2017

@author: james
"""

rows = int(input("Input number of rows: "))
cols = int(input("Input number of cols: "))

for row in range(rows):
    
    for col in range(cols):
        
        if(row%2==0):
            if(col%2 == 0):
                print("X", end="")
            else:
                print(" ", end="")
        else:
            if(col%2 == 0):
                print(" ", end="")
            else:
                print("X", end="")
                
    print()