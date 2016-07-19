from time import *
from random import *

ballX = 125
ballY = 225

xSpeed = 4
ySpeed = 4

myVariables = [-1, 1]

def setup():
    size(490, 490)
    background(255, 103, 67)
    
def draw():
    
    background(255, 103, 67)
    
    global ballX  
    
    
    global ballY
    
    
    global xSpeed
    ballX = ballX + xSpeed
    
    global ySpeed
    ballY = ballY + ySpeed
    
    noStroke()

    
   

        
    if ballY >= 475:
        ySpeed = ySpeed * -1
        xSpeed = xSpeed * choice(myVariables)
        
    if ballX >= 475:
        xSpeed = xSpeed * -1
        ySpeed = ySpeed * choice(myVariables)
        
        
    ellipse(ballX, ballY, 25, 25)    
   
    if ballY < 0:
        ySpeed = ySpeed * -1
        xSpeed = xSpeed * choice(myVariables)
    if ballX < 0:
        xSpeed = xSpeed * -1
        ySpeed = ySpeed * choice(myVariables)              
   
    
    print ballX
    print ballY
        