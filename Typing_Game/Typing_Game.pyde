from time import sleep
from random import *
letterz = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


i = randint(0, 25)
x = float(25)
y = float(randint(0, 100))



def setup():
     size(900, 600)
     background(255, 0, 0)

def draw():
    
    background(255, 0, 0)
    
    global letterz
    
    global x
    x = x + 1
    
    global i
    
    randomLetterz = choice(letterzh)

    
    def randomFunc():
        while i >= 1:
            
        
    
            stroke(1, 2, 3, 4)
    
    
    
    if i >= 875:
       fill(255, 0, 0)
       textSize(40)
       text(randomLetterz, x, y)
       
    elif i < 575:
        fill(0, 255, 0)
        textSize(40)
        text(randomLetterz, x, y)
   
        
    if keyPressed == True:
        letterz[0]
        letterz.pop(0)
        x = 0
       

       