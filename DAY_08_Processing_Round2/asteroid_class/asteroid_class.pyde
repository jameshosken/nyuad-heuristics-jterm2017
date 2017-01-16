import random
from Asteroid import *
from Spaceship import *
from Lazer import *

asteroids = []
controlsList = [False, False, False, False, True] #UP, DOWN, LEFT, RIGHT, FIREABLE

lazers = []

def setup():
    global ship
    size(1000,1000, P2D)
    
    asteroidsGenerate()
    ship = Spaceship(width/2, height/2)
    
        
        
def draw():
    background(0)

    asteroidsUpdate()
    shipUpdate()
    lazersUpdate()
    controls()

        
def shipUpdate():
    global ship
    ship.update()
    ship.checkEdges(0,0,width,height)
    ship.display()
    
def lazersUpdate():
    global lazers
    for lazer in lazers:
        lazer.update()
        lazer.display()
        
        if(lazer.timer < 0):
            lazers.remove(lazer)

def asteroidsGenerate():
    global asteroids
    for i in range(20):
        ast = Asteroid( random.randint(0,width), random.randint(0,height) ) 
        asteroids.append(ast)
        
def asteroidsUpdate():
    global asteroids
    for ast in asteroids:
        ast.update()
        ast.checkEdges(0,0,width,height)
        ast.display()
        

def controls():
    global controlsList
    global ship
    if(controlsList[0]):
        ship.boost(1)
    if(controlsList[1]):
        ship.boost(-1)
    if(controlsList[2]):
        ship.turn(-0.1)
    if(controlsList[3]):
        ship.turn(0.1)

def fireLazer():
    global ship
    global lazers
    print("Fire")
    
    lazer = Lazer(ship.pos.x, ship.pos.y, ship.vel.x, ship.vel.y, ship.rot)
    lazers.append(lazer)

def keyPressed():
    global controlsList
    if(key == "w"):
        controlsList[0] = True
    if(key == "s"):
        controlsList[1] = True
    if(key == "a"):
        controlsList[2] = True
    if(key == "d"):
        controlsList[3] = True
        
    #If space pressed and is fireable
    if(key == " " and controlsList[4] == True):
        #Fire laser
        fireLazer()
        controlsList[4] = False
        
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
    if(key == " "):
        controlsList[4] = True
        
    