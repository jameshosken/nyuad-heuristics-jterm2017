# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 11:56:28 2017

@author: james
"""
import random
# Function input
def addThreeNumbers(num1, num2, num3):
    print(num1+num2+num3)

addThreeNumbers(4,5,6)


# Function Process (no input or output)

def printPrettyPattern():
    print("**  **  **")
    print("  **  **  ")
    print("*   **   *")
    print("  **  **  ")
    print("**  **  **")

printPrettyPattern()


# Function Output ('return')
def giveMeAListOfRandomNumbers():

    randomList = []
    for i in range(10):
        randomList.append(random.randint(0,100))

    return randomList


list1 = giveMeAListOfRandomNumbers()
list2 = giveMeAListOfRandomNumbers()
list3 = giveMeAListOfRandomNumbers()

print(list1)
print(list2)
print(list3)


