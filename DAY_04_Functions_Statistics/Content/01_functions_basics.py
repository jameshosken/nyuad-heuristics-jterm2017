# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 11:18:50 2017

@author: james
"""

"""
Functions are a way of segmenting your code. Functions serve to both help 
keep track of what's going on and where in your code, 
and also to easily reuse pieces of code that are useful in many places.
"""

"""
For example, if I want to print the square of a number many times, 
previously I'd have to do this:
"""

x = int(input("What's your first number? "))
sqrX = x * x
print(sqrX)

y = int(input("What's your second number? "))
sqrY = y * y
print(sqrY)

z = int(input("What's your third number? "))
sqrZ = z * z
print(sqrZ)

"""
By writing a FUNCTION I greatly reduce the amount of lines I use
"""

def sqr(num):
    print(num*num)
    
x = int(input("What's your first number? "))
y = int(input("What's your second number? "))
z = int(input("What's your third number? "))
sqr(x)
sqr(y)
sqr(z)