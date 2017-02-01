# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 14:49:12 2017

@author: james
"""
"""

# Write a snippet that creates a list of 10 fibonnacci numbers

fibList = [1, 1]

for i in range(1, 10):
    fibList.append(fibList[i] + fibList[i-1])
    
print (fibList)
"""
# Write a function that returns the n'th fibonnacci number

def factorial(n):
    if(n == 1):
        return 1
    else:
        return ( n * factorial(n-1) )
        
        
print(factorial(10))