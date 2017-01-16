class Spaceship:
    
    maxSpeed = 5
    
    def __init__(self, _x, _y):
        
        self.pos = PVector(_x, _y)
        self.vel = PVector(0,0)
        self.acc = PVector(0,0)
    
        self.rot = 0
    
    def update(self):
        
        self.pos += self.vel
        
    def turn(self, angle):
        self.rot += angle
        
    def boost(self, thrust):
        thrustVector = PVector.fromAngle(self.rot).normalize()
        
        thrustVector.mult(thrust)

        
        self.vel += thrustVector
        self.vel.limit(self.maxSpeed)
    
    def checkEdges(self, xMin, yMin, xMax, yMax):
        
        if(self.pos.x > xMax):
            self.pos.x = xMin
            
        if(self.pos.x < xMin):
            self.pos.x = xMax
            
        if(self.pos.y > yMax):
            self.pos.y = yMin
            
        if(self.pos.y < yMin):
            self.pos.y = yMax
    
    
    def display(self):
        x = self.pos.x
        y = self.pos.y
        
        fill(255)
        noStroke()
        
        pushMatrix()
        
        translate(x,y)
        rotate(self.rot - PI/2)
        triangle(0, 30, -20, -30, 20, -30)
        
        popMatrix()