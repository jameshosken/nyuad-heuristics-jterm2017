# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 14:55:35 2017

@author: james
"""

for j in range(21):
    if(j%2 == 0):
        for i in range(21):
            if(i%2 == 0):
                print("X", end="")
            else:
                print(" ", end="")
                
    if(j%2 > 0):
        for i in range(21):
            if(i%2 == 0):
                print(" ", end="")
            else:
                print("X", end="")
        
    print(" ")
        
