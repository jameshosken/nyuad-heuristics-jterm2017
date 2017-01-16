import random

class Asteroid:
    
    def __init__(self):
        #Runs once at initialisation of each object.
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        
        self.velX = random.randint(-2,2)
        self.velY = random.randint(-2,2)
        
        self.bigness = random.randint(20,100)
    
    def move(self):
        self.x += self.velX
        self.y += self.velY
        
    def checkEdges(self, xMin, yMin, xMax, yMax):
        
        if(self.x < xMin):
            self.x = xMax
            
        if(self.y < yMin):
            self.y = yMax
            
        if(self.x > xMax):
            self.x = xMin
            
        if(self.y > yMax):
            self.y = yMin
        
    
    def display(self):
        noFill()
        stroke(255)
        
        ellipse(self.x, self.y, self.bigness, self.bigness)