# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 13:37:00 2017

@author: james
"""

guess = 0
minimum = 1
maximum = 1000

print("Think of a number between 1 and 1000")

while(True):
    
    #guess = random.randint(minimum+1, maximum)
    guess = int((minimum + maximum)/2)
    
    print("My guess is " + str(guess))
    answer = input("Is your num 'greater', 'less', or 'equal' to this? ")
    
    if(answer == "equal"):
        print("Correct! I am amazing.")
        break
    elif (answer == "greater"):
        minimum = guess
    elif (answer == "less"):
        maximum = guess
    else:
        print("Please type only 'greater', 'less', or 'equal' ")
    
while(1):
    pass