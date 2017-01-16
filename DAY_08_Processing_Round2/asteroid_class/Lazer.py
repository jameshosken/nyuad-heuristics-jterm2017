#With a "z" for Xtra zzzzap
class Lazer:
    
    calibre = 5
    
    def __init__(self, _x, _y, _vX, _vY, _rot):
        
        self.pos = PVector(_x, _y)
        self.rot = _rot
        
        self.vel = PVector.fromAngle(self.rot)
        self.vel.normalize()
        self.vel.mult(10) #THIS IS BULLET SPEED
        
        momentum = PVector(_vX, _vY)
        self.vel.add(momentum)
        
        self.timer = 120

    def update(self):
        
        self.pos += self.vel
        self.vel.mult(0.99) #Lazer friction??? Y not.
        
        #Life timer
        self.timer -= 1
    
    def display(self):
    
        noStroke()
        fill(255,0,0)
        ellipse(self.pos.x, self.pos.y, self.calibre, self.calibre)
        
        