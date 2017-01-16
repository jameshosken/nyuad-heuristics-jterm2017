import random
from AsteroidClass import *
from SpaceshipClass import *

asteroids = []


controlsList = [False, False, False, False] #UP, DOWN, LEFT, RIGHT

def setup():
    global ship
    
    size(1000,1000)
    asteroidsGenerate()
    
    ship = Spaceship()


def draw():
    
    background(0)
    
    asteroidsUpdate()
    shipUpdate()
    
    controls()
    
    
#################################################################################
#################################################################################

def shipUpdate():
    global ship
    
    
    ship.move()
    ship.checkEdges()
    ship.display()

def asteroidsGenerate():
    global asteroids
    for i in range(20):
        asteroid = Asteroid()
        asteroids.append(asteroid)

    
def asteroidsUpdate():
    global asteroids
    for asteroid in asteroids:    
        asteroid.move()
        asteroid.checkEdges(-10,-10, width+10, height+10)
        asteroid.display()
        

def controls():
    global controlsList
    global ship
    
    if(controlsList[0]):
        ship.accelerate(-0.1)
        
    if(controlsList[1]):
        ship.accelerate(0.1)
        
    if(controlsList[2]):
        ship.turn(-0.1)
                
    if(controlsList[3]):
        ship.turn(0.1)

def keyPressed():
    global controlsList
    #ORDER: W, S, A, D


    if(key == "w" and not controlsList[0]):
        controlsList[0] = True
    if(key == "s" and not controlsList[1]):
        controlsList[1] = True
    if(key == "a" and not controlsList[2]):
        controlsList[2] = True
    if(key == "d" and not controlsList[3]):
        controlsList[3] = True
        
def keyReleased():
    global controlsList
    
    if(key == "w"):
        controlsList[0] = False
    if(key == "s"):
        controlsList[1] = False
    if(key == "a"):
        controlsList[2] = False
    if(key == "d"):
        controlsList[3] = False
    
        
        

        



        
        