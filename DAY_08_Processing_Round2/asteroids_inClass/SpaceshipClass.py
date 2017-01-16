class Spaceship:
    
    
    def __init__(self):
        
        self.pos = PVector(width/2, height/2)
        
        self.vel = PVector(0,0)
    
    def move(self):
        self.pos.add(self.vel)
        
    def accelerate(self, _aX, _aY):
        self.vel.x += _aX
        self.vel.y += _aY
        
    def display(self):
        
        fill(255)
        ellipse(self.pos.x, self.pos.y, 40, 20)
        