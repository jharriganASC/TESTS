from random import *

ballX = 125
ballY = 225
xSpeed = 4
ySpeed = 4

myVars = [-1, 1]

def setup():
    size(700, 750)
    background(253, 195, 93)
    
def draw():
    background(253, 195, 93)
    
    global ballX
    global ballY
    global xSpeed
    ballX = ballX + xSpeed
    global ySpeed
    ballY = ballY + ySpeed
    
    noStroke()
    
    if ballY >= 675:
        ySpeed = ySpeed * -1
        xSpeed = xSpeed * choice(myVars)
        
    if ballX >= 675:
        xSpeed = xSpeed * -1
        ySpeed = ySpeed * choice(myVars)    
    
    for i in range(0, 10):
        fill(randint(25, 75), randint(30, 255), randint(40, 225))
        ellipse(randint(ballX, 0), randint(0, ballY), 45, 45)
        
    if ballY < 0:
        ySpeed = ySpeed * -1
        xSpeed = xSpeed * choice(myVars)
            
    if ballX < 0:
        xSpeed = xSpeed * -1
        ySpeed = ySpeed * choice(myVars)
        
    print ballX
    print ballY            
    