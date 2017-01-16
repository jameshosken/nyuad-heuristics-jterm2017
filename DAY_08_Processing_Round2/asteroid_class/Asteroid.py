import random

class Asteroid:
    
    #Put class attributs here: i.e. stuff that's shared by all objects.
    colour = color(255,200,0)  #Means ALL asteroids have this colour.
    sizeMultiplier = 20
    
    def __init__(self, _x, _y):
        #When this object is created, do this stuff.
        self.x = _x
        self.y = _y
        
        self.vX = random.randint(-2,2)
        self.vY = random.randint(-2,2)
        
        self.bigness = random.randint(1,5)
        
    def update(self):
        self.x += self.vX
        self.y += self.vY
        
    def checkEdges(self, xMin, yMin, xMax, yMax):
        if(self.x > xMax):
            self.x = xMin
            
        if(self.x < xMin):
            self.x = xMax
            
        if(self.y > yMax):
            self.y = yMin
            
        if(self.y < yMin):
            self.y = yMax
    
    def display(self):
        #when object.display() is called, do this stuff.
        
        #fill(self.colour)
        noFill()
        stroke(255)
        s = self.bigness * self.sizeMultiplier
        ellipse(self.x, self.y, s, s)