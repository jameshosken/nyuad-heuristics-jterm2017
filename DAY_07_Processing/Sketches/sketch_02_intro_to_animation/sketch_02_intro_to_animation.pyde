


#setup runs once
def setup():
    size(500,500)
    
    global ballX
    global ballY
    
    ballX = width/2
    ballY = height/2
    
    
#draw runs over and over until the end of the universe
def draw():
    background(255)
    
    global ballX
    global ballY
    
    ballX += 1
    
    if(ballX > width):
        ballX = 0
    
    fill(255,0,0)
    ellipse(ballX, ballY, 10,10)
    