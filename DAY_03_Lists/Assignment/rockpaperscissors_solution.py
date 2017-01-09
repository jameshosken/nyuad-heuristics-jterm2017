# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 16:52:24 2017

@author: james
"""

player1 = ""
player2 = ""
rounds = []

choices = ["rock", "paper", "scissors"]

#Play forever
while(True):
    
    #Input error checking, player 1
    while(True):
        player1 = input("Player 1, input 'rock', 'paper', or 'scissors': ")
        if(player1 in choices):
            break
        else:
            print("ERROR: incorrect input. Please try again")
    print("\n" * 100)
    
    #Input error checking, player 2
    while(True):
        player2 = input("Player 2, input 'rock', 'paper', or 'scissors': ")
        if(player2 in choices):
            break
        else:
            print("ERROR: incorrect input. Please try again")
    print("\n" * 100)

    #Game Logic
    if(player1 == "rock"):
        #P1 rock Logic
        if(player2 == "rock"):
            rounds.append(0)
            print("Draw. No player wins.")
        elif(player2 == "paper"):
            rounds.append(2)
            print("Player 2 wins")
        else:
            rounds.append(1)
            print("Player 1 wins")
    elif(player1 == "paper"):
        #P1 paper logic
        if(player2 == "rock"):
            rounds.append(1)
            print("Player 1 wins")
        elif(player2 == "paper"):
            rounds.append(0)
            print("Draw. No player wins.")
        else:
            rounds.append(2)
            print("Player 2 wins")
    else:
        #P1 scissors logic
        if(player2 == "rock"):
            rounds.append(2)
            print("Player 2 wins")
        elif(player2 == "paper"):
            rounds.append(1)
            print("Player 1 wins")
        else:
            rounds.append(0)
            print("Draw. No player wins.")
    
    print("Round History: " + str(rounds))
    print("End Round")
    print("-----")