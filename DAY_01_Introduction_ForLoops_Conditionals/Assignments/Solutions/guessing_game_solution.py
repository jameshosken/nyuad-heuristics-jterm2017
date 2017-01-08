# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 23:58:08 2017

@author:
    james
"""
#Access random number generation:
import random

#Assign a random number to a variable that we can access later:
randomnumber = random.randint(1, 100)

#Create a for loop for four guesses:
for i in range(4):
    
    #Ask the user to input each round:
    guess = input("What number am I thinking, between 1 and 100? ")
    
    #Use int(guess) to convert the input string guess into an int
    guess = int(guess)
    
    #If statement to determine status of player's guess:
    if(guess == randomnumber):
        print("Congratulations, you guessed my number.")
        break
    elif(guess > randomnumber):
        print("You guessed too high")
    else:
        print("You guessed too low")
        
    #Lose condition. Is this the final round?
    if(i == 3):
        print("Out of guesses. You lose!")
        print("The number was: " + str(randomnumber))
           
#For demonstration purposes: prevents console from exiting when program done.

while(1):
    pass