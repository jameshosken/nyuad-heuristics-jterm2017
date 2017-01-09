# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 13:17:24 2017

@author: james
"""

def factorial(num):
    if(num == 1):
        return 1
    else:
        return(num * factorial(num-1))
        
        
print(factorial(5))