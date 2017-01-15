import random

def setup():
    global xposition
    global xvelocity
    
    global yposition
    global yvelocity
    
    global asteroids
    
    global isDead
    isDead = False
    
    size(500, 1000)
    xposition = width/2
    xvelocity = 0
    
    yposition = height/2
    yvelocity = 0
    
    asteroids = []
    
def draw():
    global isDead
    background(0)
    
    if(isDead):
        background(255,0,0)
        fill(0)
        textSize(48)
        textAlign(CENTER)
        text("You have been \ndestroyed", width/2, height/2)
        
        return
    
    ballMove()
    checkEdges()
    ballDraw()
    
    asteroidsGenerate()
    asteroidsMove()
    asteroidsDelete()
    asteroidsDraw()
    
    collisionDetection()
    
def collisionDetection():
    global asteroids
    global xposition
    global yposition
    global isDead
    
    ballRad = 15
    asteroidRad = 15
    
    for asteroid in asteroids:
        
        distance = dist(asteroid[0], asteroid[1], xposition, yposition)
        
        if(distance < (ballRad + asteroidRad)):
            isDead = True
    
def asteroidsGenerate():
    global asteroids
    
    if(random.randint(0,100) < 5):
        asteroids.append([random.randint(0,width), 0, random.randint(1,7)])
    

def asteroidsDelete():
    global asteroids
    
    for asteroid in asteroids:
        if(asteroid[1] > height):
            asteroids.remove(asteroid)


def asteroidsMove():
    global asteroids
    
    for asteroid in asteroids:
        asteroid[1] += asteroid[2]


def asteroidsDraw():
    global asteroids
    
    for asteroid in asteroids:
        noFill()
        stroke(255)
        ellipse(asteroid[0], asteroid[1], 30, 30)

def ballMove():
    global xposition
    global xvelocity
    
    global yposition
    global yvelocity
    
    if(keyPressed):
        if(key == "a"):
            xvelocity -= 0.5
        if(key == "d"):
            xvelocity += 0.5
        if(key == "w"):
            yvelocity -= 0.5
        if(key == "s"):
            yvelocity += 0.5
     
    xposition += xvelocity
    yposition += yvelocity
    #Friction!
    xvelocity *= 0.97
    yvelocity *= 0.97
    
def checkEdges():
    global xposition
    global yposition
    if(xposition < 0):
        xposition = width
    if(xposition > width):
        xposition = 0
        
    if(yposition < 0):
        yposition = height
    if(yposition > height):
        yposition = 0
    
def ballDraw():
    global xposition
    global yposition
    fill(255,0,0)
    ellipse(xposition, yposition, 30, 30)