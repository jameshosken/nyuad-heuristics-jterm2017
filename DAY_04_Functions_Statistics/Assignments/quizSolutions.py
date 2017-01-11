# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 23:08:53 2017

@author: james
"""

#Day 04 challenges answer sheet

#1.1

for i in range(5,101):
    print(i)
    
for i in range(5,101):
    if(i%2 == 0):
        print(i)
        
        
num = int(input("Give me a number to count up to: "))
for i in range(num):
    print(i)
    
#1.2
num = 0
runningTotal = 0
while(num != -1):
    num = int(input("Input a number to add: "))
    runningTotal += num
print("Final total = " + str(runningTotal))

#2.1
bill = float(input("Input a bill: "))
tip = float(input("Input tip percentage: "))
tipdecimal = tip / 100
total = bill + (bill*tipdecimal)
print("Total = " + str(total))

#2.2
num1 = int(input("Give me a whole number: "))
num2 = int(input("Give me another whole number: "))
if(num1 > num2):
    print("Larger is " + str(num1))
else:
    print("Larger is " + str(num2))
    
#2 (Strings)
#2.1
sen = input("Input a sentence: ")
print(sen.upper())

#2.2
sen = input("Input a sentence: ")
print(sen[::-1])

#2.3
sen = input("Input a sentence: ")
if(sen == sen[::-1]):
    print("Palindrome!")
else:
    print("Not palindrome!")
    
#3.1
planets = ["Mercury", "Venus", "Earth", "Mars", "Saturn", "Jupiter", "Neptune", "Uranus", "Pluto??"]
for planet in planets:
    print(planet)
    
#3.2
numList = [1,2,3,4,15,16,14,25,35,46,35,63,52]
average = sum(numList)/len(numList)
print("Average: " + str(average))
print("Nums higher than average:")
for num in numList:
    if(num > average):
        print(num)
        
#4.1
file = open("planets.txt", "r")
lines = file.readlines()
file.close()
count = 1
for line in lines:
    print(line.strip() + " is planet number " + str(count))
    count += 1


#5
file = open("planetdescriptions.txt", "r")
lines = file.readlines()
file.close()

planets = []
descriptions = []

for line in lines:
    splitLine = line.split(":")
    planets.append(splitLine[0].strip())
    descriptions.append(splitLine[1])
    
print(planets)
print(descriptions)
for planet in planets:
    print(type(planet))
while(True):
    req = input("Give me a planet name: ")
    try:
        idx = planets.index(req)
        print(descriptions[idx])
        print()
    except:
        print("No matching planet name found. Try again.")
        