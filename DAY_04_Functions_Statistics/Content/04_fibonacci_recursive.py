# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 12:33:39 2017

@author: james
"""

import time

def fib(length):
    fibList = [1]
    for i in range(length-1):
        if(len(fibList)==1):
            fibList.append(1)
        else:
            fibList.append(fibList[i] + fibList[i-1])

    return(fibList[-1])

    
    
def fibrec(n):
    if(n == 0):
        return 0
    elif(n==1):
        return 1
    else:
        return(fibrec(n-1) + fibrec(n-2))
        

"""
print("Normal:")
start = time.clock()
for i in range(1000):
    fib(10)
end = time.clock()
timer = (end-start)/1000
print(end)

print("Recursive:")
start= time.clock()
for i in range(1000):
    fibrec(10)
end= time.clock()
timer = (end-start)/1000
print(end)
"""