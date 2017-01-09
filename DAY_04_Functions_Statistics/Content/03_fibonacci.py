# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 12:06:07 2017

@author: james
"""

def fib(length):
    fibList = [1]
    for i in range(length-1):
        if(len(fibList)==1):
            fibList.append(1)
        else:
            fibList.append(fibList[i] + fibList[i-1])

    return(fibList)
            
print(fib(10))