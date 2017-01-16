import random

def setup():
    global starField
    starField = []
    
    size(1000,1000)
    starFieldGenerate()
    
    
def draw():
    background(0)
    
    starFieldDraw()
    
    
def starFieldGenerate():
    global starField
    for i in range(500):
        #xpos, ypos, size
        starField.append([random.randint(0,width), random.randint(0, height), random.randint(1,5)])
        
def starFieldDraw():
    global starField
    fill(255)
    stroke(255)
    
    for star in starField:
        x = star[0]
        y = star[1]
        s = star[2]
        
        ellipse(x, y, s,s)
        line(x-s,y, x+s, y)
        line(x, y-s, x, y+s)