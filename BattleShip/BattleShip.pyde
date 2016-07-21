

board = [[1, 0, 0], [1, 1, 0], [1, 0, 1], [0, 0, 1], [0, 1, 1]]
varIntro = ["Welcome to BattleShip"],
i = ["These are the rules: 1. Click a square to find a ship, 2. If you guess wrong, you lose a life, 3. You have 5 lives, use them carefully!"]
# 1's and 0's are squares




def setup():
    size(700, 600)
    background(255, 0, 0)
    
    if i >= 2:
        print (varIntro[0])
        print (i[0])


    
def draw():
    global board
    boxSize = 280
    # row number 1
    for i in range(len(board[0])):
       
       if(board[0][i] == 1):
          [0]
          
          
          
          
          
    fill(255,0 ,0) 
    rect(0, 0, 280, 280) 
    fill(255,0 ,0) 
    
    rect(140, 0, 280, 280)
    fill(255,0,0)
    
    rect(280, 0, 280, 280)
    fill(255,0,0)
        
    rect(420, 0, 280, 280)
    fill(255,0,0)
        
    rect(560, 0, 280, 280)
    fill(255,0,0)
    #row 2
        
    rect(0, 120, boxSize, boxSize)
    fill(255,0,0) 
    
    rect(140, 120, boxSize, boxSize) #rect2
    fill(255,0,0)
    
    rect(280, 120, boxSize, boxSize)
    fill(255,0,0)
    
    rect(420, 120, boxSize, boxSize)
    fill(255,0,0)
    
    rect(560, 120, boxSize, boxSize)
    fill(255,0,0)
        
    # row 3
        
    rect(0, 240, boxSize, boxSize) #rect3
    fill(255,0,0) 
    
    rect(140, 240, boxSize, boxSize)
    fill(255,0,0)
    
    rect(280, 240, boxSize, boxSize)
    fill(255,0,0)
    
    rect(420, 240, boxSize, boxSize)
    fill(255,0,0)
        
    rect(560, 240, boxSize, boxSize)
    fill(255,0,0)
        
    # row 4
    
    rect(0, 360, boxSize, boxSize) #rect4
    fill(255,0,0) 
    
    rect(140, 360, boxSize, boxSize)
    fill(255,0,0)
    
    rect(280, 360, boxSize, boxSize)
    fill(255,0,0)
        
    rect(420, 360, boxSize, boxSize)
    fill(255,0,0)
    
    rect(560, 360, boxSize, boxSize)
    fill(255,0,0)
        
    # row 5
    
    rect(0, 480, boxSize, boxSize) #rect5
    fill(255,0,0) 
    
    rect(140, 480, boxSize, boxSize)
    fill(255,0,0)
    
    rect(280, 480, boxSize, boxSize)
    fill(255,0,0)
    
    rect(420, 480, boxSize, boxSize) 
    fill(255,0,0)
    
    rect(560, 480, boxSize, boxSize)"""
    
             
#def draw():
#    global boxSize
#    if mousePressed: