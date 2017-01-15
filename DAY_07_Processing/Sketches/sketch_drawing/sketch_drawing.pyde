import random

def setup():
    global mainColour
    mainColour = color(255,0,0)
    size(1000,1000)
    background(255)
    
def draw():
    global mainColour
    
    strokeWeight(3)

    if(mousePressed):
        stroke(mainColour)
        line(mouseX, mouseY, pmouseX, pmouseY)
    
    

def mouseReleased():
    global mainColour
    mainColour = color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    