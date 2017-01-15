import random

asteroids = []

ded = False

def setup():
    global shipLocX
    global shipVelX
    global asteroids

    size(500,1000)
    
    shipLocX = width/2
    shipVelX = 0


def draw():
    background(0)
    global ded
    
    if(ded):
        
        background(255,0,0)
        fill(0)
        textSize(72)
        textAlign(CENTER)
        text("You're ded", width/2, height/2)
        return
    
    playerMove()
    playerDraw()
    
    asteroidCreate()
    asteroidMove()
    asteroidDraw()
    
    collisionDetection()

def collisionDetection():
    global shipLocX
    global asteroids
    global ded
    
    for asteroid in asteroids:
        
        d = dist(shipLocX, height-100, asteroid[0], asteroid[1])
        if(d < (30/2+60/2)):
            ded = True

def asteroidCreate():
    global asteroids
    
    if(random.randint(0,100) < 5):
        asteroids.append([random.randint(0,width), 0, random.randint(2,7)])

def asteroidMove():
    global asteroids
    
    for asteroid in asteroids:
        
        if(asteroid[1] > height):
            asteroids.remove(asteroid)
        else:
            asteroid[1] += asteroid[2]

def asteroidDraw():
    for asteroid in asteroids:
        fill(255,0,0)
        ellipse(asteroid[0], asteroid[1], 30,30)
        
def playerMove():
    global shipLocX
    global shipVelX
    
    
    if(keyPressed):
        if(key == "a"):
            shipVelX -= 0.5
        if(key == "d"):
            shipVelX += 0.5
            
    #Edge conditions
    if(shipLocX > width or shipLocX < 0):
        shipVelX *= -1
            
    shipLocX += shipVelX
    
    #Friction!
    shipVelX *= 0.97
            
            
def playerDraw():
    global shipLocX
    fill(255)
    noStroke()
    #ellipse(shipLocX, height-50, 20,20)
    shipY = height-100
    
    rect(shipLocX-10, shipY - 30, 20, 50)
    rect(shipLocX-20, shipY - 20, 10, 10)
    rect(shipLocX+10, shipY - 20, 10, 10)
    rect(shipLocX-25, shipY + 10, 50, 10)
    
    noFill()
    stroke(0,0,255)
    ellipse(shipLocX, shipY, 60, 60)
    noStroke()