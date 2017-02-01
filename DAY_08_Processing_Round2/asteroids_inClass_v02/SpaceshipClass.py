class Spaceship:
    
    
    
    def __init__(self):
            
            self.pos = PVector(width/2, height/2)
            self.vel = PVector(0,0)
            
            self.rot = 0
            

            
    def move(self):
        self.pos.add(self.vel)
        
        self.checkEdges()    
        
    def checkEdges(self):
        
        if(self.pos.x > width):
            self.pos.x = 0
        if(self.pos.x < 0):
            self.pos.x = width
        if(self.pos.y > height):
            self.pos.y = 0
        if(self.pos.y < 0):
            self.pos.y = height
        
    def accelerate(self, _aY):

        thrustVector = PVector.fromAngle(self.rot)
        
        thrustVector.mult(_aY)
        
        self.vel.add(thrustVector)
        
        
        
    def turn(self, _tX):
        #Incredment or decrement the ship's angle: 
        self.rot += _tX
        
    def display(self):
        
        fill(255)
        
        translate(self.pos.x, self.pos.y)
        rotate(self.rot)
        
        triangle(-10, 0, 10, -5, 10, 5)
    
    