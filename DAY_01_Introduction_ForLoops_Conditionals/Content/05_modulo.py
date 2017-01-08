# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 16:01:18 2017

@author: james
"""


#CHECK IF SOMETHING IS BOTH DIVISIBLE BY 3 AND 2
for i in range(100):
    if(i % 2 == 0 and i % 3 == 0):
        print(str(i) + " is divisible by both 3 and 2")
        
#CHECK IF SOMETHING IS EITHER DIVIBLE BY 3 OR 2
for i in range(100):
    if(i%2 == 0 or i%3 == 0):
        print (str(i) + " is divisible by either 3 or 2")

#CHECK IF NUMBER IS ODD. 
#If not (i.e. even), check if divisible by 3. 
#Otherwise, say it's uninteresting.

for i in range(1,100):
    print (i)
    if(i%2 != 0):
        print("Odd!")
    elif(i%3 == 0):
        print("Even number divisible by 3")
    else:
        print("This number is of no interest to me")
        
