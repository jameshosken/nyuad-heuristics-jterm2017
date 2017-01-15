
size(500,500)

background(255)


fill(255,0,0)
ellipse(50,50,10,10)

fill(0,0,255)
ellipse(100,100,20,20)

for i in range(1, 10):
    fill(i * 255/10,0,0)
    ellipse(i*width/10, 250, 20, 20)