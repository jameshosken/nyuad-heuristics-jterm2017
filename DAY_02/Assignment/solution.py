# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 12:10:46 2017

@author: james
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 14:04:21 2016

@author: jh3284
"""

high = 1000
low = 1
counter = 1 #Keep track of how many times computer has guessed

answer = "" #QUESTION: Why do this? Why is answer assigned to empty string?

while(answer != "equal"):    #"End" case here is the correct guess.

    mid = (high + low)//2    #Midpoint Use '//' for integer division
 
    print("Is your number equal to, greater than, or less than: " + str(mid))
 
    answer = input("Please answer with 'equal', 'greater', or 'less'")
 
    if(answer == "equal"):
        print("Damn I'm good.")                                                
    elif(answer == "greater"):
        low = mid
        print("Okay, let me try again")
        counter += 1
    elif(answer == "less"):
        high = mid
        print ("Okay, let me try again")
        counter += 1
    else:
        print("Please check your input and answer again.")
    print()    #This adds a linebreak after each round, for readability.